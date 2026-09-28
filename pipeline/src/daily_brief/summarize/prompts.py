"""Prompts for each section. The reader profile and length targets live in brief.toml."""

from __future__ import annotations

import json
from datetime import date

LEARN_ROTATION = ["philosophy term", "economics concept", "English↔Hebrew vocabulary"]
IDEAS_ROTATION = ["philosophy", "psychology", "science", "a thought-provoking op-ed or essay"]


def system_prompt(brief_cfg: dict, today: date) -> str:
    lengths = brief_cfg["lengths"]
    return f"""You write the sections of a personal daily brief, read on a phone each morning.

<reader>
{brief_cfg["reader"]["profile"].strip()}
</reader>

Today is {today:%A, %d %B %Y} (Israel time).

<grounding>
- The input items are today's news and the source of truth for current events. Your training data is older than today, so never "correct" the input from memory: officeholders, rosters, standings, prices and alliances may have changed since. If you can't tell whether something is still true, leave it out.
- Every specific in your text (numbers, scores, quotes, dates, who holds which role) must come from the input. Background context (history, how an institution works, what a concept means) may come from your own knowledge, but only well-established facts.
- Many items have only a headline and a short snippet. Don't pad them into details you don't have. When the input is thin, a deep version can spend more of its length on context and less on the event itself.
- source_refs: list the ref ids of the input items each story draws on, using only ref ids that appear in the input.
- Politics: describe positions and moves, and attribute claims to whoever made them. No editorializing and no partisan framing.
</grounding>

<writing>
- Lengths. scroll: {lengths["scroll"]}. coffee: {lengths["coffee"]}. deep: {lengths["deep"]}.
- Write every story in both English (en) and Hebrew (he). Each version should read as if it was originally written in that language. The Hebrew should be natural modern Hebrew, not translationese. Use the usual Hebrew spellings of names (ארסנל, ברצלונה, דני אבדיה). For technical, business and economic terms, give the English term in parentheses the first time it appears, e.g. חפיר כלכלי (economic moat).
- Headlines are informative, not clickbait.
- The reader is smart and short on time. Skip filler openers, stacked hedges and emojis. Explain jargon once, briefly.
</writing>"""


def to_json(obj) -> str:
    # One value per line: the routine reads these with a tool that truncates very long lines.
    return json.dumps(obj, ensure_ascii=False, indent=1)


def section_prompt(section: str, inp, brief_cfg: dict, today: date, match_day: dict) -> str:
    cfg = brief_cfg["sections"][section]
    n = cfg["stories"]
    primary = "Hebrew" if cfg["default_lang"] == "he" else "English"
    body = SECTION_INSTRUCTIONS[section](n=n, today=today, match_day=match_day, primary=primary)
    return f"""{body}

This section opens in {primary} by default, so make the {primary} version your best writing.

Output: write `drafts/{section}.json` matching `schemas/{section}.schema.json`.

<input>
{to_json(inp.payload)}
</input>"""


def _sports(n, match_day, **_):
    md = (
        f"Today is a match day for the reader's teams: {to_json(match_day['events'])}. "
        "Lead with a preview of that game (what's at stake, form, table position)."
        if match_day["is_match_day"]
        else "No favorite team plays today."
    )
    return f"""Write the Sports section: {n} stories.

- Draw on European soccer (big-5 leagues, Champions League), Inter Miami / MLS, international soccer and the NBA.
- Arsenal and Barcelona always get a story if they played yesterday, play today or tomorrow, or have real news. Even on a quiet day, one story can cover where they stand: table, form and next fixture.
- Other clubs and leagues earn a slot only when their storyline is genuinely big.
- Include an NBA story only if there is meaningful NBA news. It may be the offseason.
- Results, fixtures and tables come from the structured data. Storylines come from the news feeds. Cite "football_data", "balldontlie" or "thesportsdb" as a source_ref when you use their data.
- {md}
- Fill israeli_players with one entry per player listed in nba_data.israeli_players, giving their latest game or news. If the input has nothing new on a player, say so plainly. Never invent stats. Box scores are often unavailable.
- Use kind "news" for everything in this section."""


def _geopolitics(n, **_):
    return f"""Write the Geopolitics section: {n} major world stories.

- Choose stories with real second-order effects: on conflicts, alliances, markets, energy, technology, or Israel's position.
- Don't just restate the headline. Give context: what led here, who wants what, and what changes next. Prefer stories that several outlets cover.
- Leave out Israeli domestic politics, which has its own section. Israel's wars and foreign relations are fine when they are the biggest world story.
- Use kind "analysis"."""


def _israeli_politics(n, **_):
    return f"""Write the Israeli Politics section: {n} developments in Israeli domestic politics.

- In scope: coalition and opposition moves, legislation, major policy shifts, elections and polls, and relations between the government, the courts and state institutions.
- Be strictly factual and non-partisan. Attribute every claim, and when a move is contested, present the main sides' positions fairly.
- Leave out crime, weather, accidents and pure security incidents unless they are driving a political development.
- Use kind "news"."""


def _business(n, today, **_):
    concept = ""
    if today.weekday() == 6:  # Sunday: first day of the Israeli week
        concept = """
- It's Sunday, so also write the weekly concept deep-dive as a second story with kind "concept". Pick one core idea (for example moats, network effects, monetary-policy transmission, price elasticity, comparative advantage), ideally one that today's story illustrates. Explain it from first principles with concrete examples. Its deep version is the centerpiece. Its source_refs may be empty. Don't repeat anything in recent_weekly_concepts."""
    return f"""Write the Business & Economics section: {n} substantive story.

- Choose a company move, an industry shift or a macro trend. It should teach how business or economics works, not just report that a price moved.
- Use kind "analysis".
- Use precise business and economics terminology; the reader wants fluency in it.
- markets_snapshot is context only. The app displays it separately, so don't write a markets story unless there is a genuine market event.{concept}"""


def _ideas(today, **_):
    rotation = IDEAS_ROTATION[today.toordinal() % len(IDEAS_ROTATION)]
    return f"""Write the Ideas section: one essay or long read, summarized.

Step 1: pick the essay.
- Choose the ONE candidate that best rewards this reader's time: substantive, idea-dense, and not news.
- It must be a written piece. Skip link roundups, videos, podcasts and short blog notes.
- Only candidates with a full_text_file can be summarized properly. Prefer those.
- Today's rotation theme is {rotation}. Prefer it if there is a strong candidate, but quality wins.
- Avoid anything in recently_featured.

Step 2: read the essay's full_text_file (under essays/) and summarize the author's argument faithfully. It is their argument, not yours.
- headline: the essay's core idea as a headline.
- scroll: the central claim.
- coffee: the argument, and why it's interesting.
- deep: a thorough walk through the argument's structure and key examples, followed by the strongest objection to it.
- Name the outlet and the author (if known) early in coffee and deep.
- Use kind "essay". source_refs is the essay's ref."""


def _learn(today, **_):
    rotation = LEARN_ROTATION[today.toordinal() % len(LEARN_ROTATION)]
    return f"""Write the Learn Something Small section: exactly 2 short stories.

1. Word or concept of the day (kind "word"). Today's rotation: {rotation}.
   - Choose something genuinely useful that isn't too basic for this reader. Don't repeat anything in recent_words_and_concepts.
   - headline: the term. For vocabulary, give the English word and its Hebrew equivalent.
   - scroll: a crisp definition.
   - coffee: an explanation with an example.
   - deep: 250-400 words (shorter than usual), covering origin or etymology, nuances, common confusions and usage examples.
   - source_refs: [].
2. On this day (kind "on_this_day").
   - Pick the most consequential or fascinating event from on_this_day_candidates.
   - The headline starts with the year.
   - coffee explains the context and why it mattered. deep is 250-400 words.
   - source_refs: the event's ref."""


SECTION_INSTRUCTIONS = {
    "sports": _sports,
    "geopolitics": _geopolitics,
    "israeli_politics": _israeli_politics,
    "business": _business,
    "ideas": _ideas,
    "learn": _learn,
}


QUIZ_PROMPT = """Write the quiz: exactly 3 multiple-choice questions on the drafts you just wrote. They test whether the reader retained today's brief, and the reader answers them tomorrow morning.

- Spread the questions across different sections.
- Test the most important facts or ideas (the ones worth remembering), not trivia like exact dates or minor numbers.
- Each question must be answerable from the coffee version of its story.
- Give 4 options with plausible distractors and exactly one correct answer.
- Provide en and he versions with the options in the same order, so answer_index works for both.
- story_id and section must match the story the question comes from.

Output: write `drafts/quiz.json` matching `schemas/quiz.schema.json`.
"""
