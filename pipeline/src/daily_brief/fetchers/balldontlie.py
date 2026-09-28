"""balldontlie.io NBA: yesterday's games + Israeli players' box scores.

Free tier: 5 requests/minute and only games/teams/players. Box-score stats need a
paid tier, so a 401/403 there is a warning rather than a failure.
"""

from __future__ import annotations

from datetime import timedelta

import httpx

from ..http import get
from ..models import ConfigError, Context, SourceResult

BASE = "https://api.balldontlie.io/v1"
RATE_WINDOW_S = 65  # 5 requests/minute on the free tier


async def fetch(ctx: Context, res: SourceResult) -> None:
    token = ctx.settings.balldontlie_token
    if not token:
        raise ConfigError("BALLDONTLIE_TOKEN not set")
    cfg = ctx.sources["balldontlie"]
    headers = {"Authorization": token}

    async def call(path: str, params: dict) -> dict:
        return (await get(ctx.client, f"{BASE}{path}", params=params, headers=headers, retries=1, max_wait=RATE_WINDOW_S)).json()

    # Israel's yesterday == the US evening that just finished by ~6am Israel time.
    # Today's slate (same request) feeds match-day mode.
    yesterday = (ctx.today - timedelta(days=1)).isoformat()
    today = ctx.today.isoformat()
    res.data["date"] = yesterday
    games = (await call("/games", {"dates[]": [yesterday, today], "per_page": 100}))["data"]
    res.data["games"] = [g for g in games if g["date"][:10] == yesterday]
    res.data["games_today"] = [g for g in games if g["date"][:10] == today]

    players = {}
    for full_name in cfg["israeli_players"]:
        last_name = full_name.split()[-1]
        matches = (await call("/players", {"search": last_name, "per_page": 25}))["data"]
        hit = next(
            (p for p in matches if f"{p['first_name']} {p['last_name']}".lower() == full_name.lower()),
            None,
        )
        if hit:
            players[full_name] = hit
        else:
            res.warnings.append(f"player not found: {full_name}")
    res.data["israeli_players"] = players

    if players:
        try:
            stats = await call(
                "/stats",
                {"player_ids[]": [p["id"] for p in players.values()], "dates[]": yesterday, "per_page": 100},
            )
            res.data["israeli_player_stats"] = stats["data"]
        except httpx.HTTPStatusError as e:
            if e.response.status_code not in (401, 403):
                raise
            res.warnings.append("box-score stats need a paid balldontlie tier; skipped")
