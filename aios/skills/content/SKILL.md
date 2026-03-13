---
name: content
description: >
  Vollständige Content-Pipeline – Gartner PDF analysieren und alle Formate erstellen
  (Blog DE × 3, LinkedIn × 3, Substack EN, 15 Notes, Hero Images, DEVONthink).
  Automatisch aktivieren wenn ein Gartner-PDF verarbeitet werden soll oder /content
  aufgerufen wird.
---

Führe die vollständige Content-Pipeline für das bereitgestellte Gartner PDF aus.
Arbeite jeden Schritt sequenziell ab. Stoppe bei Quality-Gate-Fehler und warte auf Freigabe.

Lese zunächst folgende Skills für Stil und Qualitätsanforderungen:
- `skills/writing-style/SKILL.md`
- `skills/content/references/quality-gates.md`
- `skills/content/references/content-core-template.md`

---

## WICHTIG – MCP-Einschränkungen
Lies vor der Ausführung `config/mcp-constraints.md` für bekannte API-Einschränkungen.

## WICHTIG – Checkpoint & Fortsetzen
Diese Pipeline verwendet Checkpoints (siehe `config/error-handling.md → Checkpoint-Konvention`).

**Bei Sitzungsbeginn:** Prüfe ob `output/data/checkpoint-matthias-[HEUTE]-*.md` existiert.
- Wenn ja: Inhalt dem User zeigen und fragen: „Pipeline fortsetzen ab [letztem offenen Schritt] oder neu starten?"
- Wenn nein: normal beginnen.

**Checkpoint-Datei:** `output/data/checkpoint-matthias-[DATUM]-[kurzthema].md`
Wird nach Schritt 0 angelegt und nach jedem abgeschlossenen Schritt aktualisiert.

## SCHRITT 0 – PDF automatisch aus DEVONthink laden
Prüfe den DEVONthink-Eingangsordner für neue Gartner-PDFs:

1. Rufe `devonthink_list_group_content` auf mit uuid aus `config/devonthink-groups.yaml → gartner.eingang`
2. Filtere die Ergebnisse: nur `recordType: "PDF document"`
3. **Wenn mindestens ein PDF vorhanden:**
4. Verwende das erste PDF aus der Liste
5. Lade den Inhalt mit `devonthink_get_record_content` (uuid des PDFs)
6. Merke dir die UUID des PDFs für Schritt 8
7. Melde dem User: „PDF gefunden: [Name]. Starte Analyse."
8. **CHECKPOINT:** Erstelle `output/data/checkpoint-matthias-[DATUM]-[kurzthema].md` mit allen Schritten als `[ ]`. Hake Schritt 0 ab.
9. Weiter mit Schritt 1

**Wenn der Ordner leer ist:**
Melde dem User: „Kein neues PDF im Eingangsordner gefunden." Frage ob manuell ein PDF bereitgestellt wird oder die Sitzung beendet werden soll.

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
   - Welche Annahmen werden getroffen?
   - Was wird nicht erwähnt?
   - Praktikabilität im deutschen Behördenumfeld?

Fülle das Content Core Template aus (`skills/content/references/content-core-template.md`).
Zeige den ausgefüllten Core dem User **vor** dem Weiterschreiben.
Warte auf explizite Freigabe: „ok", „weiter", „bestätigt" oder ähnlich.

## Nach SCHRITT 1
Speichere den ausgefüllten Content Core in:
output/data/content-core-[DATUM]-[KURZTHEMA].md
**CHECKPOINT:** Schritt 1 abhaken. Content-Core-Dateipfad im Checkpoint notieren.

---

## SCHRITT 2 – Quality Gate 0 prüfen

Prüfe alle 5 Punkte aus Gate 0 Schnell-Check (`skills/content/references/quality-gates.md`).

Bei einem „nein": Stoppen. Erklären welcher Punkt nicht erfüllt ist. Korrektur vorschlagen.
Bei allen „ja": **CHECKPOINT:** Schritt 2 abhaken. Weiter mit Schritt 3.

---

## SCHRITT 3 – Blog DE: Drei Varianten erstellen

Erstelle alle drei Varianten sequenziell.
Nach jeder Variante: Quality Gate 1 Schnell-Check durchführen.
Alle drei müssen das Gate bestehen bevor Schritt 4 beginnt.

### SCHRITT 3a – Blog DE: KI-Führung

Fokus: KI-Kompetenz für Führungskräfte – Entscheidungsfähigkeit ohne Expertenwissen
Ghost-Tag: KI-Führung

Speichern in Ulysses mit `ulysses_new_sheet`:
- group: siehe `config/ulysses-groups.yaml → blog_de.ki_fuehrung`
- Titel: `[SEO-Titel] – KI-Führung – [DATUM]`

### SCHRITT 3b – Blog DE: Quick Checks

Fokus: Checklisten und Prüfpunkte – sofort anwendbar, kompakt, praxisnah
Ghost-Tag: Quick Checks

Empfehlungen in konkrete Ja/Nein-Prüfpunkte übersetzen.
Jeder Punkt muss ohne technisches Vorwissen anwendbar sein.

Speichern in Ulysses mit `ulysses_new_sheet`:
- group: siehe `config/ulysses-groups.yaml → blog_de.quick_checks`
- Titel: `Quick Check: [Thema] – [DATUM]`

### SCHRITT 3c – Blog DE: Kritisches Denken

Fokus: Hype von Substanz unterscheiden – methodische Technologiebewertung
Ghost-Tag: Kritisches Denken

Artikel als Gesprächspartner nutzen, nicht als Autorität.
Explizit benennen: Was sieht der Artikel nicht? Welche Annahmen fehlen?

- Speichern in Ulysses mit `ulysses_new_sheet`:
- group: siehe `config/ulysses-groups.yaml → blog_de.kritisches_denken`
- Titel: `[Thema]: Warum [Annahme] die falsche Frage ist – [DATUM]`

**CHECKPOINT:** Schritte 3a/3b/3c abhaken. Ulysses-Sheet-IDs im Checkpoint notieren.
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
- group: siehe `config/ulysses-groups.yaml → linkedin.posts`
- Titel: `LinkedIn KI-Führung – [DATUM]`

### SCHRITT 4b – LinkedIn: Quick Checks

Bezug: Blog-Artikel aus Schritt 3b
Zielgruppe: Projektverantwortliche in Entscheidungssituationen

Speichern in Ulysses mit `ulysses_new_sheet`:
- group: siehe `config/ulysses-groups.yaml → linkedin.posts`
- Titel: `LinkedIn Quick Check – [DATUM]`

### SCHRITT 4c – LinkedIn: Kritisches Denken

Bezug: Blog-Artikel aus Schritt 3c
Zielgruppe: Erfahrene Führungskräfte mit Skepsis-Kompetenz

Speichern in Ulysses mit `ulysses_new_sheet`:
- group: siehe `config/ulysses-groups.yaml → linkedin.posts`
- Titel: `LinkedIn Kritisches Denken – [DATUM]`

Nach Erstellung aller drei: Quality Gate 3 Schnell-Check durchführen.
**CHECKPOINT:** Schritt 4 abhaken. Ulysses-Sheet-IDs im Checkpoint notieren.
Fortschrittsbericht ausgeben. Weiter mit Schritt 5.

---

## SCHRITT 5 – Substack Artikel EN erstellen

Basis: Content Core aus Schritt 1 – KEINE Übersetzung des Blog DE.
Neu schreiben für internationales Publikum.
Schreibstil: `skills/writing-style/SKILL.md` → Abschnitt EN

Nach Erstellung: Quality Gate 4 Schnell-Check durchführen.

Speichern in Ulysses mit `ulysses_new_sheet`:
- group: siehe `config/ulysses-groups.yaml → substack_en.artikel`
- Titel: `[English Title] – [DATUM]`

**CHECKPOINT:** Schritt 5 abhaken. Ulysses-Sheet-ID im Checkpoint notieren.
Fortschrittsbericht ausgeben. Weiter mit Schritt 6.

---

## SCHRITT 6 – 15 Substack Notes EN erstellen (3 Batches)

> **Kontextschonung:** 15 Notes à 150–300 Wörter = 2.250–4.500 Wörter.
> Um Context-Window-Overflow zu vermeiden, werden die Notes in 3 Batches à 5 erstellt.

Jede Note:
- Greift einen anderen Aspekt des Substack-Artikels auf
- Ist eigenständig lesbar (kein „wie oben erwähnt")
- 150–300 Wörter
- Variierender Einstieg (keine identischen Opener)
- Link-Platzhalter: `[LINK TO SUBSTACK ARTICLE – add before publishing]`

Verteilung (15 Notes = 5 Kategorien × 3 Notes):
- 3× These / Kernaussage aus verschiedenen Winkeln
- 3× Praxis-Beobachtung / Erfahrung
- 3× Frage / Zum Nachdenken einladen
- 3× Kritik / Gegenperspektive
- 3× Konkreter Tipp / Handlungsempfehlung

### Batch-Ablauf

**Batch A (Notes 01–05):** Je 1 Note pro Kategorie erstellen → sofort in Ulysses speichern.
**CHECKPOINT:** Batch A im Checkpoint notieren (5 Notes gespeichert).

**Batch B (Notes 06–10):** Je 1 Note pro Kategorie erstellen → sofort in Ulysses speichern.
**CHECKPOINT:** Batch B im Checkpoint notieren (10 Notes gespeichert).

**Batch C (Notes 11–15):** Je 1 Note pro Kategorie erstellen → sofort in Ulysses speichern.
**CHECKPOINT:** Schritt 6 abhaken. Alle 15 Notes im Checkpoint notieren.

### Ulysses-Speicherung (pro Note)

`ulysses_new_sheet`:
- group: siehe `config/ulysses-groups.yaml → substack_en.notes`
- Titel: `[NR] – Substack Note – [THEMA] – [DATUM]` (NR = 01–15)

> **Bei Sitzungsabbruch:** Checkpoint enthält die Batch-Nummer. Beim Fortsetzen nur fehlende Batches erstellen. Bereits gespeicherte Notes in Ulysses nicht duplizieren.

Fortschrittsbericht ausgeben. Weiter mit Schritt 7.

---

## SCHRITT 7 – Hero Images erstellen

Erstelle drei Hero Images (1200×628px PNG). Texte aus den fertigen Blog-Titeln ableiten.

Script: `skills/hero-images/scripts/hero-image-generator.py`
Vollständige CLI-Referenz und Parameter: siehe `skills/hero-images/SKILL.md`

| Variante | Template | Output |
|---|---|---|
| 7a KI-Führung | `ki-fuehrung-standard` | `~/Desktop/Hero-Images/hero-ki-fuehrung-[DATUM].png` |
| 7b Quick Checks | `quick-checks-standard` | `~/Desktop/Hero-Images/hero-quick-checks-[DATUM].png` |
| 7c Kritisches Denken | `kritisches-denken-standard` | `~/Desktop/Hero-Images/hero-kritisches-denken-[DATUM].png` |

Pflichtparameter: `--template`, `--title` (max 25–30 Z.), `--subtitle` (max 20–45 Z.), `--subline` (max 65–70 Z.), `--output`. Quick Checks zusätzlich: `--count`.

**CHECKPOINT:** Schritt 7 abhaken. Erstellte Image-Dateinamen notieren.
Fortschrittsbericht ausgeben. Weiter mit Schritt 8.

---

## SCHRITT 8 – DEVONthink: PDF verschieben

Verschiebe das verarbeitete PDF in die Gartner-Hauptgruppe mit `devonthink_move_record`:
- uuid: [UUID des PDFs aus Schritt 1]
- destinationGroupUuid: siehe `config/devonthink-groups.yaml → gartner.archiv`

Setze anschließend Tags mit `devonthink_add_tags`:
- tags: `["Content-Pipeline-Fertig", "Blog-Erstellt", "LinkedIn-Erstellt", "Substack-Erstellt"]`

**CHECKPOINT:** Schritt 8 abhaken.

---

## SCHRITT 9 – Abschlussbericht

**CHECKPOINT:** Alle Schritte abhaken. Pipeline als abgeschlossen markieren.

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
  📌 15 Substack Notes (3 Batches) → 15 Sheets in Ulysses

HERO IMAGES  →  ~/Desktop/Hero-Images/
  🖼  hero-ki-fuehrung-[DATUM].png
  🖼  hero-quick-checks-[DATUM].png
  🖼  hero-kritisches-denken-[DATUM].png

DEVONTHINK
  🗂  PDF → 50.01-Gartner (verschoben + getaggt)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Noch manuell nötig:
  [ ] Blog-URLs in die 3 LinkedIn-Posts eintragen
  [ ] Substack-Link in den 15 Notes ergänzen
  [ ] Hero Images in Ghost hochladen (3×)
  [ ] Veröffentlichung:
        Di → LinkedIn KI-Führung + Blog
        Mi → LinkedIn Quick Check + Blog
        Do → LinkedIn Kritisches Denken + Blog
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```