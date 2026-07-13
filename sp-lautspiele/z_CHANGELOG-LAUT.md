# Changelog Lautspiele

## Stats

Ausgangsdatum: 2026-07-13

*Diese Woche (ca. 3,3h, 2 Tage, Inhalte):* Altbestand archiviert und CardMaker-Generierung samt ARASAAC-Bildsatzimport für Gruselino, Memory, Domino und Dobble aufgebaut.

*Letzte Woche (0h, 0 Tage, Inhalte):* Keine Einträge.

*Dieser Monat (ca. 3,3h, 2 Tage, Inhalte):* Lautspiele v1.03 als Repo-Projekt angelegt, Datenkopplung korrigiert und ARASAAC-Import ergänzt.

*Letzter Monat (0h, 0 Tage, Inhalte):* Keine Einträge.

*Jahr (ca. 3,3h, 2 Tage, Inhalte):* Lautspiele v1.03 begonnen.

*Insgesamt (ca. 3,3h, 2 Tage, Inhalte):* Lautspiele v1.03 begonnen.

## Log

### 2026-07-14 - laut, tools, daten, assets, fix, doku (ca. 1,8h)

- Summary: Fehlerhafte globale Größen-Defines entfernt, CardMaker-Counts repariert und historische Gruselino-Struktur samt Memory und perfektem 6er-Dobble wiederhergestellt.
- Fix: Doppelte `symbol_01` bis `symbol_50` beseitigt; CardMaker hatte `lautspiele_defines.csv` sowohl projekt- als auch referenzbezogen geladen.
- Fix: Nicht verfügbare JavaScript-Namen wie `symbol_01__scale` entfernt; Skalierungsfaktoren werden nun aus `symbol_scale_map` der aktiven Bildsatzzeile gelesen.
- Fix: CardMaker-Referenzen erhalten nun die erforderliche Spalte `Count`; dadurch werden nicht mehr nur einzelne Karten pro Layout erzeugt.
- Refactor: `symbols_default.csv` und `symbols_k.csv` bleiben alleinige editierbare Master; Modus-CSVs werden technisch und reproduzierbar daraus abgeleitet.
- Daten: Größenkorrektur, Symbolnamen und Bildordner in `symbols_default.csv` und `symbols_k.csv` zusammengeführt; der Dateiname weist den jeweiligen Bildsatz eindeutig aus.
- Tool: Generiert je Bildsatz `gruselino`, `memory`, `domino` und `dobble` als CardMaker-Referenz mit korrekt berechnetem Count.
- Tool: `lautspiele_defines.csv` auf eine absichtlich leere Kompatibilitätskopfzeile reduziert, damit CardMaker keine fehlenden oder doppelten Defines meldet.
- Feature: Gruselino erzeugt wieder vier Grundkarten mit acht Symbolen und acht Suchkarten mit je einem fehlenden, zufällig angeordneten und gedrehten Symbol.
- Feature: Memory erzeugt pro Symbol genau zwei Karten; Domino bleibt ein geschlossener, frei konfigurierbarer Ring.
- Feature: Dobble verwendet die perfekte projektive Ebene der Ordnung 5 mit 31 Karten und sechs Symbolen je Karte.
- Test: Zwei Master-CSVs, acht abgeleitete Modus-CSVs, fünf Layouts, Gruselino-Ausblendung, Memory-Paare und perfekte Dobble-Matrix validiert.
- Doku: CSV-Auswahl pro Bildsatz, modusspezifische Felder und technische Rolle der leeren Defines-Datei erklärt.
- Feature: Neuer ARASAAC-Importer liest `Deutsch[,Englisch][,Anzahl]`, sucht beide Sprachen und erzeugt Hauptbilder sowie `-dN`-/`-eN`-Alternativen zur manuellen Auswahl.
- Daten/Assets: Importer schreibt Master, vier Modus-Referenzen, nummerierten Bildordner, Quellen-CSV und erforderliche ARASAAC-Lizenzzuordnung.
- Refactor: Bildbeschaffung und CSV-Erzeugung getrennt; `symbols_generate_sets.py` verarbeitet Namenslisten und vorhandene lückenlose Hauptbilder unabhängig von ARASAAC.
- Tool: ARASAAC-Importer delegiert Master- und Modusdateien an den gemeinsamen Bildsatz-Generator; manuell gepflegte Bildordner nutzen denselben Pfad.
- Daten: Nur `01.png`, `02.png` usw. zählen als Symbole; `-dN`- und `-eN`-Kandidaten bleiben austauschbare Alternativen.
- Struktur: Alle drei Erzeuger liegen gebündelt unter `tools/cardmaker/generators/`; Validator, Projekt und erzeugte Daten bleiben im CardMaker-Stammordner.
- Struktur: Symbolwerkzeuge einheitlich als `symbols_download_arasaac.py` und `symbols_generate_sets.py` benannt; `symbol_names.csv` liegt als ausführbares Eingabebeispiel direkt daneben.
- Doku: `generators/GENERATORS_README.md` beschreibt Zuständigkeiten, Eingabeformat, Ausgaben, Befehle und den empfohlenen Gesamtworkflow aller Generatoren.
- Test: ARASAAC-Integration real mit deutschem Haupttreffer sowie deutscher und englischer Alternative erfolgreich ausgeführt.
- Sicherheit: Vorhandene Bildsätze werden nur mit explizitem `--force` ersetzt; Suchlisten, Satznamen, PNG-Antworten und Kandidatenzahlen werden validiert.
- Versionen: build_lautspiele_project v1.03, validate_lautspiele_project v1.03, symbols_generate_sets v1.00, symbols_download_arasaac v1.00.

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
- Versionen: build_lautspiele_project v1.00, validate_lautspiele_project v1.00.
