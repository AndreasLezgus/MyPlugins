---
description: Newsletter erstellen – Newsletter DE (Ghost) und EN (Substack) aus der Wochenproduktion von Blog-Artikeln.
---

Erstelle wöchentlich zwei Newsletter:
1. **Newsletter DE** für Ghost / „Die Zweite Meinung" (auf Deutsch)
2. **Newsletter EN** für Substack (auf Englisch)

Beide fassen die Veröffentlichungen der Woche zusammen.

---

## Checkpoint & Fortsetzen
Diese Pipeline verwendet Checkpoints (siehe `config/error-handling.md → Checkpoint-Konvention`).

**Bei Sitzungsbeginn:** Prüfe ob `output/data/checkpoint-claudia-[HEUTE]-*.md` existiert.
- Wenn ja: dem User zeigen und fragen ob fortgesetzt oder neu gestartet werden soll.
- Wenn nein: normal beginnen.

**Checkpoint-Datei:** `output/data/checkpoint-claudia-[DATUM]-kw[WOCHE].md`

---

## SCHRITT 1 – Wochenproduktion ermitteln

Suche in Ulysses nach Artikeln die diese Woche erstellt wurden:
- Blog-Artikel DE: IDs aus `config/ulysses-groups.yaml → blog_de.*`
- Substack-Artikel EN: ID aus `config/ulysses-groups.yaml → substack_en.artikel`

Liste alle gefundenen Artikel mit Titel und Kurzzusammenfassung.
Zeige dem User die Liste zur Bestätigung.

**CHECKPOINT:** Erstelle Checkpoint-Datei. Schritt 1 abhaken. Artikelliste im Checkpoint notieren.

---

## SCHRITT 2 – Newsletter DE erstellen (Ghost)

Inhalte:
- Begrüßung (kurz, persönlich, nicht formelhaft)
- Überblick der Woche: Was wurde veröffentlicht?
- Für jeden Blog-Artikel: Titel + 2–3 Sätze Teaser + Link
- Ausblick: Was kommt nächste Woche?
- Abschluss mit trockenem Humor

Ton: `skills/writing-style/SKILL.md` → Blog DE Regeln, Anrede „Sie"
Länge: 400–600 Wörter

Speichern in Ulysses mit `ulysses_new_sheet`:
- group: siehe `config/ulysses-groups.yaml → newsletter.de`
- Titel: `Newsletter DE – KW[WOCHE] – [DATUM]`

## SCHRITT 2b – Quality Gate: Newsletter DE

Lese `skills/content-drafts/references/quality-gates.md` und prüfe den Newsletter DE gegen:

**Gate 0 – Universeller Schnell-Check (5 Fragen, alle „ja"):**
- [ ] Eigene Praxiserfahrung mit dem Thema vorhanden
- [ ] These in einem Satz formulierbar
- [ ] Mindestens ein konkretes Beispiel
- [ ] Ein Weg nach vorn – kein Problem ohne Lösung
- [ ] Relevant für IT-Führungskräfte oder C-Level

**Newsletter-spezifisch (aus Gate 1 / Gate 0 Deep):**
- [ ] Klingt wie Andreas – nicht wie eine KI
- [ ] Roter Faden durch den gesamten Text erkennbar
- [ ] Keine Massenware-Formeln: „In dieser Ausgabe erwartet Sie…"
- [ ] Keine Plastikphrasen oder abgedroschene Metaphern
- [ ] Länge: 400–600 Wörter
- [ ] Anrede: „Sie" durchgehend

**Ein „nein" → korrigieren, dann erneut prüfen. Nicht mit Schritt 3 fortfahren.**

**CHECKPOINT:** Schritt 2 abhaken. Newsletter-DE-Content in Fallback sichern falls nur im Kontext.

---

## SCHRITT 3 – Newsletter EN erstellen (Substack)

Inhalte:
- Opening line (stark, nicht formelhaft)
- This week's highlights: Substack-Artikel mit Teaser
- One insight from practice (kurze Beobachtung, 3–5 Sätze)
- What's coming next week
- Closing (trocken, direkt)

Ton: `skills/writing-style/SKILL.md` → Substack EN Regeln, Anrede „you"
Länge: 350–500 Wörter

Speichern in Ulysses mit `ulysses_new_sheet`:
- group: siehe `config/ulysses-groups.yaml → newsletter.en`
- Titel: `Newsletter EN – Week [WOCHE] – [DATUM]`

## SCHRITT 3b – Quality Gate: Newsletter EN

Prüfe den Newsletter EN gegen:

**Gate 0 – Universeller Schnell-Check (5 Fragen, alle „ja"):**
- [ ] Eigene Praxiserfahrung mit dem Thema vorhanden
- [ ] These in einem Satz formulierbar
- [ ] Mindestens ein konkretes Beispiel
- [ ] Ein Weg nach vorn – kein Problem ohne Lösung
- [ ] Relevant für IT-Führungskräfte oder C-Level

**Newsletter EN-spezifisch (aus Gate 4):**
- [ ] Klingt wie Andreas – nicht wie eine KI
- [ ] Persönlicher Ton: „I've seen this happen" ist hier richtig
- [ ] Deutsche Behördenrealität als Fallbeispiel eingebettet, nicht vorausgesetzt
- [ ] Mehr Einladung zur Diskussion – Substack lebt von Antworten
- [ ] Keine Plastikphrasen oder abgedroschene Metaphern
- [ ] Länge: 350–500 Wörter
- [ ] Anrede: „you" durchgehend

**Ein „nein" → korrigieren, dann erneut prüfen. Nicht mit Schritt 4 fortfahren.**

**CHECKPOINT:** Schritt 3 abhaken.

---

## SCHRITT 4 – Abschlussbericht

**CHECKPOINT:** Alle Schritte abhaken. Pipeline als abgeschlossen markieren.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ NEWSLETTER ERSTELLT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Newsletter DE (Ghost):   [Titel] – [Wörter] Wörter
Newsletter EN (Substack): [Titel] – [Wörter] Wörter

Nächste Schritte:
  [ ] Newsletter DE in Ghost überprüfen und versenden
  [ ] Newsletter EN in Substack überprüfen und versenden
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
