#!/usr/bin/env python3
"""
Flatten SSI includes for GitHub Pages deployment.

Usage:
    python build.py

Outputs to /docs folder which GitHub Pages serves directly.
"""
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
DIST = ROOT / 'docs'  # GitHub Pages serves from /docs


def process_ssi(content: str) -> str:
    """Replace <!--#include virtual="/path" --> with file contents."""
    pattern = r'<!--#include\s+virtual="([^"]+)"\s*-->'

    def replace(match):
        virtual_path = match.group(1)
        file_path = ROOT / virtual_path.lstrip('/')
        if file_path.exists():
            return file_path.read_text(encoding='utf-8')
        else:
            return f'<!-- MISSING: {virtual_path} -->'

    return re.sub(pattern, replace, content)


def build():
    """Build the static site with flattened SSI includes."""
    # Clean and create output directory
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()

    # Flatten main HTML files
    for html_file in ['index.html', 'mobile.html']:
        src_path = ROOT / html_file
        if src_path.exists():
            content = src_path.read_text(encoding='utf-8')
            flattened = process_ssi(content)
            (DIST / html_file).write_text(flattened, encoding='utf-8')
            print(f'  Built: {html_file}')

    # Flatten guides subdirectory
    guides_src = ROOT / 'guides' / 'index.html'
    if guides_src.exists():
        (DIST / 'guides').mkdir()
        content = guides_src.read_text(encoding='utf-8')
        flattened = process_ssi(content)
        (DIST / 'guides' / 'index.html').write_text(flattened, encoding='utf-8')
        print('  Built: guides/index.html')

        # Copy guides assets
        guides_css = ROOT / 'guides' / 'guides.css'
        if guides_css.exists():
            shutil.copy2(guides_css, DIST / 'guides' / 'guides.css')

    # Copy static assets
    assets = ['styles.css', 'mobile.css', 'script.js', 'favicon.svg', 'images', 'fonts']
    for item in assets:
        src = ROOT / item
        if src.is_dir():
            shutil.copytree(src, DIST / item)
            print(f'  Copied: {item}/')
        elif src.exists():
            shutil.copy2(src, DIST / item)
            print(f'  Copied: {item}')

    # Note: CNAME file is managed by repo owner, not auto-generated
    # If custom domain is needed, create docs/CNAME manually

    print(f'\nBuild complete: {DIST}')


if __name__ == '__main__':
    print('Building JAMMIX for GitHub Pages...\n')
    build()
