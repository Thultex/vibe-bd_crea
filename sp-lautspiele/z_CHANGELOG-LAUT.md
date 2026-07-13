# Changelog Lautspiele

## Stats

Ausgangsdatum: 2026-07-13

*Diese Woche (ca. 2,2h, 2 Tage, Inhalte):* Altbestand archiviert und CardMaker-Generierung mit bildsatzbezogenen Symboltabellen für Gruselino, Domino und Dobble aufgebaut.

*Letzte Woche (0h, 0 Tage, Inhalte):* Keine Einträge.

*Dieser Monat (ca. 2,2h, 2 Tage, Inhalte):* Lautspiele v1.02 als Repo-Projekt angelegt und die Datenkopplung korrigiert.

*Letzter Monat (0h, 0 Tage, Inhalte):* Keine Einträge.

*Jahr (ca. 2,2h, 2 Tage, Inhalte):* Lautspiele v1.02 begonnen.

*Insgesamt (ca. 2,2h, 2 Tage, Inhalte):* Lautspiele v1.02 begonnen.

## Log

### 2026-07-14 - laut, tools, daten, fix, doku (ca. 0,7h)

- Summary: Fehlerhafte globale Größen-Defines entfernt und alle Modusdaten in direkt auswählbaren CSVs pro Laut-/Bildsatz gebündelt.
- Fix: Doppelte `symbol_01` bis `symbol_50` beseitigt; CardMaker hatte `lautspiele_defines.csv` sowohl projekt- als auch referenzbezogen geladen.
- Fix: Nicht verfügbare JavaScript-Namen wie `symbol_01__scale` entfernt; Skalierungsfaktoren werden nun aus `symbol_scale_map` der aktiven Bildsatzzeile gelesen.
- Refactor: Zwischenstand mit `gruselino.csv`, `domino.csv` und `dobble.csv` verworfen; der Modus wird bereits durch das Layout bestimmt und benötigt keine eigene CSV.
- Daten: Größenkorrektur, Symbolnamen und Bildordner in `symbols_default.csv` und `symbols_k.csv` zusammengeführt; der Dateiname weist den jeweiligen Bildsatz eindeutig aus.
- Tool: `symbols_default.csv` und `symbols_k.csv` sind nun direkte CardMaker-Referenzen und enthalten jeweils Ordner, Namen, Skalierungen sowie Start, Ende und Shift aller Modi in einer Zeile.
- Tool: `lautspiele_defines.csv` auf eine absichtlich leere Kompatibilitätskopfzeile reduziert, damit CardMaker keine fehlenden oder doppelten Defines meldet.
- Test: Zwei direkt auswählbare Symbol-CSVs, vier Layoutreferenzen, Bildsatzzuordnung, Skalierungsdaten und Dobble-Matrix validiert.
- Doku: CSV-Auswahl pro Bildsatz, modusspezifische Felder und technische Rolle der leeren Defines-Datei erklärt.
- Versionen: build_lautspiele_project v1.02, validate_lautspiele_project v1.02.

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
