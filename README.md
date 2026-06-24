# YouTube Knowledge DB


学びたい分野の YouTube チャンネルを、まるごと AI 教材・検索可能な知識 DB に変換するための Claude Code / Codex 向け Skill / Plugin です。

この plugin / skill は、YouTube チャンネルを次のような再利用しやすいデータに変換するワークフローを提供します。

- 動画一覧
- 取得可能な字幕・文字起こし
- 字幕がない動画のログ
- 整形済み文字起こし
- 詳細サマリー
- 簡単な章単位タイムスタンプ
- タグ
- Markdown / CSV / JSON の索引
- チャットボット用の検索データ

## Example

```text
Convert this YouTube channel into a searchable knowledge DB:
https://www.youtube.com/@example
```

## Claude Code Plugin Install

このリポジトリには、Claude Code 用の自前 Marketplace カタログを含めています。

```text
.claude-plugin/marketplace.json
```

名前の関係は以下です。

```text
Marketplace name: youtube-knowledge-db-plugins
Plugin name:      youtube-knowledge-db
Skill name:       youtube-knowledge-db
```

Marketplace name と plugin name は意図的に別名にしています。Claude Code の marketplace workflow では、この2つを同名にすると環境によって衝突することがあるためです。

Claude Code 内で Marketplace を追加します。

```text
/plugin marketplace add honami341/youtube-knowledge-db
```

Plugin をインストールします。

```text
/plugin install youtube-knowledge-db@youtube-knowledge-db-plugins
```

必要に応じて plugin を再読み込みします。

```text
/reload-plugins
```

Plugin 経由で入れた場合は、Skill 名に plugin prefix が付きます。

```text
/youtube-knowledge-db:youtube-knowledge-db
Convert this YouTube channel into a searchable knowledge DB:
https://www.youtube.com/@example
```

## Claude Code Local Development

このリポジトリを clone してローカルでテストする場合は、Claude Code の plugin directory flag を使います。

```bash
claude --plugin-dir .
```

その後、Claude Code 内で以下を実行します。

```text
/youtube-knowledge-db:youtube-knowledge-db
```

これは Claude Code 公式ドキュメントの local plugin test flow に沿った方法です。`--plugin-dir` でローカル plugin directory を読み込み、plugin 内の skill は `/plugin-name:skill-name` 形式で呼び出します。

## Claude Code Manual Skill Install

Marketplace 経由ではなく、Skill として手動で入れることもできます。

このフォルダをコピーします。

```text
skills/youtube-knowledge-db
```

コピー先は以下です。

```text
~/.claude/skills/youtube-knowledge-db
```

手動 Skill として入れた場合は、短い名前で呼び出します。

```text
/youtube-knowledge-db
Convert this YouTube channel into a searchable knowledge DB:
https://www.youtube.com/@example
```

## Codex Usage

このリポジトリには Codex plugin manifest も含めています。

```text
.codex-plugin/plugin.json
```

共通 Skill 本体は以下にあります。

```text
skills/youtube-knowledge-db/SKILL.md
```

現時点では、Codex では manual skill install が一番確実です。

```text
Copy skills/youtube-knowledge-db to ~/.codex/skills/youtube-knowledge-db
```

その後、Codex に以下のように依頼します。

```text
Use youtube-knowledge-db to convert this YouTube channel into a searchable knowledge database:
https://www.youtube.com/@example
```

`.codex-plugin/plugin.json` は Codex Plugin として配布するための manifest として同梱しています。ただし、Codex の plugin installation UX は利用している Codex surface や marketplace 設定によって異なるため、plugin installer が使えない環境では manual skill install を使ってください。

## Skill Invocation Names

インストール方法によって Skill の呼び出し名が変わります。

```text
Plugin install:
/youtube-knowledge-db:youtube-knowledge-db

Manual skill install:
/youtube-knowledge-db
```

片方が見つからない場合は、もう片方を試してください。

## Output Shape

Skill は、概ね次のような出力フォルダを作ることを想定しています。

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

- 通常動画と Shorts は分けて扱います。
- 字幕は通常 `ja-orig`、`ja`、`en` の順で取得を試みます。
- 字幕がない動画は、文字起こし済みとして扱わず missing captions としてログ化します。
- Timeline notes は簡単な章単位に留めます。字幕1行ごとの timestamp は作りません。
- 大量動画では、まず index を検索し、必要な動画だけ full transcript を確認します。

## Spec Notes

Claude Code の plugin loading 仕様は、公式ドキュメントを優先します。

この README では、公式ドキュメントで確認できる以下の形式を採用しています。

- `claude --plugin-dir .`
- `/plugin marketplace add owner/repo`
- `/plugin install plugin-name@marketplace-name`
- `/plugin-name:skill-name`

Marketplace 構成は、配布参考記事の形式に従い、このリポジトリ内の `.claude-plugin/marketplace.json` にまとめています。

## License

MIT
