## Fehlerbehandlung

### MCP nicht erreichbar
- 1x Retry nach 5 Sekunden
- Bei erneutem Fehler: Inhalt in output/fallback/ als Markdown sichern
- User benachrichtigen mit konkreter Fehlermeldung

### Ulysses-Sheet-Erstellung schlägt fehl
- Content in output/fallback/[agent]-[datum]-[titel].md sichern
- Fortfahren mit nächstem Schritt
- Im Abschlussbericht als "manuell nachzuholen" markieren