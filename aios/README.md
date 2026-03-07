# MyTeam – Agenten für Andreas Lezgus

**Version 1.0.0** | Autor: Andreas Lezgus

Vollautomatische Agenten als Team-Mitglieder: 

1. Matthias: Analysiert z.B. Gartner reserach aus Devonthink und erstellt folgende Entwürfe mit meinem spezifischen Brand Guide:

- 3 Blog-Artikel für die Kategorien: KI-Führung, Quick Checks und Kritisches Denken in Deutsch
- 1 LinkedIN Artikel mit Verweis auf die Blog-Artikel in Deutsch
- 1 Substack Artikel in Englisch
- 30 Substack Notes mit Verweis auf den Substack Artikel in Englisch
- 3 Hero-Imgaes für die drei Blog-Artikel


2. Nadina: Analysiert die in der letzten Woche eröffentlichten 

---

## Installation

### Plugin installieren

```Download myteam-plugin.zip und hochladen in das Claude Cowork Plugin Verzeichnis
```

Claude Code neu starten, damit das Plugin aktiv wird.

---

## Verfügbare Commands

| Command       | Beschreibung |
|---------------|--------------|
| `/content`   | Vollständige Pipeline starten (alle Schritte) |
| `/newsletter` | Newsletter DE + EN erstellen |

---

## Hero Image Templates anpassen

Eigene Farb- und Schriftvarianten erstellen:

1. Datei in `hero-images/references/` kopieren
2. Farben, Schriften, Layout anpassen
3. Datei speichern – fertig

Vollständige Anleitung: `hero-images/IMPORT-GUIDE.md`

---

## Ulysses Gruppen-IDs
→ Siehe `config/ulysses-groups.yaml`

## DEVONthink
→ Siehe `config/devonthink-groups.yaml`

## MCP Integrations

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](CONNECTORS.md).

This plugin works with the following MCP servers:

- **Devonthink** — Share content, pdf, research articles
- **Ulysses** — Create and edit blog post, substack articles and notes, linkedIn articles
- **Noteplan** — Create and edit meeting notes, daily planning, weekly planning, special tasks
