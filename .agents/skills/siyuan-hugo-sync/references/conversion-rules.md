# Conversion Rules

## Front Matter

Use YAML front matter for Hugo Markdown. When merging front matter:

1. Parse YAML structurally.
2. Start from existing Hugo front matter when updating an existing post.
3. Overlay SiYuan front matter values.
4. Overlay explicit user-provided values.
5. If the target is Hugo and this is an update, set `lastmod` to current local time.

Common fields:

```yaml
title: "Post title"
date: 2026-04-04T01:18:48+08:00
lastmod: 2026-05-29T14:30:00+08:00
draft: false
tags:
  - 技术分享
```

For SiYuan-bound Markdown, front matter may be kept or stripped. If the user does not specify, strip Hugo-only publication fields when updating note body content.

## Callouts

SiYuan export usually represents callouts as GitHub-style blockquotes:

```markdown
> [!TIP]
> Content
```

Hugo uses shortcode blocks:

```markdown
{{< callout type="tips" >}}

Content

{{< /callout >}}
```

Mapping:

| SiYuan marker | Hugo type |
| --- | --- |
| `NOTE` | `note` |
| `TIP` | `tips` |
| `IMPORTANT` | `important` |
| `WARNING` | `warning` |
| `CAUTION` | `error` |

Reverse mapping:

| Hugo type | SiYuan marker |
| --- | --- |
| `note` | `NOTE` |
| `info` | `NOTE` |
| `tips` | `TIP` |
| `tip` | `TIP` |
| `important` | `IMPORTANT` |
| `warning` | `WARNING` |
| `error` | `CAUTION` |
| `caution` | `CAUTION` |

Keep blank lines around Hugo shortcode blocks. For SiYuan blockquotes, prefix each content line with `> ` and use a bare `>` for blank lines.

## Math

Inline math delimiters differ by target:

| Direction | Source inline math | Target inline math |
| --- | --- | --- |
| SiYuan to Hugo | `$a+b$` | `\(a+b\)` |
| Hugo to SiYuan | `\(a+b\)` | `$a+b$` |

Display math delimiters are the same in both systems and must be preserved:

```markdown
$$
E = mc^2
$$
```

When converting math:

- Convert only inline math in normal prose.
- Preserve fenced code blocks and inline code spans exactly.
- Preserve display math wrapped by `$$...$$` exactly, including multiline blocks.
- Do not use a broad `$` replacement that could rewrite display math delimiters.
- Treat `$...$` as inline math only when the opening `$` is not followed by whitespace and the closing `$` is not preceded by whitespace. This avoids most prose/currency false positives while preserving normal SiYuan inline formulas such as `$x_i$` and `$a + b$`.

## Body Cleanup

- Remove zero-width spaces (`U+200B`) from SiYuan exports unless the user explicitly needs them.
- Remove a first `# Heading` when it duplicates the front matter title.
- Preserve code fences exactly.
- Keep tables as Markdown tables; do not hand-wrap table cells.
- Preserve footnotes. Large footnote bodies may contain headings, tables, and code fences; do not flatten them.
- Replace escaped arrows from SiYuan export such as `–\>` only when they are clearly meant to be normal prose arrows.

## Summary Marker

For Hugo:

- Preserve an existing `<!--more-->`.
- If creating a new post and no marker exists, place `<!--more-->` after the first non-heading paragraph when appropriate.

For SiYuan:

- Remove `<!--more-->` by default unless the user wants to preserve Hugo publication metadata inside the note.
