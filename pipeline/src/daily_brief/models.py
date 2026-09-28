from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import date, datetime

import httpx

from .config import Settings


class ConfigError(Exception):
    """A source can't run because something (usually an API key) is missing."""


@dataclass
class Context:
    """Shared state handed to every fetcher."""

    client: httpx.AsyncClient
    settings: Settings
    sources: dict  # parsed sources.toml
    now: datetime  # tz-aware, Israel time
    today: date  # Israel date the brief is for


@dataclass
class SourceResult:
    source_id: str
    section: str
    kind: str  # "rss" | "api"
    ok: bool = True
    error: str | None = None
    warnings: list[str] = field(default_factory=list)
    fetched_at: str = ""
    elapsed_ms: int = 0
    items: list[dict] = field(default_factory=list)  # normalized articles (RSS)
    data: dict = field(default_factory=dict)  # API payloads, lightly trimmed

    @property
    def count(self) -> int:
        return len(self.items) if self.kind == "rss" else len(self.data)

    def to_dict(self) -> dict:
        return {**asdict(self), "count": self.count}
