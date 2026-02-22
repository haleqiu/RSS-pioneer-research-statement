#!/usr/bin/env python3
"""
Download RSS Pioneers 2025 research statements from OpenReview.

Requires: pip install openreview-py

Usage:
    python download.py [--output-dir DIR]
"""

import argparse
import os
import re
from pathlib import Path

try:
    import openreview
except ImportError:
    print("Error: openreview-py not installed. Run: pip install openreview-py")
    exit(1)


VENUE_ID = "roboticsfoundation.org/RSS/2025/Workshop/Pioneers"


def sanitize_filename(s: str) -> str:
    """Create a safe filename from a string."""
    s = re.sub(r'[<>:"/\\|?*]', "_", s)
    s = s.strip().strip(".")[:80]
    return s or "unnamed"


def main():
    parser = argparse.ArgumentParser(description="Download RSS Pioneers 2025 research statements")
    parser.add_argument(
        "--output-dir",
        "-o",
        type=str,
        default=Path(__file__).parent,
        help="Output directory for PDFs (default: script directory)",
    )
    args = parser.parse_args()
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    client = openreview.api.OpenReviewClient(baseurl="https://api2.openreview.net")

    notes = None
    submission_names = ["Submission", "Research_Statement"]

    try:
        venue_group = client.get_group(VENUE_ID)
        submission_name = venue_group.content.get("submission_name", {}).get("value", "Submission")
        submission_names.insert(0, submission_name)
    except Exception as e:
        print(f"Could not get venue group: {e}. Trying default invitation patterns...")

    for name in submission_names:
        invitation = f"{VENUE_ID}/-/{name}"
        try:
            notes = list(client.get_all_notes(invitation=invitation))
            if notes:
                print(f"Fetching submissions with invitation: {invitation}")
                break
        except Exception as e:
            continue
    else:
        print("Could not find valid invitation. Check venue ID and OpenReview structure.")
        return 1

    if not notes:
        print("No submissions found.")
        return 0

    print(f"Found {len(notes)} submission(s). Downloading PDFs...")
    manifest = []

    for note in notes:
        title = note.content.get("title", {}).get("value", "Untitled")
        authors = note.content.get("authors", {}).get("value", [])
        author_str = authors[0] if authors else "unknown"
        try:
            pdf_bytes = client.get_attachment(id=note.id, field_name="pdf")
        except TypeError:
            try:
                pdf_bytes = client.get_attachment(note.id, "pdf")
            except Exception as e:
                print(f"  Skip ({e}): {title[:50]}...")
                continue
        except Exception as e:
            print(f"  Skip ({e}): {title[:50]}...")
            continue

        safe_title = sanitize_filename(title)
        filename = f"{safe_title}.pdf"
        filepath = out_dir / filename
        filepath.write_bytes(pdf_bytes)
        manifest.append({"title": title, "authors": author_str, "file": filename})
        print(f"  Saved: {filename}")

    manifest_path = out_dir / "manifest.csv"
    with open(manifest_path, "w") as f:
        f.write("title,authors,file\n")
        for m in manifest:
            title_esc = m["title"].replace('"', '""')
            f.write(f'"{title_esc}","{m["authors"]}",{m["file"]}\n')
    print(f"Manifest written to {manifest_path}")
    return 0


if __name__ == "__main__":
    exit(main())
