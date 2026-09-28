"""Schemas for the drafts the daily Claude routine writes. `daily-brief assemble`
validates every draft against these and reports errors for the routine to fix."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

StoryKind = Literal["news", "analysis", "essay", "concept", "word", "on_this_day"]


class Strict(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Versions(Strict):
    """One story in one language, at all three reading lengths."""

    headline: str = Field(min_length=1)
    scroll: str = Field(min_length=1, description="~30-second version: one-sentence takeaway")
    coffee: str = Field(min_length=1, description="~3-minute version: 2-3 short paragraphs")
    deep: str = Field(min_length=1, description="~10-minute version: markdown write-up")


class Story(Strict):
    id: str = Field(min_length=1, description="short kebab-case slug, unique within the section")
    kind: StoryKind
    en: Versions
    he: Versions
    source_refs: list[str] = Field(description="ref ids of the input items this story is based on, e.g. 'bbc_world#3'")
    tags: list[str] = Field(description="2-4 lowercase topic tags, e.g. 'arsenal', 'iran', 'monetary-policy'")


class SectionOutput(Strict):
    stories: list[Story] = Field(min_length=1)


class PlayerNote(Strict):
    name: str = Field(min_length=1)
    team: str = Field(min_length=1)
    en: str = Field(min_length=1, description="1-2 sentences on the player's latest game/news, or that there is none")
    he: str = Field(min_length=1)


class SportsOutput(SectionOutput):
    israeli_players: list[PlayerNote]


class QuizText(Strict):
    question: str = Field(min_length=1)
    options: list[str] = Field(min_length=4, max_length=4, description="exactly 4 options")
    explanation: str = Field(min_length=1, description="one sentence explaining the right answer")


class QuizQuestion(Strict):
    id: str = Field(min_length=1)
    section: str = Field(min_length=1)
    story_id: str = Field(min_length=1)
    answer_index: int = Field(ge=0, le=3, description="0-based index of the correct option (same in both languages)")
    en: QuizText
    he: QuizText


class QuizOutput(Strict):
    questions: list[QuizQuestion] = Field(min_length=3, max_length=3)


SECTION_SCHEMAS: dict[str, type[SectionOutput]] = {
    "sports": SportsOutput,
    "geopolitics": SectionOutput,
    "israeli_politics": SectionOutput,
    "business": SectionOutput,
    "ideas": SectionOutput,
    "learn": SectionOutput,
}
SECTIONS = list(SECTION_SCHEMAS)
