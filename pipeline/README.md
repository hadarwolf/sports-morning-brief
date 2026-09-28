# Daily Brief — pipeline

Python content pipeline for the Daily Brief PWA.

- **Phase 1 (this):** fetch every source concurrently and dump raw JSON to `data/raw/<YYYY-MM-DD>/`.
- Phase 2: Claude ranks + writes Scroll / Coffee / Deep versions per section.

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
| `ANTHROPIC_API_KEY` | Phase 2 summarization | https://console.anthropic.com/ |

RSS feeds, Yahoo Finance (`yfinance`) and Wikipedia need no keys.

## Usage

```bash
uv run daily-brief sources                     # list configured sources
uv run daily-brief fetch                       # fetch everything -> data/raw/<today>/
uv run daily-brief fetch --no-write            # connectivity check only
uv run daily-brief fetch --section sports      # one section
uv run daily-brief fetch --only aeon,markets   # specific sources
uv run daily-brief fetch --strict              # exit 1 if any source fails (for CI)
```

"Today" is always the Israel date (`Asia/Jerusalem`).

## Output

```
data/raw/2026-09-28/
├── _manifest.json          # per-source status, counts, warnings, timings
├── football_data.json      # API sources: {"data": {...}}
├── aeon.json               # RSS sources: {"items": [{title, url, published, summary, ...}]}
└── ...
```

Every file has the same envelope: `source_id, section, kind, ok, error, warnings, fetched_at, elapsed_ms, items, data`.
A failing source never stops the run — it's recorded with `ok: false` and an `error`.

## Adding / fixing a source

Feeds live in [`sources.toml`](sources.toml) — adding an RSS feed is a config change, not a code change.
API sources live in `src/daily_brief/fetchers/` and are registered in `fetchers/__init__.py`.

## Tests

```bash
uv run pytest
```
