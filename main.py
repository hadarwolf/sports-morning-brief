"""
Sports Morning Brief — Phase 2

Reads config.json to know which teams the user follows (dynamic — anyone
can edit the config without touching code). Fetches league standings +
each favorite team's recent form, then asks an LLM (via Groq's free API,
running Meta's Llama model) to write a personalized natural-language brief.

Prints:
  1. The AI-written brief
  2. The raw JSON data (so you can see what the AI was working with)
"""

import os
import json
from datetime import datetime, timedelta, timezone
import requests
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

FOOTBALL_TOKEN = os.getenv("FOOTBALL_DATA_TOKEN")
BALLDONTLIE_TOKEN = os.getenv("BALLDONTLIE_TOKEN")
GROQ_KEY = os.getenv("GROQ_API_KEY")

FOOTBALL_BASE = "https://api.football-data.org/v4"
BALLDONTLIE_BASE = "https://api.balldontlie.io/v1"

# Which Groq model to use for the brief.
# llama-3.3-70b-versatile = best quality, still free
# llama-3.1-8b-instant    = faster, less rich prose
# See https://console.groq.com/docs/models for current model IDs
GROQ_MODEL = "llama-3.3-70b-versatile"


# --- Team lookup ---
# Maps a friendly team name (lowercase) to its football-data.org info.
# This is the "database" for now — you edit config.json with team NAMES,
# and this dict resolves them to IDs. Add more teams here as needed.
TEAM_LOOKUP = {
    # Premier League (code "PL")
    "arsenal": {"league_code": "PL", "team_id": 57, "league_name": "Premier League"},
    "aston villa": {"league_code": "PL", "team_id": 58, "league_name": "Premier League"},
    "chelsea": {"league_code": "PL", "team_id": 61, "league_name": "Premier League"},
    "everton": {"league_code": "PL", "team_id": 62, "league_name": "Premier League"},
    "fulham": {"league_code": "PL", "team_id": 63, "league_name": "Premier League"},
    "liverpool": {"league_code": "PL", "team_id": 64, "league_name": "Premier League"},
    "manchester city": {"league_code": "PL", "team_id": 65, "league_name": "Premier League"},
    "man city": {"league_code": "PL", "team_id": 65, "league_name": "Premier League"},
    "manchester united": {"league_code": "PL", "team_id": 66, "league_name": "Premier League"},
    "man united": {"league_code": "PL", "team_id": 66, "league_name": "Premier League"},
    "newcastle": {"league_code": "PL", "team_id": 67, "league_name": "Premier League"},
    "tottenham": {"league_code": "PL", "team_id": 73, "league_name": "Premier League"},
    "spurs": {"league_code": "PL", "team_id": 73, "league_name": "Premier League"},

    # La Liga (code "PD")
    "barcelona": {"league_code": "PD", "team_id": 81, "league_name": "La Liga"},
    "barça": {"league_code": "PD", "team_id": 81, "league_name": "La Liga"},
    "real madrid": {"league_code": "PD", "team_id": 86, "league_name": "La Liga"},
    "atletico madrid": {"league_code": "PD", "team_id": 78, "league_name": "La Liga"},
    "atleti": {"league_code": "PD", "team_id": 78, "league_name": "La Liga"},
    "sevilla": {"league_code": "PD", "team_id": 559, "league_name": "La Liga"},
    "valencia": {"league_code": "PD", "team_id": 95, "league_name": "La Liga"},
    "villarreal": {"league_code": "PD", "team_id": 94, "league_name": "La Liga"},
    "real betis": {"league_code": "PD", "team_id": 90, "league_name": "La Liga"},
    "real sociedad": {"league_code": "PD", "team_id": 92, "league_name": "La Liga"},
    "athletic": {"league_code": "PD", "team_id": 77, "league_name": "La Liga"},
}


# ---------- Data fetching ----------

def football_headers():
    return {"X-Auth-Token": FOOTBALL_TOKEN}


def summarize_standing_row(row: dict) -> dict:
    team = row["team"]
    return {
        "position": row["position"],
        "team_id": team["id"],
        "team": team.get("shortName") or team["name"],
        "played": row["playedGames"],
        "won": row["won"],
        "drawn": row["draw"],
        "lost": row["lost"],
        "goal_difference": row["goalDifference"],
        "points": row["points"],
        "form": row.get("form"),
    }


def summarize_football_match(match: dict) -> dict:
    return {
        "competition": match["competition"]["name"],
        "date_utc": match["utcDate"],
        "home": match["homeTeam"].get("shortName") or match["homeTeam"]["name"],
        "away": match["awayTeam"].get("shortName") or match["awayTeam"]["name"],
        "status": match["status"],
        "score": {
            "home": match["score"]["fullTime"]["home"],
            "away": match["score"]["fullTime"]["away"],
        },
    }


def fetch_league_standings(league_code: str) -> list:
    resp = requests.get(
        f"{FOOTBALL_BASE}/competitions/{league_code}/standings",
        headers=football_headers(),
    )
    resp.raise_for_status()
    return [summarize_standing_row(row) for row in resp.json()["standings"][0]["table"]]


def fetch_team_recent(team_id: int) -> dict:
    """Get the last 5 finished matches + next scheduled match for a team."""
    headers = football_headers()

    last5 = requests.get(
        f"{FOOTBALL_BASE}/teams/{team_id}/matches",
        headers=headers,
        params={"status": "FINISHED", "limit": 5},
    )
    last5.raise_for_status()

    nxt = requests.get(
        f"{FOOTBALL_BASE}/teams/{team_id}/matches",
        headers=headers,
        params={"status": "SCHEDULED", "limit": 1},
    )
    nxt.raise_for_status()
    next_matches = nxt.json().get("matches", [])

    return {
        "last_5_matches": [summarize_football_match(m) for m in last5.json().get("matches", [])],
        "next_match": summarize_football_match(next_matches[0]) if next_matches else None,
    }


def summarize_nba_game(game: dict) -> dict:
    return {
        "date": game["date"],
        "status": game["status"],
        "home_team": game["home_team"]["full_name"],
        "away_team": game["visitor_team"]["full_name"],
        "home_score": game["home_team_score"],
        "away_score": game["visitor_team_score"],
    }


def fetch_nba_yesterday() -> list:
    yesterday = (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%d")
    resp = requests.get(
        f"{BALLDONTLIE_BASE}/games",
        headers={"Authorization": BALLDONTLIE_TOKEN},
        params={"dates[]": yesterday, "per_page": 25},
    )
    resp.raise_for_status()
    return [summarize_nba_game(g) for g in resp.json().get("data", [])]


# ---------- Config + assembly ----------

def load_config() -> dict:
    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)


def build_brief_data(config: dict) -> dict:
    """Turn a config into a full data dict ready to hand to the LLM."""
    brief = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "football": [],
        "nba_yesterday": [],
        "unknown_teams": [],
    }

    # Resolve each team name from config into (league_code, team_id, etc.)
    resolved = []
    for name in config.get("football_teams", []):
        info = TEAM_LOOKUP.get(name.strip().lower())
        if info:
            resolved.append({"name": name, **info})
        else:
            brief["unknown_teams"].append(name)

    # Group favorite teams by league so we only fetch each league's standings once
    leagues_seen = {}
    for team in resolved:
        code = team["league_code"]
        if code not in leagues_seen:
            leagues_seen[code] = {
                "code": code,
                "name": team["league_name"],
                "favorite_teams": [],
            }
        leagues_seen[code]["favorite_teams"].append(team)

    # For each league, fetch standings once, then extra detail per fav team
    for league in leagues_seen.values():
        try:
            standings = fetch_league_standings(league["code"])
        except requests.HTTPError as e:
            brief["football"].append({"league": league["name"], "error": str(e)})
            continue

        fav_details = []
        for team in league["favorite_teams"]:
            try:
                recent = fetch_team_recent(team["team_id"])
            except requests.HTTPError as e:
                fav_details.append({"team": team["name"], "error": str(e)})
                continue
            row = next((r for r in standings if r["team_id"] == team["team_id"]), None)
            fav_details.append({
                "team": team["name"],
                "position": row["position"] if row else None,
                "points": row["points"] if row else None,
                "played": row["played"] if row else None,
                "recent_form": row["form"] if row else None,
                **recent,
            })

        brief["football"].append({
            "league": league["name"],
            "favorite_teams": [t["name"] for t in league["favorite_teams"]],
            "standings": standings,
            "favorite_details": fav_details,
        })

    # NBA
    try:
        brief["nba_yesterday"] = fetch_nba_yesterday()
    except requests.HTTPError as e:
        brief["nba_yesterday"] = {"error": str(e)}

    return brief


# ---------- AI brief ----------

def write_ai_brief(brief_data: dict, style: str, language: str) -> str:
    """Send the raw data to Groq (Llama) and get back a natural-language brief."""
    client = Groq(api_key=GROQ_KEY)

    prompt = f"""You are writing a personalized morning sports brief for a fan.

Their preferred style: {style}
Language: {language}

Here is the raw data (JSON):
{json.dumps(brief_data, indent=2, ensure_ascii=False)}

Write the brief. Cover, in this order:
1. What each favorite team did most recently and how it went (be specific about scores + opponents)
2. Where they sit in the league table right now and what that means (title race, mid-table, etc.)
3. What's coming up next and who they're playing
4. If NBA data exists, one line on it. If it's empty (offseason), skip it entirely.

Rules:
- Skip corporate sports-writing clichés. Sound like a friend who knows the game.
- No bullet points, no headers — flowing paragraphs.
- Do NOT invent stats. If the data doesn't say it, don't say it.
- Ignore the "unknown_teams" field unless it's non-empty (then briefly warn the user).
"""

    response = client.chat.completions.create(
        model=GROQ_MODEL,
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


# ---------- Main ----------

def main():
    config = load_config()
    print("Fetching data...\n")
    brief_data = build_brief_data(config)

    print("Asking Llama (via Groq) to write the brief...\n")
    narrative = write_ai_brief(
        brief_data,
        style=config.get("brief_style", "friendly and concise"),
        language=config.get("language_hint", "English"),
    )

    print("=" * 60)
    print("MORNING BRIEF")
    print("=" * 60)
    print(narrative)
    print()
    print("=" * 60)
    print("RAW DATA (for debugging)")
    print("=" * 60)
    print(json.dumps(brief_data, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
