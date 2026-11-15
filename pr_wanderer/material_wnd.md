# Wanderer und Träumende Götter
## Material
**Version 1.05 · Konkreter Kartenbestand und Prototypplanung**

Das Materialdokument erfasst **tatsächlich konkretisierte Karten** und getrennt davon **Kandidaten**. Es ersetzt die Materialtabellen im Designdokument.

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

Die maschinenlesbaren Daten stehen in je einer gemeinsamen TSV-Datei pro Kartengruppe: `cards/ort/liste-orte.tsv`, `cards/aufgabe/liste-aufgaben.tsv`, `cards/wort/liste-wörter.tsv` und `cards/figur/liste-figuren.tsv`. In jeder Kartenliste sind `anzahl` und `subtyp` die ersten beiden Spalten; jede konkretisierte Karte hat derzeit die Stückzahl `1`. Die optionalen Felder `bild_png` und `bild_ai` bleiben leer, solange keine entsprechende Datei vorhanden ist. Wortkandidaten ohne ID werden getrennt in `cards/wort/liste-wörter-kandidaten.tsv` geführt.

### 2. Ortskarten (e)

| ID | Ort | Phrase | Wort 1 | Wort 2 |
|---|---|---|---|---|
| `e01` | Wüste | „In der Wüste ist der Sand heiß.“ | Sand | heiß |
| `e02` | Wald | „Im Wald ist es dunkel. Überall stehen Bäume.“ | Baum | dunkel |

**Zielmenge: 6.** Weitere Karten offen. Das Adjektiv soll **typisch für den Ort selbst** sein, nicht bloß für ein dortiges Objekt.

### 3. Aufgabenkarten (ax)

Alle Aufgaben besitzen eine **Art/Kategorie, Phrase, zwei Zielwörter, ein festes Kleinod-Symbol** und eine Liste **antizipierter Lösungsverben**. Die Lösungsverben sind qualitativ nach vermuteter Naheliegenheit geordnet, **nicht** empirisch getestet. Sie sind weder Pflichtlösungen noch Wortkarten.

#### 3.1 Gefahr (ag)

| ID | Phrase | Wort 1 | Wort 2 | Kleinod | Lösungsverben |
|---|---|---|---|---|---|
| `ag01` | „Ein Haus brennt.“ | Haus | brennen | Schlüsselanhänger | löschen, abkühlen, retten, schützen |
| `ag02` | „Ein Dieb klaut Geld.“ | Dieb | klauen | Münze | greifen, erschrecken, fangen, finden, verfolgen, stehlen |

Zur Materialprüfung für `ag02` mögliche Verknüpfungen: **greifen – Greifer; erschrecken – Maske oder laut; fangen – Netz; finden – Lupe; verfolgen – schnell; stehlen – leise**. Nicht alle genannten Wörter sind bereits in den Prototyp aufgenommen.

#### 3.2 Sozial (as)

| ID | Phrase | Wort 1 | Wort 2 | Kleinod | Lösungsverben |
|---|---|---|---|---|---|
| *noch offen* | – | – | – | – | – |

#### 3.3 Technisch (at)

| ID | Phrase | Wort 1 | Wort 2 | Kleinod | Lösungsverben |
|---|---|---|---|---|---|
| *noch offen* | – | – | – | – | – |

#### 3.4 Hindernis (ah)

| ID | Phrase | Wort 1 | Wort 2 | Kleinod | Lösungsverben |
|---|---|---|---|---|---|
| *noch offen* | – | – | – | – | – |

**Zielmenge: 16 Aufgabenkarten**, vorläufig je vier in jeder der vier Kategorien. **Kleinode sind keine eigenen Karten.** Das auf einer Aufgabenkarte abgebildete Kleinod wird bei erfolgreicher Lösung gewonnen, ohne dafür sofort einen Punkt zu erhalten.

### 4. Wortkarten – Nomen (wn)

| ID | Wort | Artikel | Bildmotiv | Mögliche Handlungsverben | Punkte |
|---|---|---|---|---|---:|
| `wn01` | Eimer | der | Einfacher Eimer | füllen, tragen, schütten, holen, löschen | **2** |
| `wn02` | Seil | das | Aufgerolltes Seil | ziehen, halten, binden, verbinden | **2** |

**Zielmenge: 12 Nomenkarten.** Die Handlungsverben sind typische Verwendungen, keine zusätzlichen Regeln.

#### Weitere Kandidaten (noch keine Karten-ID)

| Wort | Mögliche Verwendung | Vorgesehene Punkte | Status |
|---|---|---:|---|
| Lupe | suchen, finden, untersuchen; als Brennglas mit besonderer Begründung | **3** | Kandidat |
| Kompass | orientieren, finden | **3** | Kandidat |
| Greifer | greifen, festhalten | offen | Kandidat aus Aufgabenprüfung |
| Maske | verkleiden, erschrecken | offen | Kandidat aus Aufgabenprüfung |
| Netz | fangen, abdecken | offen | Kandidat aus Aufgabenprüfung |

Diese Kandidaten sind **nicht** in den Zählungen der konkretisierten Karten enthalten.

### 5. Wortkarten – Adjektive (wa)

| ID | Wort | Bildmotiv | Punkte |
|---|---|---|---:|
| `wa01` | schnell | Luftwirbel, Bewegungsstreifen | **1** |
| `wa02` | kalt | Eiskristalle | offen |

**Zielmenge: 12 Adjektivkarten.** Die Wörter *laut* und *leise* sind bisher nur Kombinationskandidaten und noch keine konkretisierten Karten.

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
| **1** | Leicht und vielseitig | `wa01` schnell |
| **2** | Mittlere Anforderung | `wn01` Eimer; `wn02` Seil |
| **3** | Spezifisch, erklärungsbedürftig | Lupe und Kompass (noch Kandidaten) |

Ob der Punktwert **mitgedruckt** wird, ist offen. Die Einordnung muss anhand der Aufgabe-Wort-Kombinationen geprüft werden. Gegenstände sollen weder nahezu alles lösen noch nutzlos sein.

**Kleinode:** Kein Punkt für den Erwerb; **1 Punkt** für eine erfolgreiche Verwendung zur Lösung, auch bei erneuter Verwendung in einer späteren Aufgabe. Die **+1 Bonuspunkt** für eine besonders originelle Aufgabenlösung ist **nicht an Kleinode gebunden**. In der **taktischen** Variante erhält jede am Ende verbliebene, unverbrauchte Wortkarte **1 Punkt**.

Die Punktewertung ist optional: **leicht ohne Punkte, mittel mit Kartenpunkten und Originalitätsbonus, schwer zusätzlich mit Restkartenwertung**. Sie wird im Design- und Anleitungsdokument geregelt und hier für die Materialwerte zusammengefasst.

**Ende Material – v1.05**
