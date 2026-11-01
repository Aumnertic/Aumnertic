"""Generate profile SVGs (header + project cards) in light and dark themes."""
import sys
from pathlib import Path

OUT = Path(sys.argv[1])

THEMES = {
    "light": dict(bg="#f6f2ea", ink="#2f2a25", muted="#8a8076", line="#ddd5c7",
                  accent="#d4876a", fill="#f6f2ea"),
    "dark": dict(bg="#1a1c21", ink="#e8e2d8", muted="#9a958d", line="#33363d",
                 accent="#e09a7e", fill="#1a1c21"),
}

SERIF = "Georgia, 'Songti SC', 'Noto Serif CJK SC', 'Source Han Serif SC', serif"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"


def cat(t, x, y):
    """Sleeping curled cat; (x, y) = left end of the ground it rests on."""
    return f"""
  <g transform="translate({x} {y})" fill="{t['fill']}" stroke="{t['ink']}" stroke-width="2.4"
     stroke-linecap="round" stroke-linejoin="round">
    <path d="M52 0 C46 -48 88 -78 140 -78 C194 -78 230 -48 226 0"/>
    <path d="M226 -6 C246 4 236 14 200 14 C160 14 110 12 74 6" fill="none"/>
    <path d="M10 0 C4 -24 12 -46 30 -54 L28 -82 L50 -62 C58 -64 68 -64 76 -62 L96 -80 L96 -52 C110 -42 114 -20 108 0"/>
    <path d="M30 -30 Q36 -25 42 -30 M64 -30 Q70 -25 76 -30" fill="none" stroke-width="2"/>
    <path d="M51 -18 L55 -18 L53 -15Z" fill="{t['ink']}" stroke-width="1.6"/>
    <ellipse cx="26" cy="-17" rx="7" ry="3.5" fill="{t['accent']}" stroke="none" opacity=".45"/>
    <ellipse cx="82" cy="-17" rx="7" ry="3.5" fill="{t['accent']}" stroke="none" opacity=".45"/>
    <g fill="{t['muted']}" stroke="none" font-family="{SERIF}" font-style="italic">
      <text x="118" y="-96" font-size="16">z</text>
      <text x="134" y="-114" font-size="21">z</text>
    </g>
  </g>"""


def header(t):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="960" height="250" viewBox="0 0 960 250" role="img" aria-labelledby="title">
  <title id="title">Aum · aumnertic</title>
  <rect width="960" height="250" rx="18" fill="{t['bg']}"/>
  <text x="64" y="76" font-family="{MONO}" font-size="13" letter-spacing="2" fill="{t['muted']}">~/aumnertic</text>
  <text x="60" y="146" font-family="{SERIF}" font-size="68" fill="{t['ink']}">Aum</text>
  <text x="64" y="186" font-family="{SANS}" font-size="17" fill="{t['muted']}">学生，在杭州。写一点 Rust 和 Python。</text>
  <line x1="64" y1="210" x2="896" y2="210" stroke="{t['line']}" stroke-width="1.5"/>
  {cat(t, 660, 210)}
</svg>
"""


PROJECTS = [
    ("neko", ["AI 伙伴本体，", "Rust 核心加 Python 应用。"], [("Rust", "#dea584"), ("Python", "#3572a5")]),
    ("neko-mind", ["neko 的运行时，负责上下文", "和记忆，还在很早期。"], [("Rust", "#dea584")]),
    ("vman-py", ["扫描、记录、检查本机", "Python 虚拟环境的小工具。"], [("Python", "#3572a5"), ("SQLite", "#5fa8c9")]),
]


def card(t, name, lines, langs):
    desc = "".join(
        f'<text x="26" y="{88 + i * 22}" font-family="{SANS}" font-size="14" fill="{t["muted"]}">{l}</text>'
        for i, l in enumerate(lines))
    tags, x = [], 26
    for lang, color in langs:
        if t["bg"] == "#1a1c21" and color == "#3572a5":
            color = "#6b9fd6"
        tags.append(f'<circle cx="{x + 4}" cy="150" r="4" fill="{color}"/>'
                    f'<text x="{x + 14}" y="154.5" font-family="{MONO}" font-size="12" fill="{t["muted"]}">{lang}</text>')
        x += 24 + len(lang) * 7.4
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="300" height="178" viewBox="0 0 300 178" role="img" aria-labelledby="title">
  <title id="title">{name}</title>
  <rect x=".75" y=".75" width="298.5" height="176.5" rx="14" fill="{t['bg']}" stroke="{t['line']}" stroke-width="1.5"/>
  <text x="26" y="50" font-family="{SERIF}" font-size="24" fill="{t['ink']}">{name}</text>
  <path d="M272 38 l6 6 l-6 6" fill="none" stroke="{t['muted']}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
  {desc}
  {''.join(tags)}
</svg>
"""


for mode, t in THEMES.items():
    (OUT / f"header-{mode}.svg").write_text(header(t))
    for name, lines, langs in PROJECTS:
        (OUT / f"card-{name}-{mode}.svg").write_text(card(t, name, lines, langs))
print("ok")
