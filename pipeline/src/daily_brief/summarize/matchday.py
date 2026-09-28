"""Match-day mode: is a favorite team playing today (Israel date)? Pure data, no LLM."""

from __future__ import annotations

from datetime import date

from .inputs import israel_date


def detect_match_day(raw: dict[str, dict], sources_cfg: dict, today: date) -> dict:
    events = []

    fd = raw.get("football_data", {}).get("data", {})
    favorite_ids = set(sources_cfg.get("football_data", {}).get("favorite_teams", {}).values())
    for m in fd.get("matches_window", {}).get("matches", []):
        home, away = m["homeTeam"], m["awayTeam"]
        if {home["id"], away["id"]} & favorite_ids and israel_date(m["utcDate"]) == today:
            events.append({
                "sport": "soccer",
                "competition": m["competition"]["name"],
                "home": home.get("shortName") or home["name"],
                "away": away.get("shortName") or away["name"],
                "kickoff_utc": m["utcDate"],
            })

    for team in raw.get("thesportsdb", {}).get("data", {}).get("teams", {}).values():
        for e in team["next_events"]:
            ts = e.get("strTimestamp")
            if ts and israel_date(ts) == today:
                events.append({
                    "sport": "soccer",
                    "competition": e.get("strLeague"),
                    "home": e.get("strHomeTeam"),
                    "away": e.get("strAwayTeam"),
                    "kickoff_utc": ts,
                })

    # NBA: a game tonight (US date == Israel today) for an Israeli player's team.
    bdl = raw.get("balldontlie", {}).get("data", {})
    player_teams = {(p.get("team") or {}).get("id") for p in bdl.get("israeli_players", {}).values()}
    for g in bdl.get("games_today", []):
        if {g["home_team"]["id"], g["visitor_team"]["id"]} & player_teams:
            events.append({
                "sport": "nba",
                "competition": "NBA",
                "home": g["home_team"]["full_name"],
                "away": g["visitor_team"]["full_name"],
                "kickoff_utc": g.get("datetime") or g["date"],
            })

    return {"is_match_day": bool(events), "events": events}
