# Wanderer und Träumende Götter
## Design- und Entwicklungsdokument
**Version 1.18 · Entwurf**

### 1. Grundkonzept

Ein kooperatives Geschichtenspiel mit logopädischen Anteilen. Die Spieler übernehmen die Rolle der **Traumkinder** und helfen Wanderern, die nach dem Fall durch ein Loch eine fremde Welt durchqueren und zum nächsten Heimkehrloch gelangen wollen.

**Leitlinien:**

- **Sprache als Handlung:** Worte schaffen Möglichkeiten; die Wanderer müssen selbst handeln.
- **Offene Erzählwelt:** Orte, Aufgaben und Wörter sind möglichst frei kombinierbar.
- **Klare Sprachkerne:** Leicht verständliche Zielwörter und kurze, einprägsame Phrasen.
- **Kontrollierte Mehrdeutigkeit:** Bilder erklären das Zielwort eindeutig, lassen die Geschichte offen.
- **Balance:** Alle Wortkarten sollen brauchbar sein, keine darf nahezu jedes Problem allein lösen.
- **Skalierbarkeit:** Vom Einwort-Lösen ohne Punkte bis zur taktischen Reise mit Ressourcenplanung.
- **Gedächtnisstützen:** Besuchte Orte und gelöste Aufgaben dienen der Rekapitulation.

### 2. Sprachliche Konzeption

#### 2.1 Zielbereiche

| Bereich | Schwerpunkte |
|---|---|
| **Lexikalisch-semantisch** | Wortschatz, Abruf, Bedeutungsmerkmale, Funktionen, Begriffsbeziehungen |
| **Grammatisch** | Nominal- und Verbalphrasen, Satzbildung, Erweiterung, Verknüpfung |
| **Narrativ** | Ereignisfolge, Ursache und Wirkung, zusammenhängendes Erzählen, Nacherzählen |
| **Pragmatisch** | Vorschläge machen, Zusammenarbeiten, Erklären, Begründen, Perspektivwechsel |

#### 2.2 Wortauswahl

**Schwerpunkt:** Häufige, möglichst früh erworbene Alltagswörter. Ein gewisser Anteil **niederfrequenter Wörter** ist erwünscht, wenn sie bildlich und spielerisch sinnvoll sind. Es gilt keine starre Quote.

- **Nomen:** konkrete Gegenstände mit unterscheidbaren Eigenschaften und mehreren plausiblen Verwendungen.
- **Verben:** häufige, handlungsbezogene Wörter, beispielsweise *gehen, machen, geben, nehmen, holen, bringen, tragen, suchen, helfen*.
- **Adjektive:** charakteristische, gut unterscheidbare Eigenschaften wie *groß/klein, schnell/langsam, heiß/kalt, hart/weich*.

**Prüfkriterien:** Gebrauchshäufigkeit, früher Erwerb, semantische Klarheit, Bildbarkeit, Differenzierbarkeit, Kombinierbarkeit und Handlungsrelevanz. Häufigkeit und Erwerbsalter der endgültigen Karten sind noch anhand geeigneter Quellen zu überprüfen.

Ortskarten sollen **typische Eigenschaften des Ortes selbst** zeigen: *Wald – dunkel* statt *Baum – hoch*. Das Nomen kann ein charakteristisches Material oder Objekt des Ortes sein.

#### 2.3 Sprachliche Staffelung

| Stufe | Beispiel / Ziel |
|---|---|
| **Einzelwort** | Mit nur einer Aufgabenkarte „löschen“ als Handlung benennen |
| **Wortgruppe** | „mit dem Eimer“ |
| **Satz** | „Jonas trägt Sand.“ |
| **Erzählung** | Ereignisse sinnvoll verbinden und begründen |
| **Strategie** | Wortvorrat planen, Kleinode klug erklären und einsetzen |

Die Grundkarten sollen **mehrere naheliegende Vorschläge-Verben je Aufgabe und Gegenstand** ermöglichen, bevorzugt auch solche aus den ersten Spracherwerbsjahren. Sprachliche und spielmechanische Schwierigkeit sind getrennt einstellbar.

### 3. Kartensystem

| Typ | Präfix | Sprachlicher Kern | Aufgabe im Spiel |
|---|---|---|---|
| **Ort / Environment** | `e` | Ort mit Nomen und ortstypischem Adjektiv | Kontext und nutzbare Umgebung |
| **Aufgabe – Gefahr** | `ag` | Nomen + Verb | Gefahr bewältigen |
| **Aufgabe – Sozial** | `as` | Nomen + Verb | Helfen und Versorgen |
| **Aufgabe – Technisch** | `at` | Nomen + Verb | Defekt oder Bauproblem |
| **Aufgabe – Hindernis** | `ah` | Nomen + Verb | Zugang oder Weg ermöglichen |
| **Wort – Nomen** | `wn` | Gegenstand | Den Wanderern ein Objekt schenken |
| **Wort – Adjektiv** | `wa` | Eigenschaft | Einen Wanderer mit Eigenschaft ausstatten |
| **Figur** | `f` | Name | Optionaler neutraler Handlungsträger |

**`ax`** bezeichnet die Aufgabenkarten zusammengefasst. Die IDs sind klein geschrieben und zweistellig nummeriert: `e01`, `ag01`, `wn01` usw. **Kleinode** sind feste Symbole auf Aufgabenkarten; **Lösungen** sind keine Karten.

Die maschinenlesbaren Kartendaten stehen in je einer gemeinsamen TSV-Datei pro übergeordneter Kartengruppe: `liste-ort.tsv`, `liste-aufgabe.tsv`, `liste-wort.tsv` und `liste-figur.tsv`. Alle Listen verwenden dieselbe Produktionsstruktur: Auf `anzahl`, `id` und `punkte` folgen die gruppenspezifischen Inhaltsfelder und `format_text`; anschließend stehen `img`, `ai`, eine leere Trennspalte und die Metadaten `subtyp`, `bildmotiv`, `frequenz`, `komplexität` und `spezifität`. Die universelle Spalte `vorschläge-verben` bildet den Abschluss.

Bei Aufgaben stehen nach `phrase` unmittelbar `wort_1`, `wort_2` und `kleinod`; bei Orten folgen auf `ort` und `phrase` die beiden Zielwörter. Figuren behalten `name` und `faehigkeiten`, Wörter das Feld `wort`. Visuelle Beschreibungen stehen unabhängig von der Kartengruppe in `bildmotiv`, Verbideen ausschließlich in `vorschläge-verben`.

`format_text` enthält den sichtbaren Karteninhalt in CardMakers `FormattedText`-Syntax. Zielwörter werden semantisch einheitlich farbig hervorgehoben; die Karte selbst bleibt auch ohne Bild lesbar. Das CardMaker-Projekt besitzt je Kartentyp genau ein Layout und wird über einen Modusschalter entweder als helle A4-Papierfassung mit Schnittmarken oder als Bridge-Printkarte mit Bild beziehungsweise heller Schrift auf Schwarz erzeugt.

Die Bewertungsfelder verwenden vorläufig eine Skala von 1 bis 5. Bei `frequenz` bedeutet 1 hochfrequent und 5 selten, bei `komplexität` bedeutet 1 sehr einfach und 5 hochkomplex, bei `spezifität` bedeutet 1 breit einsetzbar und 5 stark spezifisch. Sie unterstützen Materialauswahl und Balance, ersetzen aber keine spätere empirische Prüfung. Details und aktuelle Werte stehen in `cards/info-listen.md`.

#### 3.1 Orte

Ortskarten führen die Umgebung und ihre typischen Materialien/Eigenschaften ein. Die Phrase ist kurz und soll ein **charakteristisches Adjektiv für den Ort** verwenden, nicht bloß für irgendein Objekt darin. Ortsmaterialien dürfen später Teil einer Lösung werden. Dieselbe Aufgabenkarte soll in unterschiedlichen Orten funktionieren.

#### 3.2 Aufgaben

Vier Kategorien: **Sozial, Gefahr, Technisch, Hindernis**. Eine Aufgabenkarte zeigt nur ein knappes Kernereignis mit zwei Zielwörtern und festem Kleinod-Symbol. **Ort, Ursache, Verlauf und Lösung bleiben offen**; mehrere Aufgaben dürfen sich zu einer Handlung verbinden.

#### 3.3 Vorschläge-Verben

Jede Aufgabe und jede passende Wortkarte kann eine Liste möglicher **Vorschläge-Verben** erhalten, geordnet nach vorläufig geschätzter Naheliegenheit. Gesucht werden insbesondere **konkrete, bildlich vermittelbare und durch Wortkarten unterstützbare Handlungen** statt unspezifischer Sammelverben.

Beispiele:

- *Ein Haus brennt!*: löschen, abkühlen, retten, schützen.
- *Ein Dieb klaut Geld!*: greifen (Greifer), erschrecken (Maske, laut), fangen (Netz), finden (Lupe), verfolgen (schnell), stehlen (leise).
- *Eimer*: füllen, tragen, schütten, holen, löschen.

Diese Verben und Klammerbeispiele sind **Hypothesen für Materialentwicklung und gegebenenfalls Spielleitung**, keine Musterlösungen oder bereits beschlossenen Wortkarten. Die Reihenfolge ist nicht empirisch gemessen. Kreative, plausible Alternativen bleiben offen.

### 4. Mechanik und Balance

#### 4.1 Wortmagie und Wirkungsdauer

Nomen geben einem Wanderer einen Gegenstand; Adjektive verleihen einem Wanderer eine Eigenschaft. Die Magie **wirkt nicht unmittelbar auf das Problem**. Die Wanderer müssen Gegenstände und Fähigkeiten sinnvoll einsetzen, um beispielsweise ein Feuer zu löschen oder einen Dieb zu fangen.

Wirkungen gelten für **die gesamte Station mit allen Aufgaben**. Verwendete Wortkarten werden **nach der Station verbraucht**. Die passende Zahl an Karten ist noch zu erproben.

#### 4.2 Verteilung und Prototypbestand

Der erste Prototyp enthält **12 Nomen- und 12 Adjektiv-Wortkarten**. Die Kennungen sind nach Wortart getrennt, der Spielstapel muss es nicht sein.

- Offene gemeinsame Karten (z. B. drei je Aufgabe)
- Verdeckte Spielerhände (z. B. zwei je Spieler)
- Größerer, begrenzter Reisevorrat ohne Nachziehen

Wie viele Karten pro Gruppe, Spieler, Aufgabe und Schwierigkeit sinnvoll sind, muss getestet werden.

#### 4.3 Spielbalance

Gegenstände und Eigenschaften sollen **valide und nützlich**, aber nicht universell sein. Das Material soll mehrere klar verschiedene Wege pro Aufgabe zulassen.

| Prüfung | Erwünscht | Vermeiden |
|---|---|---|
| **Wortkarte** | Mehrere plausible Verwendungen | Universallösung oder praktisch nutzlose Karte |
| **Adjektiv** | Klare begrenzte Wirkung | Beliebig mächtige Eigenschaft |
| **Lösungsverb** | Konkrete, gut erklärbare Handlung | Bloßes „machen“ ohne klare Handlung |
| **Aufgabe** | Verschiedene Lösungswege | Nur ein passender Gegenstand |
| **Kartensatz** | Vielfältige Kombinationen | Einzelne Wörter dominieren fast alles |

Für 24 Wortkarten × 16 Aufgabenkarten wird im Prototyp eine **qualitative Kompatibilitätsprüfung** empfohlen: **gut / möglich / kaum**. „Gut“ bedeutet naheliegende Verwendung, nicht automatische Lösung. Die Verteilung muss **nicht künstlich identisch** sein; wichtig ist eine insgesamt ausgewogene Auswahl. Ergebnisse sind noch nicht erhoben.

#### 4.4 Optionale Wortkartenpunkte

Wortkarten können nach der Schwierigkeit eines **sinnvollen Einsatzes**, nicht nach ihrer magischen Stärke oder bloßen Seltenheit, bewertet werden:

| Punkte | Charakter | Beispiele |
|---|---|---|
| **1** | Universell oder leicht zu begründen | schnell, stark |
| **2** | Vielseitig, aber mit etwas Planung | Eimer, Seil |
| **3** | Spezifisch, situationsabhängig und erklärungsbedürftiger | Lupe, Kompass |

**Festgelegte vorläufige Werte:** Eimer = **2**, Seil = **2**, schnell = **1**, kalt = **1**, Lupe als Kandidat = **3**. Ob der Punktwert auf Karten gedruckt wird, bleibt offen.

#### 4.5 Kleinode

Kleinode sind **feste Symbole auf den Aufgabenkarten** und dürfen nach Gewinn mehrfach als schwache Hilfsmittel verwendet werden. Ihr gewöhnlicher Zweck begrenzt die Wirksamkeit. Ein besonders geschickter Einsatz kann dennoch eine größere Aufgabe bewältigen. Optional kann die Nutzung über das zeitweilige Abdecken/Umdrehen der Aufgabenkarte eingeschränkt werden; genaue Sperrdauer offen.

#### 4.6 Optionale Punktewertung

Das frühere Schema **1 Punkt gelöst / 2 geschickt / 3 originell** ist **gestrichen**. Stattdessen gelten in den Varianten mit Wertung:

| Wert | Ereignis |
|---|---|
| **1–3 Punkte** | Eine Wortkarte wird erfolgreich zur Lösung eingesetzt, gemäß Kartenwert |
| **1 Punkt** | Ein bereits gewonnenes Kleinod wird erfolgreich zur Lösung eingesetzt |
| **+1 Bonuspunkt** | Eine Aufgabe wird besonders originell gelöst, **unabhängig** vom eingesetzten Material; höchstens einmal je Aufgabe |
| **+1 Punkt pro Karte** | Nur bei **schwer/taktisch** am Reiseende für jede verbleibende, ungenutzte Wortkarte |

**Kein Punkt allein für den Erwerb** eines Kleinods. Wortkarten- und Kleinodpunkte können innerhalb einer Aufgabe **addiert** werden; der Originalitätsbonus ist zusätzlich.

**Beispiel: 4 Punkte** für eine Falle, in die der Dieb mithilfe einer bereits gewonnenen Münze und eines magisch geschaffenen Seils gelockt wird: Münze 1 + Seil 2 + originelle Lösung 1. Eine **Lupe als Brennglas** kann als sehr originelle 3-Punkte-Wortkartenlösung ebenfalls 4 Punkte ergeben (3 + 1).

Eine Wortkarte kann magisch für mehrere Aufgaben derselben Station wirken. **Ob und wie häufig dieselbe Karte dabei erneut punktet, ist noch zu erproben**; als einfache Vorabregel nur einmal pro Karte und Station werten. Kleinode dürfen bei späteren Aufgaben erneut eingesetzt werden und dabei wieder einen Punkt einbringen.

#### 4.7 Entscheidung über Lösungen

Entweder **gemeinsame Abstimmung** oder eine **Spielleitung**, die ähnlich einer Pen-and-Paper-Runde Hindernisse auswählt und Lösungen beurteilt. Vorab festgelegte Vorschläge-Verben sind Hilfen für die Entwicklung, keine Pflichtantworten. Der Bonus soll originelle, plausible Handlungen fördern.

### 5. Spielwelt und Schwierigkeit

Die Traumkinder kennen als Einzige das nächste Heimkehrloch und weisen den Wanderern den Weg. **Neugier aufeinander, Entdeckung einer fremden Kultur und der Wunsch nach Heimkehr** tragen die Erzählung.

Regelumfang: etwa **3–5 Stationen** und **1–3 Aufgabenkarten pro Station**. Der leichteste Einstieg darf ausschließlich Aufgabenkarten verwenden.

#### 5.1 Schwierigkeitsmatrix (Wortauswahl ausgenommen)

| Mechanik | **Leicht** | **Mittel** | **Schwer / taktisch** |
|---|---|---|---|
| **Umfang** | Nur Aufgabenkarten, optional ca. 3 Stationen | Ca. 3–4 Stationen | Ca. 5 Stationen |
| **Aufgaben pro Station** | 1 | 1–2 | 2–3 |
| **Wortkartenverteilung** | Offen und gemeinsam, sofern genutzt | Gemeinsam oder verdeckte Spielerhände | Begrenzter Reisevorrat |
| **Nachziehen** | Nach jeder Aufgabe möglich | Vereinbartes Nachziehen | Kein Nachziehen |
| **Sprache** | Einwortlösung und kurze Aussagen | Sätze und begründete Verknüpfungen | Mehrstufige Planung und längere Begründung |
| **Kleinode** | Frei verwendbar | Frei verwendbar | Optional vorübergehend sperrbar |
| **Punkte** | Keine | Kartenpunkte + Originalitätsbonus | Wie Mittel + Restkartenpunkte |
| **Entscheidung** | Gemeinsam mit Hilfe | Abstimmung oder Spielleitung | Spielleitung oder taktische Abstimmung |
| **Ende** | Kurzer Rückblick | Nacherzählen | Nacherzählen + Schlusswertung |

Die Stufen sind **vorläufige Testkonfigurationen**. Sprache, Alter, Kartenverteilung und Aufgabenmenge können individuell kombiniert werden.

### 6. Grafisches Design

#### 6.1 Stil

**Einfach, zeichnerisch, farbig, symbolisch.** Klare Umrisse, kräftige unterscheidbare Farben, wenige Details, erkennbare Bewegungen. Nicht benötigte Bildelemente weglassen.

**Kontrollierte Mehrdeutigkeit:** Das Zielwort bleibt eindeutig, während Ort und Ursache der Aufgabe sowie mögliche Lösungen nicht vorweggenommen werden.

| Element | Visuelle Leitidee |
|---|---|
| **Wüste** | Düne und Fußspuren, Sand und Hitze |
| **Wald** | Dichtes, dunkles Waldmotiv |
| **Haus brennt** | Brennendes Fenster statt vollständig festgelegter Szene |
| **Eimer** | Klar umrissener einfacher Gegenstand |
| **Schnell** | Cartoon-Luftwirbel oder Bewegungsstreifen |
| **Kleinod** | Kleines prägnantes Symbol auf der Aufgabenkarte |
| **Figur** | Einfacher Wanderer ohne Beruf oder vorgegebene Spezialfähigkeit |

#### 6.2 Kartenlayout

- **Ort:** Name, Bild, kurze Phrase mit zwei hervorgehobenen Zielwörtern.
- **Aufgabe:** Phrase, Kernereignis, Kategorienkennzeichnung, festes Kleinod-Symbol.
- **Wort:** Großes Bild, Begriff, gegebenenfalls Artikel/Wortart und **optional** Punktwert.
- **Figur:** Name und einfache Personendarstellung.

Farbsystem, Kartengröße und Schriftarten sind noch offen.

### 7. Offene Entwicklungsfragen

| Bereich | Noch zu erproben/klären |
|---|---|
| **Kartenanzahl** | Anzahl pro Aufgabe, Hand und Reise; Nachziehregeln |
| **Balance** | Wirksamkeit jeder Wortkarte gegen alle 16 Prototypaufgaben |
| **Punkte** | Karteneinstufung, Wertung mehrmaliger Verwendung innerhalb derselben Station, möglicher Aufdruck |
| **Kleinode** | Dauer einer optionalen Nutzungssperre |
| **Sprachliche Eignung** | Häufigkeit, Erwerbsalter, Verständlichkeit, Verbvielfalt |
| **Bewertung** | Kriterien für originelle Lösungen und Verfahren der Spielleitung |
| **Design** | Maße, Farben, Typografie und Symbolverständlichkeit |

**Das vollständige konkrete Karteninventar steht ausschließlich im separat versionierten Dokument `material_wnd.md` und den zugehörigen TSV-Dateien.**

**Ende des Designdokuments – v1.18**
