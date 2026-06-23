# Implementation Notes

## Acquisition

Use `yt-dlp --flat-playlist --dump-json <channel>/videos` to create `logs/videos.jsonl`.
If the channel handle URL has no `/videos` suffix, append `/videos` for normal videos. Use `/shorts` only when requested.

Caption pass order:

1. `ja-orig`
2. `ja`
3. `en`
4. user-requested fallback languages

After each pass, compute missing video IDs from the saved video list and existing caption files, then run the next pass only for missing IDs.

## File Naming

Prefer stable video IDs in machine data. For human-facing Markdown, use a safe title plus the video ID when possible. Avoid relying on title-only filenames because titles can change and collide.

## Summary Quality

Do not summarize only from title/description when captions are unavailable. Mark those entries as caption-missing and keep the summary limited to available metadata.

When captions are available, create summaries that answer:

- What is the video about?
- Who is it for?
- What problem or question does it address?
- What steps, exercises, explanations, or recommendations appear?
- What should a viewer search for later to find this video?

## Search Ranking

A simple first version can score:

- exact query terms in title: high
- query terms in tags: high
- query terms in summary/key points: medium
- query terms in transcript excerpt: medium
- caption missing penalty: negative

For larger corpora, add embeddings or a local vector index, but keep the Markdown/CSV/JSON indexes as inspectable ground truth.

## Final Report

Report exact counts and exclusions:

```text
Output:
- Root:
- Normal videos listed:
- Captions retrieved:
- Captions missing:
- Shorts included: yes/no
- Index files:
- Chatbot folder:
```
