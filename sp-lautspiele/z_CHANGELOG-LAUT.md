# Changelog Lautspiele

## Stats

Ausgangsdatum: 2026-07-13

*Diese Woche (ca. 4,8h, 2 Tage, Inhalte):* Altbestand archiviert und CardMaker-Skripte samt ARASAAC-Bildsatzimport für Gruselino, Memory/Domino, Dobble, Spielplan und Bingo aufgebaut.

*Letzte Woche (0h, 0 Tage, Inhalte):* Keine Einträge.

*Dieser Monat (ca. 4,8h, 2 Tage, Inhalte):* Lautspiele v1.08 als Repo-Projekt angelegt, Datenkopplung korrigiert und um Spielplan sowie Bingo ergänzt.

*Letzter Monat (0h, 0 Tage, Inhalte):* Keine Einträge.

*Jahr (ca. 4,8h, 2 Tage, Inhalte):* Lautspiele v1.08 begonnen.

*Insgesamt (ca. 4,8h, 2 Tage, Inhalte):* Lautspiele v1.08 begonnen.

## Log

### 2026-07-14 - laut, tools, daten, assets, fix, doku (ca. 3,3h)

- Summary: CardMaker-Counts und Datenkopplung repariert, Layouts und Satzreferenzen originalnah zusammengeführt sowie die gemeinsame Symbolauswahl über `build.ini` konfigurierbar gemacht.
- Fix: Doppelte `symbol_01` bis `symbol_50` beseitigt; CardMaker hatte `lautspiele_defines.csv` sowohl projekt- als auch referenzbezogen geladen.
- Fix: Nicht verfügbare JavaScript-Namen wie `symbol_01__scale` entfernt; Skalierungsfaktoren werden nun aus `symbol_scale_map` der aktiven Bildsatzzeile gelesen.
- Fix: CardMaker-Referenzen erhalten nun die erforderliche Spalte `Count`; dadurch werden nicht mehr nur einzelne Karten pro Layout erzeugt.
- Refactor: `symbols_default.csv` und `symbols_k.csv` bleiben alleinige editierbare Master; Modus-CSVs werden technisch und reproduzierbar daraus abgeleitet.
- Daten: Größenkorrektur, Symbolnamen und Bildordner in `symbols_default.csv` und `symbols_k.csv` zusammengeführt; der Dateiname weist den jeweiligen Bildsatz eindeutig aus.
- Tool: Generiert je Bildsatz `gruselino`, `domino`, `dobble`, `spiel` und `bingo` als CardMaker-Referenz mit korrekt berechnetem Count.
- Tool: `lautspiele_defines.csv` auf eine absichtlich leere Kompatibilitätskopfzeile reduziert, damit CardMaker keine fehlenden oder doppelten Defines meldet.
- Feature: Ausschließlich Gruselino Papier erzeugt vier Grundkarten und acht Suchkarten; Symbolflächen um 20 Prozent reduziert und Drehung auf ±20 Grad begrenzt.
- Feature: Memory und Domino teilen ein originalnahes Doppelmodul mit zwei identischen 560er Karten, 550er Symbolflächen, UI-Ebenen und mittiger Schnittzone; Rotation bleibt null.
- Feature: Dobble verwendet die perfekte projektive Ebene der Ordnung 5 mit 31 Karten und sechs weiter verteilten Symbolen; Größenvarianz auf ±18 Prozent erweitert.
- Test: Zwei Master-CSVs, zehn abgeleitete Modus-CSVs und fünf Layouts einschließlich Spielplan und Bingo validiert.
- Doku: CSV-Auswahl pro Bildsatz, modusspezifische Felder und technische Rolle der leeren Defines-Datei erklärt.
- Feature: Neuer ARASAAC-Importer liest `Deutsch[,Englisch][,Anzahl]`, sucht beide Sprachen und erzeugt Hauptbilder sowie `-dN`-/`-eN`-Alternativen zur manuellen Auswahl.
- Daten/Assets: Importer schreibt Master, fünf Modus-Referenzen, nummerierten Bildordner, Quellen-CSV und erforderliche ARASAAC-Lizenzzuordnung.
- Refactor: Bildbeschaffung und CSV-Erzeugung getrennt; `symbols_generate_sets.py` verarbeitet Namenslisten und vorhandene lückenlose Hauptbilder unabhängig von ARASAAC.
- Tool: ARASAAC-Importer delegiert Master- und Modusdateien an den gemeinsamen Bildsatz-Generator; manuell gepflegte Bildordner nutzen denselben Pfad.
- Daten: Nur `01.png`, `02.png` usw. zählen als Symbole; `-dN`- und `-eN`-Kandidaten bleiben austauschbare Alternativen.
- Struktur: Skripte liegen unter `tools/cardmaker/scripts/`; Build und Prüfung sind in `build/`, Bildsatz-Erzeugung und Vorlagen in `generate/` getrennt.
- Struktur: Symbolwerkzeuge einheitlich als `symbols_download_arasaac.py` und `symbols_generate_sets.py` benannt; `symbol_names.csv` liegt als ausführbares Eingabebeispiel direkt daneben.
- Doku: `scripts/SCRIPTS_README.md` beschreibt Zuständigkeiten, Eingabeformat, Ausgaben, Befehle und den empfohlenen Gesamtworkflow aller Skripte.
- Feature: `symbol_ids.csv` ergänzt einen direkten ARASAAC-ID-Modus ohne Suchlauf; deutsche API-Begriffe werden als Namen übernommen.
- Daten: Leere, selbsterklärende `scripts/generate/symbol_ids.csv` als Vorlage neben `symbol_names.csv` angelegt.
- Test: ARASAAC-Integration real mit deutschem Haupttreffer sowie deutscher und englischer Alternative erfolgreich ausgeführt.
- Sicherheit: Vorhandene Bildsätze werden nur mit explizitem `--force` ersetzt; Suchlisten, Satznamen, PNG-Antworten und Kandidatenzahlen werden validiert.
- Feature: Jedes Layout bindet alle vorhandenen Satz-CSVs seines Modus ein; `default` und `k` lassen sich dadurch unmittelbar in CardMaker wechseln.
- Export: Historische Layout-Standardcounts und PDF-Seitenflächen übernommen; Memory/Domino bezieht seine Ausgabezahl weiterhin dynamisch aus der Symbolspanne.
- Konfiguration: `scripts/build/build.ini` steuert das gemeinsame Symbolfenster mit Startsymbol und automatischer oder fester Anzahl und dokumentiert die Symbolzahlen der Layouts.
- Refactor: Builder prägnant in `build_lautspiele_files.py` umbenannt und alle Aufrufe angepasst.
- Refactor: Sämtliche aktiven Pfade, Importe und Befehlsbeispiele von `generators` auf die getrennte `scripts`-Struktur umgestellt.
- Fix: Memory/Domino verwendet wieder die vollständigen `#roundedrect…#`-Shape-Strings; dadurch erscheinen die zwei getrennten Kartenkästchen wie im Original.
- Export: Domino-Zoom, Crop-Definition und `2362 × 7400` übernommen; zwei Doppelmodule beziehungsweise vier Memory-Karten passen nebeneinander.
- Refactor: Statische Rahmen, Geometrie, Farben und Exportwerte verbleiben im Layout; JavaScript bleibt auf dynamische Symbolberechnung beschränkt.
- Feature: Minimalistischer A4-Spielplan mit zehn Symbolstationen, vergrößerten normalen Feldern, zwei Vorwärts- und zwei Rückwärtssprüngen sowie doppelt umkreistem Ziel ergänzt.
- Regel: Vorwärtspfeile beginnen ausschließlich an Symbolstationen und springen höchstens neun Felder; Rückwärtspfeile setzen höchstens sechs Felder zurück.
- Feature: Vier vollständige 4x4-Bingokarten ergänzt; derselbe Symbolbestand wird je Karte reproduzierbar neu angeordnet.
- Export: Eine Bingokarte belegt eine halbe A4-Seite bei 300 DPI, sodass zwei Karten je Seite und alle vier Karten auf zwei Seiten ausgegeben werden.
- Material: Eine der vier vollständigen Bingokarten kann entlang des statischen Rasters als Ziehsatz ausgeschnitten werden; eine separate Ziehseite ist nicht nötig.
- Daten: `spiel_*` und `bingo_*` ergänzen Start, Ende und Shift in Master- und Modus-CSVs; bei weniger als 16 Bingo-Symbolen wird zyklisch ohne leere Felder aufgefüllt.
- Test: Zwei Master-CSVs, zehn abgeleitete Modus-CSVs, fünf Layouts, Sprunggrenzen, Doppelziel und vollständige Bingo-Raster validiert.
- Versionen: build_lautspiele_files v1.08, validate_lautspiele_project v1.08, symbols_generate_sets v1.03, symbols_download_arasaac v1.02.

### 2026-07-13 - laut, struktur, tools, design, material, doku (ca. 1,5h)

- Summary: Bestehende Lautspiele-Materialien unverändert archiviert und eine gemeinsame, feldbasierte CardMaker-Generierung für drei Spielarten geschaffen.
- Struktur: Spielordner `sp-lautspiele` mit dem Kürzel `laut` und allen vorgeschriebenen Dokumenten angelegt.
- Material: 56 Quelldateien sowie `Logospiele.xlsx` unverändert unter `files/archive/` gesichert; aktive Symbol- und UI-Bilder beim CardMaker-Tool eingeordnet.
- Struktur: Einen überlangen historischen Stockgrafik-Pfad in der Archivkopie Windows-/Git-kompatibel gekürzt; die beiden Dateien selbst blieben unverändert und die Pfadabbildung ist dokumentiert.
- Refactor: Alte Google-/Tabellenberechnungen durch eine gemeinsame sieben-spaltige `lautspiele.csv` ersetzt; alle vier Layouts verwenden dieselbe Referenz.
- Feature: Größenkorrektur mit Namen in `lautspiele_defines.csv` überführt und auf 50 erweiterbare Symbol-IDs vorbereitet; die ersten zehn Faktoren entsprechen der alten Arbeitsmappe.
- Feature: Gruselino erzeugt eine Übersicht und zehn 9-aus-10-Karten; Start, Ende und zyklische Verschiebung erlauben verschiedene Symbolfenster und Bildordner.
- Feature: Domino verwendet konfigurierbare Ringgrenzen und verbindet das letzte Symbol wieder mit dem ersten; Quelldateien bleiben unverändert, das ganze Element wird erst in CardMaker rotiert.
- Feature: Perfekte Dobble-Minivariante mit sieben Karten, drei Symbolen je Karte und exakt einem Treffer pro Kartenpaar ergänzt.
- Design: Zufallsrotationen und die Größenvariation von ±5 % liegen direkt in den JavaScript-Feldern; Grundpositionen und -größen bleiben im Editor die maßgebliche Geometrie.
- Test: Gemeinsame Referenzen, CSV-Schema, 50 Definitionen, aktive Bilddateien, Gruselino-Ausblendung, Domino-Ring und perfekte Dobble-Matrix durch einen Validator abgesichert.
- Doku: Datenmodell, Generatorbedienung, Spielkurzregeln, Ideen und nächste Schritte dokumentiert.
- Versionen: build_lautspiele_files v1.00, validate_lautspiele_project v1.00.
