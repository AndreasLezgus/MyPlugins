# Carousel Templates

Two branded templates: **Dark** and **Light**. Both use embedded fonts (Inter by default) with teal accent and include a branded footer with headshot, name/handle, navigation dots, and directional chevron.

---

## Branding Defaults

These values appear throughout both templates. To customize, find-and-replace:

| Element | Default value |
|---|---|
| **Author name** | `Andreas Lezgus` |
| **Handle** | `@andreaslezgus` |
| **Accent color** | `#0d9488` |
| **Accent light** | `#14b8a6` |
| **Font family** | `'Inter', sans-serif` |
| **Font npm package** | `@fontsource/inter` |
| **Font file slug** | `inter` (used in file paths: `inter-latin-400-normal.woff2`) |
| **Background image scale** | `1000px` (options: 600, 800, 1000, 1200) |

### Changing the font

To use a different font, update three values:

1. **Font family** — the CSS name, e.g. `'Playfair Display'`
2. **Font npm package** — the @fontsource package, e.g. `@fontsource/playfair-display`
3. **Font file slug** — the kebab-case prefix in file names, e.g. `playfair-display`

The build script will `npm install` the package, base64-encode the latin 400 + 700 woff2 files, and embed them as `@font-face` rules. See SKILL.md Step 3 for details.

Browse available fonts at [fontsource.org](https://fontsource.org/).

---

## Color Systems

### Dark theme

| Role | Hex | Usage |
|---|---|---|
| Background primary | `#0f172a` | Odd slides |
| Background alternate | `#111b30` | Even slides — creates visual rhythm |
| Text primary | `#f1f5f9` | Headlines |
| Text body | `#e2e8f0` | Bullet text |
| Text muted | `#94a3b8` | Subtitles, handle, page numbers |
| Accent | `#0d9488` | Category labels, dots, page number, CTA, chevron |
| Accent light | `#14b8a6` | Highlighted headline words, arrow bullets |
| Dot border | `#475569` | Inactive nav dots, page number slash |
| Footer border | `#1e293b` | Top border on footer bar |

### Light theme

| Role | Hex | Usage |
|---|---|---|
| Background primary | `#ffffff` | Odd slides |
| Background alternate | `#f8fafc` | Even slides |
| Text primary | `#0f172a` | Headlines |
| Text body | `#334155` | Bullet text |
| Text muted | `#64748b` | Subtitles, handle, page numbers |
| Accent | `#0d9488` | Category labels, dots, page number, CTA, chevron |
| Accent light | `#0d9488` | Highlighted headline words, arrow bullets |
| Dot border | `#cbd5e1` | Inactive nav dots |
| Footer border | `#e2e8f0` | Top border on footer bar |

---

## Slide Components

### Page number (top-left)

Just the slide number, zero-padded, large and bold in accent color.

**Dark:**
```html
<div style="position: absolute; top: 48px; left: 100px; font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; font-size: 42px; font-weight: 800; color: #0d9488;">03</div>
```

**Light:**
```html
<div style="position: absolute; top: 48px; left: 100px; font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; font-size: 42px; font-weight: 800; color: #0d9488;">03</div>
```

### Background image (centered watermark)

Large, centered, low-opacity. Only rendered if `references/background.png` exists.

```html
<img src="data:image/png;base64,..." style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 1000px; height: 1000px; opacity: 0.08; object-fit: contain; pointer-events: none;" />
```

Scale options: 600px (subtle), 800px (medium), 1000px (large, default), 1200px (immersive).

### Bullet rows

Table layout for reliable spacing in WeasyPrint (flexbox margin/gap is buggy in PDF engines). One `<tr>` per bullet, with `padding-bottom: 28px` on cells for spacing.

**Dark:**
```html
<table cellspacing="0" cellpadding="0" style="border-collapse: collapse; width: 100%;">
  <tr>
    <td style="vertical-align: top; padding: 0 16px 28px 0; width: 32px;">
      <span style="color: #14b8a6; font-weight: 700; font-size: 32px; line-height: 1.5;">→</span>
    </td>
    <td style="vertical-align: top; padding: 0 0 28px 0;">
      <p style="font-size: 32px; color: #e2e8f0; line-height: 1.5; margin: 0;">Bullet text goes here</p>
    </td>
  </tr>
  <!-- one tr per bullet -->
</table>
```

**Light:**
```html
<table cellspacing="0" cellpadding="0" style="border-collapse: collapse; width: 100%;">
  <tr>
    <td style="vertical-align: top; padding: 0 16px 28px 0; width: 32px;">
      <span style="color: #0d9488; font-weight: 700; font-size: 32px; line-height: 1.5;">→</span>
    </td>
    <td style="vertical-align: top; padding: 0 0 28px 0;">
      <p style="font-size: 32px; color: #334155; line-height: 1.5; margin: 0;">Bullet text goes here</p>
    </td>
  </tr>
</table>
```

---

## Footer Bar

160px tall. Three zones in a flex row: identity (left), nav dots (center), chevron (right).

### Dark footer

```html
<div style="position: absolute; bottom: 0; left: 0; right: 0; height: 160px; padding: 0 100px; display: flex; flex-direction: row; align-items: center; font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; border-top: 1px solid #1e293b;">
  <!-- Left: identity -->
  <div style="display: flex; flex-direction: row; align-items: center; gap: 20px; white-space: nowrap; flex-shrink: 0;">
    <img src="data:image/png;base64,HEADSHOT_B64" width="64" height="64" style="width: 64px; height: 64px; border-radius: 50%; object-fit: cover; display: block; flex-shrink: 0;" />
    <div style="flex-shrink: 0;">
      <p style="font-size: 22px; font-weight: 600; color: #f1f5f9; margin: 0; line-height: 1.3;">Andreas Lezgus</p>
      <p style="font-size: 17px; color: #94a3b8; margin: 0; line-height: 1.3;">@andreaslezgus</p>
    </div>
  </div>
  <!-- Center: nav dots -->
  <div style="flex: 1; display: flex; justify-content: center;">
    <table cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
      <tr>
        <td style="padding: 0 6px;"><div style="width: 14px; height: 14px; border-radius: 50%; background: #0d9488;"></div></td>
        <td style="padding: 0 6px;"><div style="width: 14px; height: 14px; border-radius: 50%; border: 2px solid #475569;"></div></td>
        <!-- one td per slide -->
      </tr>
    </table>
  </div>
  <!-- Right: nav chevron (omit on last slide) -->
  <div style="flex-shrink: 0;">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="display: block;">
      <path d="M9 6L15 12L9 18" stroke="#0d9488" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </div>
</div>
```

### Light footer

Same structure, different colors:

```html
<div style="position: absolute; bottom: 0; left: 0; right: 0; height: 160px; padding: 0 100px; display: flex; flex-direction: row; align-items: center; font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; border-top: 1px solid #e2e8f0;">
  <div style="display: flex; flex-direction: row; align-items: center; gap: 20px; white-space: nowrap; flex-shrink: 0;">
    <img src="data:image/png;base64,HEADSHOT_B64" width="64" height="64" style="width: 64px; height: 64px; border-radius: 50%; object-fit: cover; display: block; flex-shrink: 0;" />
    <div style="flex-shrink: 0;">
      <p style="font-size: 22px; font-weight: 600; color: #0f172a; margin: 0; line-height: 1.3;">Andreas Lezgus</p>
      <p style="font-size: 17px; color: #64748b; margin: 0; line-height: 1.3;">@andreaslezgus</p>
    </div>
  </div>
  <div style="flex: 1; display: flex; justify-content: center;">
    <table cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
      <tr>
        <td style="padding: 0 6px;"><div style="width: 14px; height: 14px; border-radius: 50%; background: #0d9488;"></div></td>
        <td style="padding: 0 6px;"><div style="width: 14px; height: 14px; border-radius: 50%; border: 2px solid #cbd5e1;"></div></td>
      </tr>
    </table>
  </div>
  <div style="flex-shrink: 0;">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="display: block;">
      <path d="M9 6L15 12L9 18" stroke="#0d9488" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </div>
</div>
```

---

## DARK THEME — Full Slide Examples

### Hook slide

```html
<div class="slide" style="width:1080px; height:1350px; background:#0f172a; color:#f1f5f9; font-family:'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; position:relative; overflow:hidden;">
  <!-- Background watermark -->
  <img src="data:image/png;base64,..." style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); width:1000px; height:1000px; opacity:0.08; object-fit:contain; pointer-events:none;" />
  <!-- Page number -->
  <div style="position:absolute; top:48px; left:100px; font-size:42px; font-weight:800; color:#0d9488;">01</div>
  <!-- Content -->
  <div style="position:absolute; top:130px; left:100px; right:100px; bottom:180px; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center;">
    <p style="font-size:22px; font-weight:700; letter-spacing:3px; text-transform:uppercase; color:#0d9488; margin:0 0 36px 0;">CATEGORY</p>
    <h1 style="font-size:64px; font-weight:800; line-height:1.15; margin:0 0 32px 0;">Bold Hook Title<br>Goes <span style="color:#14b8a6">Right Here</span></h1>
    <p style="font-size:28px; color:#94a3b8; line-height:1.5; max-width:750px; margin:0;">Subtitle that sets up the carousel's promise</p>
  </div>
  <!-- Footer (see footer section above) -->
</div>
```

### Content slide

```html
<div class="slide" style="width:1080px; height:1350px; background:#111b30; color:#f1f5f9; font-family:'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; position:relative; overflow:hidden;">
  <img src="data:image/png;base64,..." style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); width:1000px; height:1000px; opacity:0.08; object-fit:contain; pointer-events:none;" />
  <div style="position:absolute; top:48px; left:100px; font-size:42px; font-weight:800; color:#0d9488;">03</div>
  <div style="position:absolute; top:130px; left:100px; right:100px; bottom:180px; display:flex; flex-direction:column; justify-content:center;">
    <p style="font-size:22px; font-weight:700; letter-spacing:2px; text-transform:uppercase; color:#0d9488; margin:0 0 28px 0;">SECTION LABEL</p>
    <h2 style="font-size:52px; font-weight:700; line-height:1.2; margin:0 0 48px 0;">Headline Goes<br>On <span style="color:#14b8a6">Two Lines</span></h2>
    <!-- bullets using table layout (see bullet section above) -->
  </div>
  <!-- Footer -->
</div>
```

### CTA slide (final)

```html
<div class="slide" style="width:1080px; height:1350px; background:#0f172a; color:#f1f5f9; font-family:'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; position:relative; overflow:hidden;">
  <img src="data:image/png;base64,..." style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); width:1000px; height:1000px; opacity:0.08; object-fit:contain; pointer-events:none;" />
  <div style="position:absolute; top:48px; left:100px; font-size:42px; font-weight:800; color:#0d9488;">10</div>
  <div style="position:absolute; top:130px; left:100px; right:100px; bottom:180px; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center;">
    <h2 style="font-size:56px; font-weight:800; line-height:1.2; margin:0 0 32px 0;">Closing Headline<br>With <span style="color:#14b8a6">Takeaway</span></h2>
    <p style="font-size:28px; color:#94a3b8; line-height:1.5; max-width:700px; margin:0 0 48px 0;">Reinforcing sentence here</p>
    <div style="background:#0d9488; color:#f1f5f9; padding:24px 52px; border-radius:14px;">
      <p style="font-size:28px; font-weight:700; margin:0;">Call to Action Text →</p>
    </div>
  </div>
  <!-- Footer (no chevron on last slide) -->
</div>
```

---

## LIGHT THEME — Differences Only

The light theme uses the same layout structure. Only colors change:

| Element | Dark value | Light value |
|---|---|---|
| Slide background (odd) | `#0f172a` | `#ffffff` |
| Slide background (even) | `#111b30` | `#f8fafc` |
| Headline color | `#f1f5f9` | `#0f172a` |
| Body/bullet text | `#e2e8f0` | `#334155` |
| Muted text | `#94a3b8` | `#64748b` |
| Accent highlight | `#14b8a6` | `#0d9488` |
| Inactive dot border | `#475569` | `#cbd5e1` |
| Footer border | `#1e293b` | `#e2e8f0` |
| Footer name color | `#f1f5f9` | `#0f172a` |
| Footer handle color | `#94a3b8` | `#64748b` |
| CTA button text | `#f1f5f9` | `#ffffff` |
