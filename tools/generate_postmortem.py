#!/usr/bin/env python3
"""
Post-Mortem Report Generator

This tool creates a new Post-Mortem report from the template with
auto-incrementing incident ID and pre-filled metadata.

Usage:
    python tools/generate_postmortem.py

The tool will:
1. Prompt for incident details
2. Generate a post-mortem file in docs/postmortems/
"""

import os
import re
from datetime import datetime
from pathlib import Path


def get_next_incident_id(pm_dir: Path) -> int:
    """Find the next available incident ID."""
    if not pm_dir.exists():
        pm_dir.mkdir(parents=True, exist_ok=True)
        return 1
    
    existing_ids = []
    for file in pm_dir.glob("inc-*.md"):
        match = re.match(r"inc-(\d+)", file.stem)
        if match:
            existing_ids.append(int(match.group(1)))
    
    return max(existing_ids, default=0) + 1


def get_severity() -> str:
    """Prompt for incident severity."""
    print("\nSeverity levels:")
    print("  1. P1 - Critical (User-facing outage)")
    print("  2. P2 - Major (Degraded service)")
    print("  3. P3 - Minor (Internal tooling affected)")
    
    while True:
        choice = input("\nSelect severity (1-3): ").strip()
        if choice == "1":
            return "P1"
        elif choice == "2":
            return "P2"
        elif choice == "3":
            return "P3"
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def generate_postmortem(inc_id: int, title: str, severity: str, pm_dir: Path) -> Path:
    """Generate the post-mortem file from template."""
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"inc-{inc_id:04d}-{date_str}.md"
    filepath = pm_dir / filename
    
    content = f"""# Post-Mortem: {title}

## Metadata
*   **Incident ID**: INC-{inc_id:04d}
*   **Date**: {date_str}
*   **Severity**: {severity}
*   **Duration**: [HH:MM]
*   **Author**: [Your Name]

---

## 1. Executive Summary

[2-3 sentence summary for leadership]

---

## 2. Timeline (All times in UTC)

| Time | Event |
| :--- | :--- |
| HH:MM | [Event description] |
| HH:MM | Incident declared |
| HH:MM | Root cause identified |
| HH:MM | Mitigation applied |
| HH:MM | Service restored |

---

## 3. Root Cause Analysis (5 Whys)

1. **Why** did [symptom]? → [answer]
2. **Why** [answer 1]? → [answer]
3. **Why** [answer 2]? → [answer]
4. **Why** [answer 3]? → [answer]
5. **Why** [answer 4]? → [TRUE ROOT CAUSE]

---

## 4. Impact

*   **User Impact**: [Number of affected users/transactions]
*   **Revenue Impact**: [$X estimated loss]
*   **SLO Impact**: [X% of error budget consumed]

---

## 5. Action Items

| Action | Owner | Due Date | Status |
| :--- | :--- | :--- | :--- |
| [Action 1] | @team | YYYY-MM-DD | [ ] |
| [Action 2] | @team | YYYY-MM-DD | [ ] |

---

## 6. Lessons Learned

*   **What went well**: [e.g., Alerting fired quickly]
*   **What went poorly**: [e.g., Runbook was outdated]
*   **Where we got lucky**: [e.g., Happened during low traffic]
"""
    
    filepath.write_text(content, encoding="utf-8")
    return filepath


def main():
    print("=" * 60)
    print("  Post-Mortem Report Generator")
    print("=" * 60)
    
    repo_root = Path(__file__).parent.parent
    pm_dir = repo_root / "docs" / "postmortems"
    
    next_id = get_next_incident_id(pm_dir)
    print(f"\nNext available Incident ID: INC-{next_id:04d}")
    
    title = input("\nEnter incident title (e.g., 'Payment Service Outage'): ").strip()
    if not title:
        print("Error: Title is required.")
        return
    
    severity = get_severity()
    
    filepath = generate_postmortem(next_id, title, severity, pm_dir)
    print(f"\n✅ Post-Mortem created: {filepath}")
    print("\nNext steps:")
    print("  1. Fill in the timeline with accurate timestamps")
    print("  2. Complete the 5 Whys analysis")
    print("  3. Assign owners to action items")
    print("  4. Schedule a review meeting within 48 hours")


if __name__ == "__main__":
    main()
