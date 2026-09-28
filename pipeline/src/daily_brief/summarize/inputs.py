"""Turn data/raw/<date>/ into compact, per-section inputs for Claude.

Every citable item gets a ref id ("bbc_world#3"). Claude cites refs, never URLs;
links are resolved from the refs afterwards, so they can't be hallucinated.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

from ..config import TZ

SUMMARY_CHARS = 400  # per RSS item; titles carry most of the signal


@dataclass
class Ref:
    outlet: str
    title: str
    url: str | None = None


@dataclass
class SectionInput:
    section: str
    payload: dict  # JSON-serializable; this is what Claude sees
    refs: dict[str, Ref] = field(default_factory=dict)


def load_raw(raw_dir: Path) -> dict[str, dict]:
    """source_id -> result envelope, for every source that succeeded."""
    out = {}
    for path in sorted(raw_dir.glob("*.json")):
        if path.name.startswith("_"):
            continue
        res = json.loads(path.read_text(encoding="utf-8"))
        if res.get("ok"):
            out[res["source_id"]] = res
    return out


def _rss_block(raw: dict, section: str, feed_names: dict[str, str], inp: SectionInput) -> list[dict]:
    feeds = []
    for source_id, res in raw.items():
        if res["kind"] != "rss" or res["section"] != section or not res["items"]:
            continue
        outlet = feed_names.get(source_id, source_id)
        items = []
        for i, item in enumerate(res["items"]):
            ref = f"{source_id}#{i}"
            inp.refs[ref] = Ref(outlet=outlet, title=item["title"], url=item["url"])
            entry = {"ref": ref, "title": item["title"], "published": item["published"]}
            if item["summary"] and item["summary"] != item["title"]:
                entry["summary"] = item["summary"][:SUMMARY_CHARS]
            items.append(entry)
        feeds.append({"outlet": outlet, "lang": res["items"][0]["lang"], "items": items})
    return feeds


# ---------------------------------------------------------------- sports helpers


def israel_date(utc_iso: str) -> date:
    """Israel calendar date of a UTC timestamp (naive timestamps are taken as UTC)."""
    dt = datetime.fromisoformat(utc_iso.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(TZ).date()


def _fd_match(m: dict) -> dict:
    score = m["score"]["fullTime"]
    return {
        "competition": m["competition"]["name"],
        "kickoff_utc": m["utcDate"],
        "home": m["homeTeam"].get("shortName") or m["homeTeam"]["name"],
        "away": m["awayTeam"].get("shortName") or m["awayTeam"]["name"],
        "status": m["status"],
        "score": f"{score['home']}-{score['away']}" if score["home"] is not None else None,
    }


def _fd_block(fd: dict, favorite_ids: dict[str, int], today: date) -> dict:
    matches = fd.get("matches_window", {}).get("matches", [])
    yesterday = today - timedelta(days=1)
    by_day = {"yesterday": [], "today": [], "tomorrow": []}
    for m in matches:
        d = israel_date(m["utcDate"])
        key = "yesterday" if d == yesterday else "today" if d == today else "tomorrow" if d > today else None
        if key:
            by_day[key].append(_fd_match(m))

    fav_ids = set(favorite_ids.values())
    standings = {}
    for code, payload in fd.get("standings", {}).items():
        table = payload["standings"][0]["table"]
        rows = [
            {
                "pos": r["position"],
                "team": r["team"].get("shortName") or r["team"]["name"],
                "played": r["playedGames"],
                "pts": r["points"],
                "gd": r["goalDifference"],
                **({"form": r["form"]} if r.get("form") else {}),
            }
            for r in table
            if r["position"] <= 6 or r["team"]["id"] in fav_ids
        ]
        standings[payload["competition"]["name"]] = rows

    favorites = {}
    for name, payload in fd.get("favorite_teams", {}).items():
        ms = [_fd_match(m) for m in payload.get("matches", [])]
        favorites[name] = {
            "recent": [m for m in ms if m["status"] == "FINISHED"][-3:],
            "upcoming": [m for m in ms if m["status"] != "FINISHED"][:2],
        }
    return {"matches": by_day, "standings_top6_plus_favorites": standings, "favorite_teams": favorites}


def _nba_game(g: dict) -> dict:
    return {
        "home": g["home_team"]["full_name"],
        "away": g["visitor_team"]["full_name"],
        "score": f"{g['home_team_score']}-{g['visitor_team_score']}" if g["home_team_score"] else None,
        "status": g["status"],
    }


def _nba_block(bdl: dict) -> dict:
    players = {
        name: {"team": (p.get("team") or {}).get("full_name"), "position": p.get("position")}
        for name, p in bdl.get("israeli_players", {}).items()
    }
    return {
        "games_last_night": [_nba_game(g) for g in bdl.get("games", [])],
        "games_today": [_nba_game(g) for g in bdl.get("games_today", [])],
        "israeli_players": players,
        "israeli_player_box_scores": bdl.get("israeli_player_stats"),  # None on the free tier
    }


def _tsdb_event(e: dict) -> dict:
    score = f"{e['intHomeScore']}-{e['intAwayScore']}" if e.get("intHomeScore") not in (None, "") else None
    return {
        "competition": e.get("strLeague"),
        "kickoff_utc": e.get("strTimestamp"),
        "home": e.get("strHomeTeam"),
        "away": e.get("strAwayTeam"),
        "score": score,
    }


def _tsdb_block(tsdb: dict) -> dict:
    return {
        name: {
            "recent": [_tsdb_event(e) for e in t["last_events"][:2]],
            "upcoming": [_tsdb_event(e) for e in t["next_events"][:2]],
        }
        for name, t in tsdb.get("teams", {}).items()
    }


# ---------------------------------------------------------------- builders


def build_inputs(raw: dict[str, dict], today: date, sources_cfg: dict, history: dict[str, list[str]]) -> dict[str, SectionInput]:
    feed_names = {f["id"]: f.get("name", f["id"]) for f in sources_cfg.get("rss", [])}
    data = lambda sid: raw.get(sid, {}).get("data", {})  # noqa: E731
    inputs: dict[str, SectionInput] = {}

    for section in ("geopolitics", "israeli_politics", "business", "ideas"):
        inp = SectionInput(section, {})
        inp.payload["news_feeds" if section != "ideas" else "candidates"] = _rss_block(raw, section, feed_names, inp)
        inputs[section] = inp

    inputs["business"].payload["markets_snapshot"] = data("markets").get("quotes")
    inputs["business"].payload["recent_weekly_concepts"] = history.get("concept", [])
    inputs["ideas"].payload["recently_featured"] = history.get("essay", [])

    sports = SectionInput("sports", {})
    favorite_ids = sources_cfg.get("football_data", {}).get("favorite_teams", {})
    if "football_data" in raw:
        sports.refs["football_data"] = Ref("football-data.org", "Match data & standings")
        sports.payload["european_soccer_data"] = _fd_block(data("football_data"), favorite_ids, today)
    if "balldontlie" in raw:
        sports.refs["balldontlie"] = Ref("balldontlie.io", "NBA games")
        sports.payload["nba_data"] = _nba_block(data("balldontlie"))
    if "thesportsdb" in raw:
        sports.refs["thesportsdb"] = Ref("TheSportsDB", "Inter Miami & Israel national team")
        sports.payload["inter_miami_and_israel_national_team"] = _tsdb_block(data("thesportsdb"))
    sports.payload["news_feeds"] = _rss_block(raw, "sports", feed_names, sports)
    inputs["sports"] = sports

    learn = SectionInput("learn", {})
    events = []
    for i, e in enumerate(data("wikipedia").get("en", [])):
        ref = f"wikipedia#{i}"
        url = next((p["url"] for p in e["pages"] if p.get("url")), None)
        learn.refs[ref] = Ref("Wikipedia", f"{e['year']}: {e['text']}", url)
        events.append({"ref": ref, "year": e["year"], "text": e["text"], "context": [p["extract"] for p in e["pages"][:1]]})
    learn.payload["on_this_day_candidates"] = events
    learn.payload["recent_words_and_concepts"] = history.get("word", [])
    inputs["learn"] = learn

    return inputs


def load_history(briefs_dir: Path, today: date, days: int = 30) -> dict[str, list[str]]:
    """Recent headlines by story kind, so rotating items (word of the day, weekly
    concept, featured essay) don't repeat."""
    history: dict[str, list[str]] = {}
    for back in range(1, days + 1):
        day_dir = briefs_dir / (today - timedelta(days=back)).isoformat()
        for path in day_dir.glob("*.json") if day_dir.exists() else []:
            try:
                section = json.loads(path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                continue
            for story in section.get("stories", []) if isinstance(section, dict) else []:
                if story.get("kind") in ("word", "concept", "essay"):
                    history.setdefault(story["kind"], []).append(story["en"]["headline"])
    return history
