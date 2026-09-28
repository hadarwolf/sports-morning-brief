"use client";

import { useEffect, useMemo, useState } from "react";

import { loadBrief, loadIndex } from "@/lib/data";
import { useStored } from "@/lib/storage";
import type { Brief, Lang, Length, Section } from "@/lib/types";

import { IsraeliPlayers, Markets, MatchDayBanner } from "./Extras";
import { StoryCard } from "./StoryCard";

const LENGTHS: { id: Length; label: string; hint: string }[] = [
  { id: "scroll", label: "Scroll", hint: "30s" },
  { id: "coffee", label: "Coffee", hint: "3m" },
  { id: "deep", label: "Deep", hint: "10m" },
];

type State = { status: "loading" } | { status: "empty" } | { status: "error"; message: string } | { status: "ready"; brief: Brief };

function formatDate(iso: string): string {
  return new Date(`${iso}T12:00:00`).toLocaleDateString("en-GB", { weekday: "long", day: "numeric", month: "long" });
}

export function BriefApp() {
  const [state, setState] = useState<State>({ status: "loading" });
  const [length, setLength] = useStored<Length>("length", "coffee");
  const [langOverrides, setLangOverrides] = useStored<Record<string, Lang>>("section-lang", {});
  const [activeId, setActiveId] = useState<string | null>(null);

  useEffect(() => {
    loadIndex()
      .then((index) => (index.latest ? loadBrief(index.latest) : null))
      .then((brief) => setState(brief ? { status: "ready", brief } : { status: "empty" }))
      .catch((e: Error) => setState({ status: "error", message: e.message }));

    if ("serviceWorker" in navigator && process.env.NODE_ENV === "production") {
      navigator.serviceWorker.register("/sw.js").catch(() => {});
    }
  }, []);

  const sections = useMemo(() => {
    if (state.status !== "ready") return [];
    const byId = new Map(state.brief.sections.map((s) => [s.section, s]));
    return state.brief.meta.order.map((id) => byId.get(id)).filter((s): s is Section => Boolean(s));
  }, [state]);

  if (state.status === "loading") return <Centered>Loading today&apos;s brief…</Centered>;
  if (state.status === "empty") return <Centered>No brief yet. The first one arrives tomorrow morning.</Centered>;
  if (state.status === "error") return <Centered>Couldn&apos;t load the brief ({state.message}).</Centered>;

  const { meta } = state.brief;
  const active = sections.find((s) => s.section === activeId) ?? sections[0];
  const activeIndex = sections.indexOf(active);
  const next = sections[activeIndex + 1];
  const langOf = (s: Section): Lang => langOverrides[s.section] ?? s.default_lang;
  const lang = langOf(active);
  const title = (s: Section) => (langOf(s) === "he" ? s.title_he : s.title_en);

  const goTo = (id: string) => {
    setActiveId(id);
    window.scrollTo({ top: 0 });
  };

  return (
    <div className="mx-auto w-full max-w-xl pb-16">
      <header className="sticky top-0 z-10 border-b border-line bg-bg/90 px-4 pt-[max(env(safe-area-inset-top),0.75rem)] pb-3 backdrop-blur">
        <div className="flex items-baseline justify-between gap-3">
          <h1 className="text-lg font-bold tracking-tight">Daily Brief</h1>
          <p className="text-sm text-muted">{formatDate(meta.date)}</p>
        </div>

        <div className="mt-3 grid grid-cols-3 rounded-xl bg-card p-1 ring-1 ring-line" role="radiogroup" aria-label="Reading length">
          {LENGTHS.map((l) => (
            <button
              key={l.id}
              role="radio"
              aria-checked={length === l.id}
              onClick={() => setLength(l.id)}
              className={`rounded-lg py-1.5 text-sm font-medium transition-colors ${
                length === l.id ? "bg-accent text-accent-fg" : "text-muted"
              }`}
            >
              {l.label} <span className="text-xs opacity-75">{l.hint}</span>
            </button>
          ))}
        </div>

        <nav className="-mx-4 mt-3 overflow-x-auto px-4" aria-label="Sections">
          <ul className="flex gap-2">
            {sections.map((s) => (
              <li key={s.section}>
                <button
                  onClick={() => goTo(s.section)}
                  className={`whitespace-nowrap rounded-full px-3.5 py-1.5 text-sm font-medium ring-1 transition-colors ${
                    s === active ? "bg-fg text-bg ring-fg" : "ring-line text-muted"
                  }`}
                >
                  {title(s)}
                  {s.match_day?.is_match_day && " ⚽"}
                </button>
              </li>
            ))}
          </ul>
        </nav>
      </header>

      <main className="px-4 pt-5" dir={lang === "he" ? "rtl" : "ltr"} lang={lang}>
        <div className="flex items-center justify-between gap-3">
          <h2 className="text-2xl font-bold tracking-tight">{title(active)}</h2>
          <button
            onClick={() => setLangOverrides((prev) => ({ ...prev, [active.section]: lang === "he" ? "en" : "he" }))}
            className="rounded-full px-3 py-1 text-sm font-medium ring-1 ring-line"
            aria-label="Switch language"
          >
            {lang === "he" ? "English" : "עברית"}
          </button>
        </div>

        <div className="mt-4 space-y-4">
          {active.match_day && <MatchDayBanner matchDay={active.match_day} lang={lang} />}
          {active.markets && <Markets quotes={active.markets} />}
          {active.stories.map((story) => (
            <StoryCard key={story.id} story={story} lang={lang} length={length} />
          ))}
          {active.israeli_players && <IsraeliPlayers players={active.israeli_players} lang={lang} />}
        </div>

        {next && (
          <button
            onClick={() => goTo(next.section)}
            className="mt-6 w-full rounded-2xl bg-card py-4 text-center font-medium ring-1 ring-line"
            dir={langOf(next) === "he" ? "rtl" : "ltr"}
          >
            {langOf(next) === "he" ? `הבא: ${title(next)} ←` : `Next: ${title(next)} →`}
          </button>
        )}
      </main>
    </div>
  );
}

function Centered({ children }: { children: React.ReactNode }) {
  return <div className="flex min-h-dvh items-center justify-center px-8 text-center text-muted">{children}</div>;
}
