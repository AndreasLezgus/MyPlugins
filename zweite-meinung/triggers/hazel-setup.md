# Trigger-Setup: Automatisch & Manuell

## Übersicht

Der Workflow kann auf zwei Wegen gestartet werden:

```
AUTOMATISCH  →  Hazel erkennt neues PDF in DEVONthink → startet Plugin
MANUELL      →  Claude Cowork Interface → Command „Vollständige Pipeline"
```

---

## Option A: Automatischer Trigger via Hazel

### Voraussetzungen
- Hazel (von Noodlesoft) installiert
- DEVONthink 3 installiert
- Claude Cowork installiert und Plugin geladen

### Schritt-für-Schritt

**1. DEVONthink-Gruppe als Ordner sichtbar machen**

DEVONthink speichert Daten intern. Für Hazel brauchst du den Dateisystem-Pfad:

```
Öffne DEVONthink 3
→ Rechtsklick auf Gruppe „Gartner-Inbox"
→ „Im Finder zeigen" (oder: Skript unten verwenden)
```

Alternativer Weg via AppleScript:
```applescript
tell application "DEVONthink 3"
    set theGroup to get record with name "Gartner-Inbox" in current database
    set thePath to path of theGroup
    return thePath
end tell
```

Notiere dir den vollständigen Pfad.

**2. Hazel-Regel erstellen**

```
Hazel öffnen
→ Ordner hinzufügen: [DEVONthink Gartner-Inbox Pfad]
→ Neue Regel erstellen
```

Regel-Konfiguration:
```
Name:       "Gartner PDF → Content Pipeline"

Bedingungen:
  Name     enthält    "Gartner" ODER
  Extension entspricht "pdf"
  Datum hinzugefügt  ist heute

Aktionen:
  1. Skript ausführen (AppleScript):
     → [Inhalt: siehe unten]
  2. Warte 5 Sekunden
  3. Farbmarkierung: Grün (= verarbeitet)
```

**3. AppleScript für Hazel-Aktion**

```applescript
-- Hazel AppleScript: Startet Claude Cowork Plugin
-- Speichern als: trigger-content-pipeline.applescript

on hazelProcessFile(theFile)
    set filePath to POSIX path of theFile
    set fileName to name of theFile

    -- Claude Cowork via URL-Schema triggern
    set coworkURL to "claudecowork://run?plugin=zweite-meinung-content-pipeline&command=full-pipeline&file=" & filePath

    -- URL öffnen (startet Cowork mit dem Dokument)
    open location coworkURL

    -- Optional: Benachrichtigung
    display notification "Content Pipeline gestartet für: " & fileName ¬
        with title "Die Zweite Meinung" ¬
        subtitle "Gartner PDF erkannt"
end hazelProcessFile
```

**4. Testen**

```
Lege ein Test-PDF in DEVONthink „Gartner-Inbox"
→ Hazel sollte die Regel innerhalb von 30 Sekunden auslösen
→ Claude Cowork sollte sich öffnen und die Pipeline starten
```

---

## Option B: Manueller Trigger

### Über Claude Cowork Interface

```
1. Claude Cowork öffnen
2. Plugin „Die Zweite Meinung – Content Pipeline" auswählen
3. Command „Vollständige Pipeline starten" klicken (oder ⌘⇧P)
4. PDF-Datei aus DEVONthink übergeben:
   → Drag & Drop auf das Cowork-Fenster
   → ODER: „Datei auswählen" → DEVONthink Gartner-Inbox navigieren
5. Pipeline läuft durch
```

### Über DEVONthink direkt

DEVONthink unterstützt Skripte direkt aus der Toolbar.
Skript in DEVONthink-Skriptmenü ablegen:

```applescript
-- DEVONthink Skript: Ausgewähltes Dokument an Content Pipeline übergeben
-- Ablegen in: ~/Library/Application Scripts/com.devon-technologies.think3/Menu/

tell application "DEVONthink 3"
    set theRecord to (get selection)
    if theRecord is {} then
        display dialog "Bitte zuerst ein Dokument in DEVONthink auswählen."
        return
    end if

    set theFile to item 1 of theRecord
    set filePath to path of theFile

    -- Claude Cowork starten
    set coworkURL to "claudecowork://run?plugin=zweite-meinung-content-pipeline&command=full-pipeline&file=" & filePath
    open location coworkURL
end tell
```

**Installation:**
```
Datei speichern als: "Content Pipeline starten.applescript"
Ablegen in: ~/Library/Application Scripts/com.devon-technologies.think3/Menu/
DEVONthink neu starten
→ Skript erscheint im Skript-Menü (☆) von DEVONthink
```

---

## Freitags-Newsletter manuell starten

Da der Newsletter einmal wöchentlich läuft:

```
Claude Cowork öffnen
→ Command „Freitags-Newsletter erstellen" klicken
→ Kein Datei-Input nötig – Agent liest Ulysses-Gruppen selbst aus
```

Optional als macOS Kalender-Erinnerung:
```
Kalender-Event: Jeden Freitag 09:00
Titel: "Newsletter erstellen – Claude Cowork"
Notiz: "Command: Freitags-Newsletter | Plugin: zweite-meinung-content-pipeline"
```

---

## Troubleshooting

**Hazel erkennt das PDF nicht:**
→ DEVONthink-Gruppe als Ordner prüfen (Hazel braucht echten Dateisystem-Pfad)
→ DEVONthink-Einstellung: „Dateien extern sichtbar" aktivieren

**Claude Cowork öffnet sich nicht:**
→ URL-Schema prüfen: `claudecowork://` muss registriert sein
→ Cowork neu starten, dann Hazel-Regel nochmal testen

**Ulysses-Gruppen nicht gefunden:**
→ Gruppennamen in `plugin.json` → `integrations.ulysses` prüfen
→ Exakt dieselbe Schreibweise wie in Ulysses verwenden
