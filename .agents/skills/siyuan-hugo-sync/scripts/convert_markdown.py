#!/usr/bin/env python3
"""Convert Markdown between SiYuan export style and Hugo post style."""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None


SIYUAN_TO_HUGO = {
    "NOTE": "note",
    "TIP": "tips",
    "IMPORTANT": "important",
    "WARNING": "warning",
    "CAUTION": "error",
}

HUGO_TO_SIYUAN = {
    "note": "NOTE",
    "info": "NOTE",
    "tips": "TIP",
    "tip": "TIP",
    "important": "IMPORTANT",
    "warning": "WARNING",
    "error": "CAUTION",
    "caution": "CAUTION",
}


def split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    raw = text[4:end].strip()
    body = text[end + len("\n---") :].lstrip("\n")
    if not raw:
        return {}, body
    if yaml is None:
        raise SystemExit("PyYAML is required to parse front matter")
    data = yaml.safe_load(raw) or {}
    if not isinstance(data, dict):
        raise SystemExit("Front matter must be a YAML mapping")
    return data, body


def dump_frontmatter(data: dict[str, Any]) -> str:
    if yaml is None:
        raise SystemExit("PyYAML is required to write front matter")

    class HugoDumper(yaml.SafeDumper):
        def increase_indent(self, flow: bool = False, indentless: bool = False) -> Any:
            return super().increase_indent(flow, False)

    def normalize(value: Any) -> Any:
        if isinstance(value, dt.datetime):
            return value.isoformat()
        if isinstance(value, dt.date):
            return value.isoformat()
        if isinstance(value, list):
            return [normalize(item) for item in value]
        if isinstance(value, dict):
            return {key: normalize(item) for key, item in value.items()}
        return value

    ordered: dict[str, Any] = {}
    for key in ("title", "date", "lastmod", "draft", "tags"):
        if key in data:
            ordered[key] = normalize(data[key])
    for key, value in data.items():
        if key not in ordered:
            ordered[key] = normalize(value)
    return yaml.dump(
        ordered,
        Dumper=HugoDumper,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    ).strip()


def parse_metadata(items: list[str]) -> dict[str, Any]:
    if not items:
        return {}
    if yaml is None:
        raise SystemExit("PyYAML is required to parse metadata overrides")
    out: dict[str, Any] = {}
    for item in items:
        if "=" not in item:
            raise SystemExit(f"Metadata override must be key=value: {item}")
        key, value = item.split("=", 1)
        out[key] = yaml.safe_load(value)
    return out


def now_iso() -> str:
    return dt.datetime.now().astimezone().replace(microsecond=0).isoformat()


def remove_duplicate_h1(body: str, title: Any) -> str:
    if not title:
        return body
    lines = body.splitlines()
    if len(lines) >= 2 and lines[0].startswith("# ") and lines[0][2:].strip() == str(title).strip():
        return "\n".join(lines[2:]).lstrip("\n") + ("\n" if body.endswith("\n") else "")
    return body


def ensure_summary_marker(body: str) -> str:
    if "<!--more-->" in body:
        return body
    lines = body.splitlines()
    for i, line in enumerate(lines):
        if not line.strip() or line.startswith("#") or line.startswith(">") or line.startswith("```"):
            continue
        insert_at = i + 1
        while insert_at < len(lines) and lines[insert_at].strip():
            insert_at += 1
        lines[insert_at:insert_at] = ["", "<!--more-->"]
        return "\n".join(lines).rstrip() + "\n"
    return body


def is_escaped(text: str, pos: int) -> bool:
    backslashes = 0
    i = pos - 1
    while i >= 0 and text[i] == "\\":
        backslashes += 1
        i -= 1
    return backslashes % 2 == 1


def is_single_dollar(text: str, pos: int) -> bool:
    if text[pos] != "$" or is_escaped(text, pos):
        return False
    previous_is_dollar = pos > 0 and text[pos - 1] == "$"
    next_is_dollar = pos + 1 < len(text) and text[pos + 1] == "$"
    return not previous_is_dollar and not next_is_dollar


def convert_siyuan_inline_math_plain(text: str) -> str:
    out: list[str] = []
    i = 0
    while i < len(text):
        if is_single_dollar(text, i) and i + 1 < len(text) and not text[i + 1].isspace():
            j = i + 1
            while j < len(text):
                if is_single_dollar(text, j) and not text[j - 1].isspace():
                    content = text[i + 1 : j]
                    if content:
                        out.append(r"\(")
                        out.append(content)
                        out.append(r"\)")
                        i = j + 1
                        break
                j += 1
            else:
                out.append(text[i])
                i += 1
        else:
            out.append(text[i])
            i += 1
    return "".join(out)


def is_hugo_inline_math_delimiter(text: str, pos: int, paren: str) -> bool:
    return text.startswith("\\" + paren, pos) and (pos == 0 or text[pos - 1] != "\\")


def convert_hugo_inline_math_plain(text: str) -> str:
    out: list[str] = []
    i = 0
    while i < len(text):
        if is_hugo_inline_math_delimiter(text, i, "("):
            j = i + 2
            while j < len(text):
                if is_hugo_inline_math_delimiter(text, j, ")"):
                    content = text[i + 2 : j]
                    if content:
                        out.append("$")
                        out.append(content)
                        out.append("$")
                        i = j + 2
                        break
                j += 1
            else:
                out.append(text[i])
                i += 1
        else:
            out.append(text[i])
            i += 1
    return "".join(out)


def convert_inline_math_outside_code_spans(text: str, direction: str) -> str:
    convert_plain = (
        convert_siyuan_inline_math_plain
        if direction == "siyuan-to-hugo"
        else convert_hugo_inline_math_plain
    )
    out: list[str] = []
    i = 0
    while i < len(text):
        if text[i] == "`":
            tick_count = 1
            while i + tick_count < len(text) and text[i + tick_count] == "`":
                tick_count += 1
            marker = "`" * tick_count
            end = text.find(marker, i + tick_count)
            if end == -1:
                out.append(text[i:])
                break
            out.append(text[i : end + tick_count])
            i = end + tick_count
            continue

        start = i
        while i < len(text) and text[i] != "`":
            i += 1
        out.append(convert_plain(text[start:i]))
    return "".join(out)


def find_unescaped_double_dollar(text: str, start: int = 0) -> int:
    i = start
    while i < len(text) - 1:
        if text.startswith("$$", i) and not is_escaped(text, i):
            return i
        i += 1
    return -1


def find_display_math_delimiter(text: str, start: int = 0) -> int:
    i = start
    while i < len(text) - 1:
        if text[i] == "`":
            tick_count = 1
            while i + tick_count < len(text) and text[i + tick_count] == "`":
                tick_count += 1
            marker = "`" * tick_count
            end = text.find(marker, i + tick_count)
            if end == -1:
                return -1
            i = end + tick_count
            continue
        if text.startswith("$$", i) and not is_escaped(text, i):
            return i
        i += 1
    return -1


def convert_inline_math_line(line: str, direction: str, in_display_math: bool) -> tuple[str, bool]:
    out: list[str] = []
    i = 0
    while i < len(line):
        if in_display_math:
            marker = find_unescaped_double_dollar(line, i)
            if marker == -1:
                out.append(line[i:])
                return "".join(out), True
            out.append(line[i : marker + 2])
            i = marker + 2
            in_display_math = False
            continue

        marker = find_display_math_delimiter(line, i)
        if marker == -1:
            out.append(convert_inline_math_outside_code_spans(line[i:], direction))
            return "".join(out), False

        out.append(convert_inline_math_outside_code_spans(line[i:marker], direction))
        close = find_unescaped_double_dollar(line, marker + 2)
        if close == -1:
            out.append(line[marker:])
            return "".join(out), True
        out.append(line[marker : close + 2])
        i = close + 2

    return "".join(out), in_display_math


def convert_inline_math(body: str, direction: str) -> str:
    lines = body.splitlines()
    out: list[str] = []
    in_code_fence = False
    code_fence_char = ""
    code_fence_len = 0
    in_display_math = False

    for line in lines:
        fence = re.match(r"^\s*(`{3,}|~{3,})", line)
        if fence and not in_display_math:
            marker = fence.group(1)
            fence_char = marker[0]
            if not in_code_fence:
                in_code_fence = True
                code_fence_char = fence_char
                code_fence_len = len(marker)
            elif fence_char == code_fence_char and len(marker) >= code_fence_len:
                in_code_fence = False
                code_fence_char = ""
                code_fence_len = 0
            out.append(line)
            continue

        if in_code_fence:
            out.append(line)
            continue

        converted, in_display_math = convert_inline_math_line(line, direction, in_display_math)
        out.append(converted)

    return "\n".join(out) + ("\n" if body.endswith("\n") else "")


def convert_siyuan_callouts(body: str) -> str:
    lines = body.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        marker = re.match(r"^> \[!(\w+)\]\s*$", lines[i])
        if not marker:
            out.append(lines[i])
            i += 1
            continue
        callout_type = SIYUAN_TO_HUGO.get(marker.group(1).upper(), marker.group(1).lower())
        content: list[str] = []
        i += 1
        while i < len(lines) and (lines[i] == ">" or lines[i].startswith("> ")):
            content.append(lines[i][2:] if lines[i].startswith("> ") else "")
            i += 1
        if out and out[-1] != "":
            out.append("")
        out.extend([f'{{{{< callout type="{callout_type}" >}}}}', ""])
        out.extend(content)
        out.extend(["", "{{< /callout >}}"])
        if i < len(lines) and lines[i] != "":
            out.append("")
    return "\n".join(out).rstrip() + "\n"


def convert_hugo_callouts(body: str) -> str:
    pattern = re.compile(
        r'\{\{<\s*callout\s+type="([^"]+)"\s*>\}\}\s*\n(.*?)\n\s*\{\{<\s*/callout\s*>\}\}',
        re.S,
    )

    def replace(match: re.Match[str]) -> str:
        marker = HUGO_TO_SIYUAN.get(match.group(1).lower(), match.group(1).upper())
        content = match.group(2).strip("\n").splitlines()
        quoted = [f"> [!{marker}]"]
        quoted.extend("> " + line if line else ">" for line in content)
        return "\n".join(quoted)

    return pattern.sub(replace, body)


def siyuan_to_hugo(args: argparse.Namespace) -> None:
    src = Path(args.input).read_text(encoding="utf-8")
    src_meta, body = split_frontmatter(src)
    existing_meta: dict[str, Any] = {}
    if args.existing and Path(args.existing).exists():
        existing_meta, _ = split_frontmatter(Path(args.existing).read_text(encoding="utf-8"))
    meta = {**existing_meta, **src_meta, **parse_metadata(args.set)}
    if args.lastmod == "now":
        meta["lastmod"] = now_iso()
    elif args.lastmod:
        meta["lastmod"] = args.lastmod
    body = body.replace("\u200b", "")
    body = remove_duplicate_h1(body, meta.get("title"))
    body = convert_siyuan_callouts(body)
    body = convert_inline_math(body, "siyuan-to-hugo")
    if args.insert_more:
        body = ensure_summary_marker(body)
    output = f"---\n{dump_frontmatter(meta)}\n---\n\n{body.rstrip()}\n"
    Path(args.output).write_text(output, encoding="utf-8")


def hugo_to_siyuan(args: argparse.Namespace) -> None:
    src = Path(args.input).read_text(encoding="utf-8")
    meta, body = split_frontmatter(src)
    if not args.strip_frontmatter:
        meta = {**meta, **parse_metadata(args.set)}
    body = body.replace("<!--more-->", "").replace("\u200b", "")
    body = convert_inline_math(body, "hugo-to-siyuan")
    body = convert_hugo_callouts(body).strip() + "\n"
    if args.strip_frontmatter:
        output = body
    else:
        output = f"---\n{dump_frontmatter(meta)}\n---\n\n{body}"
    Path(args.output).write_text(output, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p1 = sub.add_parser("siyuan-to-hugo")
    p1.add_argument("input")
    p1.add_argument("output")
    p1.add_argument("--existing")
    p1.add_argument("--lastmod", default="now", help="'now', explicit ISO timestamp, or empty string")
    p1.add_argument("--set", action="append", default=[], metavar="KEY=YAML")
    p1.add_argument("--insert-more", action="store_true")
    p1.set_defaults(func=siyuan_to_hugo)

    p2 = sub.add_parser("hugo-to-siyuan")
    p2.add_argument("input")
    p2.add_argument("output")
    p2.add_argument("--strip-frontmatter", action="store_true")
    p2.add_argument("--set", action="append", default=[], metavar="KEY=YAML")
    p2.set_defaults(func=hugo_to_siyuan)

    args = parser.parse_args()
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
