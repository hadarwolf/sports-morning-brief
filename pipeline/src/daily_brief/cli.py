"""Command line entry point: `daily-brief fetch` / `daily-brief sources`."""

from __future__ import annotations

import argparse
import asyncio
import sys
from datetime import date, datetime

from .config import TZ, Settings, load_sources
from .fetchers import build_sources
from .runner import run_sources, write_results


def _select(sources, only: str | None, section: str | None):
    if only:
        wanted = {s.strip() for s in only.split(",")}
        unknown = wanted - {s.id for s in sources}
        if unknown:
            sys.exit(f"unknown source id(s): {', '.join(sorted(unknown))}")
        sources = [s for s in sources if s.id in wanted]
    if section:
        sources = [s for s in sources if s.section == section]
    return sources


def _print_report(results) -> None:
    width = max(len(r.source_id) for r in results)
    for r in sorted(results, key=lambda r: (r.section, r.source_id)):
        status = "OK  " if r.ok else "FAIL"
        detail = r.error if not r.ok else f"{r.count:>3} {'items' if r.kind == 'rss' else 'keys '}"
        line = f"{status} {r.section:<16} {r.source_id:<{width}} {r.elapsed_ms:>6}ms  {detail}"
        if r.warnings:
            line += "  ! " + "; ".join(r.warnings)
        print(line)
    ok = sum(r.ok for r in results)
    print(f"\n{ok}/{len(results)} sources OK")


def cmd_fetch(args) -> int:
    settings = Settings.from_env()
    cfg = load_sources()
    sources = _select(build_sources(cfg), args.only, args.section)
    if not sources:
        sys.exit("no sources selected")
    day = date.fromisoformat(args.date) if args.date else None

    results = asyncio.run(run_sources(sources, settings, cfg, today=day))
    _print_report(results)
    if not args.no_write:
        out_dir = write_results(results, settings.data_dir, day or _israel_today())
        print(f"wrote {out_dir}")
    return 1 if args.strict and not all(r.ok for r in results) else 0


def cmd_sources(args) -> int:
    for s in build_sources(load_sources()):
        print(f"{s.section:<16} {s.kind:<4} {s.id:<24} {s.description}")
    return 0


def _israel_today() -> date:
    return datetime.now(TZ).date()


def main(argv: list[str] | None = None) -> int:
    # Hebrew text in warnings/errors must not crash a cp1252 Windows console.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(prog="daily-brief")
    sub = parser.add_subparsers(dest="command", required=True)

    p_fetch = sub.add_parser("fetch", help="fetch all sources and dump raw JSON to data/raw/<date>/")
    p_fetch.add_argument("--only", help="comma-separated source ids")
    p_fetch.add_argument("--section", help="only sources in this section")
    p_fetch.add_argument("--date", help="Israel date to fetch for (YYYY-MM-DD); default today")
    p_fetch.add_argument("--no-write", action="store_true", help="connectivity check only")
    p_fetch.add_argument("--strict", action="store_true", help="exit 1 if any source fails")
    p_fetch.set_defaults(func=cmd_fetch)

    p_sources = sub.add_parser("sources", help="list configured sources")
    p_sources.set_defaults(func=cmd_sources)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
