# Die Zweite Meinung – Content Pipeline Plugin
**Claude Cowork Plugin | Version 1.0**

---

## Was dieses Plugin tut

Nimmt ein Gartner Research PDF aus DEVONthink und erstellt vollautomatisch:

| Output | Format | Sprache | Ulysses-Gruppe |
|---|---|---|---|
| Blog KI-Führung | Markdown | Deutsch | Blog DE/KI-Führung |
| Blog Quick Checks | Markdown | Deutsch | Blog DE/Quick Checks |
| Blog Kritisches Denken | Markdown | Deutsch | Blog DE/Kritisches Denken |
| LinkedIn: KI-Führung | Text | Deutsch | LinkedIn |
| LinkedIn: Quick Checks | Text | Deutsch | LinkedIn |
| LinkedIn: Kritisches Denken | Text | Deutsch | LinkedIn |
| Substack Artikel | Markdown | Englisch | Substack EN |
| 30 Substack Notes | Text (einzeln) | Englisch | Substack Notes |
| Newsletter DE | Markdown | Deutsch | Newsletter DE |
| Newsletter EN | Markdown | Englisch | Newsletter EN |

---

## Dateistruktur

```
zweite-meinung-plugin/
│
├── plugin.json                        ← Plugin-Manifest (Cowork liest das zuerst)
├── agent.md                           ← Haupt-Agent-Definition
├── README.md                          ← Diese Datei
│
├── commands/
│   ├── 00-full-pipeline.md            ← Vollständige Pipeline (Hauptbefehl)
│   └── 06-newsletter.md               ← Freitags-Newsletter
│
├── templates/
│   ├── blog-de.md                     ← Blog Deutsch
│   ├── linkedin-post.md               ← LinkedIn Post Deutsch
│   ├── substack-article-en.md         ← Substack Artikel Englisch
│   ├── substack-note.md               ← Einzelne Substack Note (×30)
│   ├── newsletter-de.md               ← Newsletter Deutsch (Ghost)
│   └── newsletter-en.md               ← Newsletter Englisch (Substack)
│
├── skills/
│   ├── writing-style.md               ← Brand Voice & Channel-Regeln
│   ├── quality-gates.md               ← Go/No-Go Checklisten
│   └── content-core-template.md       ← Strukturiertes Denken vor dem Schreiben
│
└── triggers/
    └── hazel-setup.md                 ← Automatischer Trigger via Hazel
```

---

## Dokumenten-Architektur: Warum so?

### Agent vs. Command vs. Skill vs. Template

```
AGENT       = Der Dirigent. Kennt den Gesamtworkflow, koordiniert alle Schritte,
              trifft Entscheidungen bei Fehlern. Bleibt während der ganzen
              Pipeline aktiv.

COMMAND     = Ein ausführbarer Schritt. Hat klaren Input, klaren Output,
              klare Abbruchbedingungen. Kann einzeln aufgerufen werden.

SKILL       = Nachschlagewerk. Wird vom Agent und Commands konsultiert,
              aber nicht ausgeführt. Enthält Regeln, Stil, Qualitätskriterien.

TEMPLATE    = Leeres Gerüst. Gibt Struktur und Hinweise vor.
              Wird von Commands ausgefüllt.

TRIGGER     = Anleitung wie der Agent gestartet wird (Hazel, manuell, etc.)
```

### Warum nicht alles in einen Prompt?

Ein einzelner langer Prompt verliert bei komplexen Workflows an Präzision.
Die Aufteilung erlaubt:
- Einzelne Commands ohne Neustart der Pipeline aufrufen
- Skills unabhängig aktualisieren ohne den Agent anzufassen
- Templates anpassen ohne die Logik zu ändern

---

## Einrichtung in VS Code

### 1. Projektordner öffnen

```bash
# Plugin-Ordner in VS Code öffnen
code /pfad/zu/zweite-meinung-plugin
```

### 2. Empfohlene VS Code Extensions

```json
// .vscode/extensions.json
{
  "recommendations": [
    "yzhang.markdown-all-in-one",     // Markdown Preview + Editing
    "davidanson.vscode-markdownlint", // Markdown Qualität
    "streetsidesoftware.code-spell-checker", // Rechtschreibung
    "ms-vscode.wordcount"             // Wortzählung
  ]
}
```

### 3. Workspace-Einstellungen

```json
// .vscode/settings.json
{
  "editor.wordWrap": "on",
  "editor.rulers": [80],
  "files.encoding": "utf8",
  "markdown.preview.fontSize": 14,
  "[markdown]": {
    "editor.defaultFormatter": "yzhang.markdown-all-in-one",
    "editor.wordWrap": "on"
  }
}
```

### 4. Plugin in Claude Cowork laden

```
Claude Cowork öffnen
→ Einstellungen → Plugins → Plugin hinzufügen
→ Ordner auswählen: zweite-meinung-plugin/
→ Cowork liest plugin.json automatisch
→ Plugin erscheint in der Command-Leiste
```

---

## Skills einrichten

Die drei Skill-Dateien im `skills/`-Ordner sind die Inhalte aus:
- `writing-style.md` → Deine fertige writing-style.md
- `quality-gates.md` → Deine fertige Quality Gates.md
- `content-core-template.md` → Dein fertiges Content Core Template.md

**Diese Dateien musst du mit deinen finalen Versionen befüllen.**
Sie sind bereits als Referenz-Dateien angelegt – einfach ersetzen.

---

## Ulysses-Gruppen einrichten

Der Agent erwartet diese Gruppen in Ulysses (exakte Schreibweise):

```
Die Zweite Meinung/
├── Blog DE/
│   ├── KI-Führung
│   ├── Quick Checks
│   └── Kritisches Denken
├── LinkedIn
├── Substack EN
├── Substack Notes
├── Newsletter DE
└── Newsletter EN
```

**Wichtig:** Die drei Blog-Untergruppen sind neu und müssen in Ulysses angelegt werden.
`Blog DE` selbst bleibt als übergeordnete Gruppe – die drei Varianten landen in den Untergruppen.

---

## DEVONthink-Gruppen einrichten

Der Agent erwartet zwei Gruppen in DEVONthink:

```
Gartner-Inbox       ← Neue PDFs landen hier (Hazel überwacht das)
Gartner-Verarbeitet ← PDFs nach Verarbeitung landen hier
```

Falls anders benannt: `plugin.json` → `integrations.devonthink` anpassen.

---

## Workflow: Schritt für Schritt

### Normaler Workflow (automatisch)

```
1. Gartner PDF in DEVONthink ablegen (Gruppe: Gartner-Inbox)
2. Hazel erkennt das PDF (innerhalb ~30 Sekunden)
3. Claude Cowork öffnet sich automatisch
4. Agent analysiert PDF und zeigt Content Core zur Freigabe
5. Du bestätigst: "ok" oder "weiter"
6. Agent erstellt alle Content-Formate (ca. 10–15 Minuten)
7. Alle Drafts liegen in Ulysses in den jeweiligen Gruppen
8. PDF wird in DEVONthink nach "Gartner-Verarbeitet" verschoben
```

### Freitags-Newsletter

```
1. Freitag morgen: Claude Cowork öffnen
2. Command "Freitags-Newsletter erstellen" ausführen
3. Agent liest Ulysses-Gruppen aus und listet Wochenproduktion
4. Du bestätigst die Liste
5. Agent erstellt Newsletter DE (Ghost) und EN (Substack)
6. Du überprüfst, ergänzt Links und versendest
```

### Manuelle Nachbearbeitung

Nach jedem Pipeline-Lauf:
```
[ ] Blog-Link in LinkedIn Post eintragen
[ ] Substack-Link in allen 30 Notes eintragen
[ ] Featured Images für Blog und Substack erstellen
[ ] Veröffentlichungsreihenfolge planen: Di–Do für LinkedIn
[ ] Notes über die Woche verteilen (6 Notes/Tag)
```

---

## Anpassungen

### Neue Ulysses-Gruppe hinzufügen

1. Gruppe in Ulysses anlegen
2. `plugin.json` → `integrations.ulysses` → neue Gruppe eintragen
3. Entsprechenden Command und Template anlegen

### Template anpassen

Templates in `templates/` können jederzeit angepasst werden –
ohne dass Agent oder Commands geändert werden müssen.

### Neuen Command hinzufügen

1. Neue Datei in `commands/` anlegen (z.B. `07-blog-en.md`)
2. Eintrag in `plugin.json` → `commands` hinzufügen
3. Cowork neu laden

---

## Versionierung

Empfehlung: Plugin-Ordner mit Git versionieren.

```bash
cd zweite-meinung-plugin
git init
git add .
git commit -m "Initial setup: Die Zweite Meinung Content Pipeline v1.0"
```

So kannst du Änderungen an Templates und Skills nachverfolgen
und bei Bedarf zurückrollen.
