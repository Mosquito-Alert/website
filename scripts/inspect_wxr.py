#!/usr/bin/env python3
"""Quick inspection helpers for WordPress WXR exports."""
from __future__ import annotations

import argparse
import collections
import xml.etree.ElementTree as ET
from pathlib import Path

NS = {
    "content": "http://purl.org/rss/1.0/modules/content/",
    "dc": "http://purl.org/dc/elements/1.1/",
    "wp": "http://wordpress.org/export/1.2/",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Inspect a WXR file")
    parser.add_argument("wxr", type=Path, help="Path to export file")
    return parser.parse_args()


def load_items(path: Path):
    tree = ET.parse(path)
    channel = tree.getroot().find("channel")
    return [] if channel is None else channel.findall("item")


def summarize(items):
    totals = collections.Counter()
    statuses = collections.Counter()
    languages = collections.Counter()
    meta_keys = collections.Counter()
    for item in items:
        post_type = item.findtext("wp:post_type", namespaces=NS)
        status = item.findtext("wp:status", namespaces=NS)
        totals[post_type] += 1
        statuses[(post_type, status)] += 1
        for meta in item.findall("wp:postmeta", namespaces=NS):
            key = meta.findtext("wp:meta_key", namespaces=NS)
            val = meta.findtext("wp:meta_value", namespaces=NS)
            if key == "_locale" and val:
                languages[val] += 1
            if key:
                meta_keys[key] += 1
    print("Post types:")
    for key, value in totals.most_common():
        print(f"  {key}: {value}")
    print("\nStatus counts:")
    for (ptype, status), value in statuses.most_common():
        print(f"  {ptype} / {status}: {value}")
    print("\nLocales (_locale):")
    for key, value in languages.most_common():
        print(f"  {key}: {value}")
    print("\nTop meta keys:")
    for key, value in meta_keys.most_common(20):
        print(f"  {key}: {value}")


def main() -> None:
    args = parse_args()
    items = load_items(args.wxr)
    summarize(items)


if __name__ == "__main__":
    main()
