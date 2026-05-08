#!/usr/bin/env python3
"""
html_to_png.py — Convert any HTML file to a PNG image using headless Chromium.

Renders modern HTML/CSS/SVG (gradients, custom fonts, inline SVG, animations)
exactly as a real browser would, then captures it as a PNG.

Quick install
-------------
    pip install playwright
    playwright install chromium

Usage
-----
    # Basic — captures the whole page at 1200x1900 viewport
    python html_to_png.py poster.html

    # Custom output path
    python html_to_png.py poster.html -o output.png

    # Custom viewport (matches the .poster/.canvas div size)
    python html_to_png.py poster.html -W 1400 -H 1000

    # Capture ONLY a specific element (cleanest for posters/diagrams)
    python html_to_png.py poster.html --selector .poster
    python html_to_png.py diagram.html --selector .canvas

    # Full scrollable page (if content overflows the viewport)
    python html_to_png.py page.html --full-page

    # High-resolution export (2x = retina, 3x = print quality)
    python html_to_png.py poster.html --scale 3

    # Batch mode — convert every .html in current folder
    python html_to_png.py --batch .
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit(
        "[ERR] playwright is not installed.\n"
        "  Install it with:\n"
        "      pip install playwright\n"
        "      playwright install chromium\n"
    )


def html_to_png(
    html_path: Path,
    output_path: Path,
    width: int = 1200,
    height: int = 1900,
    selector: str | None = None,
    full_page: bool = False,
    scale: float = 2.0,
    wait_ms: int = 600,
    transparent: bool = False,
) -> Path:
    """
    Render an HTML file to a PNG.

    If `selector` is given, only that element is captured (best for posters
    where one wrapper div holds the whole design — set selector=".poster"
    or ".canvas"). Otherwise captures the viewport (or full page if
    `full_page=True`).
    """
    if not html_path.exists():
        raise FileNotFoundError(f"HTML file not found: {html_path}")

    file_url = html_path.resolve().as_uri()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": width, "height": height},
            device_scale_factor=scale,
        )
        page = context.new_page()
        page.goto(file_url, wait_until="networkidle")
        # Let fonts / SVG animations settle
        page.wait_for_timeout(wait_ms)

        screenshot_kwargs = {
            "path": str(output_path),
            "omit_background": transparent,
        }

        if selector:
            element = page.query_selector(selector)
            if element is None:
                browser.close()
                raise ValueError(
                    f"Selector '{selector}' not found in {html_path.name}"
                )
            element.screenshot(**screenshot_kwargs)
        elif full_page:
            page.screenshot(full_page=True, **screenshot_kwargs)
        else:
            page.screenshot(**screenshot_kwargs)

        browser.close()

    return output_path


# ---------- auto-detect helpers ---------------------------------------------

def _autodetect_size(html_path: Path) -> tuple[int, int] | None:
    """
    Peek into the HTML for the first .poster / .canvas style block and try
    to read width/height in pixels. Returns (w, h) or None if not found.
    """
    import re

    try:
        text = html_path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return None

    # Look for `.poster {... width:1200px; height:1900px; ...}` or `.canvas`
    for klass in (".poster", ".canvas"):
        pattern = re.compile(
            rf"{re.escape(klass)}\s*\{{([^}}]*)\}}",
            re.IGNORECASE | re.DOTALL,
        )
        m = pattern.search(text)
        if not m:
            continue
        body = m.group(1)
        w = re.search(r"width\s*:\s*(\d+)\s*px", body, re.IGNORECASE)
        h = re.search(r"height\s*:\s*(\d+)\s*px", body, re.IGNORECASE)
        if w and h:
            return int(w.group(1)), int(h.group(1))
    return None


def _autodetect_selector(html_path: Path) -> str | None:
    """Return '.poster' or '.canvas' if either appears in the file."""
    try:
        text = html_path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return None
    if 'class="poster"' in text or "class='poster'" in text:
        return ".poster"
    if 'class="canvas"' in text or "class='canvas'" in text:
        return ".canvas"
    return None


# ---------- CLI --------------------------------------------------------------

def _convert_one(args, html_path: Path) -> None:
    output = (
        args.output
        if args.output and not args.batch
        else html_path.with_suffix(".png")
    )

    width, height = args.width, args.height
    selector = args.selector

    # Auto-detect dimensions/selector unless user overrode them
    if args.auto:
        detected_size = _autodetect_size(html_path)
        if detected_size:
            width, height = detected_size
        if selector is None:
            selector = _autodetect_selector(html_path)

    print(f"-> {html_path.name}")
    print(f"   viewport: {width}x{height}  scale: {args.scale}x"
          + (f"  selector: {selector}" if selector else ""))

    html_to_png(
        html_path=html_path,
        output_path=output,
        width=width,
        height=height,
        selector=selector,
        full_page=args.full_page,
        scale=args.scale,
        wait_ms=args.wait,
        transparent=args.transparent,
    )

    size_kb = output.stat().st_size / 1024
    print(f"   [OK] {output.name}  ({size_kb:,.1f} KB)\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert HTML file(s) to PNG using headless Chromium.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "input",
        type=Path,
        help="Input HTML file (or folder when --batch is used)",
    )
    parser.add_argument("-o", "--output", type=Path, default=None,
                        help="Output PNG path (default: same name as input)")
    parser.add_argument("-W", "--width", type=int, default=1200,
                        help="Viewport width in CSS px (default: 1200)")
    parser.add_argument("-H", "--height", type=int, default=1900,
                        help="Viewport height in CSS px (default: 1900)")
    parser.add_argument("-s", "--selector", default=None,
                        help="CSS selector to capture only one element "
                             "(e.g. '.poster', '.canvas')")
    parser.add_argument("--full-page", action="store_true",
                        help="Capture the full scrollable page")
    parser.add_argument("--scale", type=float, default=2.0,
                        help="Device pixel ratio (1=normal, 2=retina, 3=print)")
    parser.add_argument("--wait", type=int, default=600,
                        help="Extra wait in ms after networkidle (default 600)")
    parser.add_argument("--transparent", action="store_true",
                        help="Omit background (PNG transparency)")
    parser.add_argument("--batch", action="store_true",
                        help="Treat input as a folder; convert every *.html in it")
    parser.add_argument("--auto", action="store_true", default=True,
                        help="Auto-detect .poster/.canvas size and selector "
                             "(on by default)")
    parser.add_argument("--no-auto", dest="auto", action="store_false",
                        help="Disable auto-detection of dimensions/selector")

    args = parser.parse_args()

    if args.batch:
        if not args.input.is_dir():
            sys.exit(f"[ERR] --batch requires a folder, got: {args.input}")
        html_files = sorted(args.input.glob("*.html"))
        if not html_files:
            sys.exit(f"[ERR] No .html files found in {args.input}")
        print(f"Batch mode — {len(html_files)} file(s)\n")
        for h in html_files:
            _convert_one(args, h)
    else:
        if not args.input.is_file():
            sys.exit(f"[ERR] File not found: {args.input}")
        _convert_one(args, args.input)


if __name__ == "__main__":
    main()
