# Sitzungsprotokoll-Template

Erstelle `output/memory/YYYY-MM-DD-[agent].md` mit diesem Format:

```markdown
# Sitzungsprotokoll [agent] – YYYY-MM-DD

## Erledigt
- [Aufgabe 1]: ✅ / ⚠️ (mit Fallback) / ❌ (gescheitert)

## Fehler
- [Fehler 1]: [Was passiert ist] → [Was getan wurde / Fallback-Pfad]
- Keine Fehler (wenn zutreffend)

## Manuell nachzuholen
- [ ] [Aktion 1] – [Details]
- Nichts (wenn zutreffend)

## Nächstes Mal beachten
- [Erkenntnis 1]

## Memory-Kandidaten
- [Wenn etwas dauerhaft in skills/memory/SKILL.md gehört, hier notieren]
```

**Memory prüfen:** Falls Memory-Kandidaten vorhanden → `skills/memory/SKILL.md` lesen, prüfen ob bereits existiert, ggf. anfügen.

**Fallback:** Falls `output/memory/` nicht beschreibbar → Protokoll als letzte Chat-Nachricht ausgeben (siehe `config/error-handling.md` §11).
