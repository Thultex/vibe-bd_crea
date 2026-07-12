# Changelog Ruckpacken

## Stats

Ausgangsdatum: 2026-07-12

*Diese Woche (ca. 0,8h, 1 Tag, Inhalte):* Bestehende Daten, nanDECK-Paket, Anleitung und Projektdokumentation eingebracht.

*Letzte Woche (0h, 0 Tage, Inhalte):* Keine Einträge.

*Dieser Monat (ca. 0,8h, 1 Tag, Inhalte):* Ruckpacken-Projektgrundlage angelegt.

*Letzter Monat (0h, 0 Tage, Inhalte):* Keine Einträge.

*Jahr (ca. 0,8h, 1 Tag, Inhalte):* Ruckpacken v1.00 begonnen.

*Insgesamt (ca. 0,8h, 1 Tag, Inhalte):* Ruckpacken v1.00 begonnen.

## Log

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
- Refactor: ARASAAC-Mapping und Downloader funktional unter `tools/arasaac/` gebündelt.
- Regeln/Design: Überdeckungsmechanik, A/B/C-Aufgaben und organisches Neun-Symbol-Layout dokumentiert.
- Test: CSV-Zeilen, ZIP-Struktur, Python-Syntax und Dobble-Validierung geprüft.
- Versionen: ruckpacken_arasaac_mapping_api_offiziell v1.00.
