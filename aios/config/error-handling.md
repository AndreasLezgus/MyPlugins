# Fehlerbehandlung

> Zentrale Fehlerbehandlung für alle Agenten und Commands.
> Agenten-spezifische Szenarien: siehe `config/errors/[agent].md`

---

## Grundprinzipien

1. **Kein stiller Fehler.** Jeder Fehler wird im Sitzungsprotokoll dokumentiert.
2. **Fallback vor Abbruch.** Content wird immer gesichert: wenn nicht im Zielsystem, dann in `output/fallback/`.
3. **Fortfahren wenn möglich.** Ein Fehler in Schritt N blockiert nur abhängige Folgeschritte.
4. **User informieren.** Jeder Fehler erscheint im Abschlussbericht.

---

## Checkpoint-Konvention

Jede Pipeline führt eine Checkpoint-Datei: `output/data/checkpoint-[agent]-[YYYY-MM-DD]-[kurzthema].md`

**Format:** Markdown mit Meta-Block (Agent, Zeitstempel, Quelle, PDF-UUID) und Fortschritts-Checkliste aller Schritte.

**Regeln:**
1. Anlegen nach Schritt 0. Nach jedem Hauptschritt: Checkbox abhaken + IDs notieren.
2. Bei Sitzungsbeginn: prüfen ob Checkpoint existiert → User fragen ob fortsetzen oder neu.
3. Nach Abschluss: Checkpoint-Datei behalten (dient als Protokoll).

---

## Fallback-Konvention

Alle Fallback-Dateien: `output/fallback/[agent]-[YYYY-MM-DD]-[kurzthema]-[typ].md`

---

## Universelle Fehlerszenarien

| § | Szenario | Betrifft | Ablauf |
|---|----------|----------|--------|
| 1 | MCP-Server nicht erreichbar | Alle | 1× Retry → Fallback in `output/fallback/` → User benachrichtigen → im Abschlussbericht als „manuell nachzuholen" |
| 9 | Quality-Gate-Fehler | Matthias, Claudia | **Sofort stoppen.** User exakt mitteilen: welches Gate, welcher Prüfpunkt, Korrekturvorschlag. Auf explizite Freigabe warten. Nach Korrektur: Gate erneut prüfen. Nie stillschweigend überspringen. |
| 11 | Sitzungsprotokoll Schreibfehler | Alle | Falls `output/memory/` nicht beschreibbar → Protokoll als letzte Chat-Nachricht ausgeben. Protokoll enthält immer: alle Fehler + Fallback-Pfade + „manuell nachzuholen"-Punkte + Memory-Kandidaten. |

---

## Abschlussbericht – Fehlerdarstellung

Jeder Abschlussbericht enthält einen Fehlerblock wenn Fehler auftraten:

```
⚠️ FEHLER / MANUELLE NACHARBEIT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[1] [MCP/System]: [Beschreibung]
    Fallback: output/fallback/[dateiname].md
    Aktion: [Konkrete manuelle Aktion]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Wenn keine Fehler auftraten: Block weglassen.

---

*Letzte Aktualisierung: 2026-03-08 (Phase 3: komprimiert + aufgeteilt)*
*Agenten-spezifische Szenarien: `config/errors/matthias.md`, `claudia.md`, `sebastian.md`, `gudrun.md`*
