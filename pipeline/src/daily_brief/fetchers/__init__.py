"""Source registry: turns sources.toml into a list of runnable sources."""

from __future__ import annotations

from dataclasses import dataclass
from functools import partial
from typing import Awaitable, Callable

from ..models import Context, SourceResult
from . import balldontlie, football_data, markets, rss, thesportsdb, wikipedia

FetchFn = Callable[[Context, SourceResult], Awaitable[None]]


@dataclass(frozen=True)
class Source:
    id: str
    section: str
    kind: str
    fetch: FetchFn
    description: str = ""


# API sources: (config table in sources.toml, section, fetch fn)
API_SOURCES = {
    "football_data": ("sports", football_data.fetch),
    "balldontlie": ("sports", balldontlie.fetch),
    "thesportsdb": ("sports", thesportsdb.fetch),
    "markets": ("business", markets.fetch),
    "wikipedia": ("learn", wikipedia.fetch),
}


def build_sources(cfg: dict) -> list[Source]:
    sources = []
    for source_id, (section, fn) in API_SOURCES.items():
        table = cfg.get(source_id, {})
        if table.get("enabled", True):
            sources.append(Source(source_id, section, "api", fn, table.get("description", "")))
    for feed in cfg.get("rss", []):
        if feed.get("enabled", True):
            sources.append(
                Source(feed["id"], feed["section"], "rss", partial(rss.fetch_feed, feed=feed), feed.get("name", ""))
            )
    return sources
