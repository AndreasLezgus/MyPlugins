---
name: content-post-workflow
description: Draft blog posts with ulysses app, from ulysses app connect to publish on personal ghost blog
argument-hint: "<content type and topic>"
---

## Workflow

### Schritt 1: Quelldokumente scannen

	1. DEVONthink-Ordner auslesen:
	   Ordner: "10.10-Social-Media"
	   UUID: 8AB280B1-55E7-4B02-ABFE-3B761CC58B22
	   Tool: list_group_content(uuid="8AB280B1-55E7-4B02-ABFE-3B761CC58B22")
	
	2. Für jedes Dokument: 
	   - Name und Typ erfassen
	   - UUID speichern für spätere Verarbeitung

### Schritt 2: Referenzen lesen

	1. writing-style:
	    Ordner: `/references/writing-style.md` lesen
       
    2. visual-design: 
	    Ordner: `/references/visual-design.md` lesen
    
    3. quality-gates: 
	    Ordner: `/references/quality-gates.md` lesen 
  

#### Schritt 3: Quelldokument laden

	Tool: get_record_content(uuid="[Dokument-UUID]")
	
	Den Inhalt als Arbeitsgrundlage verwenden.
	Falls das Dokument ein PDF ist: Kernaussagen extrahieren.

#### Schritt 4: Blog-Artikel erstellen

	1. Lade den Kanal-Prompt: `/workflows/blog-post-creation.md`
	2. Generiere den Blog-Artikel gemäß allen Schritte
	3. Speichere in Ulysses:
	   Tool: ulysses_new_sheet(
	     text="[Markdown-Artikel]",
	     group="UaxFYZgfWzstxBwjRWXpUw"    ← Blog/1-Ideen
	   )
	4. Merke dir die Sheet-ID für den LinkedIn-Verweis
	5. Füge Keywords hinzu:
	   Tool: ulysses_attach_keywords(
	     sheet_id="[neue Sheet-ID]",
	     keywords=["Blog", "Pipeline", "[Thema-Tag]"]
	   )

#### Schritt 5: LinkedIn-Beitrag erstellen

	1. Lade den Kanal-Prompt: `/workflows/linkedin-article-creation.md
	2. Verwende den gerade erstellten Blog-Artikel als Input
	3. Generiere den LinkedIn-Beitrag gemäß allen Schritten
	4. Speichere in Ulysses:
	   Tool: ulysses_new_sheet(
	     text="[Markdown-Beitrag]",
	     group="QIC4zWg_pU1WD9y3FKvS1Q"    ← LinkedIn/1-Ideen
	   )
	5. Füge Keywords hinzu:
	   Tool: ulysses_attach_keywords(
	     sheet_id="[neue Sheet-ID]",
	     keywords=["LinkedIn", "Pipeline", "[Thema-Tag]"]
	   )

#### Schritt 6: Substack-Artikel erstellen

	1. Lade den Kanal-Prompt: `/references/substack-article.md`
	2. Verwende das Original-Quelldokument als Input (NICHT den Blog-Artikel)
	3. Generiere den Substack-Artikel
	4. Speichere in Ulysses:
	   Tool: ulysses_new_sheet(
	     text="[Markdown-Artikel]",
	     group="vakDORAkFmOO99q_YZAvoQ"    ← Substack/1-Ideen
	   )
	5. Füge Keywords hinzu:
	   Tool: ulysses_attach_keywords(
	     sheet_id="[neue Sheet-ID]",
	     keywords=["Substack", "Pipeline", "[Thema-Tag]"]
	   )

#### Schritt 7: Substack-Artikel erstellen

	1. Lade den Kanal-Prompt: '/references/substack-artike-creation.md'
	2. Speichere in Ulysses:
	   Tool: ulysses_new_sheet(
	     text="[Markdown-Artikel]",
	     group="vakDORAkFmOO99q_YZAvoQ"    ← Substack/1-Ideen/1-Ideen-Notes
	   )
	3. Füge Keywords hinzu:
	   Tool: ulysses_attach_keywords(
	     sheet_id="[neue Sheet-ID]",
	     keywords=["Substack-Notes", "Pipeline", "[Thema-Tag]"]
	   )

### Schritt 8: Aufräumen

**Erst NACH Abschluss ALLER Dokumente:**

	1. Tag "Ulysses" setzen für ALLE verarbeiteten Dokumente:
	   Tool: add_tags(uuid="[Dokument-UUID]", tags=["Ulysses"])
	   → Für jedes einzelne Dokument wiederholen
	
	2. ALLE Dokumente verschieben nach 50.01-Gartner:
	   Tool: move_record(
	     uuid="[Dokument-UUID]", 
	     destinationGroupUuid="18B2F3AE-9D1E-448F-ABA2-236549FD71BA"
	   )
	   → Für jedes einzelne Dokument wiederholen

### Schritt 9: Abschlussbericht

	Dem User eine Zusammenfassung zeigen:
	
	"✅ Content-Pipeline abgeschlossen
	
	Verarbeitete Dokumente: [N]
	
	| Quelle | Blog | LinkedIn | Substack |
	|--------|------|----------|----------|
	| [Dok1] | ✅   | ✅       | ✅       |
	| [Dok2] | ✅   | ✅       | ✅       |
	
	Alle Quelldokumente:
	- Tag "Ulysses" gesetzt
	- Verschoben nach 50.01-Gartner
	
	Nächste Schritte:
	- Artikel in Ulysses überprüfen und ggf. überarbeiten
	
  

## Die Schwerpunkte auf meinem persönlichen Blog

> Eine zweite unabhängige Meinung hilft immer.  Am besten von Leuten, die Erfahrung in vergleichbaren Positionen gesammelt haben.

Es gibt viel Meinung, viel Marketing und viele Schlagworte. Aber es fehlt oft an Orientierung, die in der Realität funktioniert. Hier geht es nicht um perfekte PowerPoint-Sätze. Sondern um die Fragen, die auf dem Tisch liegen, wenn man Verantwortung trägt.

- KI-Kompetenz in der Führung gestalten
Ich zeige, wie man KI realistisch bewertet: Was kann sie wirklich? Wo sind Grenzen? Welche Regeln helfen, damit sie sicher eingesetzt wird?

- Quick-Checks bei Unsicherheit (Cloud, KI, Cyber-Security)
Wenn eine Entscheidung dringend ist, braucht es schnelle Orientierung. Ich nutze einfache Checks: Was ist relevant, was ist nur Lärm, und wo liegt das echte Risiko?

- Digitale Souveränität und Handlungsfähigkeit
Ich interessiere mich stark dafür, wie Organisationen Optionen behalten: bei Plattformen, Daten, Abhängigkeiten und Lieferketten. Es geht darum, nicht festzuhängen -- sondern handlungsfähig zu bleiben.

- Positive Sturheit gegenüber jedem neuen IT-Trend
Nicht alles Neue ist automatisch gut. Ich halte es für klug, Trends freundlich zu prüfen -- und auch mal Nein zu sagen, wenn der Nutzen nicht stimmt.
 

## Basis-Stimme (PFLICHT)

Befolge ALLE Regeln aus dem Skill `/references/writing-style.md`. Die folgenden Kernregeln dürfen NIEMALS verletzt werden:

**IMMER:**
- Kurze, prägnante Sätze (10-20 Wörter, keine Schachtelsätze)
- These + rhetorische Frage als Eröffnung
- Problem → Analyse → Lösung als Grundstruktur
- Mit Lösung/Ausblick enden
- Konkrete Beispiele aus eigener Praxis
- Trockener Humor, besonders am Ende
- Autorität durch Spezifik (Zahlen, Projekte) statt Behauptung
- „Wir"-Formulierung bei Überleitung zur Lösung

**NIE:**
- „10 Tipps für…"-Listicles
- Semikolons
- Schachtelsätze
- Plastikphrasen: „Im Mittelpunkt steht der Mensch", „Einfach mal machen", „KI verändert alles", „Daten sind das neue Öl"
- Persönliche Angriffe auf namentlich genannte Personen
- Parteipolitische Aussagen
- Wütend, resigniert oder belehrend von oben herab
- Übertriebener Enthusiasmus

**Übersetzungsschicht:** Scharfe Kritik diplomatisch formulieren, aber Biss behalten. Spott durch Bilder erlaubt, Schimpfwörter nicht.

## Blog-spezifische Regeln

- **Anrede:** „Sie" (professionell)
- **Länge:** 1500–2500 Wörter (ca. 5–8 Minuten Lesezeit)
- **Ton:** Kritisch-konstruktiv, analytisch tiefer als Newsletter
- **Perspektive:** „Die Zweite Meinung" – unabhängig, erfahrungsbasiert, keine Vendor-Werbung
- **Zielgruppe:** IT-Führungskräfte und Entscheider im öffentlichen Sektor

## Artikelstruktur

Verwende exakt diese Struktur:

```markdown
---
title: [SEO-optimierter Titel, 50-60 Zeichen, Keyword am Anfang]
excerpt: [150-160 Zeichen Teaser, Neugier wecken, Hauptkeyword enthalten]
tags: [3-5 Tags, z.B. KI-Leadership, Digitale-Transformation, Technologie-Bewertung]
reading_time: [geschätzte Minuten]
---

# [Artikel-Titel]

> **TL;DR:** [3-4 Sätze Kernaussage für schnelle Leser]

## Das Problem

[Warum ist das Thema jetzt relevant? Warum ist eine Lösung so wichtig? Was passiert, wenn man nicht reagiert? Persönlicher Bezug/Perspektive. Fragestellung etablieren. 200-300 Wörter]

## Die Analyse

### [Unterabschnitt 1: Allgemeine Perspektive]
[Hauptthesen der Quelle zusammenfassen. Evidenz und Statistiken nennen. Empfehlungen aufzeigen.]

### [Unterabschnitt 2: Praxis-Check]
[Wo stimmt die Quelle? Wo weicht die Realität ab? 
Konkrete Beispiele aus der Behörden-Praxis (anonymisiert).]

### [Unterabschnitt 3: Die Zweite Meinung]
[Kritische Bewertung. Unbequeme Wahrheiten.
Behörden-spezifische Anpassungen. Was die Quelle nicht sieht.]

## Die Empfehlung

**Für IT-Führungskräfte:**
[3-4 konkrete, umsetzbare Schritte. Do's and Don'ts. Quick Wins.]

**Für Entscheider:**
[Strategische Überlegungen. Budget-Aspekte. Timing. Risiken]

## Fazit

[Kernbotschaft wiederholen. Ausblick geben.
Call-to-Action: Diskussion auf LinkedIn, Newsletter abonnieren.
Appell mit trockenem Humor.]

---

**Quellen:**
- [Weitere relevante Quellen zum Nachlesen, die öffentlich erreichbar sind]
```

## Quellenbehandlung

- Kurze Zitate (max. 1-2 Sätze) in Anführungszeichen
- Paraphrasieren bevorzugt
- Eigene „Zweite Meinung" immer gegenüberstellen
- Quellenabschnitt am Ende des Artikels

## Eröffnungsmuster

Nutze eines dieser Muster als Eröffnung im Kontext-Abschnitt:

- **These + Frage:** „[These mit aufgereihten Substantiven]. [Rhetorische Warum-Frage mit Vorwurf]?"
- **Erfahrungseinstieg:** „In meiner langjährigen Erfahrung stelle ich fest…"
- **Problem-Hook:** „Die Diskussion über [Thema] übersieht einen wichtigen Punkt…"

## Formulierungsmuster

**Für Kritik:**
- „Dies kann man so machen. Es ist allerdings nicht erfolgsversprechend, dass…"
- „Das klingt gut in der Theorie, aber…"
- „Was dabei übersehen wird…"

**Übergang zur Lösung:**
- „Wie können wir die dargestellten Probleme lösen?"

**Für Empfehlungen:**
- „Mein Rat: Beginnen Sie mit…"
- „Praxiserprobt ist folgende Herangehensweise…"

**Abschluss jeden Artikels mit Hinweis auf Newsletter wie folgt verbinden**
- Beende mit einem kurzen, warmen Call-to-Action. Kein harter Verkauf.
- Muster: Bezug zur Kernbotschaft des Artikels herstellen, dann die Leserin/den Leser zum Abonnieren einladen.
- Verwende diesen Stil: 
"Wenn dir das eine Idee geliefert hat, die sich zu testen lohnt – dann abonniere gern. Ich veröffentliche wöchentlich praktische Frameworks für KI-Verantwortliche, die Klarheit brauchen, nicht Hype."

Mein Newsletter. Keine Buzzwords. Keine Verkaufsfloskeln.  
Kostenlose praxisnahe Insights von einem CTO für Entscheider.

✓ Monatlich eine praxisnahe Analyse und Artikel  
✓ Konkrete Handlungsempfehlungen und Entscheidungshilfen  
✓ Früher Zugang zu neuen Artikeln

[Button: Anmelden]

**Nur für Mitglieder**

- Führe mit einem kurzen Übergang ein, zum Beispiel: „Bevor du diesen Tab schließt – hier ist dein praktisches Fazit.“

- Gib 5–7 umsetzbare Checklistenpunkte, die die Leserin/der Leser diese Woche anwenden kann.

- Format: ✅ [Handlungsverb] + [konkrete Aktion] + [warum es wichtig ist, in einem Nebensatz]

- Die Punkte müssen wirklich nützlich sein, kein generisches Füllmaterial.

- Was sind einige Dinge, die ein kritisches Denken in dem Thema fördern?

- Führe mit einem Übergang zu diesen Kritischen Denkmustern ein, zum Beispiel: "Weitere kritische Fragen, die für die individuelle Situation auch noch zu beantworten sind?"

- Gibt 5-7 kritische Fragen als Denkmuster an, die der Leser/die Leserin zur weiteren Prüfung individuel beantworten sollte.

- Format: ❓ [Handlungsverb] + [konkrete Aktion] + [warum es wichtig ist, in einem Nebensatz]

## Qualitätskriterien vor Ausgabe

- [ ] Klingt es wie Andreas? (Authentizitäts-Check)
- [ ] Anrede durchgängig „Sie"?
- [ ] 1500-2500 Wörter?
- [ ] Eigene Praxis-Perspektive eingebracht (nicht nur Quelle zusammengefasst)?
- [ ] Konkrete Handlungsempfehlungen vorhanden?
- [ ] Hinweise auf Gartner-Artikel und Verweise entfernt
- [ ] Sauberes Markdown, keine HTML-Tags?
- [ ] Trockener Humor oder pointierter Abschluss?
- [ ] Keine Plastikphrasen, keine Semikolons, keine Schachtelsätze?

## Ausgabeformat

Reines Markdown für Ulysses. Unix Line Endings (LF). Keine HTML-Tags. Verwende IMMER echte deutsche Umlaute (ä, ö, ü, Ä, Ö, Ü, ß) und niemals die ASCII-Umschreibungen (ae, oe, ue, ss). Der Text wird als UTF-8 weiterverarbeitet.
