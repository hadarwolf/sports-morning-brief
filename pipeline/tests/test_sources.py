from daily_brief.config import load_sources
from daily_brief.fetchers import build_sources

SECTIONS = {"sports", "geopolitics", "israeli_politics", "business", "ideas", "learn"}


def test_sources_toml_is_valid_and_covers_every_section():
    sources = build_sources(load_sources())
    ids = [s.id for s in sources]
    assert len(ids) == len(set(ids)), "duplicate source ids"
    assert {s.section for s in sources} == SECTIONS
    for s in sources:
        assert s.section in SECTIONS, s.id


def test_disabled_sources_are_skipped():
    cfg = {
        "markets": {"enabled": False},
        "rss": [
            {"id": "on", "section": "ideas", "url": "https://x"},
            {"id": "off", "section": "ideas", "url": "https://y", "enabled": False},
        ],
    }
    ids = {s.id for s in build_sources(cfg)}
    assert "markets" not in ids
    assert "on" in ids and "off" not in ids
