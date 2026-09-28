"""Shared async HTTP client with small, polite retry logic."""

from __future__ import annotations

import asyncio

import httpx

USER_AGENT = "DailyBrief/0.1 (personal news digest; +https://github.com/hadarwolf/sports-morning-brief)"
# Some publishers 403 anything that doesn't look like a browser.
BROWSER_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/128.0 Safari/537.36"
)

RETRY_STATUS = {429, 500, 502, 503, 504}
DEFAULT_MAX_WAIT = 15.0


def make_client() -> httpx.AsyncClient:
    return httpx.AsyncClient(
        timeout=httpx.Timeout(25.0, connect=10.0),
        follow_redirects=True,
        headers={"User-Agent": USER_AGENT},
    )


def _retry_wait(resp: httpx.Response | None, attempt: int, max_wait: float) -> float:
    if resp is not None:
        retry_after = resp.headers.get("Retry-After") or resp.headers.get("X-RequestCounter-Reset")
        if retry_after and retry_after.isdigit():
            return min(float(retry_after) + 1, max_wait)
        if resp.status_code == 429:
            return max_wait
    return min(1.5 * 2**attempt, max_wait)


async def get(
    client: httpx.AsyncClient,
    url: str,
    *,
    params: dict | None = None,
    headers: dict | None = None,
    retries: int = 2,
    max_wait: float = DEFAULT_MAX_WAIT,
) -> httpx.Response:
    """GET with retries on transport errors and 429/5xx. Raises on final failure.

    Per-minute-quota APIs should pass max_wait ~65s so a 429 waits out the window.
    """
    for attempt in range(retries + 1):
        resp = None
        try:
            resp = await client.get(url, params=params, headers=headers)
        except httpx.TransportError:
            if attempt == retries:
                raise
        else:
            if resp.status_code not in RETRY_STATUS or attempt == retries:
                resp.raise_for_status()
                return resp
        await asyncio.sleep(_retry_wait(resp, attempt, max_wait))
    raise AssertionError("unreachable")
