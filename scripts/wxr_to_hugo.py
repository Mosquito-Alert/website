#!/usr/bin/env python3
"""Convert a WordPress WXR export into Hugo-friendly Markdown files.

This script deliberately keeps transformations simple so you can iterate safely.
- Front matter is emitted as YAML with a few common fields.
- HTML from the export is written verbatim; let Hugo render it or post-process later.
- Language is inferred from wp:postmeta (configurable) or falls back to a default.
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import textwrap
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, Iterable, List, Optional
from urllib.parse import urlparse

# Namespaces declare once for readability.
NS = {
    "content": "http://purl.org/rss/1.0/modules/content/",
    "dc": "http://purl.org/dc/elements/1.1/",
    "wp": "http://wordpress.org/export/1.2/",
}

LANG_CHOICES = ("es", "ca", "en")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert WordPress WXR export to Hugo content structure.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("wxr", type=Path, help="Path to the WordPress export (.xml)")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("content"),
        help="Hugo content directory to populate",
    )
    parser.add_argument(
        "--default-language",
        default="es",
        help="Fallback language code when no meta value is found.",
    )
    parser.add_argument(
        "--language-meta-key",
        default=None,
        help=(
            "Name of the wp:postmeta key holding the language code (e.g. _locale, "
            "wpml_language, polylang_language)."
        ),
    )
    parser.add_argument(
        "--translation-meta-key",
        default=None,
        help="Optional wp:postmeta key that groups translations (e.g. translation_group).",
    )
    parser.add_argument(
        "--type-map",
        nargs="*",
        default=["post=blog"],
        help=(
            "Mapping from WordPress post_type to Hugo section. "
            "Example: post=blog page=landing event=events"
        ),
    )
    parser.add_argument(
        "--filter-status",
        nargs="*",
        default=["publish", "draft"],
        help="List of WordPress statuses to include (e.g. publish draft future).",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Optional limit on number of items converted (useful for pilots).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Parse entries and report destinations without writing files.",
    )
    return parser.parse_args()


def build_type_map(pairs: Iterable[str]) -> Dict[str, str]:
    mapping: Dict[str, str] = {}
    for pair in pairs:
        if "=" not in pair:
            raise ValueError(f"Invalid type mapping '{pair}'. Use post=blog format.")
        src, dest = pair.split("=", 1)
        mapping[src.strip()] = dest.strip()
    return mapping


def parse_meta(item: ET.Element) -> Dict[str, str]:
    meta: Dict[str, str] = {}
    for meta_el in item.findall("wp:postmeta", NS):
        key_el = meta_el.find("wp:meta_key", NS)
        val_el = meta_el.find("wp:meta_value", NS)
        if key_el is None or key_el.text is None:
            continue
        key = key_el.text.strip()
        value = val_el.text.strip() if val_el is not None and val_el.text else ""
        meta[key] = value
    return meta


def parse_categories(item: ET.Element) -> Dict[str, List[str]]:
    taxonomies: Dict[str, List[str]] = {}
    for cat_el in item.findall("category"):
        domain = cat_el.get("domain") or "category"
        value = (cat_el.text or "").strip()
        if not value:
            continue
        taxonomies.setdefault(domain, []).append(value)
    return taxonomies


def iso_date(pub_date: Optional[str]) -> Optional[str]:
    if not pub_date:
        return None
    try:
        dt_obj = dt.datetime.strptime(pub_date, "%a, %d %b %Y %H:%M:%S %z")
        return dt_obj.isoformat()
    except ValueError:
        # Leave room for manual review rather than failing hard.
        return None


def parse_url_language(link: Optional[str], choices: Iterable[str]) -> Optional[str]:
    if not link:
        return None
    path = urlparse(link).path
    segments = [seg for seg in path.split("/") if seg]
    if segments:
        head = segments[0].lower()
        if head in choices:
            return head
    return None


def determine_language(link: Optional[str], meta: Dict[str, str], args: argparse.Namespace, choices: Iterable[str]) -> str:
    lang = parse_url_language(link, choices)
    if lang:
        return lang
    if args.language_meta_key and args.language_meta_key in meta:
        fallback = meta[args.language_meta_key].strip().lower()
        if fallback and fallback in choices:
            return fallback
    return args.default_language


def normalize_translation_key(link: Optional[str], slug: str, meta: Dict[str, str], args: argparse.Namespace, choices: Iterable[str]) -> Optional[str]:
    if args.translation_meta_key and args.translation_meta_key in meta:
        key = meta[args.translation_meta_key].strip()
        if key:
            return key
    duplicate_of = meta.get("_icl_lang_duplicate_of")
    if duplicate_of:
        return f"wpml-{duplicate_of}"
    old_slug = meta.get("_wp_old_slug")
    if old_slug:
        return old_slug
    if link:
        parsed = urlparse(link)
        segments = [seg for seg in parsed.path.split("/") if seg]
        if segments and segments[0].lower() in choices:
            segments = segments[1:]
        if segments:
            return segments[-1]
    return slug


def slugify(slug: Optional[str], title: Optional[str]) -> str:
    if slug:
        return slug
    if not title:
        return "untitled"
    cooked = "".join(ch.lower() if ch.isalnum() else "-" for ch in title)
    return "-".join(filter(None, cooked.split("-"))) or "untitled"


def hugo_path(base: Path, language: str, section: str, slug: str) -> Path:
    # Hugo expects directories per content item; use index.md naming for bundles.
    return base / language / section / slug / "index.md"


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def yaml_scalar(value: object) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    text = str(value)
    if text == "":
        return "''"
    if any(ch in text for ch in ":#{}[]\n\r\t\"' "):
        escaped = text.replace("\\", "\\\\").replace("\"", "\\\"")
        return f'"{escaped}"'
    return text


def to_front_matter(data: Dict[str, object]) -> str:
    # YAML front matter with standard ordering.
    lines = ["---"]
    for key in ["title", "date", "slug", "language", "draft", "translationKey", "author", "categories", "tags", "wordpress_id"]:
        if key not in data or data[key] in (None, [], ""):
            continue
        value = data[key]
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - {yaml_scalar(item)}")
        else:
            lines.append(f"{key}: {yaml_scalar(value)}")
    if data.get("meta"):
        lines.append("meta:")
        for mkey, mval in sorted(data["meta"].items()):
            lines.append(f"  {mkey}: {yaml_scalar(mval)}")
    lines.append("---")
    return "\n".join(lines)


def extract_items(tree: ET.ElementTree) -> Iterable[ET.Element]:
    channel = tree.getroot().find("channel")
    if channel is None:
        return []
    return channel.findall("item")


def main() -> None:
    args = parse_args()
    type_map = build_type_map(args.type_map)

    tree = ET.parse(args.wxr)
    items = extract_items(tree)

    count = 0
    for item in items:
        post_type = item.findtext("wp:post_type", namespaces=NS)
        if not post_type:
            continue
        if post_type not in type_map:
            continue
        status = item.findtext("wp:status", namespaces=NS)
        if status in {"auto-draft", "trash"}:
            continue
        if status not in args.filter_status:
            continue

        title = item.findtext("title")
        slug = slugify(item.findtext("wp:post_name", namespaces=NS), title)
        pub_date = iso_date(item.findtext("pubDate"))
        author = item.findtext("dc:creator", namespaces=NS)
        content_html = item.findtext("content:encoded", namespaces=NS) or ""
        meta = parse_meta(item)
        taxonomies = parse_categories(item)

        link = item.findtext("link")
        language = determine_language(link, meta, args, LANG_CHOICES)
        translation_key = normalize_translation_key(link, slug, meta, args, LANG_CHOICES)

        front_matter: Dict[str, object] = {
            "title": title or "",
            "date": pub_date,
            "slug": slug,
            "draft": status != "publish",
            "translationKey": translation_key,
            "author": author,
            "categories": taxonomies.get("category", []),
            "tags": taxonomies.get("post_tag", []),
            "wordpress_id": item.findtext("wp:post_id", namespaces=NS),
            "meta": meta,
            "language": language,
        }

        md_path = hugo_path(args.output, language, type_map[post_type], slug)
        count += 1
        if args.dry_run:
            print(f"Would write {md_path}")
        else:
            ensure_parent(md_path)
            with md_path.open("w", encoding="utf-8") as fh:
                fh.write(to_front_matter(front_matter))
                fh.write("\n\n")
                fh.write(content_html.strip())
                fh.write("\n")

        if args.limit is not None and count >= args.limit:
            break

    if args.dry_run:
        print("Dry run complete; nothing written.")


if __name__ == "__main__":
    main()
