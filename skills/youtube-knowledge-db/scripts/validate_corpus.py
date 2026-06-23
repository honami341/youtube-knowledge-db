#!/usr/bin/env python3
"""Validate a YouTube knowledge DB output folder."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def count_lines(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for line in path.read_text(encoding="utf-8", errors="replace").splitlines() if line.strip())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", help="Knowledge DB output root")
    args = parser.parse_args()
    root = Path(args.root)

    videos_total = count_lines(root / "logs" / "videos.jsonl")
    markdown_count = len(list((root / "videos").glob("*.md"))) if (root / "videos").exists() else 0
    txt_count = len(list((root / "transcripts_txt").glob("*.txt"))) if (root / "transcripts_txt").exists() else 0
    caption_count = len(list((root / "captions").glob("*.json3"))) if (root / "captions").exists() else 0
    missing_count = count_lines(root / "logs" / "missing_captions.txt")

    index_path = root / "00_INDEX.json"
    if index_path.exists():
        try:
            data = json.loads(index_path.read_text(encoding="utf-8"))
            index_count = len(data) if isinstance(data, list) else len(data.get("videos", []))
        except Exception:
            index_count = -1
    else:
        index_count = 0

    checks = {
        "videos_total": videos_total,
        "markdown_count": markdown_count,
        "transcript_txt_count": txt_count,
        "caption_json3_count": caption_count,
        "missing_captions_count": missing_count,
        "index_json_count": index_count,
        "markdown_matches_videos": markdown_count == videos_total,
        "txt_matches_videos": txt_count == videos_total,
        "index_matches_videos": index_count == videos_total,
        "captions_plus_missing_matches_videos": caption_count + missing_count == videos_total,
    }

    print(json.dumps(checks, ensure_ascii=False, indent=2))
    ok = all(value for key, value in checks.items() if key.endswith("_matches_videos"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
