---
name: youtube-knowledge-db
description: Convert a YouTube channel into a searchable reusable knowledge database. Use when the user asks to collect videos from a YouTube channel, download available captions/transcripts, clean transcript text, create detailed summaries, tag videos, build Markdown/CSV/JSON indexes, or create chatbot-ready search data for recommending related videos from a channel corpus.
---

# YouTube Knowledge DB

## Goal

Turn a YouTube channel into a local knowledge base that can be searched and reused by an AI assistant. Produce source-preserving artifacts: raw metadata, raw captions, cleaned transcripts, detailed video summaries, tags, indexes, missing-caption logs, and chatbot search data.

## Fast Workflow

1. Confirm the target URL and output root. If the user does not specify a root, create a clearly named folder on the Desktop or in the current workspace.
2. Fetch the normal video tab first (`/videos`). Treat Shorts separately unless the user explicitly requests Shorts.
3. Save the flat video list before captions: `logs/videos.jsonl`.
4. Probe one representative video for subtitle languages. Prefer this order: `ja-orig`, `ja`, `en`, then any user-requested language.
5. Download captions in passes by language, retrying only the missing IDs each pass. Avoid repeatedly hitting every video.
6. Build per-video Markdown and text files from the saved video list and available caption files.
7. Generate indexes: `00_INDEX.md`, `00_INDEX.csv`, `00_INDEX.json`, `tags/`, and `tag_index.md` or localized equivalent.
8. Generate chatbot-ready data only after indexes exist.
9. Validate counts against the saved video list, not against the channel UI.
10. Report exact counts: total videos, captions found, captions missing, index rows, output path, and what was excluded.

## Output Layout

Use this structure unless the existing project already has a compatible convention:

```text
<output-root>/
  README.md
  00_INDEX.md
  00_INDEX.csv
  00_INDEX.json
  tag_index.md
  logs/
    videos.jsonl
    processing_report.json
    missing_captions.txt
  captions/
    *.json3
    *.info.json
  videos/
    <video-id-or-safe-title>.md
  transcripts_txt/
    <video-id-or-safe-title>.txt
  tags/
    <tag>.md
  chatbot/
    search_videos.py
    data/
      video_search_index.jsonl
      metadata.json
      tags.json
    chatbot_prompt.md
```

## Caption Policy

- Preserve raw caption files separately from cleaned output.
- Do not claim a transcript was retrieved when only metadata exists.
- If captions are missing, create a placeholder transcript file that clearly says no downloadable caption was found.
- If English captions are used for a Japanese channel, label that source clearly in metadata and summaries.
- Do not fabricate transcript details from title or description.

## Cleaning And Summarizing

For each video Markdown file include:

```markdown
# <title>

- URL:
- Video ID:
- Published:
- Caption source:
- Tags:

## Summary
Detailed, topic-oriented summary.

## Key Points
- Point
- Point

## Timeline Notes
- [00:00] Opening or topic setup
- [03:20] Main topic or explanation
- [08:45] Exercise, method, example, or key shift

## Cleaned Transcript
...
```

Clean obvious caption fragmentation, repeated fillers, spacing artifacts, and simple transcription noise. Keep meaning conservative. When unsure, preserve the original wording rather than rewriting aggressively.

Keep Timeline Notes lightweight. Use only broad chapter-level timestamps, usually 3-8 entries per video. Prefer topic changes, demonstrations, conclusions, and practical steps. Do not create a timestamp for every caption line or every sentence.

## Tagging

Tag for search behavior, not decoration. Use tags that a future question is likely to contain. Prefer domain terms, symptoms, body parts, methods, audience, and workflow phase.

For physical therapy, training, bodywork, or clinic channels, include tags such as:

```text
low-back-pain, shoulder, neck, hip, knee, foot, breathing, thorax, scapula,
core, posture, gait, running, training, performance, assessment,
self-care, mobility, strength, pain, nervous-system
```

Localize visible tag names when the output language requires it, but keep machine keys stable in JSON.

## Chatbot Search Data

Create a compact JSONL record per video. Include:

```json
{
  "video_id": "...",
  "title": "...",
  "url": "...",
  "published": "...",
  "caption_available": true,
  "caption_source": "ja-orig",
  "summary": "...",
  "key_points": ["..."],
  "tags": ["..."],
  "search_text": "title summary key points tags cleaned transcript excerpt"
}
```

Use the index first for retrieval, then read full transcripts only for the shortlisted videos. This prevents loading the entire corpus into context for every question.

## Token Discipline

- Use tools and scripts for acquisition, parsing, counting, and deterministic file generation.
- Keep raw transcript text on disk; do not paste large transcripts into the conversation.
- Summarize per video in batches and store results immediately.
- Keep timestamps concise: chapter-level notes only, not line-by-line timestamped transcripts.
- For answering questions later, search the index first, then inspect only the top matches.
- Put long implementation details in scripts or references, not in chat.

## Verification

Before final reporting, verify:

```text
videos_total == line count of logs/videos.jsonl
index_json_count == videos_total
markdown_file_count == videos_total
transcript_txt_count == videos_total
captions_found + captions_missing == videos_total
missing_captions.txt matches captions_missing
```

Open a sample video Markdown and check that Summary, Key Points, Tags, Timeline Notes, and Cleaned Transcript are present.

## Recommended Tools

Prefer `yt-dlp` for video lists and captions when available. Use structured caption formats such as `json3` when possible. Use Python for JSON/CSV/Markdown generation. Use an external speech-to-text service only when the user explicitly wants audio transcription beyond YouTube captions.

Read `references/implementation-notes.md` when implementing scripts or adapting the workflow to a new machine.
