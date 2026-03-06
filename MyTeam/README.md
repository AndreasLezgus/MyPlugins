# MyTeam – Agenten für Andreas Lezgus

**Version 1.0.0** | Autor: Andreas Lezgus

Vollautomatische Content-Pipeline: 
Analysiert z.B. Gartner reserach aus Devonthink und erstellt folgende Entwürfe mit meinem spezifischen Brand Guide:
- 3 Blog-Artikel für die Kategorien: KI-Führung, Quick Checks und Kritisches Denken in Deutsch
- 1 LinkedIN Artikel mit Verweis auf die Blog-Artikel in Deutsch
- 1 Substack Artikel in Englisch
- 30 Substack Notes mit Verweis auf den Substack Artikel in Englisch
- 3 Hero-Imgaes für die drei Blog-Artikel

Weitere Agenten für den Tagesalltag:

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
| `/pipeline`   | Vollständige Pipeline starten (alle Schritte) |
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

| Gruppe | ID |
|--------|----|
| Blog DE / KI-Führung | `aEabxcQsV6hz0jZ7F7jiaA` |
| Blog DE / Quick Checks | `Ji9rIHGlNVFhxSdZXacQEg` |
| Blog DE / Kritisches Denken | `vuROqgmapR70lV49mty2lA` |
| LinkedIN | `qrJnA9hWVujo-yB_HNAdPQ` |
| Substack EN | `WfAl6Ob7Qe6c_2K2IhnBFQ` |
| Substack Notes | `1zd3tHuyCwmGRJn1iHTMcA` |
| Newsletter DE | `0Q-jME_qsk8pGVqIje_xSQ` |
| Newsletter EN | `7_8DSLUtrezBJopbYRIkDA` |

## DEVONthink

PDF nach Verarbeitung → Gruppe `50.01-Gartner`
UUID: `18B2F3AE-9D1E-448F-ABA2-236549FD71BA`

## MCP Integrations

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](CONNECTORS.md).

This plugin works with the following MCP servers:

- **Devonthink** — Share content, pdf, research articles
- **Ulysses** — Create and edit blog post, substack articles and notes, linkedIn articles
- **Noteplan** — Create and edit meeting notes, daily planning, weekly planning, special tasks
