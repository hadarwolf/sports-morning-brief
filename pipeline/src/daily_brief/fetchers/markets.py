"""Markets snapshot via yfinance (unauthenticated Yahoo Finance)."""

from __future__ import annotations

import asyncio

from ..models import Context, SourceResult


def _snapshot(tickers: dict[str, str]) -> tuple[dict, list[str]]:
    import yfinance as yf  # slow import; only pay for it when this source runs

    out, warnings = {}, []
    for name, symbol in tickers.items():
        try:
            closes = yf.Ticker(symbol).history(period="10d", interval="1d", auto_adjust=False)["Close"].dropna()
            if len(closes) < 2:
                raise ValueError(f"only {len(closes)} closes returned")
            last, prev = float(closes.iloc[-1]), float(closes.iloc[-2])
            out[name] = {
                "symbol": symbol,
                "last": round(last, 4),
                "prev_close": round(prev, 4),
                "change_pct": round((last / prev - 1) * 100, 2),
                "as_of": closes.index[-1].date().isoformat(),
            }
        except Exception as e:  # yfinance raises a zoo of exception types
            warnings.append(f"{name} ({symbol}): {e}")
    return out, warnings


async def fetch(ctx: Context, res: SourceResult) -> None:
    tickers = ctx.sources["markets"]["tickers"]
    quotes, warnings = await asyncio.to_thread(_snapshot, tickers)
    if not quotes:
        raise RuntimeError("no quotes returned: " + "; ".join(warnings))
    res.data["quotes"] = quotes
    res.warnings.extend(warnings)
