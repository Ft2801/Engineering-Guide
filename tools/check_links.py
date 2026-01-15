#!/usr/bin/env python3
"""
Link Checker for Markdown Files

This tool scans all markdown files in the repository and validates
internal links (relative paths) to ensure no broken references.

Usage:
    python tools/check_links.py

Exit codes:
    0 - All links valid
    1 - Broken links found
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple


def find_markdown_files(root: Path) -> List[Path]:
    """Find all markdown files in the repository."""
    return list(root.rglob("*.md"))


def extract_links(filepath: Path) -> List[Tuple[int, str]]:
    """Extract all markdown links from a file with line numbers."""
    links = []
    content = filepath.read_text(encoding="utf-8")
    
    # Match [text](path) but not external URLs
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    
    for line_num, line in enumerate(content.split("\n"), 1):
        for match in re.finditer(pattern, line):
            link_target = match.group(2)
            # Skip external URLs, anchors, and mailto
            if link_target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            # Remove anchor from internal links
            link_target = link_target.split("#")[0]
            if link_target:
                links.append((line_num, link_target))
    
    return links


def validate_link(source_file: Path, link: str, repo_root: Path) -> bool:
    """Check if a link target exists."""
    # Resolve relative path from source file's directory
    source_dir = source_file.parent
    target_path = (source_dir / link).resolve()
    
    return target_path.exists()


def main():
    print("=" * 60)
    print("  Markdown Link Checker")
    print("=" * 60)
    
    repo_root = Path(__file__).parent.parent
    markdown_files = find_markdown_files(repo_root)
    
    print(f"\nScanning {len(markdown_files)} markdown files...\n")
    
    broken_links = []
    total_links = 0
    
    for filepath in markdown_files:
        # Skip node_modules, .git, etc.
        if any(part.startswith(".") for part in filepath.parts):
            continue
        if "node_modules" in filepath.parts:
            continue
        
        links = extract_links(filepath)
        total_links += len(links)
        
        for line_num, link in links:
            if not validate_link(filepath, link, repo_root):
                relative_path = filepath.relative_to(repo_root)
                broken_links.append((relative_path, line_num, link))
    
    print(f"Total internal links checked: {total_links}")
    print(f"Broken links found: {len(broken_links)}")
    
    if broken_links:
        print("\n❌ BROKEN LINKS:\n")
        for filepath, line_num, link in broken_links:
            print(f"  {filepath}:{line_num}")
            print(f"    → {link}")
            print()
        sys.exit(1)
    else:
        print("\n✅ All internal links are valid!")
        sys.exit(0)


if __name__ == "__main__":
    main()
