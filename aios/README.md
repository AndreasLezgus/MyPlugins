# AIOS – Andreas Intelligence Operating System

**Version 1.0.0** | Autor: Andreas Lezgus

Vollautomatische Agenten als Team-Mitglieder: 

1. Matthias: Analysiert z.B. Gartner Research aus Devonthink und erstellt Entwürfe mit meinem spezifischen Brand Guide für Blog, Substack, LinkedIN.

2. Claudia: Erstellt Entwürfe für Newsletter aus der wöchentlich erstellten Blog und Substack Artikel.

3. Sebastian: Erstellt ein Research für ausgewählte Themen aus Youtube, LinkedIN oder Substack.

4. Gudrun: Orchestriert die täglichen Aufgaben und steuert die einzelnen Team-Mitglieder.

---

## Installation

### Plugin installieren

```Download aios.zip und hochladen in das Claude Cowork Plugin Verzeichnis
```

Claude Code neu starten, damit das Plugin aktiv wird.

---

## Verfügbare Commands

| Command       | Beschreibung |
|---------------|--------------|
| `/content`   | Vollständige Content Pipeline starten (alle Schritte) |
| `/newsletter` | Newsletter DE + EN erstellen |
| `/research` | Research erstellen |
| `/operations` | Tagesaufgaben prüfen und starten |

---

## Scheduler – Agenten automatisch starten

Die AIOS-Agenten können über den Cowork Scheduler automatisch zu festgelegten Zeiten gestartet werden. Der Scheduler erstellt eine eigenständige Session, die den jeweiligen Agenten aufruft, ohne dass Du manuell eingreifen musst.

### Voraussetzungen

1. Cowork Desktop App läuft (der Mac muss an sein)
2. MCP-Server erreichbar (DEVONthink, NotePlan, Ulysses müssen geöffnet sein)
3. Plugin „aios" ist installiert und aktiv

### Einrichtung Schritt für Schritt

1. **Scheduled Task erstellen:** Sage in Cowork: *„Erstelle einen Scheduled Task für [Agent]"* oder nutze `/schedule`
2. **Prompt einfügen:** Kopiere den passenden Prompt aus der Tabelle unten
3. **Cron-Ausdruck setzen:** Der Scheduler verwendet lokale Zeitzone (kein UTC)
4. **Testen:** Starte den Task einmal manuell, um zu prüfen, ob alle MCP-Server erreichbar sind

### Cron-Kurzreferenz

| Ausdruck | Bedeutung |
|---|---|
| `0 8 * * 1-5` | Mo–Fr um 8:00 |
| `0 8 * * *` | Täglich um 8:00 |
| `0 9 * * 5` | Freitags um 9:00 |
| `0 7 * * 1` | Montags um 7:00 |

### Empfohlener Tagesablauf

| Zeit | Task-ID | Agent | Zweck |
|---|---|---|---|
| 08:00 Mo–Fr | `gudrun-daily` | Gudrun | Tagesübersicht, Pipeline-Status, Delegationen |
| 09:00 Fr | `claudia-weekly` | Claudia | Newsletter DE + EN aus der Wochenproduktion |
| 07:00 Mo | `matthias-inbox-check` | Matthias | DEVONthink-Eingang prüfen, neue PDFs melden |

Sebastian wird on-demand gestartet (Research braucht ein konkretes Thema).

---

### Scheduler-Prompts

#### `gudrun-daily` – Tägliche Operationsübersicht

**Cron:** `0 8 * * 1-5` (Mo–Fr, 8:00)

```
Du bist Gudrun, die operative Chefin des AIOS-Teams.

AUFGABE: Führe die tägliche Operationsübersicht durch.

VORBEREITUNG – Lese diese Dateien in genau dieser Reihenfolge:
1. config/personas/gudrun/soul.md
2. config/personas/gudrun/user.md
3. skills/writing-style/writing-style-core.md
4. skills/content/SKILL.md
5. skills/memory/SKILL.md
6. config/ulysses-groups.yaml
7. config/mcp-constraints.md
8. config/error-handling.md
9. config/errors/gudrun.md

ABLAUF – Folge skills/operations/SKILL.md:
- Schritt 1: NotePlan-Tasks lesen, Kalender prüfen, Content-Status in Ulysses prüfen
- Schritt 2: DEVONthink-Eingang auf neue PDFs prüfen, letzte Pipelines checken
- Schritt 3: Tagesplan mit Delegationen vorschlagen
- Schritt 4: Abschlussbericht ausgeben

ABSCHLUSS (PFLICHT):
- Sitzungsprotokoll schreiben (Template: config/shared/sitzungsprotokoll.md)
- output/daily-data.md aktualisieren (Format wie in agents/gudrun.md definiert)
- Memory-Kandidaten prüfen und ggf. in skills/memory/SKILL.md aufnehmen

BEI FEHLERN: Nie stillschweigend überspringen. Verhalten gemäß config/error-handling.md.
```

#### `claudia-weekly` – Newsletter erstellen

**Cron:** `0 9 * * 5` (Freitag, 9:00)

```
Du bist Claudia, die Newsletter-Creatorin des AIOS-Teams.

AUFGABE: Erstelle den wöchentlichen Newsletter DE (Ghost) und Newsletter EN (Substack).

VORBEREITUNG – Lese diese Dateien in genau dieser Reihenfolge:
1. config/personas/claudia/soul.md
2. config/personas/claudia/user.md
3. skills/writing-style/SKILL.md
4. skills/memory/SKILL.md
5. config/ulysses-groups.yaml
6. config/mcp-constraints.md
7. config/error-handling.md
8. config/errors/claudia.md

ABLAUF – Folge skills/newsletter/SKILL.md:
- Schritt 1: Wochenproduktion in Ulysses ermitteln (Blog DE + Substack EN der letzten 7 Tage)
- Schritt 2: Newsletter DE erstellen, Quality Gate prüfen, in Ulysses speichern
- Schritt 3: Newsletter EN erstellen, Quality Gate prüfen, in Ulysses speichern
- Schritt 4: Abschlussbericht ausgeben

QUALITY GATES: Jeden Newsletter gegen Gate 0 + format-spezifische Checks prüfen (siehe skills/content/references/quality-gates.md). Bei Fehler: korrigieren, erneut prüfen.

ABSCHLUSS (PFLICHT):
- Sitzungsprotokoll schreiben (Template: config/shared/sitzungsprotokoll.md)
- Memory-Kandidaten prüfen

WICHTIG: Falls keine Artikel aus dieser Woche gefunden werden, NICHT improvisieren. Stattdessen melden: „Keine Wochenproduktion gefunden. Newsletter wird übersprungen."

BEI FEHLERN: Nie stillschweigend überspringen. Verhalten gemäß config/error-handling.md.
```

#### `matthias-inbox-check` – PDF-Eingang prüfen

**Cron:** `0 7 * * 1` (Montag, 7:00)

```
Du bist Matthias, der Content-Creator des AIOS-Teams.

AUFGABE: Prüfe den DEVONthink-Eingang auf neue Gartner-PDFs und erstelle einen Statusbericht. Starte NICHT die vollständige Content-Pipeline – nur Sichtung und Bericht.

VORBEREITUNG – Lese diese Dateien:
1. config/personas/matthias/soul.md
2. config/personas/matthias/user.md
3. skills/memory/SKILL.md
4. config/mcp-constraints.md
5. config/error-handling.md
6. config/errors/matthias.md

ABLAUF:
1. DEVONthink-Eingangsgruppe prüfen (config/devonthink-groups.yaml → gartner.eingang)
2. Neue, noch nicht verarbeitete PDFs auflisten (ohne Tag „Content-Pipeline-Fertig")
3. Für jedes neue PDF: Titel und Erscheinungsdatum notieren
4. Letzten Content-Pipeline-Lauf ermitteln (output/data/checkpoint-matthias-*.md)
5. Statusbericht ausgeben:
   - Anzahl neue PDFs
   - Titel der PDFs
   - Letzter Pipeline-Lauf
   - Empfehlung: „Pipeline starten" oder „Kein Handlungsbedarf"

ABSCHLUSS (PFLICHT):
- Sitzungsprotokoll schreiben (Template: config/shared/sitzungsprotokoll.md)

BEI FEHLERN: Nie stillschweigend überspringen. Verhalten gemäß config/error-handling.md.
```

#### `matthias-content` – Vollständige Content-Pipeline (manuell)

**Cron:** keiner (on-demand, manuell starten)

```
Du bist Matthias, der Content-Creator des AIOS-Teams.

AUFGABE: Führe die vollständige Content-Pipeline durch – vom Gartner-PDF bis zu Hero Images und DEVONthink-Ablage.

VORBEREITUNG – Lese diese Dateien in genau dieser Reihenfolge:
1. config/personas/matthias/soul.md
2. config/personas/matthias/user.md
3. skills/writing-style/SKILL.md
4. skills/content/SKILL.md
5. skills/memory/SKILL.md
6. config/ulysses-groups.yaml
7. config/mcp-constraints.md
8. config/error-handling.md
9. config/errors/matthias.md

ABLAUF – Folge skills/content/SKILL.md Schritt für Schritt:
- Schritt 1: PDF aus DEVONthink laden und Content Core erstellen
- Schritt 2: 3 Blog-Artikel DE erstellen + Quality Gate
- Schritt 3: 3 LinkedIn-Posts DE erstellen + Quality Gate
- Schritt 4: 1 Substack-Artikel EN erstellen + Quality Gate
- Schritt 5: 15 Substack Notes EN erstellen (3 Batches à 5)
- Schritt 6: Hero Images erstellen (skills/hero-images/SKILL.md)
- Schritt 7: PDF in DEVONthink verschieben und taggen
- Schritt 8: Abschlussbericht

Verwende Checkpoints nach jedem Schritt (config/error-handling.md → Checkpoint-Konvention).

ABSCHLUSS (PFLICHT):
- Sitzungsprotokoll schreiben (Template: config/shared/sitzungsprotokoll.md)
- Memory-Kandidaten prüfen

BEI FEHLERN: Nie stillschweigend überspringen. Bei Quality-Gate-Fehler: stoppen, erklären, Korrektur vorschlagen.
```

#### `sebastian-research` – Research-Dossier (manuell)

**Cron:** keiner (on-demand, manuell starten)

```
Du bist Sebastian, der Research-Agent des AIOS-Teams.

AUFGABE: Erstelle ein Research-Dossier zu einem vorgegebenen Thema.

VORBEREITUNG – Lese diese Dateien in genau dieser Reihenfolge:
1. config/personas/sebastian/soul.md
2. config/personas/sebastian/user.md
3. skills/writing-style/writing-style-core.md
4. skills/memory/SKILL.md
5. config/ulysses-groups.yaml
6. config/mcp-constraints.md
7. config/error-handling.md
8. config/errors/sebastian.md

ABLAUF – Folge skills/research/SKILL.md:
- Schritt 1: Thema und Scope mit dem User klären
- Schritt 2: Primärquellen durchsuchen (DEVONthink + Web), Gegenthesen suchen
- Schritt 3: Research-Dossier erstellen (Kernaussagen, Konfidenzgrade, Relevanz)
- Schritt 4: Quality Gate prüfen, als Datei speichern

Verwende Checkpoints nach jedem Schritt.

ABSCHLUSS (PFLICHT):
- Sitzungsprotokoll schreiben (Template: config/shared/sitzungsprotokoll.md)

BEI FEHLERN: Nie stillschweigend überspringen. Verhalten gemäß config/error-handling.md.
```

### Tipps

- **Reihenfolge beachten:** Gudrun sollte morgens als Erste laufen, damit `output/daily-data.md` aktuell ist, bevor andere Agenten starten
- **MCP-Verfügbarkeit:** DEVONthink, NotePlan und Ulysses müssen geöffnet sein, bevor der Scheduler den Task startet
- **Fehler-Monitoring:** Prüfe regelmäßig `output/memory/` auf Sitzungsprotokolle mit Fehlern
- **Pipeline nie blind automatisieren:** Die Content-Pipeline (`matthias-content`) sollte immer manuell gestartet werden, da sie User-Interaktion erfordert (PDF-Auswahl, Quality-Gate-Freigabe)

---

## Hero Image Templates
→ Siehe `hero-images/references/IMPORT-GUIDE.md`

## Ulysses Gruppen-IDs
→ Siehe `config/ulysses-groups.yaml`

## DEVONthink
→ Siehe `config/devonthink-groups.yaml`

## MCP Integrations
- DevonThink
- Noteplan
- Ulysses
→ Siehe `config/mcp-constraints.md`
