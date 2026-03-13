# Hero-Image Templates – Import-Anleitung

Jedes Template ist eine einfache JSON-Datei in diesem Ordner.
Neue Templates können ohne technisches Wissen erstellt werden.

---

## Schnellstart: Neues Template erstellen

1. Eine bestehende JSON-Datei kopieren (z.B. `ki-fuehrung-standard.json`)
2. Umbenennen: `ki-fuehrung-dunkel.json` oder `mein-thema-blau.json`
3. Werte anpassen (Farben, Schriftgrößen, Layout – alles in der Datei kommentiert)
4. Im Content-Command den Template-Namen eintragen

---

## Farbangaben

Alle Farben als Hex-Code: `"#RRGGBB"`

Beispiele:
```
"#FFFFFF"  = Weiß
"#000000"  = Schwarz
"#08143A"  = Dunkel-Navy
"#F5F8FA"  = Hell-Grau
"#FFB932"  = Amber/Gold
"#00968C"  = Teal
"#DC4632"  = Rot
```

Hex-Farbwähler: https://www.google.com/search?q=color+picker

---

## Hintergründe

### Einfarbig (solid)
```json
"background": {
  "type": "solid",
  "color": "#08143A"
}
```

### Verlauf von oben nach unten (gradient)
```json
"background": {
  "type": "gradient",
  "color_top": "#08143A",
  "color_bottom": "#162347"
}
```

---

## Schriften (font)

Es stehen zwei Schriftarten zur Verfügung:

| Wert            | Stil                        | Verwendung          |
|-----------------|-----------------------------|---------------------|
| `serif-bold`    | DejaVu Serif Bold           | Überschriften       |
| `sans-regular`  | FreeSans Regular            | Fließtext, Tags     |
| `sans-bold`     | FreeSans Bold               | Tags, Labels        |

```json
"font": {
  "headline":      "serif-bold",
  "body":          "sans-regular",
  "headline_size": 54,
  "sub_size":      44,
  "tag_size":      14,
  "subline_size":  18
}
```

**Schriftgrößen-Orientierung:**
- Große Überschrift: 48–60
- Mittlere Überschrift: 36–46
- Subline / Ergänzung: 16–22
- Tag / Label: 12–16

---

## Dekoration (accent.decoration)

| Wert                | Beschreibung                        |
|---------------------|-------------------------------------|
| `circle-top-right`  | Großer Kreis oben rechts (navy)     |
| `triangle-top-right`| Rotes Dreieck-Keil oben rechts      |
| `checklist-right`   | Stilisierte Checkboxen rechts       |
| `none`              | Keine Dekoration                    |

```json
"accent": {
  "color": "#FFB932",
  "bar_left": true,
  "decoration": "circle-top-right",
  "decoration_opacity": 0.12
}
```

`decoration_opacity`: 0.0 (unsichtbar) bis 1.0 (voll sichtbar). Empfehlung: 0.08–0.20

---

## Layout-Optionen

```json
"layout": {
  "text_x": 96,              // Linksbündige Textposition (Pixel)
  "headline_y": 158,         // Y-Position der ersten Überschrift
  "show_divider": true,      // Trennlinie unter der Überschrift
  "divider_color": "#FFB932",
  "show_meta_bar": true,     // Dunkle Leiste am unteren Rand
  "meta_bar_opacity": 0.55   // 0.0–1.0
}
```

**Spezielle Layout-Optionen:**

`"show_count_badge": true` → Runde Badge mit Zahl (nur Quick Checks)
`"badge_bg": "#00968C"` → Farbe der Badge

`"show_warning_icon": true` → Ausrufezeichen rechts (nur Kritisches Denken)

---

## Texte

```json
"tag_label":   "KI-FÜHRUNG",         // Oben links, klein
"site_label":  "DIE ZWEITE MEINUNG", // Darunter, dunkler
"footer_text": "lezgus.mymagic.page · AI Leadership with Trust and Security in Mind"
```

---

## Vollständiges Minimal-Beispiel

```json
{
  "_name": "Mein Custom Template",
  "_variant": "ki-fuehrung",

  "background": {
    "type": "solid",
    "color": "#1A1A2E"
  },

  "accent": {
    "color": "#E94560",
    "bar_left": true,
    "decoration": "circle-top-right",
    "decoration_opacity": 0.10
  },

  "text": {
    "headline":     "#FFFFFF",
    "headline_sub": "#F0C0A0",
    "subline":      "#A0A8B8",
    "tag":          "#E94560",
    "meta":         "#707888"
  },

  "font": {
    "headline":      "serif-bold",
    "body":          "sans-regular",
    "headline_size": 52,
    "sub_size":      40,
    "tag_size":      14,
    "subline_size":  18
  },

  "layout": {
    "text_x":        96,
    "headline_y":    158,
    "show_divider":  true,
    "divider_color": "#E94560",
    "show_meta_bar": true,
    "meta_bar_opacity": 0.55
  },

  "tag_label":  "KI-FÜHRUNG",
  "site_label": "DIE ZWEITE MEINUNG",
  "footer_text": "lezgus.mymagic.page  ·  AI Leadership with Trust and Security in Mind"
}
```

---

## Template im Pipeline-Command aktivieren

In `skills/content/SKILL.md`, Schritt 7, die Template-Namen anpassen:

```
hero_template_ki_fuehrung:       ki-fuehrung-standard
hero_template_quick_checks:      quick-checks-standard
hero_template_kritisches_denken: kritisches-denken-standard
```

Einfach den Dateinamen ohne `.json` eintragen.
