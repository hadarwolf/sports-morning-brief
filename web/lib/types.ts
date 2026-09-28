// Mirrors the JSON written by `daily-brief assemble` (pipeline/src/daily_brief/summarize/).

export type Lang = "en" | "he";
export type Length = "scroll" | "coffee" | "deep";
export type StoryKind = "news" | "analysis" | "essay" | "concept" | "word" | "on_this_day";

export interface Versions {
  headline: string;
  scroll: string;
  coffee: string;
  deep: string;
}

export interface Source {
  outlet: string;
  title: string;
  url: string | null;
}

export interface Story {
  id: string;
  kind: StoryKind;
  en: Versions;
  he: Versions;
  sources: Source[];
  tags: string[];
}

export interface PlayerNote {
  name: string;
  team: string;
  en: string;
  he: string;
}

export interface MatchDayEvent {
  sport: "soccer" | "nba";
  competition: string | null;
  home: string | null;
  away: string | null;
  kickoff_utc: string | null;
}

export interface MatchDay {
  is_match_day: boolean;
  events: MatchDayEvent[];
}

export interface Quote {
  symbol: string;
  last: number;
  prev_close: number;
  change_pct: number;
  as_of: string;
}

export interface Section {
  section: string;
  date: string;
  title_en: string;
  title_he: string;
  default_lang: Lang;
  stories: Story[];
  israeli_players?: PlayerNote[];
  match_day?: MatchDay;
  markets?: Record<string, Quote> | null;
}

export interface QuizText {
  question: string;
  options: string[];
  explanation: string;
}

export interface QuizQuestion {
  id: string;
  section: string;
  story_id: string;
  answer_index: number;
  en: QuizText;
  he: QuizText;
}

export interface Quiz {
  date: string;
  questions: QuizQuestion[];
}

export interface BriefMeta {
  date: string;
  order: string[];
  match_day: MatchDay;
  sections: { id: string; title_en: string; title_he: string; default_lang: Lang; file: string }[];
  quiz: string | null;
}

export interface Brief {
  meta: BriefMeta;
  sections: Section[];
}
