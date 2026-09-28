"""Build data/inbox/: everything the daily Claude routine needs to write the brief.

Runs in GitHub Actions right after `fetch` (which needs open internet). The routine
then works only from these files, so it needs no network access and no API key.

data/inbox/
├── meta.json              date, match day, markets, section order
├── refs.json              ref id -> {outlet, title, url}, per section (used by assemble)
├── system.md              reader profile, grounding and writing rules (applies to every section)
├── sections/<name>.md     task + input data, one per section, plus quiz.md
├── schemas/<name>.schema.json
├── essays/<ref>.txt       full text of Ideas candidates
└── drafts/                (routine output, gitignored)
"""

from __future__ import annotations

import asyncio
import json
import shutil
import tomllib
from dataclasses import asdict
from datetime import date, datetime, timezone
from pathlib import Path

from ..config import PIPELINE_DIR, Settings, load_sources
from ..http import make_client
from . import prompts
from .articles import fetch_article_text
from .inputs import SectionInput, build_inputs, load_history, load_raw
from .matchday import detect_match_day
from .schemas import SECTION_SCHEMAS, SECTIONS, QuizOutput

BRIEF_FILE = PIPELINE_DIR / "brief.toml"
MAX_ESSAYS = 12
GENERATED_DIRS = ("sections", "schemas", "essays", "drafts")


def load_brief_cfg(path: Path = BRIEF_FILE) -> dict:
    with open(path, "rb") as f:
        return tomllib.load(f)


def inbox_dir(settings: Settings) -> Path:
    return settings.data_dir / "inbox"


def essay_filename(ref: str) -> str:
    return ref.replace("#", "_") + ".txt"


async def _fetch_essays(ideas: SectionInput, essays_dir: Path) -> int:
    """Fetch full text for the newest Ideas candidates and point each candidate at its file."""
    items = sorted(
        (i for feed in ideas.payload.get("candidates", []) for i in feed["items"]),
        key=lambda i: i.get("published") or "",
        reverse=True,
    )[:MAX_ESSAYS]
    sem = asyncio.Semaphore(6)

    async with make_client() as client:
        async def one(item):
            url = ideas.refs[item["ref"]].url
            async with sem:
                text = await fetch_article_text(client, url) if url else None
            if text:
                name = essay_filename(item["ref"])
                (essays_dir / name).write_text(text, encoding="utf-8")
                item["full_text_file"] = f"essays/{name}"
            return bool(text)

        return sum(await asyncio.gather(*(one(i) for i in items)))


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def prepare(day: date, settings: Settings) -> dict:
    raw_dir = settings.data_dir / "raw" / day.isoformat()
    if not raw_dir.exists():
        raise FileNotFoundError(f"no raw data for {day}: run `daily-brief fetch` first")

    sources_cfg = load_sources()
    brief_cfg = load_brief_cfg()
    raw = load_raw(raw_dir)
    inputs = build_inputs(raw, day, sources_cfg, load_history(settings.data_dir / "briefs", day))
    match_day = detect_match_day(raw, sources_cfg, day)

    inbox = inbox_dir(settings)
    for name in GENERATED_DIRS:
        shutil.rmtree(inbox / name, ignore_errors=True)
    (inbox / "essays").mkdir(parents=True)

    essays = asyncio.run(_fetch_essays(inputs["ideas"], inbox / "essays"))

    _write(inbox / "system.md", prompts.system_prompt(brief_cfg, day))
    skipped = []
    for section in SECTIONS:
        inp = inputs[section]
        if not inp.refs:
            skipped.append(section)  # every source for this section failed today
            continue
        _write(inbox / "sections" / f"{section}.md", prompts.section_prompt(section, inp, brief_cfg, day, match_day))
        _write(inbox / "schemas" / f"{section}.schema.json", json.dumps(SECTION_SCHEMAS[section].model_json_schema(), indent=1))
    _write(inbox / "sections" / "quiz.md", prompts.QUIZ_PROMPT)
    _write(inbox / "schemas" / "quiz.schema.json", json.dumps(QuizOutput.model_json_schema(), indent=1))

    order = list(brief_cfg["layout"]["order"])
    if match_day["is_match_day"] and "sports" in order:
        order.remove("sports")
        order.insert(0, "sports")

    meta = {
        "date": day.isoformat(),
        "prepared_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "sections": [s for s in SECTIONS if s not in skipped],
        "skipped_sections": skipped,
        "order": order,
        "match_day": match_day,
        "markets": raw.get("markets", {}).get("data", {}).get("quotes"),
        "essays_fetched": essays,
    }
    _write(inbox / "meta.json", json.dumps(meta, ensure_ascii=False, indent=1))
    refs = {s: {ref: asdict(r) for ref, r in inputs[s].refs.items()} for s in SECTIONS}
    _write(inbox / "refs.json", json.dumps(refs, ensure_ascii=False, indent=1))
    return meta
