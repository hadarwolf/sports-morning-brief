import Markdown from "react-markdown";

import type { Lang, Length, Story, StoryKind } from "@/lib/types";

const KIND_LABEL: Record<StoryKind, Record<Lang, string>> = {
  news: { en: "News", he: "חדשות" },
  analysis: { en: "Analysis", he: "ניתוח" },
  essay: { en: "Essay", he: "מאמר" },
  concept: { en: "Concept of the week", he: "מושג השבוע" },
  word: { en: "Word of the day", he: "מילת היום" },
  on_this_day: { en: "On this day", he: "היום בהיסטוריה" },
};

const SOURCES_LABEL: Record<Lang, string> = { en: "Sources", he: "מקורות" };

export function StoryCard({ story, lang, length }: { story: Story; lang: Lang; length: Length }) {
  const v = story[lang];
  return (
    <article className="rounded-2xl bg-card p-5 ring-1 ring-line">
      <p className="text-xs font-medium uppercase tracking-wider text-accent">{KIND_LABEL[story.kind][lang]}</p>
      <h2 className="mt-1.5 text-[1.3rem] font-semibold leading-snug text-balance">{v.headline}</h2>

      {length === "scroll" ? (
        <p className="mt-2 text-[1.02rem] leading-relaxed text-muted">{v.scroll}</p>
      ) : (
        <div className="prose-brief mt-3">
          <Markdown>{length === "coffee" ? v.coffee : v.deep}</Markdown>
        </div>
      )}

      {length !== "scroll" && story.sources.length > 0 && (
        <div className="mt-4 border-t border-line pt-3">
          <p className="text-xs font-medium text-muted">{SOURCES_LABEL[lang]}</p>
          <ul className="mt-1 space-y-1">
            {story.sources.map((s, i) => (
              <li key={i} className="text-sm leading-snug" dir="auto">
                {s.url ? (
                  <a href={s.url} target="_blank" rel="noopener noreferrer" className="text-accent underline-offset-2 hover:underline">
                    {s.outlet}
                  </a>
                ) : (
                  <span className="text-muted">{s.outlet}</span>
                )}
                <span className="text-muted"> · {s.title}</span>
              </li>
            ))}
          </ul>
        </div>
      )}
    </article>
  );
}
