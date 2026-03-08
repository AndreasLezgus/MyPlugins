# MCP-Einschränkungen

> Diese Datei dokumentiert bekannte Einschränkungen und Workarounds der MCP-Server.
> Alle Agenten lesen diese Datei in ihrer Startup-Sequenz.
> Bei neuen Erkenntnissen: hier eintragen, nicht in einzelnen Commands.

---

## Ulysses

### Titel-Handling

**Niemals `ulysses_set_sheet_title` aufrufen.**

Der MCP-Server leitet den erforderlichen `type`-Parameter nicht an die Ulysses-API weiter. Der Aufruf schlägt immer fehl.

**Workaround:** Den Titel als erste Zeile im Content als H1-Heading setzen (`# Mein Titel`). `ulysses_new_sheet` übernimmt den Titel automatisch aus dieser Zeile.

### Sheet-Erstellung

Bei `ulysses_new_sheet` immer die Gruppen-ID aus `config/ulysses-groups.yaml` verwenden. Content muss vollständiges Markdown sein, beginnend mit `# Titel`.

### Bulk-Operationen

Bei Bulk-Operationen (z.B. 15 Substack Notes in 3 Batches à 5): nach jedem Batch den Fortschritt melden und Checkpoint aktualisieren. Bei Fehler: ab der letzten erfolgreichen Note fortfahren, nicht von vorn beginnen.

---

## DEVONthink

### Record-Verschiebung

`devonthink_move_record` erwartet die UUID des Records und die UUID der Zielgruppe. Beide IDs aus `config/devonthink-groups.yaml` beziehen.

### Tags setzen

`devonthink_add_tags` nach dem Verschieben aufrufen, nicht gleichzeitig. Tags als Array übergeben.

---

## NotePlan

Keine bekannten Einschränkungen. Pfad konfiguriert über `.mcp.json`.

---

*Letzte Aktualisierung: 2026-03-07*
*Bei neuen MCP-Problemen: hier dokumentieren und Datum aktualisieren.*
