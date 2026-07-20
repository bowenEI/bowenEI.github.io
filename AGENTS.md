# Repository Guidelines

## Project Structure & Module Organization

This is a Hugo static site using the Hextra theme as a Go module. Site content lives in `content/`: blog posts use `content/blog/<year>/<slug>/index.md`, while documentation-style sections use `content/<section>/` with `_index.md` landing pages. Keep post-local images beside the relevant Markdown file; place shared images and browser assets in `static/images/` and `static/js/`. Custom presentation code belongs in `layouts/` (templates, partials, and shortcodes) and `assets/css/custom.css`. Site-wide settings and menus are in `hugo.yaml`; deployment is defined in `.github/workflows/pages.yaml` and `netlify.toml`.

## Build, Test, and Development Commands

Use Hugo extended `0.161.1`, matching CI, plus Go (CI uses `1.24`). Run:

```sh
hugo mod tidy
hugo server --logLevel debug --disableFastRender -p 1313
hugo --gc --minify
```

The server previews at `http://localhost:1313`; the production build writes `public/`. Treat a successful production build as the primary validation because this repository has no separate automated test suite. To update Hextra intentionally, run `hugo mod get -u && hugo mod tidy`, then review `go.mod` and `go.sum`.

## Content, Style, and Naming

Use Markdown with YAML front matter. Blog posts should provide `title`, `date`, `lastmod`, `draft`, and, when useful, a YAML-list `tags` field. Use lowercase, hyphen-separated blog slugs, for example `content/blog/2026/new-topic/index.md`. Preserve the established Chinese/English prose and heading style in the section being edited. Keep one blank line around Hextra shortcodes and use Hugo math delimiters (`\(...\)` inline, `$$...$$` display). YAML and CSS use two-space indentation; follow the existing CSS selector wrapping and avoid unrelated reformatting.

## Testing and Review

Before submitting, run `hugo --gc --minify` and inspect the affected page locally. Confirm links, code fences, tables, images, front matter, and shortcode rendering. Do not commit generated `public/`, `resources/`, or `.hugo_build.lock` files.

## Commits and Pull Requests

History uses concise imperative subjects, often Conventional Commit prefixes such as `feat:` and `style:`; use the same pattern (for example, `feat: add Linux installation guide`). Keep each commit focused. PRs should explain the visitor-facing change, link related issues when applicable, include screenshots for layout or styling changes, and state the build command and result.
