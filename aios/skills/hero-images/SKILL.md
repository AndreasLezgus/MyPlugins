---
name: hero-images
description: Erstellt Hero Images (1200×628px PNG) für Blog-Artikel von "Die Zweite Meinung". Aktivieren wenn Hero Images für Blog-Artikel generiert werden sollen oder nach Abschluss der Content-Pipeline (Schritt 7).
---

# Hero Image Generator

Erstellt professionelle Hero Images (1200×628px) für die drei Blog-Varianten von "Die Zweite Meinung".

## Script ausführen

```bash
python3 scripts/hero-image-generator.py \
  --templates-dir assets \
  --template      [TEMPLATE-NAME] \
  --title         "[Zeile 1, max 25 Zeichen]" \
  --subtitle      "[Zeile 2, max 45 Zeichen]" \
  --subline       "[Beschreibung, max 70 Zeichen]" \
  --output        ~/Desktop/Hero-Images/hero-[VARIANTE]-[DATUM].png
```

## Verfügbare Templates (assets/)

| Template-Datei | Variante | Design |
|----------------|----------|--------|
| `assets/ki-fuehrung-standard.json` | KI-Führung | Dunkel-Navy, Amber-Akzent |
| `assets/quick-checks-standard.json` | Quick Checks | Hell-Grau, Teal-Akzent |
| `assets/kritisches-denken-standard.json` | Kritisches Denken | Dunkel-Charcoal, Rot-Akzent |

Für Quick Checks zusätzlich `--count [Anzahl]` angeben.

## Eigene Templates erstellen

1. JSON-Datei aus `assets/` kopieren und umbenennen (z.B. `ki-fuehrung-blau.json`)
2. Felder anpassen (Farben, Schriften, Layout)
3. Vollständige Anleitung: `references/IMPORT-GUIDE.md`

## Ausgabe

Bilder landen in `~/Desktop/Hero-Images/` (Ordner wird automatisch erstellt).
Format: PNG, 1200×628px, für Ghost CMS optimiert.
