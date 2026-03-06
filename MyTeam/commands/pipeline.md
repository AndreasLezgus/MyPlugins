---
description: Vollständige Content-Pipeline – Gartner PDF analysieren und alle Formate erstellen (Blog DE × 3, LinkedIn × 3, Substack EN, 30 Notes, Hero Images, DEVONthink)
---

Führe die vollständige Content-Pipeline für das bereitgestellte Gartner PDF aus.
Arbeite jeden Schritt sequenziell ab. Stoppe bei Quality-Gate-Fehler und warte auf Freigabe.

Lese zunächst folgende Skills für Stil und Qualitätsanforderungen:
- `skills/writing-style/SKILL.md`
- `skills/gartner-pipeline/references/quality-gates.md`
- `skills/gartner-pipeline/references/content-core-template.md`

---
---

## WICHTIG – Ulysses Titel-Handling

Beim Speichern in Ulysses mit `ulysses_new_sheet` wird der Titel automatisch
aus der **ersten Markdown-Zeile** (`# Titel`) übernommen.
**Rufe NIEMALS `ulysses_set_sheet_title` auf** – der MCP-Server leitet den
erforderlichen `type`-Parameter nicht an die Ulysses-API weiter, was zu einem
Fehler führt. Stelle stattdessen sicher, dass die erste Zeile des Contents
immer den gewünschten Titel als H1-Heading enthält (`# Mein Titel`).

---

## SCHRITT 0 – PDF automatisch aus DEVONthink laden
Prüfe den DEVONthink-Eingangsordner für neue Gartner-PDFs:

1. Rufe `devonthink_list_group_content` auf mit uuid: `8AB280B1-55E7-4B02-ABFE-3B761CC58B22`
2. Filtere die Ergebnisse: nur `recordType: "PDF document"`
3. **Wenn mindestens ein PDF vorhanden:**
   4. Verwende das erste PDF aus der Liste
   5. Lade den Inhalt mit `devonthink_get_record_content` (uuid des PDFs)
   6. Merke dir die UUID des PDFs für Schritt 8
   7. Melde dem User: „PDF gefunden: [Name]. Starte Analyse."
   8. Weiter mit Schritt 1
4. **Wenn der Ordner leer ist:**
   10. Frage den User: „Kein neues Gartner-PDF im Eingangsordner gefunden. Bitte lade ein PDF hoch oder nenne mir den Titel/die UUID des Dokuments in DEVONthink."
   11. Warte auf Antwort, dann weiter mit Schritt 1

---

## SCHRITT 1 – PDF analysieren & Content Core erstellen

Lies das PDF vollständig. Extrahiere:

1. **Bibliografische Daten**
   - Vollständiger Titel
   - Gartner Research ID
   - Publikationsjahr
   - Autoren (falls angegeben)
   - DEVONthink UUID des Dokuments (für Schritt 8)

2. **Kernaussagen** (3–5 Hauptthesen)

3. **Statistiken & Prognosen** (mit Jahreszahl und Kontext)

4. **Empfehlungen** (Quick Wins / Mittelfristig / Langfristig)

5. **Kritische Prüfung**
   - Welche Annahmen trifft Gartner?
   - Was wird nicht erwähnt?
   - Praktikabilität im deutschen Behördenumfeld?

Fülle das Content Core Template aus (`skills/gartner-pipeline/references/content-core-template.md`).
Zeige den ausgefüllten Core dem User **vor** dem Weiterschreiben.
Warte auf explizite Freigabe: „ok", „weiter", „bestätigt" oder ähnlich.

---

## SCHRITT 2 – Quality Gate 0 prüfen

Prüfe alle 5 Punkte aus Gate 0 Schnell-Check (`skills/gartner-pipeline/references/quality-gates.md`).

Bei einem „nein": Stoppen. Erklären welcher Punkt nicht erfüllt ist. Korrektur vorschlagen.
Bei allen „ja": Weiter mit Schritt 3.

---

## SCHRITT 3 – Blog DE: Drei Varianten erstellen

Erstelle alle drei Varianten sequenziell.
Nach jeder Variante: Quality Gate 1 Schnell-Check durchführen.
Alle drei müssen das Gate bestehen bevor Schritt 4 beginnt.

### SCHRITT 3a – Blog DE: KI-Führung

Fokus: KI-Kompetenz für Führungskräfte – Entscheidungsfähigkeit ohne Expertenwissen
Ghost-Tag: KI-Führung

Speichern in Ulysses mit `ulysses_new_sheet`:
- group: `aEabxcQsV6hz0jZ7F7jiaA`
- Titel: `[SEO-Titel] – KI-Führung – [DATUM]`

### SCHRITT 3b – Blog DE: Quick Checks

Fokus: Checklisten und Prüfpunkte – sofort anwendbar, kompakt, praxisnah
Ghost-Tag: Quick Checks

Empfehlungen in konkrete Ja/Nein-Prüfpunkte übersetzen.
Jeder Punkt muss ohne technisches Vorwissen anwendbar sein.

Speichern in Ulysses mit `ulysses_new_sheet`:
- group: `Ji9rIHGlNVFhxSdZXacQEg`
- Titel: `Quick Check: [Thema] – [DATUM]`

### SCHRITT 3c – Blog DE: Kritisches Denken

Fokus: Hype von Substanz unterscheiden – methodische Technologiebewertung
Ghost-Tag: Kritisches Denken

Artikel als Gesprächspartner nutzen, nicht als Autorität.
Explizit benennen: Was sieht der Artikel nicht? Welche Annahmen fehlen?

Speichern in Ulysses mit `ulysses_new_sheet`:
- group: `vuROqgmapR70lV49mty2lA`
- Titel: `[Thema]: Warum [Annahme] die falsche Frage ist – [DATUM]`

Fortschrittsbericht ausgeben (alle drei Varianten zusammen). Weiter mit Schritt 4.

---

## SCHRITT 4 – LinkedIn: Drei Varianten erstellen

Eine LinkedIn-Variante pro Blog-Variante.
Jede Variante referenziert ihren zugehörigen Blog-Artikel.
Alle Links als Platzhalter – werden vor Veröffentlichung ergänzt.

### SCHRITT 4a – LinkedIn: KI-Führung

Bezug: Blog-Artikel aus Schritt 3a
Zielgruppe: C-Level und Senior Führungskräfte

Speichern in Ulysses mit `ulysses_new_sheet`:
- group: `qrJnA9hWVujo-yB_HNAdPQ`
- Titel: `LinkedIn KI-Führung – [DATUM]`

### SCHRITT 4b – LinkedIn: Quick Checks

Bezug: Blog-Artikel aus Schritt 3b
Zielgruppe: Projektverantwortliche in Entscheidungssituationen

Speichern in Ulysses mit `ulysses_new_sheet`:
- group: `qrJnA9hWVujo-yB_HNAdPQ`
- Titel: `LinkedIn Quick Check – [DATUM]`

### SCHRITT 4c – LinkedIn: Kritisches Denken

Bezug: Blog-Artikel aus Schritt 3c
Zielgruppe: Erfahrene Führungskräfte mit Skepsis-Kompetenz

Speichern in Ulysses mit `ulysses_new_sheet`:
- group: `qrJnA9hWVujo-yB_HNAdPQ`
- Titel: `LinkedIn Kritisches Denken – [DATUM]`

Nach Erstellung aller drei: Quality Gate 3 Schnell-Check durchführen.
Fortschrittsbericht ausgeben. Weiter mit Schritt 5.

---

## SCHRITT 5 – Substack Artikel EN erstellen

Basis: Content Core aus Schritt 1 – KEINE Übersetzung des Blog DE.
Neu schreiben für internationales Publikum.
Schreibstil: `skills/writing-style/SKILL.md` → Abschnitt EN

Nach Erstellung: Quality Gate 4 Schnell-Check durchführen.

Speichern in Ulysses mit `ulysses_new_sheet`:
- group: `WfAl6Ob7Qe6c_2K2IhnBFQ`
- Titel: `[English Title] – [DATUM]`

Fortschrittsbericht ausgeben. Weiter mit Schritt 6.

---

## SCHRITT 6 – 30 Substack Notes EN erstellen

Erstelle 30 individuelle Notes aus dem Substack-Artikel.
Jede Note:
- Greift einen anderen Aspekt auf
- Ist eigenständig lesbar
- 150–300 Wörter
- Variierender Einstieg (keine identischen Opener)
- Link-Platzhalter: `[LINK TO SUBSTACK ARTICLE – add before publishing]`

Verteilung:
- 8x These / Kernaussage aus verschiedenen Winkeln
- 7x Praxis-Beobachtung / Erfahrung
- 6x Frage / Zum Nachdenken einladen
- 5x Kritik / Gegenperspektive
- 4x Konkreter Tipp / Handlungsempfehlung

Alle 30 Notes in einem Sheet speichern in Ulysses mit `ulysses_new_sheet`:
- group: `1zd3tHuyCwmGRJn1iHTMcA`
- Titel: `Substack Notes – [THEMA] – [DATUM]`

Fortschrittsbericht ausgeben. Weiter mit Schritt 7.

---

## SCHRITT 7 – Hero Images erstellen

Erstelle drei Hero Images (1200×628px PNG) direkt im Anschluss.
Nutze `skills/hero-images/hero-image-generator.py` mit den JSON-Templates aus `hero-images/`.

Leite die Texte aus den fertigen Blog-Titeln ab und rufe das Script auf:

**7a – KI-Führung** (Template: `ki-fuehrung-standard`):
```
python3 [PLUGIN-PFAD]/skills/hero-images/hero-image-generator.py \
  --templates-dir [PLUGIN-PFAD]/templates/hero-templates \
  --template      ki-fuehrung-standard \
  --title         "[Kurzform des Blog-Titels, max 25 Zeichen]" \
  --subtitle      "[Untertitel, max 45 Zeichen]" \
  --subline       "[Kernaussage, max 70 Zeichen]" \
  --output        ~/Desktop/Hero-Images/hero-ki-fuehrung-[DATUM].png
```

**7b – Quick Checks** (Template: `quick-checks-standard`):
```
python3 [PLUGIN-PFAD]/skills/hero-images/hero-image-generator.py \
  --templates-dir [PLUGIN-PFAD]/templates/hero-templates \
  --template      quick-checks-standard \
  --title         "[Frage aus dem Titel, max 30 Zeichen]" \
  --subtitle      "[Antwort / Thema, max 20 Zeichen]" \
  --subline       "[Einladender Satz, max 65 Zeichen]" \
  --count         [Anzahl der Prüfpunkte] \
  --output        ~/Desktop/Hero-Images/hero-quick-checks-[DATUM].png
```

**7c – Kritisches Denken** (Template: `kritisches-denken-standard`):
```
python3 [PLUGIN-PFAD]/skills/hero-images/hero-image-generator.py \
  --templates-dir [PLUGIN-PFAD]/templates/hero-templates \
  --template      kritisches-denken-standard \
  --title         "[Oberbegriff, max 25 Zeichen]" \
  --subtitle      "[Kritische These, max 45 Zeichen]" \
  --subline       "[Kontext-Satz, max 70 Zeichen]" \
  --output        ~/Desktop/Hero-Images/hero-kritisches-denken-[DATUM].png
```

Neue Templates anlegen: JSON-Datei in `hero-images/` kopieren und anpassen.
Anleitung: `hero-immages/IMPORT-GUIDE.md`

Fortschrittsbericht ausgeben. Weiter mit Schritt 8.

---

## SCHRITT 8 – DEVONthink: PDF verschieben

Verschiebe das verarbeitete PDF in die Gartner-Hauptgruppe mit `devonthink_move_record`:
- uuid: [UUID des PDFs aus Schritt 1]
- destinationGroupUuid: `18B2F3AE-9D1E-448F-ABA2-236549FD71BA`  (50.01-Gartner)

Setze anschließend Tags mit `devonthink_add_tags`:
- tags: `["Content-Pipeline-Fertig", "Blog-Erstellt", "LinkedIn-Erstellt", "Substack-Erstellt"]`

---

## SCHRITT 9 – Abschlussbericht

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ PIPELINE ABGESCHLOSSEN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Quelle:  [Gartner Titel] (ID: [xxx], [Jahr])
Datum:   [Datum/Uhrzeit]

CONTENT
  📝 Blog DE – KI-Führung        → [Titel] ([Wörter] Wörter)
  📝 Blog DE – Quick Checks      → [Titel] ([Wörter] Wörter)
  📝 Blog DE – Kritisches Denken → [Titel] ([Wörter] Wörter)
  💼 LinkedIn × 3                → KI-Führung | Quick Check | Kritisch
  🌍 Substack EN                 → [Titel] ([Wörter] Wörter)
  📌 30 Substack Notes           → 1 Sheet in Ulysses

HERO IMAGES  →  ~/Desktop/Hero-Images/
  🖼  hero-ki-fuehrung-[DATUM].png
  🖼  hero-quick-checks-[DATUM].png
  🖼  hero-kritisches-denken-[DATUM].png

DEVONTHINK
  🗂  PDF → 50.01-Gartner (verschoben + getaggt)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Noch manuell nötig:
  [ ] Blog-URLs in die 3 LinkedIn-Posts eintragen
  [ ] Substack-Link in den 30 Notes ergänzen
  [ ] Hero Images in Ghost hochladen (3×)
  [ ] Veröffentlichung:
        Di → LinkedIn KI-Führung + Blog
        Mi → LinkedIn Quick Check + Blog
        Do → LinkedIn Kritisches Denken + Blog
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
