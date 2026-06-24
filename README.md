# YouTube Knowledge DB

Turn a YouTube channel in any field you want to learn into AI-ready learning material and a searchable knowledge database.

This plugin/skill helps an AI agent convert a channel into:

- video lists
- downloadable captions or transcript placeholders
- cleaned transcripts
- detailed summaries
- simple chapter-level timestamps
- tags
- Markdown / CSV / JSON indexes
- chatbot-ready search data

Example request:

```text
Convert this YouTube channel into a searchable knowledge DB:
https://www.youtube.com/@example
```

## Claude Code Plugin Install

This repository includes a self-hosted Claude Code marketplace catalog at:

```text
.claude-plugin/marketplace.json
```

The marketplace name is:

```text
youtube-knowledge-db-plugins
```

The plugin name is:

```text
youtube-knowledge-db
```

These names are intentionally different. Some Claude Code marketplace workflows can fail when the marketplace name and plugin name collide.

Add the marketplace from Claude Code:

```text
/plugin marketplace add honami341/youtube-knowledge-db
```

Then install the plugin:

```text
/plugin install youtube-knowledge-db@youtube-knowledge-db-plugins
```

Reload plugins if Claude Code asks you to, or run:

```text
/reload-plugins
```

Invoke the skill as a plugin skill:

```text
/youtube-knowledge-db:youtube-knowledge-db
Convert this YouTube channel into a searchable knowledge DB:
https://www.youtube.com/@example
```

## Claude Code Local Development

For local testing from a clone of this repository, use Claude Code's plugin directory flag:

```bash
claude --plugin-dir .
```

Then invoke:

```text
/youtube-knowledge-db:youtube-knowledge-db
```

This follows the current Claude Code plugin documentation: `--plugin-dir` loads a local plugin directory, and plugin skills are namespaced as `/plugin-name:skill-name`.

## Claude Code Manual Skill Install

If you do not want to use the plugin marketplace flow, copy the skill folder manually:

```text
skills/youtube-knowledge-db
```

to:

```text
~/.claude/skills/youtube-knowledge-db
```

Then invoke it as a standalone skill:

```text
/youtube-knowledge-db
Convert this YouTube channel into a searchable knowledge DB:
https://www.youtube.com/@example
```

## Codex Usage

This repository includes a Codex plugin manifest:

```text
.codex-plugin/plugin.json
```

The shared skill lives at:

```text
skills/youtube-knowledge-db/SKILL.md
```

Manual Codex skill install:

```text
Copy skills/youtube-knowledge-db to ~/.codex/skills/youtube-knowledge-db
```

Then ask Codex:

```text
Use youtube-knowledge-db to convert this YouTube channel into a searchable knowledge database:
https://www.youtube.com/@example
```

Codex plugin packaging metadata is included, but installation UX can differ by Codex surface and plugin marketplace configuration. Treat `.codex-plugin/plugin.json` as the included plugin manifest, and use manual skill install when a plugin installer is not available in your Codex environment.

## Skill Invocation Names

Use the invocation that matches how you installed it:

```text
Plugin install:
/youtube-knowledge-db:youtube-knowledge-db

Manual skill install:
/youtube-knowledge-db
```

If one name is not found, try the other.

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
- Timeline notes should stay simple: a few chapter-level timestamps, not one timestamp per caption line.
- For large channels, search the generated indexes first and only inspect full transcripts for shortlisted videos.

## Spec Notes

Claude Code's official docs are the source of truth for plugin loading. This README uses the official `claude --plugin-dir .` local test flow and plugin skill namespace format. The marketplace structure follows the referenced distribution article, with `marketplace.json` added to this same repository for a compact self-hosted marketplace.

## License

MIT
