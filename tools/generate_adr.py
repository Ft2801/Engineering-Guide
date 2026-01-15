#!/usr/bin/env python3
"""
ADR (Architectural Decision Record) Generator

This tool creates a new ADR from the template with auto-incrementing ID.

Usage:
    python tools/generate_adr.py

The tool will:
1. Scan existing ADRs to find the next available ID
2. Prompt for the ADR title
3. Generate a new ADR file in docs/adr/
"""

import os
import re
from datetime import datetime
from pathlib import Path


def get_next_adr_id(adr_dir: Path) -> int:
    """Find the next available ADR ID by scanning existing files."""
    if not adr_dir.exists():
        adr_dir.mkdir(parents=True, exist_ok=True)
        return 1
    
    existing_ids = []
    for file in adr_dir.glob("adr-*.md"):
        match = re.match(r"adr-(\d+)", file.stem)
        if match:
            existing_ids.append(int(match.group(1)))
    
    return max(existing_ids, default=0) + 1


def slugify(title: str) -> str:
    """Convert a title to a URL-friendly slug."""
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    return slug.strip("-")


def generate_adr(adr_id: int, title: str, adr_dir: Path) -> Path:
    """Generate the ADR file from template."""
    slug = slugify(title)
    filename = f"adr-{adr_id:03d}-{slug}.md"
    filepath = adr_dir / filename
    
    content = f"""# ADR-{adr_id:03d}: {title}

## Metadata
*   **ADR ID**: ADR-{adr_id:03d}
*   **Date**: {datetime.now().strftime("%Y-%m-%d")}
*   **Status**: Proposed
*   **Deciders**: [List architects involved]

---

## 1. Context

[Describe the technical, business, or political forces at play.]

---

## 2. Decision

[State the architectural decision that was made.]

---

## 3. Rationale

| Option | Pros | Cons | Verdict |
| :--- | :--- | :--- | :--- |
| **Option A** | | | **Chosen** |
| **Option B** | | | Rejected |

---

## 4. Consequences

**Positive**:
*   [Benefit 1]

**Negative**:
*   [Trade-off 1]

---

## 5. Related Documents

*   [Link to RFC or Decision Matrix]
"""
    
    filepath.write_text(content, encoding="utf-8")
    return filepath


def main():
    print("=" * 60)
    print("  ADR (Architectural Decision Record) Generator")
    print("=" * 60)
    
    # Determine ADR directory
    repo_root = Path(__file__).parent.parent
    adr_dir = repo_root / "docs" / "adr"
    
    next_id = get_next_adr_id(adr_dir)
    print(f"\nNext available ADR ID: ADR-{next_id:03d}")
    
    title = input("\nEnter ADR title: ").strip()
    if not title:
        print("Error: Title is required.")
        return
    
    filepath = generate_adr(next_id, title, adr_dir)
    print(f"\n✅ ADR created: {filepath}")
    print("\nNext steps:")
    print("  1. Edit the ADR to fill in the details")
    print("  2. Submit for review via Pull Request")
    print("  3. Update status to 'Accepted' after approval")


if __name__ == "__main__":
    main()
