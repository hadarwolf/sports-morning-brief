"""Run sources concurrently and write raw JSON to data/raw/<date>/."""

from __future__ import annotations

import asyncio
import json
import time
from datetime import date, datetime, timezone
from pathlib import Path

import httpx

from .config import TZ, Settings
from .fetchers import Source
from .http import make_client
from .models import Context, SourceResult

# RSS feeds are cheap and on different hosts; API sources self-throttle internally.
MAX_CONCURRENCY = 10


def _describe_error(e: Exception) -> str:
    if isinstance(e, httpx.HTTPStatusError):
        return f"HTTP {e.response.status_code} from {e.request.url.host}"
    if isinstance(e, httpx.TimeoutException):
        return f"timeout ({type(e).__name__})"
    return f"{type(e).__name__}: {e}"


async def _run_one(ctx: Context, source: Source, sem: asyncio.Semaphore) -> SourceResult:
    res = SourceResult(source.id, source.section, source.kind)
    async with sem:
        start = time.perf_counter()
        try:
            await source.fetch(ctx, res)
        except Exception as e:
            res.ok = False
            res.error = _describe_error(e)
        res.elapsed_ms = int((time.perf_counter() - start) * 1000)
        res.fetched_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    return res


async def run_sources(sources: list[Source], settings: Settings, cfg: dict, today: date | None = None) -> list[SourceResult]:
    now = datetime.now(TZ)
    sem = asyncio.Semaphore(MAX_CONCURRENCY)
    async with make_client() as client:
        ctx = Context(client=client, settings=settings, sources=cfg, now=now, today=today or now.date())
        return await asyncio.gather(*(_run_one(ctx, s, sem) for s in sources))


def write_results(results: list[SourceResult], data_dir: Path, day: date) -> Path:
    out_dir = data_dir / "raw" / day.isoformat()
    out_dir.mkdir(parents=True, exist_ok=True)
    for res in results:
        (out_dir / f"{res.source_id}.json").write_text(
            json.dumps(res.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8"
        )
    manifest = {
        "date": day.isoformat(),
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "ok": sum(r.ok for r in results),
        "failed": sum(not r.ok for r in results),
        "sources": [
            {k: v for k, v in r.to_dict().items() if k not in ("items", "data")} for r in results
        ],
    }
    (out_dir / "_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return out_dir
