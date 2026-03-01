---
name: create-content
description: 'Automatisierte Content-Pipeline: Liest Quelldokumente aus einem DEVONthink-Ordner und erstellt daraus kanalspezifische Inhalte (Substack-Artikel, Blog-Artikel, LinkedIn-Beiträge) in Ulysses. Verwende diesen Skill wenn (1) Dokumente aus DEVONthink in Content umgewandelt werden sollen, (2) die Content-Pipeline gestartet wird, (3) Batch-Content für mehrere Kanäle erstellt werden soll.'
---

# Content-Pipeline skill

**Quelldokumente → Kanalspezifischer Content → Ulysses**

## Übersicht

Dieser Skill orchestriert die automatische Erstellung von Content für drei Kanäle aus Quelldokumenten in DEVONthink:

1. **Blog-Artikel** → Ulysses: Blog/1-Ideen
2. **LinkedIn-Beitrag** → Ulysses: LinkedIn/1-Ideen (basiert auf dem Blog-Artikel)
3. **Substack-Artikel** → Ulysses: Substack/1-Ideen

Anschließend werden die Quelldokumente getaggt und verschoben.

## Trigger

User sagt etwas wie:
- "Verarbeite die Dokumente aus DEVONthink"
- "Content-Pipeline starten"
- "Erstelle Content aus dem Social-Media-Ordner"
- "Batch-Content erstellen"

## Dreischichtiges Prompt-System

Jeder generierte Artikel wird mit drei Kontextschichten erstellt:

| Schicht              | Quelle                                                                                       | Zweck                                                 |
| -------------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| **1. Basis-Stimme**  | `SKILL.md` + `/references/stimmprofil-andreas.md`                  | DNA aller Texte: Tonalität, Tabus, Signatur-Phrasen   |
| **2. Kanal-Prompt**  | `/workflows/substack-article.md` oder `/workflows/blog-article.md` oder `/workflows/linkedin-article.md` | Kanalspezifische Regeln: Anrede, Länge, Struktur, CTA |
| **3. Quelldokument** | DEVONthink-Inhalt via `get_record_content`                                                   | Der variable Inhalt, aus dem der Artikel entsteht     |

**Kritisch:** Bei JEDEM Artikel Schicht 1 laden. Nie direkt mit Schicht 2 beginnen.

## Workflow

### Phase 1: Quelldokumente scannen

	1. DEVONthink-Ordner auslesen:
	   Ordner: "10.10-Social-Media"
	   UUID: 8AB280B1-55E7-4B02-ABFE-3B761CC58B22
	   Tool: list_group_content(uuid="8AB280B1-55E7-4B02-ABFE-3B761CC58B22")
	
	2. Für jedes Dokument: 
	   - Name und Typ erfassen
	   - UUID speichern für spätere Verarbeitung
	   
	3. Dokumentliste dem User zur Bestätigung zeigen:
	   "Ich habe [N] Dokumente gefunden:
	    1. [Name] ([Typ])
	    2. [Name] ([Typ])
	    Soll ich für alle Dokumente Content erstellen?"
	    
	4. Auf Bestätigung warten. Nicht ohne Freigabe fortfahren.

### Phase 2: Content generieren

**Reihenfolge pro Dokument: Blog → LinkedIn → Substack**

Blog wird zuerst erstellt, weil der LinkedIn-Beitrag darauf aufbaut.

#### Schritt 2a: Basis-Stimme laden

	Lade und lies:
	- SKILL.md
	- /references/stimmprofil-andreas.md
	
	Dies ist der PFLICHT-Kontext für jeden einzelnen Artikel.

#### Schritt 2b: Quelldokument laden

	Tool: get_record_content(uuid="[Dokument-UUID]")
	
	Den Inhalt als Arbeitsgrundlage verwenden.
	Falls das Dokument ein PDF ist: Kernaussagen extrahieren.

#### Schritt 2c: Blog-Artikel erstellen

	1. Lade den Kanal-Prompt: /workflows/blog-article.md
	2. Generiere den Blog-Artikel gemäß allen drei Schichten
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

#### Schritt 2d: LinkedIn-Beitrag erstellen

	1. Lade den Kanal-Prompt: /references/linkedin-article.md
	2. Verwende den gerade erstellten Blog-Artikel als Input
	3. Generiere den LinkedIn-Beitrag gemäß allen drei Schichten
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

#### Schritt 2e: Substack-Artikel erstellen

	1. Lade den Kanal-Prompt: /references/substack-article.md
	2. Verwende das Original-Quelldokument als Input (NICHT den Blog-Artikel)
	3. Generiere den Substack-Artikel gemäß allen drei Schichten
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

#### Schritt 2f: Substack-Artikel erstellen

	1. Lade den Kanal-Prompt: /references/substack-notes.md
	2. Verwende den in Schritt 2e erstellten Substack-Article als Input (NICHT den Blog-Artikel)
	3. Generiere den Substack-Notes gemäß im Kanal-Promot erstellen Regeln
	4. Speichere in Ulysses:
	   Tool: ulysses_new_sheet(
	     text="[Markdown-Artikel]",
	     group="vakDORAkFmOO99q_YZAvoQ"    ← Substack/1-Ideen/1-Ideen-Notes
	   )
	5. Füge Keywords hinzu:
	   Tool: ulysses_attach_keywords(
	     sheet_id="[neue Sheet-ID]",
	     keywords=["Substack-Notes", "Pipeline", "[Thema-Tag]"]
	   )

#### Schritt 2g: Nächstes Dokument

	Wiederhole Schritte 2a-2e für das nächste Dokument.

### Phase 3: Aufräumen

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

### Phase 4: Abschlussbericht

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
	- Blog-Artikel von 1-Ideen nach 2-Artikel/1-Pipeline verschieben
	- LinkedIn-Beiträge von 1-Ideen nach 2-Beiträge/1-Pipeline verschieben"

## Ulysses-Ordner-Referenz

| Kanal            | Ordnerpfad               | Ulysses Group-ID         |
| ---------------- | ------------------------ | ------------------------ |
| Blog/1-Ideen     | Notizen/Blog/1-Ideen     | `UaxFYZgfWzstxBwjRWXpUw` |
| LinkedIn/1-Ideen | Notizen/LinkedIn/1-Ideen | `QIC4zWg_pU1WD9y3FKvS1Q` |
| Substack/1-Ideen | Notizen/Substack/1-Ideen | `vakDORAkFmOO99q_YZAvoQ` |

## DEVONthink-Referenz

| Ordner          | Name               | UUID                                   |
| --------------- | ------------------ | -------------------------------------- |
| Quelle (Input)  | 10.10-Social-Media | `8AB280B1-55E7-4B02-ABFE-3B761CC58B22` |
| Archiv (Output) | 50.01-Gartner      | `18B2F3AE-9D1E-448F-ABA2-236549FD71BA` |

## Fehler vermeiden

### ❌ NICHT

- Artikel ohne Basis-Stimme (Schicht 1) generieren
- LinkedIn-Beitrag vor dem Blog-Artikel erstellen
- Dokumente verschieben, bevor ALLE Artikel erstellt sind
- Ohne User-Bestätigung in Phase 1 starten
- Blog-Artikel als Grundlage für Substack nehmen (Substack basiert auf Quelldokument)

### ✅ STATTDESSEN

- IMMER zuerst `/references/stimmprofil-andreas.md` laden
- Blog → LinkedIn → Substack Reihenfolge einhalten
- Dokumente erst nach vollständigem Durchlauf taggen und verschieben
- Dokumentliste zeigen und auf Freigabe warten
- Substack eigenständig aus dem Quelldokument ableiten

## Qualitätssicherung

Vor dem Speichern jedes Artikels prüfen:

1. **Stimme:** Klingt es wie Andreas? (Kurze Sätze, keine Plastikphrasen, trockener Humor)
2. **Kanal:** Stimmt die Anrede? (Du/Sie) Stimmt die Länge? Stimmt der CTA?
3. **Inhalt:** Eigene Perspektive eingebracht? Nicht nur Zusammenfassung?
4. **Format:** Sauberes Markdown? Keine HTML-Tags? UTF-8?
5. **Quellen:** Korrekt zitiert mit Titel und Jahr?

Konsultiere `/references/workflow-checklist.md` für die vollständige Checkliste.