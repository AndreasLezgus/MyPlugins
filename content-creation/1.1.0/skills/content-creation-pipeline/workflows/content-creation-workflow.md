---
name: content-creation-workflow
description: Draft blog posts, substack article, substack notes, linkedin article with ulysses app, from ulysses app connect to publish on personal ghost blog, substack and linkedin
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
	2. Generiere den Blog-Artikel gemäß allen Schritten
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

	1. Lade den Kanal-Prompt: `/workflows/linkedin-article-creation.md`
	2. Verwende den gerade erstellten Blog-Artikel als Input
	3. Generiere den LinkedIn-Beitrag gemäß allen Schritten
	4. Speichere in Ulysses:
	   Tool: ulysses_new_sheet(`
	     text="[Markdown-Beitrag]",
	     group="QIC4zWg_pU1WD9y3FKvS1Q"    ← LinkedIn/1-Ideen
	   )
	5. Füge Keywords hinzu:
	   Tool: ulysses_attach_keywords(
	     sheet_id="[neue Sheet-ID]",
	     keywords=["LinkedIn", "Pipeline", "[Thema-Tag]"]
	   )

#### Schritt 6: Substack-Artikel erstellen

	1. Lade den Kanal-Prompt: `/workflows/substack-article-creation.md`
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

#### Schritt 7: Substack-Notes erstellen

	1. Lade den Kanal-Prompt: '/workflows/substack-notes-creation.md'
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
	
	"✅ Content-Creation-Pipeline abgeschlossen
	
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
	
  