# YouTube Knowledge DB Plugin

Convert a YouTube channel into a searchable, reusable knowledge database for AI assistants.

This repository packages one shared Agent Skill for both Codex and Claude Code. It is designed for workflows that turn YouTube videos into:

- video lists
- downloadable captions or transcript placeholders
- cleaned transcripts
- detailed summaries
- tags
- Markdown / CSV / JSON indexes
- chatbot-ready search data

## Best Use

Use this when you want to turn video assets into a knowledge base that an AI can search later.

Example request:

```text
Convert this YouTube channel into a searchable knowledge DB:
https://www.youtube.com/@example
```

## Install For Codex

Copy the skill folder into your Codex skills directory:

```text
skills/youtube-knowledge-db
```

to:

```text
~/.codex/skills/youtube-knowledge-db
```

Then ask Codex:

```text
Use youtube-knowledge-db to convert this YouTube channel into a searchable knowledge database.
```

The repository also includes `.codex-plugin/plugin.json` so it can be packaged as a Codex plugin.

## Install For Claude Code

Copy the same skill folder:

```text
skills/youtube-knowledge-db
```

to:

```text
~/.claude/skills/youtube-knowledge-db
```

Then ask Claude Code:

```text
/youtube-knowledge-db
Convert this YouTube channel into a searchable knowledge database.
```

The repository also includes `.claude-plugin/plugin.json` so it can be packaged as a Claude Code plugin.

## Output Shape

The skill asks the agent to create an output folder like this:

```text
<output-root>/
  README.md
  00_INDEX.md
  00_INDEX.csv
  00_INDEX.json
  tag_index.md
  logs/
  captions/
  videos/
  transcripts_txt/
  tags/
  chatbot/
```

## Notes

- Normal videos are treated separately from Shorts.
- Captions are retrieved in language passes, usually `ja-orig`, then `ja`, then `en`.
- Missing captions are logged instead of being silently treated as transcripts.
- For large channels, search the generated indexes first and only inspect full transcripts for shortlisted videos.

## License

MIT
