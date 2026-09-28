"""Validate the routine's drafts and publish them to data/briefs/<date>/ for the app.

Errors are phrased for the routine: it re-runs `assemble` after fixing its drafts
until everything passes.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from pydantic import ValidationError

from ..config import Settings
from .prepare import inbox_dir, load_brief_cfg
from .schemas import SECTION_SCHEMAS, QuizOutput

MAX_ERRORS_SHOWN = 12


@dataclass
class Report:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    written: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def _load_json(path: Path, rep: Report):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        rep.errors.append(f"{path.name}: invalid JSON at line {e.lineno} col {e.colno}: {e.msg}")
        return None


def _validation_errors(name: str, e: ValidationError) -> list[str]:
    errs = [f"{name}: {'.'.join(map(str, err['loc']))}: {err['msg']}" for err in e.errors()]
    if len(errs) > MAX_ERRORS_SHOWN:
        errs = errs[:MAX_ERRORS_SHOWN] + [f"{name}: ... and {len(errs) - MAX_ERRORS_SHOWN} more"]
    return errs


def _write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def assemble(settings: Settings) -> Report:
    rep = Report()
    inbox = inbox_dir(settings)
    meta = json.loads((inbox / "meta.json").read_text(encoding="utf-8"))
    refs = json.loads((inbox / "refs.json").read_text(encoding="utf-8"))
    brief_cfg = load_brief_cfg()
    day = meta["date"]
    drafts = inbox / "drafts"

    # Validate everything first; publish only if the whole brief is valid.
    sections: dict[str, dict] = {}
    for section in meta["sections"]:
        path = drafts / f"{section}.json"
        if not path.exists():
            rep.errors.append(f"{section}: missing drafts/{section}.json")
            continue
        data = _load_json(path, rep)
        if data is None:
            continue
        try:
            parsed = SECTION_SCHEMAS[section].model_validate(data)
        except ValidationError as e:
            rep.errors.extend(_validation_errors(section, e))
            continue

        ids = [s.id for s in parsed.stories]
        if len(ids) != len(set(ids)):
            rep.errors.append(f"{section}: story ids must be unique, got {ids}")
        doc = parsed.model_dump()
        for story in doc["stories"]:
            known = refs.get(section, {})
            unknown = [r for r in story["source_refs"] if r not in known]
            if unknown:
                rep.errors.append(f"{section}/{story['id']}: unknown source_refs {unknown}; use ref ids from sections/{section}.md")
            story["sources"] = [known[r] for r in story.pop("source_refs") if r in known]
        sections[section] = doc

    quiz = None
    quiz_path = drafts / "quiz.json"
    if not quiz_path.exists():
        rep.errors.append("quiz: missing drafts/quiz.json")
    elif (data := _load_json(quiz_path, rep)) is not None:
        try:
            quiz = QuizOutput.model_validate(data).model_dump()
        except ValidationError as e:
            rep.errors.extend(_validation_errors("quiz", e))
        else:
            story_ids = {(sec, s["id"]) for sec, doc in sections.items() for s in doc["stories"]}
            for q in quiz["questions"]:
                if (q["section"], q["story_id"]) not in story_ids:
                    rep.errors.append(f"quiz/{q['id']}: no story {q['story_id']!r} in section {q['section']!r}")

    if not rep.ok:
        return rep

    out = settings.data_dir / "briefs" / day
    generated_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    for section, doc in sections.items():
        cfg = brief_cfg["sections"][section]
        extras = {}
        if section == "sports":
            extras["match_day"] = meta["match_day"]
        if section == "business":
            extras["markets"] = meta["markets"]
        _write_json(out / f"{section}.json", {
            "section": section,
            "date": day,
            "title_en": cfg["title_en"],
            "title_he": cfg["title_he"],
            "default_lang": cfg["default_lang"],
            "generated_at": generated_at,
            **doc,
            **extras,
        })
        rep.written.append(f"{section}.json")
    _write_json(out / "quiz.json", {"date": day, **quiz})

    _write_json(out / "brief.json", {
        "date": day,
        "generated_at": generated_at,
        "order": [s for s in meta["order"] if s in sections],
        "match_day": meta["match_day"],
        "sections": [
            {
                "id": s,
                "title_en": brief_cfg["sections"][s]["title_en"],
                "title_he": brief_cfg["sections"][s]["title_he"],
                "default_lang": brief_cfg["sections"][s]["default_lang"],
                "file": f"{s}.json",
            }
            for s in meta["order"]
            if s in sections
        ],
        "quiz": "quiz.json",
    })
    rep.written += ["quiz.json", "brief.json"]

    briefs = settings.data_dir / "briefs"
    dates = sorted((p.parent.name for p in briefs.glob("*/brief.json")), reverse=True)
    _write_json(briefs / "index.json", {"latest": dates[0], "dates": dates})
    if meta["skipped_sections"]:
        rep.warnings.append(f"skipped today (no source data): {', '.join(meta['skipped_sections'])}")
    return rep
