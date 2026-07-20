# Bowen's Home

一个基于 [Hugo](https://gohugo.io/) 与 [Hextra](https://github.com/imfing/hextra) 构建的个人静态博客，用于沉淀技术笔记、学习资料与博客文章。本仓库面向内容维护者和站点开发者。

## 技术栈

- **Hugo extended 0.161.1**：静态站点生成器；版本与 CI、Netlify 配置保持一致。
- **Hextra**：通过 Hugo Module 引入的主题，依赖声明位于 `go.mod`。
- **GitHub Actions**：负责 `main` 分支的构建与 GitHub Pages 发布。
- **Netlify**：保留可选构建配置，见 `netlify.toml`。

## 项目结构

```text
content/                     页面、知识库与博客 Markdown
content/blog/<year>/<slug>/  博客文章及其本地资源
layouts/                     自定义模板、局部模板与 shortcode
assets/                      经 Hugo 处理的资源（含自定义 CSS）
static/                      原样发布的图片、脚本与图标
hugo.yaml                    全局站点、菜单、数学与主题配置
.github/workflows/pages.yaml GitHub Pages 构建与发布流程
```

## 本地开发

请安装 Hugo **extended 0.161.1**、Go 和 Git；CI 使用 Go 1.24。首次运行或模块变更后，先整理依赖：

```sh
hugo mod tidy
```

启动带实时预览的本地服务器：

```sh
hugo server --logLevel debug --disableFastRender -p 1313
```

浏览器访问 `http://localhost:1313`。提交前请执行生产构建：

```sh
hugo --gc --minify
```

构建结果写入 `public/`；`public/`、`resources/` 和 `.hugo_build.lock` 均为生成文件，不应提交。需要升级 Hextra 时，执行 `hugo mod get -u` 和 `hugo mod tidy`，并审查 `go.mod`、`go.sum` 的变更。

## 内容维护

博客文章放在 `content/blog/<year>/<slug>/index.md`，其中 `<slug>` 使用小写连字符命名，例如 `content/blog/2026/new-topic/index.md`。文章使用 YAML front matter，通常包含：

```yaml
---
title: "文章标题"
date: 2026-01-01T12:00:00+08:00
lastmod: 2026-01-01T12:00:00+08:00
draft: false
tags:
  - 技术分享
---
```

将文章专属图片放在对应的文章目录；跨页面复用的图片和脚本分别放在 `static/images/`、`static/js/`。保持现有 Markdown 标题层级，并在 Hextra shortcode 前后保留空行。行内数学使用 `\(...\)`，块级数学使用 `$$...$$`；站点已在 `hugo.yaml` 中启用 KaTeX 支持。

## 思源笔记同步

仓库提供思源笔记与 Hugo Markdown 的双向同步工作流：思源导出内容可转换并写入博客文章，Hugo 文章也可转换回思源兼容 Markdown。使用 `.agents/skills/siyuan-hugo-sync/scripts/convert_markdown.py` 执行转换，并在同步到 Hugo 后运行 `hugo --gc --minify`。

完整的元数据合并、提示块、数学公式、摘要和引用转换规则见 [思源—Hugo 同步技能](.agents/skills/siyuan-hugo-sync/SKILL.md)。

## 发布与排查

推送到 `main` 会触发 GitHub Actions，按 `.github/workflows/pages.yaml` 构建并发布站点；也可在 GitHub Actions 页面手动运行该工作流。Netlify 使用 `netlify.toml` 中的同一 Hugo 版本和生产构建命令，作为可选部署入口。

若模块下载或远程主题资源获取失败，请检查网络、代理和 Git 访问权限后重试 `hugo mod tidy` 或构建命令。若页面异常，优先检查 front matter、内部链接、图片路径、代码围栏和 shortcode 是否闭合。

## 贡献约定

保持每次提交聚焦单一变更，并在提交前检查受影响页面和生产构建结果。提交消息沿用简洁的动词式风格，常用前缀包括 `feat:`、`fix:` 与 `style:`。修改模板或样式时，请在本地预览相关页面；更多协作约定见 [AGENTS.md](AGENTS.md)。
