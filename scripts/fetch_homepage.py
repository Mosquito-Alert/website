#!/usr/bin/env python3
"""Download the current WordPress homepage and core assets for reference."""
from __future__ import annotations

import argparse
import pathlib
import sys
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from typing import Iterable, Set

BASE_URL = "https://www.mosquitoalert.com/"
ALLOWED_HOSTS = {"www.mosquitoalert.com", "mosquitoalert.com"}


class AssetCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.assets: Set[str] = set()

    def handle_starttag(self, tag: str, attrs: Iterable[tuple[str, str]]) -> None:
        attr_map = {key.lower(): value for key, value in attrs if value}
        if tag == "link":
            rel = attr_map.get("rel", "").lower()
            if "stylesheet" in rel:
                href = attr_map.get("href")
                if href:
                    self.assets.add(href)
        elif tag == "script":
            src = attr_map.get("src")
            if src:
                self.assets.add(src)
        elif tag == "img":
            src = attr_map.get("src")
            if src and src.endswith((".png", ".jpg", ".jpeg", ".webp", ".svg")):
                self.assets.add(src)


def download(url: str, destination: pathlib.Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url) as response, destination.open("wb") as fh:
        fh.write(response.read())


def normalize_url(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme and parsed.netloc:
        if parsed.netloc not in ALLOWED_HOSTS:
            return ""
        return url
    return urllib.parse.urljoin(BASE_URL, url)


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch homepage HTML and assets")
    parser.add_argument(
        "--output",
        type=pathlib.Path,
        default=pathlib.Path("reference/wp_homepage"),
        help="Directory to store fetched files.",
    )
    args = parser.parse_args()

    args.output.mkdir(parents=True, exist_ok=True)
    homepage_path = args.output / "homepage.html"
    print(f"Downloading homepage to {homepage_path}")
    with urllib.request.urlopen(BASE_URL) as response, homepage_path.open("wb") as fh:
        html_bytes = response.read()
        fh.write(html_bytes)

    collector = AssetCollector()
    collector.feed(html_bytes.decode("utf-8", errors="ignore"))

    assets_downloaded = 0
    for asset in sorted(collector.assets):
        normalized = normalize_url(asset)
        if not normalized:
            continue
        parsed = urllib.parse.urlparse(normalized)
        rel_path = pathlib.Path(parsed.path.lstrip("/"))
        destination = args.output / rel_path
        try:
            print(f"→ {normalized}")
            download(normalized, destination)
            assets_downloaded += 1
        except Exception as exc:  # pragma: no cover - network errors
            print(f"  ! Failed to fetch {normalized}: {exc}")

    print(f"Fetched {assets_downloaded} assets.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
