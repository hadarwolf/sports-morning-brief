# ⚽ Sports Morning Brief

A tiny Python tool that reads the teams you follow, pulls their **league standings**, **recent form**, and **upcoming fixtures** (plus last night's **NBA** scores), and then asks an LLM to write you a personalized, natural-language morning brief — like a text from a mate who actually knows the game.

No dashboards, no doomscrolling. Just run it with your coffee.

```
============================================================
MORNING BRIEF
============================================================
Morning! Arsenal keep grinding it out — that 2-1 win over
Everton makes it three on the bounce, and it's lifted them to
2nd, just two points off top. Next up they host Chelsea on
Saturday, so clear your afternoon. Barça, meanwhile, had a
frustrating night...
```

## How it works

```
config.json  ──▶  fetch standings + form + fixtures  ──▶  LLM writes the brief
(your teams)      (football-data.org + balldontlie.io)     (Llama 3.3 via Groq)
```

1. **You** list the teams you follow in `config.json` (no code changes needed).
2. The script resolves those names to teams and fetches live data from two free sports APIs.
3. The raw data is handed to an LLM (Meta's **Llama 3.3 70B**, served free by **Groq**), which writes the brief in the style you asked for.
4. It prints the brief, followed by the raw JSON it was based on (so nothing is a black box).

## Setup

You'll need **Python 3.9+**.

```bash
# 1. Clone the repo
git clone https://github.com/hadarwolf/sports-morning-brief.git
cd sports-morning-brief

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
# .venv\Scripts\activate       # Windows (PowerShell)

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your API keys (see below)
cp .env.example .env
# then open .env and paste in your keys

# 5. Run it
python main.py
```

## API keys

All three are **free**. Copy `.env.example` to `.env` and fill them in:

| Key | Where to get it | Notes |
| --- | --- | --- |
| `FOOTBALL_DATA_TOKEN` | [football-data.org](https://www.football-data.org/client/register) | Free tier: 10 requests/min |
| `BALLDONTLIE_TOKEN` | [balldontlie.io](https://app.balldontlie.io/) | Free NBA data |
| `GROQ_API_KEY` | [console.groq.com/keys](https://console.groq.com/keys) | Free LLM inference |

Your `.env` file is git-ignored and never committed.

## Configuration

Edit `config.json` — no code required:

```json
{
  "football_teams": ["Arsenal", "Barcelona"],
  "nba_teams": [],
  "brief_style": "friendly and knowledgeable, like a mate who really knows football. Keep it under 200 words.",
  "language_hint": "English"
}
```

- **`football_teams`** — friendly names of the teams you follow. Supported clubs are listed in `TEAM_LOOKUP` in [`main.py`](main.py) (most of the Premier League and La Liga's big names, plus common nicknames like "Spurs" or "Barça"). Add more by dropping their [football-data.org](https://www.football-data.org/) team ID into that dict.
- **`brief_style`** — tell the LLM how to write. Casual, punchy, detailed — your call.
- **`language_hint`** — e.g. `"English"`, `"Hebrew"`, `"Spanish"`.

## Supported leagues

- 🏴 Premier League
- 🇪🇸 La Liga
- 🏀 NBA (last night's scores)

## Tech

- **Python** — `requests` for the APIs, `python-dotenv` for secrets
- **[football-data.org](https://www.football-data.org/)** — standings, form, fixtures
- **[balldontlie.io](https://www.balldontlie.io/)** — NBA scores
- **[Groq](https://groq.com/)** running Meta's **Llama 3.3 70B** — the natural-language brief

## Roadmap

- [x] Fetch live sports data as structured JSON
- [x] Feed it to an LLM for a natural-language brief
- [ ] More leagues (Serie A, Bundesliga, Champions League)
- [ ] Web dashboard (Next.js + Tailwind)
- [ ] Daily automation (GitHub Actions → email/Telegram)

## License

[MIT](LICENSE) — do whatever you like with it.
