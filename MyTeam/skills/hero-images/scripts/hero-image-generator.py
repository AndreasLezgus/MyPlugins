#!/usr/bin/env python3
"""
Hero Image Generator – Die Zweite Meinung
Liest JSON-Templates aus templates/hero-templates/ und erstellt 1200×628px PNGs.

Verwendung:
  python3 hero-image-generator.py \
    --template ki-fuehrung-standard \
    --title "Ihr Artikel-Titel" \
    --subtitle "Ergänzende Zeile (optional)" \
    --subline "Kurze Beschreibung unter dem Trennstrich" \
    --count 8 \
    --output /pfad/zum/output.png

Argumente:
  --template    Name der JSON-Datei (ohne .json)
  --title       Erste Überschrift (Pflicht)
  --subtitle    Zweite Überschrift (optional)
  --subline     Kleiner Text unter dem Divider (optional)
  --count       Zahl für Badge (nur Quick-Checks-Layout, optional)
  --output      Ausgabepfad (Standard: ./hero-output.png)
  --templates-dir  Pfad zum templates/hero-templates/ Ordner
"""

import sys
import json
import argparse
import os
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Fehler: Pillow nicht installiert. Bitte ausführen:")
    print("  pip install Pillow --break-system-packages")
    sys.exit(1)

# ── Systemfonts ──────────────────────────────────────────────────────────────

FONT_PATHS = {
    "serif-bold":   [
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf",
    ],
    "sans-regular": [
        "/usr/share/fonts/truetype/freefont/FreeSans.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ],
    "sans-bold": [
        "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ],
}

W, H = 1200, 628


def find_font(style: str) -> str:
    for path in FONT_PATHS.get(style, FONT_PATHS["sans-regular"]):
        if os.path.exists(path):
            return path
    # Fallback: any truetype font on the system
    import glob
    fonts = glob.glob("/usr/share/fonts/**/*.ttf", recursive=True)
    return fonts[0] if fonts else None


def hex_to_rgb(hex_str: str) -> tuple:
    h = hex_str.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def hex_to_rgba(hex_str: str, opacity: float = 1.0) -> tuple:
    r, g, b = hex_to_rgb(hex_str)
    return (r, g, b, int(opacity * 255))


def get_font(style: str, size: int) -> ImageFont.FreeTypeFont:
    path = find_font(style)
    if path:
        return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def draw_gradient_bg(draw: ImageDraw.Draw, color_top: str, color_bottom: str):
    r1, g1, b1 = hex_to_rgb(color_top)
    r2, g2, b2 = hex_to_rgb(color_bottom)
    for y in range(H):
        t = y / H
        r = int(r1 + (r2 - r1) * t)
        g = int(g1 + (g2 - g1) * t)
        b = int(b1 + (b2 - b1) * t)
        draw.line([(0, y), (W, y)], fill=(r, g, b, 255))


def draw_solid_bg(draw: ImageDraw.Draw, color: str):
    r, g, b = hex_to_rgb(color)
    draw.rectangle([(0, 0), (W, H)], fill=(r, g, b, 255))


def draw_decoration_circle(draw: ImageDraw.Draw, color: str, opacity: float):
    c = hex_to_rgba(color, opacity)
    draw.ellipse([(850, -120), (1320, 350)], outline=c, width=2)
    draw.ellipse([(890, -80), (1280, 310)],  outline=hex_to_rgba(color, opacity * 0.5), width=1)


def draw_decoration_triangle(draw: ImageDraw.Draw, color: str, opacity: float):
    c1 = hex_to_rgba(color, opacity)
    c2 = hex_to_rgba(color, opacity * 0.75)
    c3 = hex_to_rgba(color, opacity * 0.5)
    draw.polygon([(W - 380, 0), (W, 0), (W, 420)], fill=c1)
    draw.polygon([(W - 240, 0), (W, 0), (W, 260)], fill=c2)
    draw.polygon([(W - 120, 0), (W, 0), (W, 130)], fill=c3)


def draw_decoration_checklist(draw: ImageDraw.Draw, color: str, opacity: float):
    font_check = get_font("sans-bold", 20)
    font_label = get_font("sans-regular", 15)
    items = [
        (True,  "Datenlage geprüft"),
        (True,  "Verantwortung benannt"),
        (True,  "Rechtslage geklärt"),
        (False, "Erfolgsmessung definiert"),
        (False, "Feedbackschleife aktiv"),
    ]
    check_x = 820
    for i, (done, label) in enumerate(items):
        y_pos = 80 + i * 88
        alpha = int(opacity * (200 if done else 130))
        box_color = hex_to_rgba(color, opacity * (0.85 if done else 0.5))
        draw.rectangle([(check_x, y_pos), (check_x + 36, y_pos + 36)],
                       outline=box_color, width=2)
        if done:
            draw.text((check_x + 7, y_pos + 4), "✓",
                      font=font_check, fill=box_color)
        draw.text((check_x + 50, y_pos + 9), label,
                  font=font_label, fill=(60, 70, 80, alpha))


def draw_scan_lines(draw: ImageDraw.Draw):
    for y in range(0, H, 4):
        draw.line([(0, y), (W, y)], fill=(255, 255, 255, 4))


def draw_grid(draw: ImageDraw.Draw, color: str, alpha: int = 12):
    r, g, b = hex_to_rgb(color)
    for x in range(0, W, 60):
        draw.line([(x, 0), (x, H)], fill=(r, g, b, alpha))
    for y in range(0, H, 60):
        draw.line([(0, y), (W, y)], fill=(r, g, b, alpha))


def generate_hero(template: dict, title: str, subtitle: str = "",
                  subline: str = "", count: int = 0, output_path: str = "hero-output.png"):

    img = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    draw = ImageDraw.Draw(img, "RGBA")

    # ── Background ────────────────────────────────────────────────────────────
    bg = template["background"]
    if bg["type"] == "gradient":
        draw_gradient_bg(draw, bg["color_top"], bg["color_bottom"])
    else:
        draw_solid_bg(draw, bg["color"])

    # ── Decoration ────────────────────────────────────────────────────────────
    accent   = template.get("accent", {})
    deco     = accent.get("decoration", "none")
    deco_col = accent.get("decoration_color", accent.get("color", "#FFFFFF"))
    deco_op  = accent.get("decoration_opacity", 0.12)

    if deco == "circle-top-right":
        draw_decoration_circle(draw, deco_col, deco_op)
        # Subtle diagonal lines on dark backgrounds
        for i in range(-H, W + H, 50):
            draw.line([(i, 0), (i + H, H)], fill=(255, 255, 255, 6))
    elif deco == "triangle-top-right":
        draw_decoration_triangle(draw, deco_col, deco_op)
        draw_scan_lines(draw)
    elif deco == "checklist-right":
        draw_grid(draw, accent.get("color", "#008080"), alpha=12)
        draw_decoration_checklist(draw, accent.get("color", "#008080"), deco_op)

    # ── Left accent bar ───────────────────────────────────────────────────────
    if accent.get("bar_left", True):
        bar_width  = accent.get("bar_width", 6)
        bar_color  = hex_to_rgba(accent["color"], 0.9)
        bar_margin = 72 if template["layout"].get("text_x", 96) > 50 else 0
        draw.rectangle([(bar_margin, 80), (bar_margin + bar_width, H - 80)],
                       fill=bar_color)

    # ── Fonts ─────────────────────────────────────────────────────────────────
    fonts = template["font"]
    f_headline = get_font(fonts.get("headline", "serif-bold"),
                          fonts.get("headline_size", 52))
    f_sub      = get_font(fonts.get("headline", "serif-bold"),
                          fonts.get("sub_size", 40))
    f_subline  = get_font(fonts.get("body", "sans-regular"),
                          fonts.get("subline_size", 18))
    f_tag      = get_font(fonts.get("body", "sans-bold"),
                          fonts.get("tag_size", 14))
    f_meta     = get_font(fonts.get("body", "sans-regular"), 13)

    # ── Text colors ───────────────────────────────────────────────────────────
    tc = template["text"]
    col_headline = hex_to_rgba(tc.get("headline", "#FFFFFF"))
    col_sub      = hex_to_rgba(tc.get("headline_sub", "#FFFFFF"), 0.90)
    col_subline  = hex_to_rgba(tc.get("subline", "#AAAAAA"), 0.80)
    col_tag      = hex_to_rgba(tc.get("tag", "#FFFFFF"), 0.88)
    col_meta     = hex_to_rgba(tc.get("meta", "#888888"), 0.80)

    # ── Layout ───────────────────────────────────────────────────────────────
    layout = template["layout"]
    tx = layout.get("text_x", 96)
    hy = layout.get("headline_y", 158)

    tag_y = 82 if tx > 50 else 82
    draw.text((tx, tag_y),      template.get("tag_label",  ""),  font=f_tag, fill=col_tag)
    draw.text((tx, tag_y + 18), template.get("site_label", ""), font=f_tag, fill=hex_to_rgba(tc.get("meta", "#888"), 0.6))

    # Headline line 1 (title)
    draw.text((tx, hy), title, font=f_headline, fill=col_headline)

    # Measure headline to position subtitle
    bbox = draw.textbbox((0, 0), title, font=f_headline)
    title_h = bbox[3] - bbox[1]
    sub_y = hy + title_h + 8

    # Subtitle
    if subtitle:
        draw.text((tx, sub_y), subtitle, font=f_sub, fill=col_sub)
        bbox2 = draw.textbbox((0, 0), subtitle, font=f_sub)
        sub_y += (bbox2[3] - bbox2[1]) + 4

    # Count badge (Quick Checks)
    if layout.get("show_count_badge") and count > 0:
        badge_y = sub_y + 24
        badge_bg = hex_to_rgba(accent.get("color", "#00968C"), 0.94)
        draw.ellipse([(tx, badge_y), (tx + 80, badge_y + 80)], fill=badge_bg)
        f_num = get_font("sans-bold", 36)
        num_str = str(count)
        nb = draw.textbbox((0, 0), num_str, font=f_num)
        nx = tx + (80 - (nb[2] - nb[0])) // 2
        draw.text((nx, badge_y + 14), num_str, font=f_num, fill=(255, 255, 255, 255))
        draw.text((tx + 92, badge_y + 20), "Prüfpunkte",        font=f_subline, fill=col_headline)
        draw.text((tx + 92, badge_y + 46), "für Führungskräfte", font=f_subline, fill=col_subline)
        sub_y = badge_y + 96

    # Warning icon (Kritisches Denken)
    if layout.get("show_warning_icon"):
        f_warn = get_font("serif-bold", 80)
        draw.text((1040, 180), "!", font=f_warn,
                  fill=hex_to_rgba(accent.get("color", "#DC4632"), 0.22))

    # Divider
    if layout.get("show_divider") and subline:
        div_y = sub_y + 24
        div_col = hex_to_rgba(layout.get("divider_color", accent.get("color", "#FFF")), 0.55)
        draw.line([(tx, div_y), (min(tx + 520, W - 60), div_y)], fill=div_col, width=1)
        draw.text((tx, div_y + 12), subline, font=f_subline, fill=col_subline)

    # ── Meta bar ─────────────────────────────────────────────────────────────
    if layout.get("show_meta_bar", True):
        bar_bg  = hex_to_rgb(layout.get("meta_bar_bg", "#000000"))
        bar_opa = int(layout.get("meta_bar_opacity", 0.5) * 255)
        draw.rectangle([(0, H - 52), (W, H)],
                       fill=bar_bg + (bar_opa,))

    footer = template.get("footer_text", "")
    if footer:
        draw.text((tx, H - 34), footer, font=f_meta, fill=col_meta)

    # ── Save ─────────────────────────────────────────────────────────────────
    img_rgb = img.convert("RGB")
    img_rgb.save(output_path, "PNG", quality=95)
    print(f"✅ {output_path}")
    return output_path


def load_template(templates_dir: str, name: str) -> dict:
    path = Path(templates_dir) / f"{name}.json"
    if not path.exists():
        print(f"❌ Template nicht gefunden: {path}")
        print(f"   Verfügbare Templates in {templates_dir}:")
        for f in Path(templates_dir).glob("*.json"):
            print(f"   – {f.stem}")
        sys.exit(1)
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def main():
    parser = argparse.ArgumentParser(description="Hero Image Generator – Die Zweite Meinung")
    parser.add_argument("--template",      required=True, help="Template-Name (ohne .json)")
    parser.add_argument("--title",         required=True, help="Erste Überschrift")
    parser.add_argument("--subtitle",      default="",    help="Zweite Überschrift (optional)")
    parser.add_argument("--subline",       default="",    help="Text unter Divider (optional)")
    parser.add_argument("--count",         type=int, default=0, help="Zahl für Badge (Quick Checks)")
    parser.add_argument("--output",        default="hero-output.png", help="Ausgabepfad")
    parser.add_argument("--templates-dir", default="templates/hero-templates",
                        help="Pfad zum Templates-Ordner")
    args = parser.parse_args()

    # Auto-expand ~ and create output directory
    output_path = os.path.expanduser(args.output)
    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)

    templates_dir = os.path.expanduser(args.templates_dir)

    template = load_template(templates_dir, args.template)
    generate_hero(
        template    = template,
        title       = args.title,
        subtitle    = args.subtitle,
        subline     = args.subline,
        count       = args.count,
        output_path = output_path,
    )


if __name__ == "__main__":
    main()
