---
description: Research-Dossier erstellen – Quellen sammeln, Konfidenzgrade vergeben, Gegenthesen liefern.
---

Führe die Research-Aufgabe aus.
Arbeite jeden Schritt sequenziell ab.

Lese zunächst folgende Referenz für Qualitätsanforderungen:
- `skills/content-drafts/references/quality-gates.md` (Gate 0 als Relevanzprüfung)

---

## Checkpoint & Fortsetzen
Diese Pipeline verwendet Checkpoints (siehe `config/error-handling.md → Checkpoint-Konvention`).

**Bei Sitzungsbeginn:** Prüfe ob `output/data/checkpoint-sebastian-[HEUTE]-*.md` existiert.
- Wenn ja: dem User zeigen und fragen ob fortgesetzt oder neu gestartet werden soll.
- Wenn nein: normal beginnen.

**Checkpoint-Datei:** `output/data/checkpoint-sebastian-[DATUM]-[kurzthema].md`

---

## SCHRITT 1 – Thema und Scope definieren
Frage den User nach: Thema, Zeitraum, Perspektive, gewünschte Quellen.

**CHECKPOINT:** Erstelle Checkpoint-Datei. Schritt 1 abhaken. Thema und Scope im Checkpoint notieren.

## SCHRITT 2 – Primärquellen durchsuchen
1. DEVONthink: relevante Gartner-Reports suchen
2. Web-Recherche: aktuelle Quellen (letzte 6 Monate)
3. Gegenthesen: bewusst nach Gegenpositionen suchen

**CHECKPOINT:** Schritt 2 abhaken. Gefundene Quellen-Anzahl und -Titel im Checkpoint notieren.

Zwischenergebnisse sichern: `output/data/research-quellen-[DATUM]-[kurzthema].md`
(Rohe Quellenliste als Absicherung gegen Sitzungsabbruch)

## SCHRITT 3 – Research-Dossier erstellen
Für jede Quelle:
- Kernaussage (1–2 Sätze)
- Konfidenzgrad (Hoch/Mittel/Niedrig + Begründung)
- Relevanz für "Die Zweite Meinung"

**CHECKPOINT:** Schritt 3 abhaken.

## SCHRITT 4 – Output & Quality Gate

Speichern als `output/data/research-dossier-[DATUM]-[kurzthema].md`.

**Quality Gate – Research-Dossier:**
- [ ] Mindestens 3 unabhängige Quellen (nicht nur Gartner)
- [ ] Jede Kernaussage hat einen Konfidenzgrad mit Begründung
- [ ] Mindestens 1 Gegenthese mit Quelle
- [ ] Alle Quellen aus den letzten 6 Monaten (oder Abweichung begründet)
- [ ] Relevant für IT-Führungskräfte oder C-Level (Gate 0)

**Ein „nein" → korrigieren, dann erneut prüfen.**

**CHECKPOINT:** Alle Schritte abhaken. Pipeline als abgeschlossen markieren.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ RESEARCH ABGESCHLOSSEN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Thema:    [Thema]
Quellen:  [Anzahl] Quellen ([Hoch/Mittel/Niedrig]-Verteilung)
Dossier:  output/data/research-dossier-[DATUM]-[kurzthema].md

Nächste Schritte:
  [ ] Dossier an Content-Pipeline übergeben (falls gewünscht)
  [ ] Gegenthesen in Blog-Artikel einarbeiten
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```