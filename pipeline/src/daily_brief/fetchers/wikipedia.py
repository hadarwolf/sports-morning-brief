"""Wikipedia "On this day" (selected events) for the Learn section."""

from __future__ import annotations

import httpx

from ..http import get
from ..models import Context, SourceResult


def _trim_event(event: dict) -> dict:
    return {
        "year": event.get("year"),
        "text": event.get("text"),
        "pages": [
            {
                "title": p.get("normalizedtitle") or p.get("title"),
                "description": p.get("description"),
                "extract": p.get("extract"),
                "url": p.get("content_urls", {}).get("desktop", {}).get("page"),
            }
            for p in event.get("pages", [])[:3]
        ],
    }


async def fetch(ctx: Context, res: SourceResult) -> None:
    mm, dd = f"{ctx.today.month:02d}", f"{ctx.today.day:02d}"
    for lang in ctx.sources["wikipedia"]["langs"]:
        url = f"https://{lang}.wikipedia.org/api/rest_v1/feed/onthisday/selected/{mm}/{dd}"
        try:
            events = (await get(ctx.client, url)).json().get("selected", [])
        except httpx.HTTPStatusError as e:
            # Not every language wiki publishes this feed; English is the one we rely on.
            if lang == "en":
                raise
            res.warnings.append(f"{lang}: HTTP {e.response.status_code}")
            continue
        res.data[lang] = [_trim_event(e) for e in events]
