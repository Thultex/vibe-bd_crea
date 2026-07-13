# Changelog Lautspiele

## Stats

Ausgangsdatum: 2026-07-13

*Diese Woche (ca. 4,0h, 2 Tage, Inhalte):* Altbestand archiviert und CardMaker-Generierung samt ARASAAC-Bildsatzimport für Gruselino, Memory/Domino und Dobble aufgebaut.

*Letzte Woche (0h, 0 Tage, Inhalte):* Keine Einträge.

*Dieser Monat (ca. 4,0h, 2 Tage, Inhalte):* Lautspiele v1.06 als Repo-Projekt angelegt, Datenkopplung korrigiert und ARASAAC-Import ergänzt.

*Letzter Monat (0h, 0 Tage, Inhalte):* Keine Einträge.

*Jahr (ca. 4,0h, 2 Tage, Inhalte):* Lautspiele v1.06 begonnen.

*Insgesamt (ca. 4,0h, 2 Tage, Inhalte):* Lautspiele v1.06 begonnen.

## Log

### 2026-07-14 - laut, tools, daten, assets, fix, doku (ca. 2,5h)

- Summary: CardMaker-Counts und Datenkopplung repariert, Layouts und Satzreferenzen originalnah zusammengeführt sowie die gemeinsame Symbolauswahl über `build.ini` konfigurierbar gemacht.
- Fix: Doppelte `symbol_01` bis `symbol_50` beseitigt; CardMaker hatte `lautspiele_defines.csv` sowohl projekt- als auch referenzbezogen geladen.
- Fix: Nicht verfügbare JavaScript-Namen wie `symbol_01__scale` entfernt; Skalierungsfaktoren werden nun aus `symbol_scale_map` der aktiven Bildsatzzeile gelesen.
- Fix: CardMaker-Referenzen erhalten nun die erforderliche Spalte `Count`; dadurch werden nicht mehr nur einzelne Karten pro Layout erzeugt.
- Refactor: `symbols_default.csv` und `symbols_k.csv` bleiben alleinige editierbare Master; Modus-CSVs werden technisch und reproduzierbar daraus abgeleitet.
- Daten: Größenkorrektur, Symbolnamen und Bildordner in `symbols_default.csv` und `symbols_k.csv` zusammengeführt; der Dateiname weist den jeweiligen Bildsatz eindeutig aus.
- Tool: Generiert je Bildsatz `gruselino`, `domino` und `dobble` als CardMaker-Referenz mit korrekt berechnetem Count.
- Tool: `lautspiele_defines.csv` auf eine absichtlich leere Kompatibilitätskopfzeile reduziert, damit CardMaker keine fehlenden oder doppelten Defines meldet.
- Feature: Ausschließlich Gruselino Papier erzeugt vier Grundkarten und acht Suchkarten; Symbolflächen um 20 Prozent reduziert und Drehung auf ±20 Grad begrenzt.
- Feature: Memory und Domino teilen ein originalnahes Doppelmodul mit zwei identischen 560er Karten, 550er Symbolflächen, UI-Ebenen und mittiger Schnittzone; Rotation bleibt null.
- Feature: Dobble verwendet die perfekte projektive Ebene der Ordnung 5 mit 31 Karten und sechs weiter verteilten Symbolen; Größenvarianz auf ±18 Prozent erweitert.
- Test: Zwei Master-CSVs, sechs abgeleitete Modus-CSVs, drei Layouts, Gruselino-Geometrie, trennbares Memory-/Domino-Modul und perfekte Dobble-Matrix validiert.
- Doku: CSV-Auswahl pro Bildsatz, modusspezifische Felder und technische Rolle der leeren Defines-Datei erklärt.
- Feature: Neuer ARASAAC-Importer liest `Deutsch[,Englisch][,Anzahl]`, sucht beide Sprachen und erzeugt Hauptbilder sowie `-dN`-/`-eN`-Alternativen zur manuellen Auswahl.
- Daten/Assets: Importer schreibt Master, drei Modus-Referenzen, nummerierten Bildordner, Quellen-CSV und erforderliche ARASAAC-Lizenzzuordnung.
- Refactor: Bildbeschaffung und CSV-Erzeugung getrennt; `symbols_generate_sets.py` verarbeitet Namenslisten und vorhandene lückenlose Hauptbilder unabhängig von ARASAAC.
- Tool: ARASAAC-Importer delegiert Master- und Modusdateien an den gemeinsamen Bildsatz-Generator; manuell gepflegte Bildordner nutzen denselben Pfad.
- Daten: Nur `01.png`, `02.png` usw. zählen als Symbole; `-dN`- und `-eN`-Kandidaten bleiben austauschbare Alternativen.
- Struktur: Alle drei Erzeuger liegen gebündelt unter `tools/cardmaker/generators/`; Validator, Projekt und erzeugte Daten bleiben im CardMaker-Stammordner.
- Struktur: Symbolwerkzeuge einheitlich als `symbols_download_arasaac.py` und `symbols_generate_sets.py` benannt; `symbol_names.csv` liegt als ausführbares Eingabebeispiel direkt daneben.
- Doku: `generators/GENERATORS_README.md` beschreibt Zuständigkeiten, Eingabeformat, Ausgaben, Befehle und den empfohlenen Gesamtworkflow aller Generatoren.
- Feature: `symbol_ids.csv` ergänzt einen direkten ARASAAC-ID-Modus ohne Suchlauf; deutsche API-Begriffe werden als Namen übernommen.
- Daten: Leere, selbsterklärende `generators/symbol_ids.csv` als Vorlage neben `symbol_names.csv` angelegt.
- Test: ARASAAC-Integration real mit deutschem Haupttreffer sowie deutscher und englischer Alternative erfolgreich ausgeführt.
- Sicherheit: Vorhandene Bildsätze werden nur mit explizitem `--force` ersetzt; Suchlisten, Satznamen, PNG-Antworten und Kandidatenzahlen werden validiert.
- Feature: Jedes Layout bindet alle vorhandenen Satz-CSVs seines Modus ein; `default` und `k` lassen sich dadurch unmittelbar in CardMaker wechseln.
- Export: Historische Layout-Standardcounts und PDF-Seitenflächen übernommen; Memory/Domino bezieht seine Ausgabezahl weiterhin dynamisch aus der Symbolspanne.
- Konfiguration: `generators/build.ini` steuert das gemeinsame Symbolfenster mit Startsymbol und automatischer oder fester Anzahl.
- Refactor: Builder prägnant in `build_lautspiele_files.py` umbenannt und alle Aufrufe angepasst.
- Versionen: build_lautspiele_files v1.06, validate_lautspiele_project v1.06, symbols_generate_sets v1.01, symbols_download_arasaac v1.01.

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
