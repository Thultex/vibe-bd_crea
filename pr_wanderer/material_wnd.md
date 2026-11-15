# Wanderer und Träumende Götter
## Material
**Version 1.12 · Konkreter Kartenbestand und Prototypplanung**

Das Materialdokument erfasst **tatsächlich konkretisierte Karten**. Noch nicht konkretisierte Ideen aller Kartenarten stehen getrennt in `cards/liste-ideen.md`. Es ersetzt die Materialtabellen im Designdokument.

### 1. Kennungen

| Material | Präfix |
|---|---|
| Ortskarten (Environment) | `e` |
| Aufgaben – Gefahr | `ag` |
| Aufgaben – Sozial | `as` |
| Aufgaben – Technisch | `at` |
| Aufgaben – Hindernis | `ah` |
| Aufgabenkarten gesamt | `ax` (nur Sammelbezeichnung) |
| Wortkarten – Nomen | `wn` |
| Wortkarten – Adjektive | `wa` |
| Figuren | `f` |

Kennungen sind **kleingeschrieben** und je Kategorie ab `01` zweistellig nummeriert, etwa `e01`, `ag01`, `wa02`.

Die maschinenlesbaren Daten stehen in je einer gemeinsamen TSV-Datei pro Kartengruppe: `cards/ort/liste-ort.tsv`, `cards/aufgabe/liste-aufgabe.tsv`, `cards/wort/liste-wort.tsv` und `cards/figur/liste-figur.tsv`. Auf Stückzahl, ID und Punkte folgen die gruppenspezifischen Inhaltsfelder samt den Ausgangsfarben `col1`, `col2` usw., anschließend Bildpfade, eine leere Trennspalte und die Metadaten Subtyp, Bildmotiv sowie `frequenz`, `komplexität` und `spezifität`. Bei Orten und Aufgaben stehen die Zielwörter vor `phrase` und `phrase_story`. `phrase` enthält die Minimalphrase; `phrase_story` ist für den vollständigen Erzähltext vorgesehen und bleibt bis zu dessen Festlegung leer. CardMaker kann zentral zwischen beiden Fassungen wechseln und verwendet bei leerer Story die Minimalphrase. Verbideen werden universell in der letzten Spalte `vorschläge-verben` geführt. Alle Ideen ohne ID stehen gemeinsam in `cards/liste-ideen.md`.

Die drei Bewertungsfelder verwenden vorläufig Werte von 1 bis 5: `frequenz` reicht von hochfrequent bis selten, `komplexität` von sehr einfach bis hochkomplex und `spezifität` von breit einsetzbar bis stark spezifisch. Die Einordnungen sind Materialhypothesen und später empirisch zu prüfen. Ermittlungsgrundlage und aktuelle Werte des gesamten Kartenmaterials stehen in `cards/info-listen.md`.

### 2. Ortskarten (e)

| ID | Ort | Wort 1 | Wort 2 | Minimalphrase | Storytext |
|---|---|---|---|---|---|
| `e01` | Wüste | Sand | heiß | „In der Wüste ist der Sand heiß.“ | – |
| `e02` | Wald | Baum | dunkel | „Im Wald ist es dunkel. Überall stehen Bäume.“ | – |

**Zielmenge: 6.** Weitere Karten offen. Das Adjektiv soll **typisch für den Ort selbst** sein, nicht bloß für ein dortiges Objekt.

### 3. Aufgabenkarten (ax)

Alle Aufgaben besitzen eine **Art/Kategorie, zwei Zielwörter, eine Minimalphrase, ein optionales Storytextfeld, ein festes Kleinod-Symbol** und eine Liste **antizipierter Vorschläge-Verben**. Die Vorschläge-Verben sind qualitativ nach vermuteter Naheliegenheit geordnet, **nicht** empirisch getestet. Sie sind weder Pflichtlösungen noch Wortkarten.

#### 3.1 Gefahr (ag)

| ID | Wort 1 | Wort 2 | Minimalphrase | Storytext | Kleinod | Vorschläge-Verben |
|---|---|---|---|---|---|---|
| `ag01` | Haus | brennen | „Ein Haus brennt!“ | – | Schlüsselanhänger | löschen, abkühlen, retten, schützen |
| `ag02` | Dieb | klauen | „Ein Dieb klaut Geld!“ | – | Münze | greifen, erschrecken, fangen, finden, verfolgen, stehlen |

Zur Materialprüfung für `ag02` mögliche Verknüpfungen: **greifen – Greifer; erschrecken – Maske oder laut; fangen – Netz; finden – Lupe; verfolgen – schnell; stehlen – leise**. Nicht alle genannten Wörter sind bereits in den Prototyp aufgenommen.

#### 3.2 Sozial (as)

| ID | Wort 1 | Wort 2 | Minimalphrase | Storytext | Kleinod | Vorschläge-Verben |
|---|---|---|---|---|---|---|
| *noch offen* | – | – | – | – | – | – |

#### 3.3 Technisch (at)

| ID | Wort 1 | Wort 2 | Minimalphrase | Storytext | Kleinod | Vorschläge-Verben |
|---|---|---|---|---|---|---|
| *noch offen* | – | – | – | – | – | – |

#### 3.4 Hindernis (ah)

| ID | Wort 1 | Wort 2 | Minimalphrase | Storytext | Kleinod | Vorschläge-Verben |
|---|---|---|---|---|---|---|
| *noch offen* | – | – | – | – | – | – |

**Zielmenge: 16 Aufgabenkarten**, vorläufig je vier in jeder der vier Kategorien. **Kleinode sind keine eigenen Karten.** Das auf einer Aufgabenkarte abgebildete Kleinod wird bei erfolgreicher Lösung gewonnen, ohne dafür sofort einen Punkt zu erhalten.

### 4. Wortkarten – Nomen (wn)

| ID | Wort | Artikel | Bildmotiv | Vorschläge-Verben | Punkte |
|---|---|---|---|---|---:|
| `wn01` | Eimer | der | Einfacher Eimer | füllen, tragen, schütten, holen, löschen | **2** |
| `wn02` | Seil | das | Aufgerolltes Seil | ziehen, halten, binden, verbinden | **2** |

**Zielmenge: 12 Nomenkarten.** Die Vorschläge-Verben sind typische Verwendungen, keine zusätzlichen Regeln.

Sämtliche noch nicht konkretisierten Ideen stehen ausschließlich in der gemeinsamen `cards/liste-ideen.md` und sind **nicht** in den Zählungen der konkretisierten Karten enthalten.

### 5. Wortkarten – Adjektive (wa)

| ID | Wort | Bildmotiv | Vorschläge-Verben | Punkte |
|---|---|---|---|---:|
| `wa01` | schnell | Luftwirbel | laufen, ausweichen | **1** |
| `wa02` | kalt | Eiskristalle | einfrieren, kühlen, erstarren | **1** |

**Zielmenge: 12 Adjektivkarten.** Die Wörter *laut* und *leise* bleiben Kombinationskandidaten ohne Karten-ID und stehen zusammen mit allen anderen Ideen in `cards/liste-ideen.md`.

### 6. Figurenkarten (f, optional)

| ID | Name | Darstellung | Fähigkeiten |
|---|---|---|---|
| `f01` | Jonas | offen | keine festgelegten |
| `f02` | Mira | offen | keine festgelegten |

**Zielmenge: 4**, optional. Keine festen Spezialberufe oder Startkräfte; Eigenschaften entstehen über die Wortmagie.

### 7. Sonstiges Material

| Material | Zweck | Stand |
|---|---|---|
| Startkarte „Das Loch“ | Beginn des Falls in die fremde Welt | Konzept |
| Reiseauslage | Sichtbare Anordnung der Orts- und Aufgabenkarten | Noch offen |

### 8. Umfang des ersten Prototyps

| Material | Zielmenge | Konkretisiert |
|---|---:|---:|
| Ortskarten (`e`) | 6 | 2 |
| Aufgabenkarten (`ax`) | 16 | 2 |
| Wortkarten – Nomen (`wn`) | 12 | 2 |
| Wortkarten – Adjektive (`wa`) | 12 | 2 |
| Figuren (`f`, optional) | 4 | 2 |
| Startkarte | 1 | Konzept |
| **Gesamt** | **51** | **10 Karten + Startkonzept** |

Der erste Prototyp sieht **gleich viele Nomen- und Adjektivkarten** vor. Die Zielmengen sind vorläufig.

### 9. Punkte und Materialbalance

Die Punkte auf Wortkarten beschreiben die angenommene **Schwierigkeit eines sinnvollen Einsatzes**:

| Punkte | Bedeutung | Materialbeispiele |
|---|---|---|
| **1** | Leicht und vielseitig | `wa01` schnell; `wa02` kalt |
| **2** | Mittlere Anforderung | `wn01` Eimer; `wn02` Seil |
| **3** | Spezifisch, erklärungsbedürftig | Lupe und Kompass (noch Kandidaten) |

Ob der Punktwert **mitgedruckt** wird, ist offen. Die Einordnung muss anhand der Aufgabe-Wort-Kombinationen geprüft werden. Gegenstände sollen weder nahezu alles lösen noch nutzlos sein.

**Kleinode:** Kein Punkt für den Erwerb; **1 Punkt** für eine erfolgreiche Verwendung zur Lösung, auch bei erneuter Verwendung in einer späteren Aufgabe. Die **+1 Bonuspunkt** für eine besonders originelle Aufgabenlösung ist **nicht an Kleinode gebunden**. In der **taktischen** Variante erhält jede am Ende verbliebene, unverbrauchte Wortkarte **1 Punkt**.

Die Punktewertung ist optional: **leicht ohne Punkte, mittel mit Kartenpunkten und Originalitätsbonus, schwer zusätzlich mit Restkartenwertung**. Sie wird im Design- und Anleitungsdokument geregelt und hier für die Materialwerte zusammengefasst.

**Ende Material – v1.09**
