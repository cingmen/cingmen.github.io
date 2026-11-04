#!/usr/bin/env python3
"""Static checks for the portfolio site.

Validates local links, in-page anchors, duplicate ids, image alt text, page
headings/descriptions, RSS feed targets and sitemap entries. Exits non-zero
when anything is broken so CI can gate a deploy.
"""
import os
import sys
import glob
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://cingmen.github.io"
SM_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"


class Doc(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.hrefs = []
        self.imgs = []
        self.h1 = 0
        self.has_description = False
        self.has_canonical = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.append(a["id"])
        if tag == "a" and a.get("href"):
            self.hrefs.append(a["href"])
        if tag in ("img", "script", "source"):
            if a.get("src"):
                self.hrefs.append(a["src"])
            if tag == "img":
                self.imgs.append(a)
        if tag == "link":
            if a.get("href"):
                self.hrefs.append(a["href"])
            if a.get("rel") == "canonical":
                self.has_canonical = True
        if tag == "h1":
            self.h1 += 1
        if tag == "meta" and a.get("name") == "description" and a.get("content", "").strip():
            self.has_description = True


def page_path(url):
    """Map an absolute site URL to a path inside the repository."""
    parsed = urlparse(url)
    if parsed.netloc and parsed.netloc != urlparse(SITE).netloc:
        return None
    path = unquote(parsed.path).lstrip("/") or "index.html"
    if path.endswith("/"):
        path += "index.html"
    return path, parsed.fragment


def main():
    errors = []
    docs = {}

    html_files = sorted(
        glob.glob(os.path.join(ROOT, "*.html"))
        + glob.glob(os.path.join(ROOT, "projects", "*.html"))
        + glob.glob(os.path.join(ROOT, "writeups", "*.html"))
    )
    if not html_files:
        errors.append("no HTML files found")

    for path in html_files:
        rel_name = os.path.relpath(path, ROOT)
        page_dir = os.path.dirname(path)
        doc = Doc()
        with open(path, encoding="utf-8") as fh:
            doc.feed(fh.read())
        docs[rel_name] = doc

        dupes = sorted({i for i in doc.ids if doc.ids.count(i) > 1})
        if dupes:
            errors.append(f"{rel_name}: duplicate id(s) {dupes}")

        if doc.h1 != 1:
            errors.append(f"{rel_name}: expected exactly one <h1>, found {doc.h1}")
        if not doc.has_description:
            errors.append(f"{rel_name}: missing meta description")
        if rel_name != "404.html" and not doc.has_canonical:
            errors.append(f"{rel_name}: missing rel=canonical")

        for img in doc.imgs:
            if img.get("alt") is None:
                errors.append(f"{rel_name}: <img src={img.get('src')!r}> has no alt attribute")

        for href in doc.hrefs:
            if not href or href.startswith(("mailto:", "tel:", "data:", "javascript:")):
                continue
            parsed = urlparse(href)
            if parsed.scheme in ("http", "https"):
                if parsed.netloc != urlparse(SITE).netloc:
                    continue
                local = page_path(href)
                if local and not os.path.exists(os.path.join(ROOT, local[0])):
                    errors.append(f"{rel_name}: absolute link to missing page {href}")
                continue
            if href.startswith("/"):
                # Root-relative links point at sibling project pages or root files.
                continue
            if href.startswith("#"):
                anchor = href[1:]
                if anchor and anchor not in doc.ids:
                    errors.append(f"{rel_name}: missing anchor {href}")
                continue
            target, _, anchor = href.partition("#")
            target = target.split("?")[0]
            if not target:
                continue
            resolved = os.path.normpath(os.path.join(page_dir, target))
            if not os.path.exists(resolved):
                errors.append(f"{rel_name}: broken local link {href}")
                continue
            if anchor:
                target_rel = os.path.relpath(resolved, ROOT)
                if target_rel in docs and anchor not in docs[target_rel].ids:
                    errors.append(f"{rel_name}: link {href} points at missing anchor #{anchor}")

    # RSS feed: every item must resolve to a real page, and a real anchor when given.
    feed_path = os.path.join(ROOT, "feed.xml")
    if os.path.exists(feed_path):
        try:
            root = ET.parse(feed_path).getroot()
        except ET.ParseError as exc:
            errors.append(f"feed.xml: invalid XML ({exc})")
        else:
            for item in root.findall(".//item"):
                title = (item.findtext("title") or "").strip() or "(untitled)"
                link = item.findtext("link") or ""
                local = page_path(link)
                if not local:
                    errors.append(f"feed.xml: item {title!r} links off-site: {link}")
                    continue
                target, anchor = local
                if not os.path.exists(os.path.join(ROOT, target)):
                    errors.append(f"feed.xml: item {title!r} links to missing page {link}")
                elif anchor:
                    doc = docs.get(target)
                    if doc is None:
                        with open(os.path.join(ROOT, target), encoding="utf-8") as fh:
                            doc = Doc()
                            doc.feed(fh.read())
                    if anchor not in doc.ids:
                        errors.append(f"feed.xml: item {title!r} links to missing anchor #{anchor}")

    # Sitemap: entries must exist and must not advertise the 404 page.
    sitemap_path = os.path.join(ROOT, "sitemap.xml")
    if os.path.exists(sitemap_path):
        try:
            root = ET.parse(sitemap_path).getroot()
        except ET.ParseError as exc:
            errors.append(f"sitemap.xml: invalid XML ({exc})")
        else:
            for loc in root.findall(f"{SM_NS}url/{SM_NS}loc"):
                url = (loc.text or "").strip()
                local = page_path(url)
                if not local:
                    errors.append(f"sitemap.xml: off-site entry {url}")
                    continue
                target = local[0]
                if "404" in target:
                    errors.append(f"sitemap.xml: 404 page must not be listed ({url})")
                if not os.path.exists(os.path.join(ROOT, target)):
                    errors.append(f"sitemap.xml: entry points at missing file {url}")

    if errors:
        print(f"FAILED — {len(errors)} problem(s):")
        for err in errors:
            print(f"  - {err}")
        return 1

    print(f"OK — {len(html_files)} pages, feed and sitemap are consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
