# Daily Brief — pipeline

Python content pipeline for the Daily Brief PWA.

- **Phase 1 — fetch:** pull every source concurrently, dump raw JSON to `data/raw/<YYYY-MM-DD>/` (gitignored).
- **Phase 2 — write:** `prepare` turns the raw data into per-section tasks in `data/inbox/`; a scheduled
  **Claude Code routine** (runs on a Claude Pro subscription — no API key) writes each section at three lengths
  (Scroll / Coffee / Deep) in English *and* Hebrew plus a daily quiz, and `assemble` validates and publishes it to
  `data/briefs/<YYYY-MM-DD>/`, which the app reads.

```
05:00  GitHub Action   fetch -> prepare -> commit data/inbox/          (.github/workflows/fetch.yml)
06:30  Claude routine  read inbox -> write drafts -> assemble -> commit data/briefs/   (ROUTINE.md)
```

## Setup

Requires [uv](https://docs.astral.sh/uv/) (it installs Python 3.11+ for you).

```bash
cd pipeline
uv sync
cp ../.env.example ../.env   # then fill in keys (the .env lives at the repo root)
```

| Env var | Needed for | Get it |
| --- | --- | --- |
| `FOOTBALL_DATA_TOKEN` | European soccer | https://www.football-data.org/client/register |
| `BALLDONTLIE_TOKEN` | NBA | https://app.balldontlie.io/ |
| `THESPORTSDB_KEY` | Inter Miami / national team (optional, defaults to free key `123`) | https://www.thesportsdb.com/ |

RSS feeds, Yahoo Finance (`yfinance`) and Wikipedia need no keys.

## Usage

```bash
uv run daily-brief sources                     # list configured sources
uv run daily-brief fetch                       # fetch everything -> data/raw/<today>/
uv run daily-brief fetch --no-write            # connectivity check only
uv run daily-brief fetch --section sports      # one section
uv run daily-brief fetch --only aeon,markets   # specific sources
uv run daily-brief fetch --strict              # exit 1 if any source fails (for CI)

uv run daily-brief prepare                     # raw -> data/inbox/ (tasks, inputs, schemas, essays)
uv run daily-brief assemble                    # validate data/inbox/drafts/ -> data/briefs/<date>/
```

"Today" is always the Israel date (`Asia/Jerusalem`).

## Output — Phase 1 (raw)

```
data/raw/2026-09-28/
├── _manifest.json          # per-source status, counts, warnings, timings
├── football_data.json      # API sources: {"data": {...}}
├── aeon.json               # RSS sources: {"items": [{title, url, published, summary, ...}]}
└── ...
```

Every file has the same envelope: `source_id, section, kind, ok, error, warnings, fetched_at, elapsed_ms, items, data`.
A failing source never stops the run — it's recorded with `ok: false` and an `error`.

## Output — Phase 2 (the brief)

```
data/briefs/
├── index.json                 # {"latest": "2026-09-28", "dates": [...]}
└── 2026-09-28/
    ├── brief.json             # section order (sports first on match days), per-section status, usage + cost
    ├── sports.json            # stories + israeli_players + match_day
    ├── geopolitics.json
    ├── israeli_politics.json
    ├── business.json          # stories + markets snapshot (TA-35, S&P 500, USD/ILS, Brent, BTC)
    ├── ideas.json
    ├── learn.json             # word/concept of the day + on this day
    └── quiz.json              # 3 questions; the app shows them the *next* morning
```

Every story has the same shape, so the app renders all sections with one component:

```jsonc
{
  "id": "arsenal-city-preview", "kind": "news",   // news | analysis | essay | concept | word | on_this_day
  "en": {"headline": "...", "scroll": "...", "coffee": "...", "deep": "...markdown..."},
  "he": {"headline": "...", "scroll": "...", "coffee": "...", "deep": "..."},
  "sources": [{"outlet": "BBC Sport", "title": "...", "url": "..."}],
  "tags": ["arsenal", "premier-league"]
}
```

### How it works

- The routine follows [`ROUTINE.md`](../ROUTINE.md): read `data/inbox/system.md` + one task file per section, write
  JSON drafts, then run `assemble`, which **validates every draft against Pydantic schemas** (`summarize/schemas.py`)
  and reports errors for the routine to fix. Nothing is published unless the whole brief is valid.
- **Claude cites ref ids, never URLs.** Every input item gets a ref like `bbc_world#3`; links are resolved from the
  raw data afterwards and unknown refs are dropped — so links can't be hallucinated.
- **Grounding rules** in the system prompt: the input is the source of truth for anything current (the model's
  training data is older than today's news), and every number/score/quote must come from the input.
- **Ideas:** `prepare` downloads the full text of the newest essay candidates, so the summary is of the actual
  argument, not a 400-character feed blurb.
- **Rotations without repeats:** word of the day, the Sunday concept deep-dive and the featured essay check the
  last 30 days of briefs.
- **Match-day mode**, the markets line and section order are computed in code, not by the model.
Tune the reader profile, lengths, languages and section order in [`brief.toml`](brief.toml).

## Adding / fixing a source

Feeds live in [`sources.toml`](sources.toml) — adding an RSS feed is a config change, not a code change.
API sources live in `src/daily_brief/fetchers/` and are registered in `fetchers/__init__.py`.

## Tests

```bash
uv run pytest
```
