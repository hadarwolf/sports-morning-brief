"""football-data.org v4: yesterday/today/tomorrow matches, big-5 standings, favorite teams.

Free tier allows 10 requests/minute, so calls are sequential and the total is kept
under that (1 matches window + N standings + M favorite teams).
"""

from __future__ import annotations

from datetime import timedelta

import httpx

from ..http import get
from ..models import ConfigError, Context, SourceResult

BASE = "https://api.football-data.org/v4"
RATE_WINDOW_S = 65  # quota resets per minute


async def fetch(ctx: Context, res: SourceResult) -> None:
    token = ctx.settings.football_data_token
    if not token:
        raise ConfigError("FOOTBALL_DATA_TOKEN not set")
    cfg = ctx.sources["football_data"]
    headers = {"X-Auth-Token": token}
    today = ctx.today

    async def call(path: str, params: dict | None = None) -> dict:
        return (await get(ctx.client, f"{BASE}{path}", params=params, headers=headers, max_wait=RATE_WINDOW_S)).json()

    # Every competition the plan covers, in one call. Also drives match-day mode.
    res.data["matches_window"] = await call(
        "/matches",
        {"dateFrom": (today - timedelta(days=1)).isoformat(), "dateTo": (today + timedelta(days=1)).isoformat()},
    )

    res.data["standings"] = {}
    for code in cfg["standings"]:
        try:
            res.data["standings"][code] = await call(f"/competitions/{code}/standings")
        except httpx.HTTPStatusError as e:
            res.warnings.append(f"standings {code}: HTTP {e.response.status_code}")

    window = cfg.get("favorite_window_days", 14)
    res.data["favorite_teams"] = {}
    for name, team_id in cfg["favorite_teams"].items():
        try:
            res.data["favorite_teams"][name] = await call(
                f"/teams/{team_id}/matches",
                {
                    "dateFrom": (today - timedelta(days=window)).isoformat(),
                    "dateTo": (today + timedelta(days=window)).isoformat(),
                },
            )
        except httpx.HTTPStatusError as e:
            res.warnings.append(f"team {name}: HTTP {e.response.status_code}")
