# Blog DE Template-System: Strukturvarianten-Pool
**„Die Zweite Meinung" | Andreas Lezgus**

> Dieses Dokument ersetzt starre Einzel-Templates durch einen Pool von Strukturvarianten.
> Der Sub-Agent wählt die passende Variante basierend auf dem Content Core.
> Ziel: Jeder Artikel hat eine andere Architektur. Kein erkennbares Muster über mehrere Artikel.

---

## Teil 1: Architektur-Prinzipien

### Warum mehrere Strukturen?

Ein einzelnes Template erzeugt nach 2-3 Artikeln ein erkennbares Muster. Leser (und Algorithmen) erkennen KI-generierte Inhalte vor allem an struktureller Monotonie: gleiche Abschnittszahl, gleiche Absatzdichte, gleiche Übergänge. Echte Autoren variieren ihre Artikelarchitektur je nach Inhalt.

### Trennung von Anweisung und Struktur

Jede Variante besteht aus zwei Ebenen:

- **Gerüst:** Die Abschnitte und ihre Reihenfolge (das sieht der Leser)
- **Regieanweisung:** Was der Sub-Agent in jedem Abschnitt tun soll (das sieht der Leser nicht)

Der Sub-Agent erhält beides. Er gibt nur das Gerüst aus, gefüllt mit Inhalt.

### Pflicht-Elemente (in jeder Variante, Reihenfolge variabel)

1. **TL;DR** als Blockquote (3-4 Sätze, immer am Anfang)
2. **Praxisanker** (anonymisiertes Beispiel aus reguliertem Umfeld)
3. **Eigene Einordnung** (nicht nur Quelle wiedergeben, sondern bewerten)
4. **Handlungsimpuls** (konkreter Weg nach vorn)
5. **Abschluss** mit trockenem Humor oder pointiertem Appell

### Verbotene Muster (KI-Signale)

- Exakt drei Punkte in jeder Liste (variiere: 2, 4, 5)
- Identische Absatzlänge durchgängig (mische: Einzeiler, 3-Satz-Blöcke, 5-Satz-Absätze)
- Nummerierte Schritte als Hauptstruktur in jedem Artikel
- Gleiche Übergangsformulierungen zwischen Abschnitten
- Jeder Abschnitt mit einer Frage eröffnen
- „Erstens / Zweitens / Drittens" als wiederkehrendes Muster
- Symmetrische Abschnittslängen (ein Abschnitt darf deutlich kürzer sein als andere)

---

## Teil 2: Varianten-Pool

---

### VARIANTE A: „Der Widerspruch"

**Passt wenn:** Der Content Core eine These enthält, die dem Mainstream widerspricht. Gartner sagt X, die Praxis zeigt Y. Ideal für kontroverse Positionen.

**Architektur:**

```
# [Titel]

> **TL;DR:** [...]

## [H2: Die gängige Erzählung]
Was „alle" sagen. Quelle/Gartner-Position neutral wiedergeben.
Nicht strohmannartig, sondern fair. Dann: der Bruch.
Ein Satz, der die Gegenposition eröffnet.

## [H2: Was die Praxis zeigt]
Praxisanker: konkretes Beispiel, das die gängige Erzählung infrage stellt.
Eigene Einordnung: Warum stimmt die Theorie hier nicht?
Keine Liste. Fließtext. 3-5 Absätze, unterschiedlich lang.

## [H2: Was daraus folgt]
Handlungsimpuls: Was soll die Führungskraft anders machen?
Konkret, mit Zeitrahmen oder Format. Nicht mehr als 2-4 Empfehlungen.
Kein nummeriertes Format: als Fließtext mit Fettdruck für Kernbegriffe.

## Fazit
Kernbotschaft in 2-3 Sätzen. Trockener Humor. Appell.
```

**Regieanweisung für den Sub-Agent:**

- Eröffnung: These mit aufgereihten Substantiven + rhetorische Frage (Writing Style §4)
- Der Widerspruch darf nicht konstruiert wirken. Die Gegenposition muss aus Erfahrung kommen.
- Kein „Aber Gartner irrt sich". Sondern: „Das stimmt. Nur eben nicht in jedem Kontext."
- Absätze bewusst asymmetrisch: der Praxis-Abschnitt darf der längste sein.

---

### VARIANTE B: „Die Entscheidungssituation"

**Passt wenn:** Der Content Core eine typische Führungsentscheidung beschreibt. Jemand steht vor einer Wahl. Es geht um Kriterien, nicht um Technik.

**Architektur:**

```
# [Titel]

> **TL;DR:** [...]

## [H2: Die Situation, die Sie kennen]
Szenario: Eine konkrete Entscheidungssituation direkt beschreiben.
Nicht hypothetisch, sondern: „Sie sitzen im Lenkungsausschuss. Die Präsentation
war überzeugend. Die Zahlen klingen gut."
Dann: Was wurde nicht gefragt?

## [H2: Die Fragen hinter der Frage]
Keine nummerierte Liste. Stattdessen: Im Fließtext die entscheidenden
Prüfpunkte entwickeln. Jeder Prüfpunkt als eigener kurzer Absatz.
Manche Prüfpunkte mit Fettdruck-Einleitung, andere ohne.
Variation ist entscheidend.

## [H2: Ein Beispiel, das zeigt warum]
Praxisanker: Was passiert, wenn diese Fragen nicht gestellt werden?
Anonymes Beispiel. Konkretes Ergebnis. „Das Ergebnis war vorhersehbar" darf hier stehen.

## [H2: Wie Sie sich vorbereiten]
Handlungsimpuls. Kurz. Spezifisch. Mit Zeitaufwand.
Dieser Abschnitt darf bewusst der kürzeste im Artikel sein.

## Fazit
```

**Regieanweisung für den Sub-Agent:**

- Die Eröffnung zieht den Leser in die Situation. Zweite Person Singular formal („Sie").
- Die Prüfpunkte im Mittelteil dürfen zwischen 2 und 5 liegen. Nie exakt drei.
- Der Praxis-Abschnitt ist das emotionale Zentrum. Hier darf ein längerer Absatz stehen.
- Der Vorbereitungs-Abschnitt ist bewusst knapp: Wer bis hierhin gelesen hat, braucht keine lange Anleitung.

---

### VARIANTE C: „Der Praxis-Check"

**Passt wenn:** Der Content Core hauptsächlich eine Quelle (Gartner, Studie) gegen die Praxis prüft. Die Kernfrage ist: Stimmt das so? Für wen? Unter welchen Bedingungen?

**Architektur:**

```
# [Titel]

> **TL;DR:** [...]

## [H2: Was [Quelle] sagt]
Faire, kompakte Zusammenfassung. Nicht länger als 200 Wörter.
Zentrale These und wichtigste Zahl herausgreifen.

## [H2: Der Praxis-Check]
Eigene Einordnung. Was stimmt? Was fehlt? Was gilt nur unter Bedingungen?
Hier steht der Kern des Artikels. 400-500 Wörter.
Absätze variieren: ein kurzer Einzeiler-Absatz dazwischen ist erlaubt.

## [H2: Was das für Ihre nächste Entscheidung bedeutet]
Handlungsimpuls direkt aus dem Praxis-Check ableiten.
Mischformat: Fließtext mit eingebetteten konkreten Empfehlungen.

## Fazit
```

**Regieanweisung für den Sub-Agent:**

- Kompakteste Variante. Ideal für Quellen-Bewertung. 3 Hauptabschnitte plus Fazit.
- Die Quelle wird respektiert, aber nicht ungeprüft übernommen.
- Der Praxis-Check-Abschnitt ist mit Abstand der längste. Hier zeigt sich die Expertise.
- Erlaubt: Ein direktes Zitat aus der Quelle als Aufhänger.

---

### VARIANTE D: „Die Fehldiagnose"

**Passt wenn:** Der Content Core ein verbreitetes Missverständnis oder eine falsche Priorität identifiziert. Die These lautet: Das Problem ist nicht X, sondern Y.

**Architektur:**

```
# [Titel]

> **TL;DR:** [...]

## [H2: Die Diagnose, die alle stellen]
Was wird als Problem identifiziert? Kurz, fair, ohne Strohmann.
Warum klingt diese Diagnose plausibel?

## [H2: Warum die Diagnose nicht reicht]
Der Twist. Praxisanker einbauen.
Konkretes Beispiel: Organisation behandelt Symptom statt Ursache.
Was war das tatsächliche Problem?

## [H2: Die richtige Frage]
Umformulierung des Problems. Nicht: „KI-Projekte scheitern an fehlender Strategie."
Sondern: „KI-Projekte scheitern, weil die Datenbasis vor dem Piloten nicht geprüft wurde."
Handlungsimpuls direkt in die Analyse einweben, nicht als separaten Block.

## Fazit
Pointiert. Ein Satz Kernbotschaft. Ein Satz Humor oder Appell.
```

**Regieanweisung für den Sub-Agent:**

- Diese Variante lebt vom Twist im zweiten Abschnitt. Der muss sitzen.
- Der dritte Abschnitt verbindet Analyse und Handlung. Keine separate Empfehlungsliste.
- Kürzestes Fazit aller Varianten: 2-3 Sätze, nicht mehr.
- Gesamtlänge eher am unteren Ende: 900-1.100 Wörter.

---

### VARIANTE E: „Das Werkzeug"

**Passt wenn:** Der Content Core ein konkretes Bewertungsraster, eine Methode oder ein Prüfschema enthält. Der Artikel liefert dem Leser ein Tool für eigene Entscheidungen.

**Architektur:**

```
# [Titel]

> **TL;DR:** [...]

## [H2: Warum Sie dieses Werkzeug brauchen]
Kontext: Welches wiederkehrende Problem löst dieses Werkzeug?
Praxisanker: Kurzes Beispiel einer Situation ohne das Werkzeug.
Kurz halten. 150-200 Wörter.

## [H2: Das Werkzeug / Die Methode / Die Prüffragen]
Kern des Artikels. Hier das Werkzeug vorstellen.
Format bewusst wählen (NICHT immer gleich):

Option 1: Fließtext mit Fettdruck-Begriffen
Option 2: Kurze Einleitung, dann 2-5 Prüfpunkte mit je 2-3 Sätzen Erklärung, dann Fazit
Option 3: Szenario-basiert ("Wenn X, dann fragen Sie Y")
Option 4: Tabelle (selten, nur wenn es wirklich passt)

Wichtig: Die Anzahl der Punkte ergibt sich aus dem Inhalt, nicht aus einem Template.

## [H2: Was passiert, wenn Sie es anwenden]
Konkretes Ergebnis-Szenario. Vorher/Nachher.
Oder: Was eine informierte Führungskraft anders entscheidet.

## Fazit
```

**Regieanweisung für den Sub-Agent:**

- Das Format des Werkzeug-Abschnitts muss bei jedem Einsatz variieren.
- Keine „Die 3 Fragen die Sie stellen sollten"-Überschrift. Stattdessen inhaltliche H2.
- Prüfpunkte dürfen zwischen 2 und 5 liegen. Nie fixe Anzahl.
- Der Vorher/Nachher-Abschnitt ist optional. Wenn der Praxisanker schon im Werkzeug-Teil steckt, kann er entfallen. Dann: kürzerer Artikel.

---

## Teil 3: Varianten-Wahl durch den Sub-Agent

### Entscheidungslogik

Der Sub-Agent liest den Content Core und beantwortet intern diese Fragen:

```
1. Widerspricht meine These dem Mainstream?
   → JA: Variante A (Der Widerspruch)

2. Geht es um eine konkrete Führungsentscheidung?
   → JA: Variante B (Die Entscheidungssituation)

3. Prüfe ich hauptsächlich eine externe Quelle gegen die Praxis?
   → JA: Variante C (Der Praxis-Check)

4. Identifiziere ich ein verbreitetes Missverständnis?
   → JA: Variante D (Die Fehldiagnose)

5. Liefere ich ein konkretes Bewertungswerkzeug?
   → JA: Variante E (Das Werkzeug)
```

**Wenn mehrere zutreffen:** Die erste passende Variante wählen. Bei Gleichstand entscheidet: Welche Variante wurde beim letzten Artikel NICHT verwendet?

**Rotationsregel:** Keine Variante darf zweimal hintereinander verwendet werden. Der Sub-Agent prüft die zuletzt verwendete Variante (aus dem Checkpoint oder aus der Übergabe) und schließt sie aus.

### Adaption innerhalb der Variante

Auch innerhalb einer gewählten Variante variiert der Sub-Agent:

- **Abschnittszahl:** Ein H2-Abschnitt darf bei inhaltlicher Begründung entfallen oder hinzukommen
- **Absatzlänge:** Mindestens ein Absatz pro Artikel, der nur 1-2 Sätze lang ist
- **Listenformat:** Maximal eine Liste pro Artikel. In jedem zweiten Artikel keine Liste.
- **Eröffnungsvariante:** Pool aus Writing Style §4 nutzen, nie dieselbe Eröffnung wie der letzte Artikel
- **Abschlussvariante:** Pool aus Signatur-Aphorismen nutzen, rotierend

---

## Teil 4: Blog-Kategorien und ihre Besonderheiten

### 3a – KI-Führung

**Fokus:** KI-Kompetenz für Führungskräfte. Entscheidungsfähigkeit ohne Expertenwissen.
**Ghost-Tag:** KI-Führung
**Bevorzugte Varianten:** A, B, E (D und C möglich, seltener)

**Besondere Regeln:**
- Keine technischen Details. Wenn Technik erklärt werden muss: maximal ein Satz, dann sofort Führungsrelevanz.
- Zielgruppe explizit: Menschen, die über KI-Projekte entscheiden, aber nicht aus der IT kommen.
- Ton: Respektvoll, aber direkt. „Sie müssen das nicht verstehen. Sie müssen es beurteilen können."

**Titel-Muster (variieren):**
- „[Thema]: Was Führungskräfte wirklich wissen müssen"
- „[Provokante These] – und was das für Ihre KI-Strategie bedeutet"
- „Warum [verbreitete Annahme] Führungskräfte in die Irre führt"

### 3b – Quick Checks

**Fokus:** Sofort anwendbare Prüfpunkte. Kompakt. Praxisnah.
**Ghost-Tag:** Quick Checks
**Bevorzugte Varianten:** E (primär), C (sekundär)

**Besondere Regeln:**
- Kürzer als KI-Führung: 800-1.000 Wörter Zielkorridor
- Jeder Prüfpunkt muss als Ja/Nein-Frage formulierbar sein
- Kein Prüfpunkt, der technisches Vorwissen voraussetzt
- Der Leser muss den Quick Check in der nächsten Sitzung anwenden können
- Einleitung bewusst kurz: maximal 150 Wörter vor dem ersten Prüfpunkt

**Titel-Muster (variieren):**
- „Quick Check: [Thema] – [Anzahl] Fragen vor der Entscheidung"
- „[Thema] auf dem Prüfstand: Was Sie vor dem nächsten Meeting wissen sollten"
- „Checkliste [Thema]: Bereit für die Entscheidung?"

**Struktur-Besonderheit:**
Quick Checks verwenden IMMER einen Werkzeug-Abschnitt, aber das Format variiert:

```
Format-Rotation für Quick Checks:
1. Prüffragen mit Erklärung (2-3 Sätze pro Frage)
2. Szenario-basiert ("Wenn Ihr KI-Anbieter X sagt, fragen Sie Y")
3. Vorher/Nachher ("Ohne Check: ... | Mit Check: ...")
4. Warnsignal-fokussiert ("Achten Sie auf: ...")
```

### 3c – Kritisches Denken

**Fokus:** Hype von Substanz unterscheiden. Methodische Technologiebewertung.
**Ghost-Tag:** Kritisches Denken
**Bevorzugte Varianten:** A, D (primär), C (sekundär)

**Besondere Regeln:**
- Der Artikel ist Gesprächspartner, nicht Autorität
- Explizit benennen: Was sieht die Quelle nicht? Welche Annahmen fehlen?
- Darf unbequeme Fragen stellen, ohne sofort eine Antwort zu liefern
- Offenere Abschlüsse erlaubt: „Diese Frage bleibt offen. Und das ist in Ordnung."
- Stärkster Einsatz von trockenem Humor aller drei Kategorien

**Titel-Muster (variieren):**
- „[Thema]: Warum [Annahme] die falsche Frage ist"
- „Die unbequeme Wahrheit über [Thema]"
- „[Buzzword] unter der Lupe: Was bleibt, wenn der Hype vergeht?"

**Struktur-Besonderheit:**
Kritisches Denken erlaubt als einzige Kategorie einen Abschnitt „Was wir nicht wissen" – ein bewusster Bruch mit der Erwartung, dass jeder Artikel alle Fragen beantwortet.

---

## Teil 5: Anti-KI-Checkliste

Der Sub-Agent prüft NACH dem Schreiben jedes Artikels:

```
STRUKTUR-CHECK
[ ] Weicht die Abschnittszahl vom letzten Artikel ab?
[ ] Gibt es mindestens einen Absatz mit nur 1-2 Sätzen?
[ ] Gibt es mindestens einen Absatz mit 5+ Sätzen?
[ ] Sind die Abschnitte unterschiedlich lang (nicht symmetrisch)?
[ ] Enthält der Artikel maximal eine formatierte Liste?

SPRACH-CHECK
[ ] Beginnen weniger als 30% der Sätze mit demselben Wort?
[ ] Kommen die Wörter „wichtig", „entscheidend", „zentral" zusammen weniger als 3× vor?
[ ] Gibt es mindestens einen Satz unter 8 Wörtern?
[ ] Gibt es keinen Absatz, der mit „Es ist" oder „Es gibt" beginnt?
[ ] Wurden keine Plastikphrasen verwendet? (Writing Style §3)

MUSTER-CHECK
[ ] Unterscheidet sich die Eröffnung vom letzten Artikel?
[ ] Unterscheidet sich der Abschluss vom letzten Artikel?
[ ] Ist die gewählte Variante eine andere als beim letzten Artikel?
[ ] Würde ein Leser, der die letzten 3 Artikel kennt, diesen als
    strukturell anders wahrnehmen?
```

Wenn ein Punkt nicht erfüllt ist: Überarbeiten, bevor der Artikel das Quality Gate erreicht.

---

## Teil 6: Übergabe-Format an den Sub-Agent

Der Sub-Agent erhält vom Orchestrator:

```yaml
content_core: [Pfad zum ausgefüllten Content Core]
kategorie: ki-fuehrung | quick-checks | kritisches-denken
letzte_variante: A | B | C | D | E | null
letzter_eröffnungstyp: substantiv-kette | szenario | zitat | statistik | null
letzter_abschlusstyp: aphorismus | frage | appell | humor | null
wortanzahl_ziel: 800-1200
writing_style: [Pfad zum Writing Style Skill]
quality_gates: [Pfad zu den Quality Gates]
```

Der Sub-Agent antwortet mit:

```yaml
gewählte_variante: [A-E mit Begründung]
gewählter_eröffnungstyp: [...]
gewählter_abschlusstyp: [...]
artikel: [Der fertige Artikel in Markdown]
anti_ki_check: [Ergebnis der Anti-KI-Checkliste]
wortanzahl: [tatsächlich]
```

---

## Teil 7: SEO-Metadaten (Pflicht bei jedem Artikel)

Der Sub-Agent liefert zu jedem Artikel mit:

```
seo_titel: [50-60 Zeichen, Hauptkeyword vorn, Nutzenversprechen]
excerpt: [150-160 Zeichen, Neugier wecken, Keyword enthalten, NICHT identisch mit TL;DR]
tags: [3-5 aus dem Content Core]
featured_image: TODO
```

**Titel-Regeln:**
- Der SEO-Titel darf vom H1-Titel des Artikels abweichen
- Hauptkeyword in den ersten 3 Wörtern
- Kein Clickbait, aber ein klares Nutzenversprechen

---

*Dieses Dokument arbeitet zusammen mit:*
*→ `content-core-template.md` – Was und für wen*
*→ `writing-style.md` – Wie und in welchem Ton*
*→ `quality-gates.md` – Qualitätssicherung nach dem Schreiben*
