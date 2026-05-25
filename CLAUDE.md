# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```shell
# Local development server (live preview at http://localhost:1313)
hugo server --logLevel debug --disableFastRender -p 1313

# Production build (outputs to ./public)
hugo --gc --minify

# Update Hextra theme
hugo mod get -u
hugo mod tidy

# Clean rebuild
rm -rf public/ resources/ && hugo --gc --minify
```

## Architecture

This is a personal Hugo static site using the **Hextra** theme (imported as a Hugo module, not a submodule). Deployed via GitHub Pages (GitHub Actions workflow) with optional Netlify support.

### Key config: [hugo.yaml](hugo.yaml)
- Hextra imported as a Hugo module at `github.com/imfing/hextra`
- KaTeX math engine enabled (block: `$$`/`[]`, inline: `()`)
- Goldmark HTML rendering set to `unsafe` (raw HTML in markdown is allowed)
- Blog listing sorted by `lastmod` descending
- Menu: About, Learn, Blog, Gallery, Tags, Search, GitHub link

### Content structure: [content/](content/)
- **Blog posts**: `content/blog/{year}/{slug}/index.md` with `cascade: type: blog` in `_index.md`
- **Section pages**: `content/{section}/_index.md` with card-based navigation via hextra shortcodes (`{{< cards >}}`, `{{< card >}}`)
- **Standalone pages**: `content/about.md`, `content/learn.md`, `content/gallery.md`
- Knowledge sections: marxism, leninism, maoism, finance, git, linux, mongo, python, numpy, pandas, matplotlib, algorithm, convex-optimization, love-psychology, sociology-love, music-theory

### Frontmatter conventions
- Blog posts use `date`, `title`, `tags`, and `cascade: type: blog` (from parent `_index.md`)
- Section pages use `title` and optionally `subtitle`
- The about page uses `avatar`, `author`, `role`, `institute` fields used by the `bio` shortcode

### Custom layouts: [layouts/](layouts/)
- `layouts/blog/single.html` — blog post detail page with date, lastmod, authors, tags, pagination
- `layouts/blog/list.html` — blog listing with pagination, tag display, date/lastmod
- `layouts/docs/single.html` — documentation-style section page layout
- `layouts/_shortcodes/` — custom shortcodes:
  - `bio` — about page avatar + bio layout
  - `abcjs` — ABC music notation rendering (via abcjs JS library)
  - `list_children` — auto-generates links to child pages of current section
  - `right` — right-aligned content
  - `supsub` — superscript/subscript support
- `layouts/_partials/custom/head-end.html` — loads abcjs JavaScript files

### Static assets: [static/](static/)
- `static/js/abcjs-basic-min.js` and `abcjs-plugin-min.js` — music notation rendering
- `static/images/` — avatar, gallery images, Marxism portraits
- `static/favicon.svg` and `favicon-dark.svg`

### Custom CSS: [assets/css/custom.css](assets/css/custom.css)
- Overrides max page width to 90rem
- Custom table styles (borders, alternating row colors, rounded corners)

### Deployment: [.github/workflows/pages.yaml](.github/workflows/pages.yaml)
- Triggers on push to `main`
- Hugo v0.161.1, Go 1.24
- Builds with `--gc --minify`, deploys to GitHub Pages via `actions/deploy-pages@v4`
