"""Generic RSS/Atom fetcher: download, parse, normalize, drop stale items."""

from __future__ import annotations

import html
import re
from datetime import datetime, timedelta, timezone

import feedparser

from ..http import BROWSER_USER_AGENT, get
from ..models import Context, SourceResult

DEFAULT_MAX_ITEMS = 25
DEFAULT_MAX_AGE_HOURS = 48
SUMMARY_MAX_CHARS = 1200

_TAG_RE = re.compile(r"<[^>]+>")
_WS_RE = re.compile(r"\s+")


def clean_html(text: str | None) -> str:
    if not text:
        return ""
    text = html.unescape(_TAG_RE.sub(" ", text))
    return _WS_RE.sub(" ", text).strip()


def entry_time(entry) -> datetime | None:
    struct = entry.get("published_parsed") or entry.get("updated_parsed")
    if not struct:
        return None
    return datetime(*struct[:6], tzinfo=timezone.utc)


def normalize_entry(entry, feed: dict) -> dict:
    published = entry_time(entry)
    summary = clean_html(entry.get("summary") or entry.get("description"))
    return {
        "title": clean_html(entry.get("title")),
        "url": entry.get("link"),
        "published": published.isoformat() if published else None,
        "summary": summary[:SUMMARY_MAX_CHARS],
        "author": entry.get("author"),
        "tags": [t.get("term") for t in entry.get("tags", []) if t.get("term")],
        "source": feed["id"],
        "lang": feed.get("lang", "en"),
    }


def parse_feed(content: bytes, feed: dict, now: datetime) -> tuple[list[dict], list[str]]:
    """Parse raw feed bytes into normalized items. Returns (items, warnings)."""
    parsed = feedparser.parse(content)
    if not parsed.entries:
        reason = parsed.get("bozo_exception") or "feed has no entries"
        raise ValueError(f"unparseable feed: {reason}")

    cutoff = now - timedelta(hours=feed.get("max_age_hours", DEFAULT_MAX_AGE_HOURS))
    max_items = feed.get("max_items", DEFAULT_MAX_ITEMS)
    items, stale, undated = [], 0, 0
    for entry in parsed.entries:
        item = normalize_entry(entry, feed)
        if item["published"] is None:
            undated += 1
        elif datetime.fromisoformat(item["published"]) < cutoff:
            stale += 1
            continue
        items.append(item)

    # Newest first; undated entries keep feed order at the end.
    items.sort(key=lambda i: i["published"] or "", reverse=True)
    items = items[:max_items]

    warnings = []
    if not items:
        warnings.append(f"all {stale} entries older than {feed.get('max_age_hours', DEFAULT_MAX_AGE_HOURS)}h")
    if undated:
        warnings.append(f"{undated} entries had no date")
    return items, warnings


async def fetch_feed(ctx: Context, res: SourceResult, feed: dict) -> None:
    headers = {"User-Agent": BROWSER_USER_AGENT} if feed.get("browser_ua") else None
    resp = await get(ctx.client, feed["url"], headers=headers)
    items, warnings = parse_feed(resp.content, feed, ctx.now)
    res.items = items
    res.warnings.extend(warnings)
