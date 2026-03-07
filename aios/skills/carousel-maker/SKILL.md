---
name: carousel-maker
description: >
  Create professional LinkedIn/Instagram carousel PDFs from URLs or pasted text.
  Use this skill whenever the user wants to create a carousel, slide deck for social media,
  turn an article into slides, make LinkedIn carousel posts, create Instagram carousels,
  or convert any written content into a swipeable multi-slide PDF. Also trigger when the
  user mentions "carousel," "slides for LinkedIn," "slide PDF," "social media slides,"
  or wants to repurpose articles/newsletters into visual slide formats.
---

# Carousel Maker

Create professional, branded carousel PDFs from articles, URLs, or pasted text.
Outputs clean HTML slides exported as a multi-page PDF ready for LinkedIn or Instagram.

---

## CRITICAL: No External Dependencies at Render Time

Claude's container has restricted network access. DO NOT use:
- Tailwind CSS CDN or any CDN-hosted CSS framework
- Google Fonts `<link>` tags or any externally loaded fonts at render time
- Any `<script>` or `<link>` tags that fetch from external URLs

ALL styling MUST be pure inline CSS or in a single `<style>` block within the HTML file.
Fonts are downloaded via npm at build time and base64-embedded in the HTML — no network needed at render time.

---

## Step 0: Ask the User — Light or Dark?

Before generating anything, **ask the user which theme they want**:

> "Would you like the **light** or **dark** version of this carousel?"

- If the user already specified a preference in their message, skip the question.
- Default to **dark** if the user says "surprise me" or has no preference.

---

## Step 1: Get the Content

Accept input in one of these forms:
- **URL**: Fetch the article using `web_fetch`. Extract the main body text.
- **Pasted text**: Use the text directly.
- **File**: Read from an uploaded file.

If given a URL, fetch it and extract the article body. Ignore nav, footer, sidebar, and ad content.

---

## Step 2: Generate Slide Copy

Analyze the article and break it into **8–12 slides**. Follow these constraints:

### Slide structure

- **Slide 1 (Hook):** Attention-grabbing title (max 10 words) + subtitle (max 15 words)
- **Slides 2–N (Content):** Headline (max 8 words) + 2–3 bullet points (max 15 words each) OR a single key quote/stat (max 20 words)
- **Final Slide (CTA):** Call to action with a clear next step

### Content rules

- Each slide conveys ONE idea only
- Use concrete numbers, specific examples, and strong verbs
- Bullets should be parallel in structure
- Strip jargon — write at a 6th-grade reading level where possible
- The hook slide must create curiosity or make a bold claim

---

## Step 3: Prepare Assets

### Font

The skill embeds real fonts via npm's `@fontsource` packages (registry.npmjs.org is on the allowed domains list). The default is **Inter**. Users can change the font in `references/templates.md` — see CUSTOMIZE.md for details.

**How to download and embed any font:**

```bash
# Install the font package (Inter is the default — swap the name for any Google Font)
npm install --prefix /home/claude/fonts @fontsource/inter 2>/dev/null

# The files you need are at:
# /home/claude/fonts/node_modules/@fontsource/inter/files/inter-latin-400-normal.woff2
# /home/claude/fonts/node_modules/@fontsource/inter/files/inter-latin-700-normal.woff2
```

**Pattern for any font:** `@fontsource/{font-name-kebab-case}` → files at `{font-name}-latin-{weight}-normal.woff2`

Examples:
- `@fontsource/inter` → `inter-latin-400-normal.woff2`
- `@fontsource/playfair-display` → `playfair-display-latin-400-normal.woff2`
- `@fontsource/space-grotesk` → `space-grotesk-latin-400-normal.woff2`

**In your Python build script**, base64-encode the woff2 files and embed as `@font-face` rules:

```python
import base64

FONT_FAMILY = "Inter"  # must match the actual font name (title case)
FONT_PKG = "inter"     # the npm package slug (kebab-case)

font_400_path = f"/home/claude/fonts/node_modules/@fontsource/{FONT_PKG}/files/{FONT_PKG}-latin-400-normal.woff2"
font_700_path = f"/home/claude/fonts/node_modules/@fontsource/{FONT_PKG}/files/{FONT_PKG}-latin-700-normal.woff2"

with open(font_400_path, "rb") as f:
    font_400_b64 = base64.b64encode(f.read()).decode()
with open(font_700_path, "rb") as f:
    font_700_b64 = base64.b64encode(f.read()).decode()
```

Then include in the HTML `<style>` block:

```html
@font-face {
  font-family: '{FONT_FAMILY}';
  font-weight: 400;
  src: url(data:font/woff2;base64,{font_400_b64}) format('woff2');
}
@font-face {
  font-family: '{FONT_FAMILY}';
  font-weight: 700;
  src: url(data:font/woff2;base64,{font_700_b64}) format('woff2');
}
```

**If npm install fails**, fall back to system fonts:
```
'Segoe UI', 'Helvetica Neue', Arial, sans-serif
```

### Headshot

Check for a headshot image:
```
/mnt/skills/user/carousel-maker/references/headshot.png
```
If found, base64-encode it for embedding:
```bash
HEADSHOT_B64=$(base64 -w 0 /mnt/skills/user/carousel-maker/references/headshot.png 2>/dev/null)
```
If not found, omit the headshot from the footer and show name/handle only.

### Background image (optional)

Check for a background/watermark image:
```
/mnt/skills/user/carousel-maker/references/background.png
```
If found, base64-encode it for embedding:
```bash
BG_B64=$(base64 -w 0 /mnt/skills/user/carousel-maker/references/background.png 2>/dev/null)
```
This can be any image — a logo, a photo, an illustration, an icon, an abstract shape. It displays as a large, centered, low-opacity watermark on every slide. If not found, skip — slides will have a clean solid background.

---

## Step 4: Build HTML

**IMPORTANT: Use a Python script to build the HTML.** Do NOT try to write the full HTML by hand. The script should:
1. Load the base64 assets (headshot, background image)
2. Define helper functions for reusable components (footer, page number, nav dots, background image)
3. Generate each slide by calling those functions
4. Assemble into a single HTML file

Read `references/templates.md` for the **Light** and **Dark** template designs, color systems, and component patterns.

### Page setup

- Each slide: `<div class="slide">` with explicit width/height
- Default dimensions: **1080×1350px** (4:5 ratio for LinkedIn/Instagram)
- Other options: 1080×1080px (1:1), 1080×1920px (9:16 Stories)

### Required HTML skeleton

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { margin: 0; padding: 0; }
    @media print {
      .slide { page-break-after: always; }
      .slide:last-child { page-break-after: avoid; }
      @page { size: 1080px 1350px; margin: 0; }
    }
  </style>
</head>
<body>
  <!-- slides here -->
</body>
</html>
```

### Slide layout structure

Every slide has these layers (back to front):

1. **Background color** — solid color on the slide div
2. **Background image** — large centered watermark, low opacity (see below)
3. **Page number** — top-left corner, large bold accent number (just the number, e.g., "03")
4. **Content area** — padded region for headline + bullets or centered hook text
5. **Footer bar** — anchored to bottom with headshot, name, dots, and nav chevron

### Page number (top-left)

```html
<div style="position: absolute; top: 48px; left: 100px; font-size: 42px; font-weight: 800; color: {ACCENT};">03</div>
```
- Show only the number (e.g., `03`), NOT `3 / 10`
- Zero-padded, 42px, font-weight 800, accent color

### Background image (centered watermark)

If `background.png` exists, display as:
```html
<img src="data:image/png;base64,..." style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: {BG_SIZE}px; height: {BG_SIZE}px; opacity: 0.08; object-fit: contain; pointer-events: none;" />
```

**Background image scale** — default `1000px`. The user can request a different scale:
- `600px` — subtle small watermark
- `800px` — medium
- `1000px` — large (default), fills most of the slide
- `1200px` — bleeds off edges for an immersive feel

### Content area

- **Padding:** 100px left/right (provides space for LinkedIn's navigation arrows), 130px top (clears page number), bottom stops 180px from slide bottom (clears footer)
- **Category labels:** 22px, font-weight 700, uppercase, accent color, letter-spacing 2–3px
- **Headlines:** 52–64px, font-weight 700–800
- **Body/bullets:** 32px, line-height 1.5
- **Bullet layout:** Use a table so spacing is reliable in WeasyPrint (flexbox margin/gap is buggy in PDF engines):
```html
<table cellspacing="0" cellpadding="0" style="border-collapse: collapse; width: 100%;">
  <tr>
    <td style="vertical-align: top; padding: 0 16px 28px 0; width: 32px;">
      <span style="color: {ACCENT_LT}; font-weight: 700; font-size: 32px; line-height: 1.5;">→</span>
    </td>
    <td style="vertical-align: top; padding: 0 0 28px 0;">
      <p style="font-size: 32px; color: {BODY}; line-height: 1.5; margin: 0;">Bullet text here</p>
    </td>
  </tr>
  <!-- one tr per bullet -->
</table>
```

### Footer bar (EVERY slide)

160px tall, absolutely positioned at bottom. Three sections in a flex row:

**Left — Headshot + Identity:**
```html
<div style="display: flex; align-items: center; gap: 20px; white-space: nowrap; flex-shrink: 0;">
  <img src="data:image/png;base64,..." width="64" height="64"
       style="width: 64px; height: 64px; border-radius: 50%; object-fit: cover; display: block; flex-shrink: 0;" />
  <div style="flex-shrink: 0;">
    <p style="font-size: 22px; font-weight: 600; color: {NAME_COLOR}; margin: 0;">Author Name</p>
    <p style="font-size: 17px; color: {HANDLE_COLOR}; margin: 0;">@handle</p>
  </div>
</div>
```

**Center — Navigation dots:**
Use an HTML `<table>` for reliable dot spacing (WeasyPrint handles table spacing better than flex gap):
```html
<table cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
  <tr>
    <td style="padding: 0 6px;"><div style="width: 14px; height: 14px; border-radius: 50%; background: {ACCENT};"></div></td>
    <td style="padding: 0 6px;"><div style="width: 14px; height: 14px; border-radius: 50%; border: 2px solid {DOT_BORDER};"></div></td>
    <!-- one td per slide, filled = current -->
  </tr>
</table>
```

**Right — Directional chevron:**
SVG chevron arrow pointing right. Show on all slides except the last (CTA) slide.
```html
<svg width="24" height="24" viewBox="0 0 24 24" fill="none">
  <path d="M9 6L15 12L9 18" stroke="{ACCENT}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
```
On the last slide, render an empty `<div style="width: 24px;">` to maintain layout spacing.

### Design rules

- ALL colors as hex values
- Accent color: teal (`#0d9488` primary, `#14b8a6` lighter)
- Create visual interest through the background watermark and color alternation
- Alternate background colors between slides for visual rhythm (e.g., `#0f172a` and `#111b30` for dark theme)
- Use `overflow: hidden` on every slide div to clip background elements

---

## Step 5: Convert to PDF

**The HTML file must be saved before converting.**

```bash
pip install playwright --break-system-packages -q 2>/dev/null
playwright install chromium 2>/dev/null
python /mnt/skills/user/carousel-maker/scripts/html_to_pdf.py /home/claude/carousel.html /home/claude/carousel.pdf --width 1080 --height 1350
```

**If Playwright fails**, use the WeasyPrint fallback:

```bash
pip install weasyprint --break-system-packages -q 2>/dev/null
python /mnt/skills/user/carousel-maker/scripts/html_to_pdf_fallback.py /home/claude/carousel.html /home/claude/carousel.pdf --width 1080 --height 1350
```

**If both fail**, provide the HTML file and instruct the user to print-to-PDF from Chrome (Paper: Custom 1080×1350, Margins: None, Background graphics: On).

---

## Step 6: Deliver

Copy the final PDF and HTML file to `/mnt/user-data/outputs/` and present to the user.

---

## Customization

Users can personalize this skill for their own brand. See **CUSTOMIZE.md** in the skill root for a complete guide. Key settings:

| What | Where to edit |
|---|---|
| Accent color | `references/templates.md` — swap the teal hex values |
| Font | `references/templates.md` — update Font family, Font npm package, and Font file slug |
| Author name & handle | `references/templates.md` — replace in branding defaults |
| Headshot | Drop a `headshot.png` into `references/` |
| Background image | Drop a `background.png` into `references/` |
| Background scale | Request a size when making a carousel, or edit default in templates.md |
| Slide dimensions | Request a different ratio, or edit defaults in this file |

---

## Important Reminders

- NEVER use external CDNs or scripts at render time (fonts are pre-embedded via npm + base64)
- Use a Python build script — do not hand-write the full HTML
- Leave 180px at the bottom of the content area to clear the 160px footer
- 100px side padding on all content for LinkedIn nav arrows
- Generate navigation dots dynamically based on actual slide count
- The hook slide is the most important — make it compelling
- Alternate background colors between slides for visual rhythm
