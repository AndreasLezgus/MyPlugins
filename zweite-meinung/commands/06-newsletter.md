# Command: Freitags-Newsletter

## Aufgabe

Erstelle jeden Freitag zwei Newsletter:
1. **Newsletter DE** für Ghost / „Die Zweite Meinung" (auf Deutsch)
2. **Newsletter EN** für Substack (auf Englisch)

Beide fassen die Veröffentlichungen der Woche zusammen.

## Input

```
Zeitraum:         Diese Woche (Montag–Freitag)
Ulysses Gruppen:  Blog DE, Substack EN (veröffentlichte Artikel)
Datum heute:      {{date}} (Freitag)
```

## Ausführungssequenz

### SCHRITT 1 – Wochenproduktion ermitteln

Suche in Ulysses nach Drafts/Artikeln die diese Woche erstellt wurden:
- Gruppe `{{integrations.ulysses.blog_de_group}}` → Blog-Artikel DE
- Gruppe `{{integrations.ulysses.substack_en_group}}` → Substack-Artikel EN

Liste alle gefundenen Artikel mit Titel und Kurzzusammenfassung.
Zeige dem User die Liste zur Bestätigung.

---

### SCHRITT 2 – Newsletter DE erstellen (Ghost)

Verwende Template: `templates/newsletter-de.md`

Inhalte:
- Begrüßung (kurz, persönlich, nicht formelhaft)
- Überblick der Woche: Was wurde veröffentlicht?
- Für jeden Blog-Artikel: Titel + 2–3 Sätze Teaser + Link
- Ausblick: Was kommt nächste Woche?
- Abschluss mit trockenem Humor

Ton: `skills/writing-style.md` → Blog DE Regeln, Anrede „Sie"
Länge: 400–600 Wörter

Speichern in Ulysses:
```
Gruppe:    {{integrations.ulysses.newsletter_de_group}}
Titel:     Newsletter DE – KW{{calendar_week}} – {{date}}
```

---

### SCHRITT 3 – Newsletter EN erstellen (Substack)

Verwende Template: `templates/newsletter-en.md`

Inhalte:
- Opening line (stark, nicht formelhaft)
- This week's highlights: Substack-Artikel mit Teaser
- One insight from practice (kurze Beobachtung, 3–5 Sätze)
- What's coming next week
- Closing (trocken, direkt)

Ton: `skills/writing-style.md` → Substack EN Regeln, Anrede „you"
Länge: 350–500 Wörter

Speichern in Ulysses:
```
Gruppe:    {{integrations.ulysses.newsletter_en_group}}
Titel:     Newsletter EN – Week {{calendar_week}} – {{date}}
```

---

### SCHRITT 4 – Abschlussbericht

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ NEWSLETTER ERSTELLT – KW{{calendar_week}}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Newsletter DE (Ghost):
  Titel:  Newsletter DE – KW{{calendar_week}}
  Länge:  [Wörter] Wörter
  Artikel dieser Woche: [Anzahl]

Newsletter EN (Substack):
  Titel:  Newsletter EN – Week {{calendar_week}}
  Länge:  [Wörter] Wörter
  Artikel dieser Woche: [Anzahl]

Nächste Schritte:
  [ ] Newsletter DE in Ghost überprüfen und versenden
  [ ] Newsletter EN in Substack überprüfen und versenden
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
