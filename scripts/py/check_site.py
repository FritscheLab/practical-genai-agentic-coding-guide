"""Check rendered local links, assets, and anchors without network access."""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class PageLinks(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.links: list[tuple[str, int]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"])
        for name in ("href", "src"):
            if values.get(name):
                self.links.append((values[name], self.getpos()[0]))


def check_site(root: Path, baseurl: str) -> list[str]:
    pages: dict[Path, PageLinks] = {}
    for path in sorted(root.rglob("*.html")):
        parsed = PageLinks()
        parsed.feed(path.read_text(encoding="utf-8"))
        pages[path] = parsed
    if not pages or not (root / "index.html").is_file():
        return [f"No built site with index.html found under {root}"]
    errors: list[str] = []
    prefix = "/" + baseurl.strip("/") if baseurl.strip("/") else ""
    for source, page in pages.items():
        source_url = prefix + "/" + source.relative_to(root).as_posix()
        for href, line in page.links:
            parts = urlsplit(href)
            if parts.scheme or parts.netloc:
                continue
            target_url = urlsplit(urljoin(source_url, href))
            path = unquote(target_url.path)
            if prefix and not (path == prefix or path.startswith(prefix + "/")):
                errors.append(f"{source.relative_to(root)}:{line}: link escapes the project base URL: {href}")
                continue
            relative = path[len(prefix):].lstrip("/")
            target = root / relative
            if target.is_dir():
                target /= "index.html"
            if not target.is_file():
                errors.append(f"{source.relative_to(root)}:{line}: missing target: {href}")
                continue
            fragment = unquote(target_url.fragment)
            if fragment and target in pages and fragment not in pages[target].ids:
                errors.append(f"{source.relative_to(root)}:{line}: missing anchor: {href}")
    print(f"Checked {len(pages)} rendered HTML pages.")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site_dir", type=Path)
    parser.add_argument("--baseurl", default="/practical-genai-agentic-coding-guide")
    args = parser.parse_args()
    errors = check_site(args.site_dir.resolve(), args.baseurl)
    if errors:
        print("\n".join(errors))
        return 1
    print("Local links, assets, and anchors passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
