---
name: operations
description: >
  Tägliche Operationsübersicht – NotePlan-Tasks, Kalender, Pipeline-Status
  und Tagesplan mit Delegation.
---

Führe die tägliche Operationsübersicht aus.
Arbeite jeden Schritt sequenziell ab.

---

## Checkpoint
Gudrun verwendet keinen separaten Checkpoint (kurze Pipeline, primär Lesezugriffe).
Stattdessen: Ergebnisse werden direkt in `output/daily-data.md` geschrieben (siehe Agent-Datei, Letzter Schritt).

---

## SCHRITT 1 – Tagesübersicht erstellen
1. NotePlan: `read_today_note` aufrufen → offene Tasks auflisten
2. Kalender: Termine des Tages zusammenfassen
3. Content-Status: Ulysses-Gruppen prüfen (letzte 7 Tage)

Ergebnisse zwischenspeichern: die gesammelten Daten fließen in `output/daily-data.md` (Letzter Schritt).

## SCHRITT 2 – Pipeline-Status
1. DEVONthink Eingangsordner prüfen → neue PDFs?
2. Letzte Content-Pipeline: wann zuletzt gelaufen? (Prüfe `output/data/checkpoint-matthias-*.md`)
3. Newsletter-Status: KW prüfen, Freitag Deadline? (Prüfe `output/data/checkpoint-claudia-*.md`)

## SCHRITT 3 – Tagesplan vorschlagen
Basierend auf Status eine priorisierte Aufgabenliste erstellen.
Delegation an Matthias, Claudia oder Sebastian vorschlagen.

## SCHRITT 4 – Abschlussbericht

Zusammenfassung der Tagesübersicht ausgeben.
Danach: Sitzungsprotokoll + Daily Data (wie in `agents/gudrun.md` → Letzter Schritt definiert).

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 TAGESÜBERSICHT – [DATUM]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TASKS (NotePlan):  [Anzahl offen] offen / [Anzahl erledigt] erledigt
TERMINE:           [Anzahl] heute
PIPELINE-STATUS:
  Content (Matthias):  [Letzter Lauf / Neue PDFs?]
  Newsletter (Claudia): [KW-Status / Deadline?]

TAGESPLAN:
  1. [Priorität 1] → [Agent]
  2. [Priorität 2] → [Agent]
  3. [Priorität 3] → [Agent]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```