---
name: content-drafts
description: Content-Pipeline für "Die Zweite Meinung" – analysiert Gartner-Research-PDFs und erstellt daraus Blog DE (3 Varianten), LinkedIn (3 Varianten), Substack EN und 30 Notes. Automatisch aktivieren wenn ein Gartner-PDF verarbeitet werden soll oder /content aufgerufen wird.
---

# Gartner Content Pipeline

Diese Skill enthält alle Templates und Qualitätsstandards für die vollständige Content-Pipeline von "Die Zweite Meinung" (lezgus.mymagic.page).

## Verfügbare Ressourcen

### References (Wissen & Qualitätskriterien)
- `references/content-core-template.md` – Analysevorlage für Gartner-PDFs
- `references/quality-gates.md` – Qualitätsprüfungen nach jedem Schritt

### Assets (Content-Templates)

**Blog DE:**
- `assets/blog-de-ki-fuehrung.md` – KI-Führung Variante (Entscheidungskompetenz)
- `assets/blog-de-quick-checks.md` – Quick Checks Variante (Checklisten)
- `assets/blog-de-kritisches-denken.md` – Kritisches Denken Variante (Hype vs. Substanz)
- `assets/blog-de.md` – Basis-Template

**LinkedIn:**
- `assets/linkedin-ki-fuehrung.md`
- `assets/linkedin-quick-checks.md`
- `assets/linkedin-kritisches-denken.md`
- `assets/linkedin-post.md` – Basis-Template

**Substack & Newsletter:**
- `assets/substack-article-en.md`
- `assets/substack-note.md`
- `assets/newsletter-de.md`
- `assets/newsletter-en.md`

## Ulysses Gruppen-IDs
- `README.md`


## DEVONthink

Nach Abschluss PDF verschieben nach:
- Zielgruppe: siehe `config/devonthink-groups.yaml → gartner.archiv`
- Tags setzen: `Content-Pipeline-Fertig`, `Blog-Erstellt`, `LinkedIn-Erstellt`, `Substack-Erstellt`

## Schreibstil

Alle deutschen Texte nach `writing-style` Skill.
Positionierung: "sachlich-kritisch", Zielgruppe TOP-Executives und erfahrene Führungskräfte.
Anrede: "Sie" (Blog DE, Newsletter DE), "you" (Substack EN).
