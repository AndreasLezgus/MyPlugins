# Fehlerszenarien – Matthias (Content-Creator)

> Ergänzung zu `config/error-handling.md`. Nur Matthias-relevante Szenarien.

| § | Szenario | Ablauf |
|---|----------|--------|
| 2 | Ulysses Sheet-Erstellung fehlgeschlagen | Content in `output/fallback/` sichern. Gruppen-ID notieren. Im Abschlussbericht: Ziel-Gruppe + Fallback-Pfad. **Bulk-Notes (15 Stück):** 3 Batches à 5. Checkpoint nach jedem Batch. Bei Fehler: ab letzter erfolgreicher Note fortfahren. Fehlgeschlagene einzeln in Fallback. **Nie** `ulysses_set_sheet_title` aufrufen (siehe `config/mcp-constraints.md`). |
| 3 | DEVONthink PDF laden fehlgeschlagen | 1× Retry → User benachrichtigen mit UUID + Fehlermeldung → User fragen: PDF manuell hochladen oder Sitzung abbrechen? **Nicht** ohne PDF-Inhalt fortfahren. |
| 4 | DEVONthink Verschieben/Taggen fehlgeschlagen | 1× Retry → Content ist bereits erstellt, kein Datenverlust. Im Abschlussbericht: UUID + Ziel-UUID + Tags zum manuellen Setzen. Weiter mit Abschlussbericht. |
| 5 | DEVONthink Eingangsordner leer | User informieren. Optionen: PDF manuell bereitstellen, direkt hochladen, oder Sitzung beenden. Auf explizite Antwort warten. |
| 7 | PDF-Inhalt nicht extrahierbar | Bild-PDF ohne OCR? → User muss OCR-Version liefern. Teilweise extrahierbar? → User fragen ob ausreichend. **Nie** mit leeren/fragmentarischen Daten fortfahren. |
| 8 | Hero-Image-Script Fehler | Häufige Ursachen: Pillow fehlt (`pip install Pillow --break-system-packages`), Template-JSON nicht gefunden, Textlänge überschritten. Behebbar → automatisch korrigieren. Nicht behebbar → im Abschlussbericht notieren, welche Images fehlen. |
