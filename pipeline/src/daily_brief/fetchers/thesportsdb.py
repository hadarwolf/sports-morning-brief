"""TheSportsDB: last/next events for teams football-data's free tier doesn't cover
(Inter Miami / MLS, national teams)."""

from __future__ import annotations

from ..http import get
from ..models import Context, SourceResult


async def fetch(ctx: Context, res: SourceResult) -> None:
    base = f"https://www.thesportsdb.com/api/v1/json/{ctx.settings.thesportsdb_key}"

    async def call(endpoint: str, **params) -> dict:
        return (await get(ctx.client, f"{base}/{endpoint}", params=params)).json() or {}

    teams = {}
    for name, team_id in ctx.sources["thesportsdb"]["teams"].items():
        last = await call("eventslast.php", id=team_id)
        nxt = await call("eventsnext.php", id=team_id)
        teams[name] = {
            "team_id": team_id,
            "last_events": last.get("results") or [],
            "next_events": nxt.get("events") or [],
        }
        if not teams[name]["last_events"] and not teams[name]["next_events"]:
            res.warnings.append(f"{name}: no events returned")
    res.data["teams"] = teams
