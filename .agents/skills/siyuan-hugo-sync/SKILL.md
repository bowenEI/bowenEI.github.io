---
name: siyuan-hugo-sync
description: Convert and synchronize SiYuan Note documents and Hugo Markdown content. Use when Codex needs to export a SiYuan note through the siyuan-note skill, update or create a Hugo post from it, import Hugo Markdown back into SiYuan, preserve or edit Hugo front matter fields such as title/date/lastmod/tags/draft, or translate callout/admonition blocks between SiYuan GitHub-alert style and Hugo shortcode style.
---

# SiYuan Hugo Sync

Use this skill to move content between SiYuan Note and Hugo Markdown without losing metadata or callout semantics.

## Dependencies

- Use the `siyuan-note` skill for all SiYuan API access. Open its `SKILL.md` when you need connection details, CLI usage, or API examples.
- Prefer reading from SiYuan with `tools/read.py <doc_id>` or `SiYuanClient.export_md_content(doc_id)`.
- Prefer writing to SiYuan with the `siyuan-note` update/create APIs after converting Hugo Markdown back to SiYuan-compatible Markdown.

## Workflow

1. Identify direction:
   - SiYuan to Hugo: export the SiYuan document as Markdown, convert it to Hugo style, then write the Hugo `index.md`.
   - Hugo to SiYuan: read the Hugo Markdown, convert it to SiYuan-compatible Markdown, then update or create the SiYuan document.
2. Load detailed conversion rules only when needed: `references/conversion-rules.md`.
3. Use `scripts/convert_markdown.py` for deterministic conversion of front matter, duplicate H1s, summary markers, zero-width spaces, callout blocks, and inline math delimiters.
4. Inspect the converted output before writing over an existing document.
5. Validate with a Hugo build for Hugo output, or by re-reading the SiYuan block/document after SiYuan updates.

## SiYuan To Hugo

When updating an existing Hugo document:

- Treat the SiYuan export as the source of truth for body content and conflicting metadata.
- Preserve Hugo-only metadata that is not present in SiYuan when it is still relevant, such as `draft`, `tags`, aliases, or custom params.
- Set `lastmod` to the current time for the user's timezone. Use the environment date/time or `date --iso-8601=seconds` if available.
- Keep `<!--more-->` if the existing Hugo post uses it; otherwise insert it after the first introductory paragraph when appropriate.
- Remove the exported top-level `# Title` when it duplicates the Hugo front matter title.
- Convert SiYuan inline math from `$...$` to Hugo inline math `\(...\)`.
- Preserve display math blocks delimited by `$$...$$`; both SiYuan and Hugo use the same display math wrapper.
- Convert SiYuan block/document references to plain text when importing to Hugo. This includes exported block-ref syntax, `siyuan://blocks/...` links, document/block IDs, or SiYuan-only data attributes such as block reference metadata. Keep the visible reference label or linked document title, and remove the SiYuan target/id/attribute so the Hugo Markdown contains only normal prose.
- In the final written report to the user, explicitly list every SiYuan block/document reference that was converted, including the Hugo file path plus the most specific location available (line number, heading, or nearby text) and the original reference target/id when visible.
- Convert SiYuan/GitHub callouts to Hugo shortcodes:
  - `[!NOTE]` -> `{{< callout type="info" >}}`
  - `[!TIP]` -> `{{< callout type="tips" >}}`
  - `[!IMPORTANT]` -> `{{< callout type="important" >}}`
  - `[!WARNING]` -> `{{< callout type="warning" >}}`
  - `[!CAUTION]` -> `{{< callout type="error" >}}`

Example:

```bash
python3 .agents/skills/siyuan-hugo-sync/scripts/convert_markdown.py \
  siyuan-to-hugo /tmp/siyuan.md content/blog/2025/post/index.md \
  --existing content/blog/2025/post/index.md \
  --lastmod now
```

## Hugo To SiYuan

When updating SiYuan from Hugo:

- Convert Hugo callout shortcodes back to GitHub-style callouts so SiYuan can represent them as the corresponding block style.
- Keep front matter only if the SiYuan document intentionally stores metadata; otherwise strip Hugo-only fields before updating the note.
- Convert `<!--more-->` according to user preference. If unspecified, remove it for SiYuan notes.
- Convert Hugo inline math from `\(...\)` back to SiYuan inline math `$...$`.
- Preserve display math blocks delimited by `$$...$$`; both Hugo and SiYuan use the same display math wrapper.
- Do not overwrite a SiYuan note until you have confirmed the target document ID/path.

Example:

```bash
python3 .agents/skills/siyuan-hugo-sync/scripts/convert_markdown.py \
  hugo-to-siyuan content/blog/2025/post/index.md /tmp/siyuan-import.md \
  --strip-frontmatter
```

## Metadata Rules

- Support editing `title`, `date`, `lastmod`, `tags`, `draft`, and additional YAML front matter fields.
- Quote string titles in Hugo front matter when they contain punctuation, colon-like text, or non-ASCII content if that matches local style.
- Tags should remain YAML lists unless the existing project consistently uses inline arrays.
- On Hugo updates, always update `lastmod` to current time unless the user explicitly asks not to.
- If a user gives explicit metadata values, they override both SiYuan and existing Hugo metadata.

## Validation

- For Hugo output, run the repository's normal Hugo build. If remote theme assets block validation, use a temporary config that disables remote asset fetches and state this clearly.
- Check that no raw `[!NOTE]`/`[!TIP]`/`[!IMPORTANT]`/`[!WARNING]`/`[!CAUTION]` markers remain in Hugo output.
- Check that no Hugo `{{< callout ... >}}` shortcodes remain in SiYuan-bound output.
- Check that no accidental duplicate top-level H1 was introduced.
- Check inline math directionally: Hugo-bound prose should use `\(...\)` for inline math, while SiYuan-bound prose should use `$...$`. Display math should remain wrapped with `$$...$$` in both directions.
- For Hugo output, check that no SiYuan block/document reference syntax, `siyuan://blocks/...` target, block ID, or SiYuan-only data attribute remains unless the user explicitly asked to preserve it.
