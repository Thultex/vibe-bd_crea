# Changelog Ruckpacken

## Stats

Ausgangsdatum: 2026-07-12

*Diese Woche (ca. 1,5h, 2 Tage, Inhalte):* Projektgrundlage eingebracht und Kartengenerator auf MPC-Jumboformat umgestellt.

*Letzte Woche (0h, 0 Tage, Inhalte):* Keine Einträge.

*Dieser Monat (ca. 1,5h, 2 Tage, Inhalte):* Ruckpacken-Projektgrundlage angelegt und Drucklayout vorbereitet.

*Letzter Monat (0h, 0 Tage, Inhalte):* Keine Einträge.

*Jahr (ca. 1,5h, 2 Tage, Inhalte):* Ruckpacken v1.00 begonnen.

*Insgesamt (ca. 1,5h, 2 Tage, Inhalte):* Ruckpacken v1.00 begonnen.

## Log

### 2026-07-13 - rupa, cardmaker, layout, druck (ca. 0,7h)

- Change: CardMaker-Projekt auf MPC Jumbo 3,5″ × 5″ bei 300 dpi umgestellt; 1120 × 1570 px Vollbeschnitt, 1050 × 1500 px Schnittfläche und 975 × 1425 px Sicherheitsfläche umgesetzt.
- Design: Symbolmittelpunkte auf X und Y proportional zur Schnittfläche skaliert; Symbolgrößen anhand des kleineren Achsenfaktors angepasst.
- Change: Laufzeitrotation auf den vollständigen Kreis (0° bis 359°) erweitert; Größenvariation bleibt auf ungefähr ±5 % begrenzt.
- Design: Vollflächigen weißen Hintergrund sowie rote, ungefüllte Schnitt- und Sicherheitsrahmen ergänzt; Rahmen sind nur im Editor sichtbar und werden nicht exportiert.
- Test: Layoutmaße, 300 dpi, Symbolgeometrie, Zufallstransformationen, Hilfsrahmen, weißer Hintergrund, 73 Karten und alle Bildreferenzen validiert.
- Doku: Bildmodell präzisiert: neun Layout-Bildplätze werden für 73 Karten wiederverwendet; 657 bezeichnet nur die daraus entstehenden Belegungen, nicht Layoutplätze oder Assets. Dauer: ca. 5 Minuten.

### 2026-07-12 - rupa, struktur, regeln, design, assets, tools, doku (ca. 0,8h)

- Summary: Bestehende Sitzungsartefakte als regelkonformes Spielprojekt übernommen und dokumentiert.
- Struktur: Root-Ordner `sp-ruckpacken` mit dem Kürzel `rupa` angelegt.
- Material: Korpus mit 73 Gegenständen und neu berechnete Kategorienverteilung übernommen.
- Material: Vollständiges nanDECK-Paket mit perfekter 73-Karten-Matrix übernommen.
- Tool: Offizielles ARASAAC-API-Mapping für deutsche und englische Suchen übernommen.
- Material: ARASAAC-Mapping für alle 73 Gegenstände erzeugt; 73 Haupt- und 68 Alternativtreffer stehen zur visuellen Auswahl bereit.
- Struktur: CSV-, Mapping- und nanDECK-Dateien aus `assets/` nach `files/` verschoben; `assets/` bleibt echten Medien vorbehalten.
- Struktur: nanDECK-Archiv entpackt; Vorlage, Kartenmatrizen, Validierung und 73 Platzhalterbilder als geschlossenes Werkzeug unter `tools/nandeck/` eingeordnet.
- Struktur: Allgemeine CSVs nach `files/data/` und die unveränderte ZIP-Quelle nach `files/archive/` gegliedert.
- Material: 73 farbige ARASAAC-Piktogramme heruntergeladen und als aktive nanDECK-Bilder eingebunden; Trinkflasche und Karte auf passendere Alternativtreffer korrigiert.
- Material: Attribution, tatsächliche ARASAAC-IDs und Prüfhilfen ergänzt; Arztkoffer und Verkehrsschild bleiben zur Nachprüfung markiert.
- Fix: Vollflächige Fußballszene durch ein freigestelltes Fußballtor ersetzt; technische Prüfung meldet keine quadratfüllenden Bilder mehr.
- Tool: Kartengenerierung auf `nhmkdev/cardmaker` (`cm`) v1.4.0.0 umgestellt; Projekt, Reference-CSV, Overrides und Validator unter `tools/cardmaker/` ergänzt.
- Material: Verkehrsschild von Ampel/Stopp-Geste auf ein freigestelltes Stoppschild korrigiert; Verbandskasten als Arztkoffer akzeptiert.
- Doku: `cm` eindeutig als `nhmkdev/cardmaker` definiert; nanDECK als Legacy-Prototyp markiert.
- Change: CM-Kartenformat auf 57 × 88 mm (673 × 1039 px bei 300 DPI) gesetzt; Neun-Symbol-Raute mit drei Positionsgrößen und gespeicherten leichten Drehungen umgesetzt.
- Refactor: CM-CSV auf elf Spalten reduziert; Rotation, Größe, Namen, IDs und Overrides aus der Datenquelle entfernt.
- Test: 73 Karten, sauberes CSV-Schema, neun wiederverwendete Layout-Bildplätze und 73 eindeutige Bildassets validiert.
- Struktur: Toolordner von `tools/cm/` nach `tools/cardmaker/` ausgeschrieben; `cm` bleibt nur das dokumentierte Toolkürzel.
- Change: Hart codierte Symbolrotationen entfernt; CardMaker erzeugt Drehung (−20° bis +20°) und geringe Größenabweichung nun beim Rendern über Incept-`#random`-Overrides.
- Tool: `configure_runtime_transforms.py` ergänzt und Validator auf echte Laufzeittransformationen verschärft. Dauer: ca. 25 Minuten.
- Daten: Markdown-Übersicht aller 73 Gegenstände mit laufender Nummer, leerer Notizspalte und den drei Kategoriearten unter `files/ruckpacken_gegenstaende.md` ergänzt. Dauer: ca. 10 Minuten.
- Refactor: ARASAAC-Mapping und Downloader funktional unter `tools/arasaac/` gebündelt.
- Regeln/Design: Überdeckungsmechanik, A/B/C-Aufgaben und organisches Neun-Symbol-Layout dokumentiert.
- Test: CSV-Zeilen, ZIP-Struktur, Python-Syntax und Dobble-Validierung geprüft.
- Versionen: ruckpacken_arasaac_mapping_api_offiziell v1.00.
