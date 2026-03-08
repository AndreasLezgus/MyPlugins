# Fehlerszenarien – Gudrun (Stabschefin)

> Ergänzung zu `config/error-handling.md`. Nur Gudrun-relevante Szenarien.

| § | Szenario | Ablauf |
|---|----------|--------|
| 3 | DEVONthink PDF laden fehlgeschlagen | 1× Retry → User benachrichtigen mit UUID + Fehlermeldung → Weiter mit restlichen Pipeline-Status-Prüfungen. |
| 5 | DEVONthink Eingangsordner leer | User informieren: „Kein neues PDF im Eingangsordner." Kein Blockiergrund für restliche Operations. |
| 6 | NotePlan Tagesnotiz nicht lesbar | 1× Retry → Tagesübersicht ohne NotePlan-Tasks erstellen. Im Abschlussbericht: „NotePlan-Tasks nicht lesbar." |
