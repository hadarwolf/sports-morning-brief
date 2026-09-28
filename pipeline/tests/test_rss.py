from datetime import datetime, timezone

import pytest

from daily_brief.fetchers.rss import clean_html, parse_feed

NOW = datetime(2026, 9, 28, 6, 0, tzinfo=timezone.utc)

FEED = b"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel><title>Test</title>
  <item>
    <title>Fresh &amp; relevant</title>
    <link>https://example.com/fresh</link>
    <pubDate>Mon, 28 Sep 2026 04:00:00 GMT</pubDate>
    <description>&lt;p&gt;Some &lt;b&gt;bold&lt;/b&gt;   text&lt;/p&gt;</description>
  </item>
  <item>
    <title>Newer</title>
    <link>https://example.com/newer</link>
    <pubDate>Mon, 28 Sep 2026 05:00:00 GMT</pubDate>
  </item>
  <item>
    <title>Stale</title>
    <link>https://example.com/stale</link>
    <pubDate>Mon, 21 Sep 2026 04:00:00 GMT</pubDate>
  </item>
  <item>
    <title>\xd7\x97\xd7\x93\xd7\xa9\xd7\x95\xd7\xaa</title>
    <link>https://example.com/undated</link>
  </item>
</channel></rss>"""


def test_clean_html_strips_tags_and_entities():
    assert clean_html("<p>Some <b>bold</b>&nbsp;&amp;   text</p>") == "Some bold & text"
    assert clean_html(None) == ""


def test_parse_feed_filters_sorts_and_normalizes():
    feed = {"id": "test", "lang": "he", "max_age_hours": 48}
    items, warnings = parse_feed(FEED, feed, NOW)

    assert [i["title"] for i in items] == ["Newer", "Fresh & relevant", "חדשות"]
    fresh = items[1]
    assert fresh["url"] == "https://example.com/fresh"
    assert fresh["summary"] == "Some bold text"
    assert fresh["published"] == "2026-09-28T04:00:00+00:00"
    assert fresh["source"] == "test" and fresh["lang"] == "he"
    assert warnings == ["1 entries had no date"]


def test_parse_feed_respects_max_items():
    items, _ = parse_feed(FEED, {"id": "t", "max_items": 1}, NOW)
    assert [i["title"] for i in items] == ["Newer"]


def test_parse_feed_all_stale_is_a_warning_not_an_error():
    old_only = b"""<rss version="2.0"><channel><title>T</title>
      <item><title>Old</title><link>https://x</link><pubDate>Mon, 21 Sep 2026 04:00:00 GMT</pubDate></item>
    </channel></rss>"""
    items, warnings = parse_feed(old_only, {"id": "t", "max_age_hours": 24}, NOW)
    assert items == []
    assert warnings and "older than 24h" in warnings[0]


def test_parse_feed_rejects_garbage():
    with pytest.raises(ValueError, match="unparseable"):
        parse_feed(b"<html>not a feed</html>", {"id": "t"}, NOW)
