#!/usr/bin/env python3
"""
Screenshot utility for visual comparison of design templates.

Usage:
    python screenshot.py <url> <output_path> [--width=1280] [--height=800] [--full-page]

Examples:
    python screenshot.py http://localhost:8000/design/ishikawa_clone screenshots/current/clone.png
    python screenshot.py https://ishikawakazuya.net screenshots/original/reference.png --full-page
"""
import asyncio
import argparse
import sys
from pathlib import Path

try:
    from pyppeteer import launch
except ImportError:
    print("Error: pyppeteer not installed. Run: pip install pyppeteer")
    sys.exit(1)


async def take_screenshot(
    url: str,
    output_path: str,
    width: int = 1280,
    height: int = 800,
    full_page: bool = False,
    timeout: int = 30000
):
    """Take a screenshot of the given URL."""
    browser = await launch(
        headless=True,
        args=['--no-sandbox', '--disable-setuid-sandbox']
    )

    try:
        page = await browser.newPage()
        await page.setViewport({'width': width, 'height': height})

        print(f"Navigating to {url}...")
        await page.goto(url, {'waitUntil': 'networkidle0', 'timeout': timeout})

        # Wait for animations to settle
        await asyncio.sleep(1)

        # Ensure output directory exists
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)

        print(f"Taking screenshot...")
        await page.screenshot({
            'path': output_path,
            'fullPage': full_page
        })

        print(f"Saved to {output_path}")

    finally:
        await browser.close()


def main():
    parser = argparse.ArgumentParser(description='Take screenshots of web pages')
    parser.add_argument('url', help='URL to screenshot')
    parser.add_argument('output', help='Output file path')
    parser.add_argument('--width', type=int, default=1280, help='Viewport width')
    parser.add_argument('--height', type=int, default=800, help='Viewport height')
    parser.add_argument('--full-page', action='store_true', help='Capture full page')
    parser.add_argument('--timeout', type=int, default=30000, help='Timeout in ms')

    args = parser.parse_args()

    asyncio.get_event_loop().run_until_complete(
        take_screenshot(
            args.url,
            args.output,
            args.width,
            args.height,
            args.full_page,
            args.timeout
        )
    )


if __name__ == '__main__':
    main()
