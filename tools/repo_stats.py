#!/usr/bin/env python3
"""
Repository Statistics Generator

This tool generates a comprehensive statistics report of the repository,
including file counts, content analysis, and cross-reference metrics.

Usage:
    python tools/repo_stats.py

Output:
    Prints a formatted statistics report to stdout.
"""

import os
import re
from collections import defaultdict
from pathlib import Path
from typing import Dict, List


def count_files_by_directory(root: Path) -> Dict[str, int]:
    """Count files in each directory."""
    counts = defaultdict(int)
    
    for filepath in root.rglob("*"):
        if filepath.is_file():
            # Get the top-level directory
            relative = filepath.relative_to(root)
            if len(relative.parts) > 1:
                top_dir = relative.parts[0]
            else:
                top_dir = "(root)"
            
            # Skip hidden directories
            if top_dir.startswith("."):
                continue
            
            counts[top_dir] += 1
    
    return counts


def count_words_in_markdown(root: Path) -> int:
    """Count total words in all markdown files."""
    total = 0
    for filepath in root.rglob("*.md"):
        if any(part.startswith(".") for part in filepath.parts):
            continue
        content = filepath.read_text(encoding="utf-8", errors="ignore")
        # Remove code blocks
        content = re.sub(r"```[\s\S]*?```", "", content)
        # Count words
        words = len(content.split())
        total += words
    return total


def count_diagrams(root: Path) -> int:
    """Count Mermaid diagrams in markdown files."""
    count = 0
    for filepath in root.rglob("*.md"):
        if any(part.startswith(".") for part in filepath.parts):
            continue
        content = filepath.read_text(encoding="utf-8", errors="ignore")
        count += len(re.findall(r"```mermaid", content))
    return count


def count_tables(root: Path) -> int:
    """Count markdown tables."""
    count = 0
    for filepath in root.rglob("*.md"):
        if any(part.startswith(".") for part in filepath.parts):
            continue
        content = filepath.read_text(encoding="utf-8", errors="ignore")
        # Simple heuristic: count lines with | that look like table rows
        table_lines = [l for l in content.split("\n") if "|" in l and l.strip().startswith("|")]
        # Estimate tables by looking for header separators
        count += len(re.findall(r"\|[\s:-]+\|", content))
    return count


def count_cross_references(root: Path) -> int:
    """Count internal cross-references (See Also sections)."""
    count = 0
    for filepath in root.rglob("*.md"):
        if any(part.startswith(".") for part in filepath.parts):
            continue
        content = filepath.read_text(encoding="utf-8", errors="ignore")
        # Count links in See Also sections
        if "## See Also" in content:
            see_also_section = content.split("## See Also")[-1]
            count += len(re.findall(r"\[.*?\]\(.*?\)", see_also_section))
    return count


def main():
    repo_root = Path(__file__).parent.parent
    
    print("=" * 70)
    print("  REPOSITORY STATISTICS REPORT")
    print("=" * 70)
    print()
    
    # File counts by directory
    counts = count_files_by_directory(repo_root)
    
    print("📁 FILE COUNTS BY DIRECTORY")
    print("-" * 40)
    total_files = 0
    for directory, count in sorted(counts.items()):
        print(f"  {directory:25} {count:3} files")
        total_files += count
    print("-" * 40)
    print(f"  {'TOTAL':25} {total_files:3} files")
    print()
    
    # Content metrics
    word_count = count_words_in_markdown(repo_root)
    diagram_count = count_diagrams(repo_root)
    table_count = count_tables(repo_root)
    xref_count = count_cross_references(repo_root)
    
    print("📊 CONTENT METRICS")
    print("-" * 40)
    print(f"  Total Words:              {word_count:,}")
    print(f"  Mermaid Diagrams:         {diagram_count}")
    print(f"  Markdown Tables:          {table_count}")
    print(f"  Cross-References:         {xref_count}")
    print()
    
    # Estimated reading time (200 words per minute)
    reading_time = word_count // 200
    print("⏱️  ESTIMATED READING TIME")
    print("-" * 40)
    print(f"  {reading_time} minutes ({reading_time // 60} hours {reading_time % 60} minutes)")
    print()
    
    print("=" * 70)
    print("  Report generated successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()
