"""Settings (secrets from .env) and source definitions (from sources.toml)."""

from __future__ import annotations

import os
import tomllib
from dataclasses import dataclass
from pathlib import Path
from zoneinfo import ZoneInfo

from dotenv import load_dotenv

PIPELINE_DIR = Path(__file__).resolve().parents[2]
REPO_ROOT = PIPELINE_DIR.parent
SOURCES_FILE = PIPELINE_DIR / "sources.toml"

# The brief is generated for Israel mornings; "today" always means Israel's today.
TZ = ZoneInfo("Asia/Jerusalem")

# .env lives at the repo root (shared with the legacy main.py). Real env vars win,
# which is how GitHub Actions secrets get in.
load_dotenv(REPO_ROOT / ".env", override=False)


@dataclass(frozen=True)
class Settings:
    football_data_token: str | None
    balldontlie_token: str | None
    thesportsdb_key: str
    anthropic_api_key: str | None
    data_dir: Path

    @classmethod
    def from_env(cls) -> "Settings":
        return cls(
            football_data_token=os.getenv("FOOTBALL_DATA_TOKEN") or None,
            balldontlie_token=os.getenv("BALLDONTLIE_TOKEN") or None,
            # "123" is TheSportsDB's public free-tier key.
            thesportsdb_key=os.getenv("THESPORTSDB_KEY") or "123",
            anthropic_api_key=os.getenv("ANTHROPIC_API_KEY") or None,
            data_dir=Path(os.getenv("DATA_DIR") or REPO_ROOT / "data"),
        )


def load_sources(path: Path = SOURCES_FILE) -> dict:
    with open(path, "rb") as f:
        return tomllib.load(f)
