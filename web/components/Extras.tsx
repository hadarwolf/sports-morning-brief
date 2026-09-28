import type { Lang, MatchDay, PlayerNote, Quote } from "@/lib/types";

// Section extras that aren't stories: markets line, match-day banner, Israeli players.

const MARKET_LABELS: Record<string, string> = {
  TA35: "TA-35",
  SP500: "S&P 500",
  USDILS: "USD/ILS",
  BRENT: "Brent",
  BTC: "BTC",
};

function formatQuote(name: string, q: Quote): string {
  if (name === "USDILS") return q.last.toFixed(3);
  if (name === "BTC") return `$${Math.round(q.last).toLocaleString("en-US")}`;
  if (name === "BRENT") return `$${q.last.toFixed(2)}`;
  return Math.round(q.last).toLocaleString("en-US");
}

export function Markets({ quotes }: { quotes: Record<string, Quote> }) {
  return (
    <div className="-mx-4 overflow-x-auto px-4" dir="ltr">
      <ul className="flex gap-2 pb-1">
        {Object.entries(quotes).map(([name, q]) => {
          const up = q.change_pct >= 0;
          return (
            <li key={name} className="shrink-0 rounded-xl bg-card px-3 py-2 ring-1 ring-line">
              <p className="text-xs text-muted">{MARKET_LABELS[name] ?? name}</p>
              <p className="text-sm font-semibold tabular-nums">
                {formatQuote(name, q)}{" "}
                <span className={up ? "text-up" : "text-down"}>
                  {up ? "▲" : "▼"} {Math.abs(q.change_pct).toFixed(2)}%
                </span>
              </p>
            </li>
          );
        })}
      </ul>
    </div>
  );
}

export function MatchDayBanner({ matchDay, lang }: { matchDay: MatchDay; lang: Lang }) {
  if (!matchDay.is_match_day) return null;
  const time = (iso: string | null) =>
    iso
      ? new Date(iso).toLocaleTimeString(lang === "he" ? "he-IL" : "en-GB", {
          hour: "2-digit",
          minute: "2-digit",
          timeZone: "Asia/Jerusalem",
        })
      : "";
  return (
    <div className="rounded-2xl bg-accent px-5 py-4 text-accent-fg">
      <p className="text-xs font-semibold uppercase tracking-wider opacity-90">{lang === "he" ? "יום משחק" : "Match day"}</p>
      <ul className="mt-1 space-y-0.5">
        {matchDay.events.map((e, i) => (
          <li key={i} className="font-medium" dir="ltr">
            {e.home} – {e.away} <span className="opacity-80">· {time(e.kickoff_utc)}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}

export function IsraeliPlayers({ players, lang }: { players: PlayerNote[]; lang: Lang }) {
  if (!players.length) return null;
  return (
    <section className="rounded-2xl bg-card p-5 ring-1 ring-line">
      <p className="text-xs font-medium uppercase tracking-wider text-accent">
        {lang === "he" ? "ישראלים ב-NBA" : "Israelis in the NBA"}
      </p>
      <ul className="mt-2 space-y-3">
        {players.map((p) => (
          <li key={p.name}>
            <p className="font-semibold">
              {p.name} <span className="text-sm font-normal text-muted">· {p.team}</span>
            </p>
            <p className="text-[0.95rem] leading-relaxed text-muted">{p[lang]}</p>
          </li>
        ))}
      </ul>
    </section>
  );
}
