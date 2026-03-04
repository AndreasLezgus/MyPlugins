# Command: Vollständige Pipeline starten

## Aufgabe

Führe die vollständige Content-Pipeline für das bereitgestellte Gartner PDF aus.
Arbeite jeden Schritt sequenziell ab. Stoppe bei Quality-Gate-Fehler und warte auf Freigabe.

## Input

```
PDF-Datei: {{input.file}}
Dateiname: {{input.filename}}
DEVONthink-Gruppe: {{integrations.devonthink.source_group}}
```

## Ausführungssequenz

### SCHRITT 1 – PDF analysieren & Content Core erstellen

Lies das PDF vollständig. Extrahiere:

1. **Bibliografische Daten**
   - Vollständiger Titel
   - Gartner Research ID
   - Publikationsjahr
   - Autoren (falls angegeben)

2. **Kernaussagen** (3–5 Hauptthesen)

3. **Statistiken & Prognosen** (mit Jahreszahl und Kontext)

4. **Empfehlungen** (Quick Wins / Mittelfristig / Langfristig)

5. **Kritische Prüfung**
   - Welche Annahmen trifft Gartner?
   - Was wird nicht erwähnt?
   - Praktikabilität im deutschen Behördenumfeld?

Fülle dann das Content Core Template aus (`skills/content-core-template.md`).
Zeige den ausgefüllten Core dem User **vor** dem Weiterschreiben.
Warte auf explizite Freigabe: „ok", „weiter", „bestätigt" oder ähnlich.

---

### SCHRITT 2 – Quality Gate 0 prüfen

Prüfe alle 5 Punkte aus Gate 0 Schnell-Check (`skills/quality-gates.md`).

Bei einem „nein": Stoppen. Erklären welcher Punkt nicht erfüllt ist. Korrektur vorschlagen.

Bei allen „ja": Weiter mit Schritt 3.

---

### SCHRITT 3 – Blog DE: Drei Varianten erstellen

Erstelle alle drei Varianten sequenziell.
Nach jeder Variante: Quality Gate 1 Schnell-Check durchführen.
Alle drei müssen das Gate bestehen bevor Schritt 4 beginnt.

---

#### SCHRITT 3a – Blog DE: KI-Führung

Verwende Template: `templates/blog-de-ki-fuehrung.md`
Fokus: KI-Kompetenz für Führungskräfte – Entscheidungsfähigkeit ohne Expertenwissen
Ghost-Tag: KI-Führung

Speichern in Ulysses:
```
Gruppe:    {{integrations.ulysses.blog_de_ki_fuehrung_group}}
Titel:     [SEO-Titel] – KI-Führung
Dateiname: {{date}}-[kurztitel]-ki-fuehrung
```

---

#### SCHRITT 3b – Blog DE: Quick Checks

Verwende Template: `templates/blog-de-quick-checks.md`
Fokus: Checklisten und Prüfpunkte – sofort anwendbar, kompakt, praxisnah
Ghost-Tag: Quick Checks

Gartner-Empfehlungen in konkrete Ja/Nein-Prüfpunkte übersetzen.
Jeder Punkt muss ohne technisches Vorwissen anwendbar sein.

Speichern in Ulysses:
```
Gruppe:    {{integrations.ulysses.blog_de_quick_checks_group}}
Titel:     Quick Check: [Thema] – [Anzahl] Prüfpunkte
Dateiname: {{date}}-[kurztitel]-quick-check
```

---

#### SCHRITT 3c – Blog DE: Kritisches Denken

Verwende Template: `templates/blog-de-kritisches-denken.md`
Fokus: Hype von Substanz unterscheiden – methodische Technologiebewertung
Ghost-Tag: Kritisches Denken

Gartner als Gesprächspartner nutzen, nicht als Autorität.
Explizit benennen: Was sieht Gartner nicht? Welche Annahme fehlt?

Speichern in Ulysses:
```
Gruppe:    {{integrations.ulysses.blog_de_kritisches_denken_group}}
Titel:     [Thema]: Warum [gängige Annahme] die falsche Frage ist
Dateiname: {{date}}-[kurztitel]-kritisches-denken
```

---

Fortschrittsbericht ausgeben (alle drei Varianten zusammen). Weiter mit Schritt 4.

---

### SCHRITT 4 – LinkedIn: Drei Varianten erstellen

Eine LinkedIn-Variante pro Blog-Variante.
Jede Variante referenziert ihren zugehörigen Blog-Artikel.
Alle Links als Platzhalter – werden vor Veröffentlichung ergänzt.

---

#### SCHRITT 4a – LinkedIn: KI-Führung

Verwende Template: `templates/linkedin-ki-fuehrung.md`
Bezug: Blog-Artikel aus Schritt 3a
Zielgruppe: C-Level und Senior Führungskräfte

Nach Erstellung: Quality Gate 3 Schnell-Check durchführen.

Speichern in Ulysses:
```
Gruppe:    {{integrations.ulysses.linkedin_group}}
Titel:     LinkedIn KI-Führung – {{date}}
```

---

#### SCHRITT 4b – LinkedIn: Quick Checks

Verwende Template: `templates/linkedin-quick-checks.md`
Bezug: Blog-Artikel aus Schritt 3b
Zielgruppe: Projektverantwortliche in Entscheidungssituationen

Nach Erstellung: Quality Gate 3 Schnell-Check durchführen.

Speichern in Ulysses:
```
Gruppe:    {{integrations.ulysses.linkedin_group}}
Titel:     LinkedIn Quick Check – {{date}}
```

---

#### SCHRITT 4c – LinkedIn: Kritisches Denken

Verwende Template: `templates/linkedin-kritisches-denken.md`
Bezug: Blog-Artikel aus Schritt 3c
Zielgruppe: Erfahrene Führungskräfte mit Skepsis-Kompetenz

Nach Erstellung: Quality Gate 3 Schnell-Check durchführen.

Speichern in Ulysses:
```
Gruppe:    {{integrations.ulysses.linkedin_group}}
Titel:     LinkedIn Kritisches Denken – {{date}}
```

---

Fortschrittsbericht ausgeben (alle drei Varianten). Weiter mit Schritt 5.

---

### SCHRITT 5 – Substack Artikel EN erstellen

Verwende Template: `templates/substack-article-en.md`
Befolge: `skills/writing-style.md` → Abschnitt 5.4

Basis: Content Core aus Schritt 1 – KEINE Übersetzung des Blog DE.
Neu schreiben für internationales Publikum.

Nach Erstellung: Quality Gate 4 Schnell-Check durchführen.

Speichern in Ulysses:
```
Gruppe:    {{integrations.ulysses.substack_en_group}}
Titel:     [English Title] – {{date}}
```

Fortschrittsbericht ausgeben. Weiter mit Schritt 6.

---

### SCHRITT 6 – 30 Substack Notes EN erstellen

Verwende Template: `templates/substack-note.md`
Befolge: `skills/writing-style.md` → Abschnitt 5.4 (Note-Regeln)

Erstelle 30 individuelle Notes. Jede Note:
- Greift einen anderen Aspekt des Substack-Artikels auf
- Ist eigenständig lesbar (kein Kontext aus anderen Notes nötig)
- Enthält einen Verweis auf den Substack-Artikel
- Link-Platzhalter: `[LINK TO SUBSTACK ARTICLE – add before publishing]`
- 150–300 Wörter
- Variierend in Einstieg und Perspektive (keine identischen Opener)

Verteile die 30 Notes thematisch auf diese Kategorien:
- 8x These / Kernaussage aus verschiedenen Winkeln
- 7x Praxis-Beobachtung / Erfahrung
- 6x Frage / Zum Nachdenken einladen
- 5x Kritik / Gegenperspektive
- 4x Konkreter Tipp / Handlungsempfehlung

Speichern in Ulysses – **jede Note einzeln**:
```
Gruppe:    {{integrations.ulysses.notes_group}}
Titel:     Note [01-30] – [Kurztitel] – {{date}}
```

Fortschrittsbericht ausgeben. Weiter mit Schritt 7.

---

### SCHRITT 7 – DEVONthink aufräumen

Verschiebe das verarbeitete PDF:
```
Von:  {{integrations.devonthink.source_group}}
Nach: {{integrations.devonthink.processed_group}}
```

Füge DEVONthink-Kommentar hinzu:
```
Verarbeitet: {{datetime}}
Erstellt: Blog DE, LinkedIn, Substack EN, 30 Notes
```

---

### SCHRITT 8 – Abschlussbericht

Gib eine Zusammenfassung aller erstellten Inhalte aus:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ PIPELINE ABGESCHLOSSEN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Quelle:       [Gartner Titel] (ID: [xxx], [Jahr])
Datum:        {{datetime}}

Erstellt:
  📝 Blog DE: KI-Führung          → [Titel] ([Wörter] Wörter)
  📝 Blog DE: Quick Checks        → [Titel] ([Wörter] Wörter)
  📝 Blog DE: Kritisches Denken   → [Titel] ([Wörter] Wörter)
  💼 LinkedIn: KI-Führung         → [Zeichen] Zeichen
  💼 LinkedIn: Quick Checks       → [Zeichen] Zeichen
  💼 LinkedIn: Kritisches Denken  → [Zeichen] Zeichen
  📧 Substack EN                  → [Titel] ([Wörter] Wörter)
  📱 30 Notes EN                  → Note 01–30 in Ulysses
  🗂 DEVONthink                   → PDF verschoben nach "Gartner-Verarbeitet"

Nächste Schritte:
  [ ] Blog-Links in LinkedIn Posts ergänzen (3×)
  [ ] Substack-Link in Notes ergänzen (30×)
  [ ] Featured Images erstellen (3 Blog + 1 Substack)
  [ ] Veröffentlichungsreihenfolge planen:
      Di: LinkedIn KI-Führung
      Mi: LinkedIn Quick Checks
      Do: LinkedIn Kritisches Denken
  [ ] Freitags-Newsletter: Command "newsletter" ausführen
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
