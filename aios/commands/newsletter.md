---
description: Newsletter erstellen – Newsletter DE (Ghost) und EN (Substack) aus der Wochenproduktion von Blog-Artikeln.
---

Erstelle wöchentlich zwei Newsletter:
1. **Newsletter DE** für Ghost / „Die Zweite Meinung" (auf Deutsch)
2. **Newsletter EN** für Substack (auf Englisch)

Beide fassen die Veröffentlichungen der Woche zusammen.

---

## SCHRITT 1 – Wochenproduktion ermitteln

Suche in Ulysses nach Artikeln die diese Woche erstellt wurden:
- Blog-Artikel DE: IDs aus `config/ulysses-groups.yaml → blog_de.*`
- Substack-Artikel EN: ID aus `config/ulysses-groups.yaml → substack_en.artikel`

Liste alle gefundenen Artikel mit Titel und Kurzzusammenfassung.
Zeige dem User die Liste zur Bestätigung.

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

## SCHRITT 2b – Quality Gate prüfen
Prüfe Gate 0 aus quality-gates.md für den Newsletter DE.
Bei "nein": Korrektur, nicht weitermachen.

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

---

## SCHRITT 4 – Abschlussbericht

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
