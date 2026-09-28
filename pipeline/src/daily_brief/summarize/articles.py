"""Best-effort article text extraction (no JS, no paywalls): collect <p> text,
preferring what's inside <article>."""

from __future__ import annotations

import re
from html.parser import HTMLParser

import httpx

from ..http import BROWSER_USER_AGENT, get

MIN_USEFUL_CHARS = 1500
MAX_CHARS = 60_000  # ~15k tokens; long essays get truncated at a paragraph boundary


class _ParagraphCollector(HTMLParser):
    SKIP = {"script", "style", "nav", "footer", "header", "aside", "form", "figcaption"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.article_paras: list[str] = []
        self.all_paras: list[str] = []
        self._in_article = 0
        self._skip = 0
        self._buf: list[str] | None = None

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self._skip += 1
        elif tag == "article":
            self._in_article += 1
        elif tag == "p" and not self._skip:
            self._buf = []

    def handle_endtag(self, tag):
        if tag in self.SKIP and self._skip:
            self._skip -= 1
        elif tag == "article" and self._in_article:
            self._in_article -= 1
        elif tag == "p" and self._buf is not None:
            text = re.sub(r"\s+", " ", "".join(self._buf)).strip()
            if len(text) > 40:
                self.all_paras.append(text)
                if self._in_article:
                    self.article_paras.append(text)
            self._buf = None

    def handle_data(self, data):
        if self._buf is not None and not self._skip:
            self._buf.append(data)


def extract_text(html: str) -> str:
    parser = _ParagraphCollector()
    parser.feed(html)
    paras = parser.article_paras if sum(map(len, parser.article_paras)) >= MIN_USEFUL_CHARS else parser.all_paras
    out, total = [], 0
    for p in paras:
        if total + len(p) > MAX_CHARS:
            break
        out.append(p)
        total += len(p)
    return "\n\n".join(out)


async def fetch_article_text(client: httpx.AsyncClient, url: str) -> str | None:
    """Article body text, or None if it couldn't be extracted usefully."""
    try:
        resp = await get(client, url, headers={"User-Agent": BROWSER_USER_AGENT}, retries=1)
    except httpx.HTTPError:
        return None
    text = extract_text(resp.text)
    return text if len(text) >= MIN_USEFUL_CHARS else None
