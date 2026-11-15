# Wanderer und Träumende Götter

Kurzversion: `wnd`

## Dateien

- `anleitung_wnd.md`: Spielanleitung v1.10.
- `design_wnd.md`: Design- und Entwicklungsdokument v1.21.
- `material_wnd.md`: konkreter Kartenbestand und Prototypplanung v1.11.
- `cards/`: gemeinsame TSV-Kartenlisten pro Kartengruppe und zugehörige Bildordner.
- `cardmaker/`: getrennte Print- und Paper-Projekte, erzeugte Referenzdaten sowie Build- und Prüfskripte.
- `z_CHANGELOG-WND.md`: Arbeits- und Versionsverlauf.
- `z_referenzen/gfx/`: grafische Referenzen.

## Kartendaten

Orte, Aufgaben, Wörter und Figuren liegen jeweils in einer gemeinsamen TSV-Liste ihrer Kartengruppe: `liste-ort.tsv`, `liste-aufgabe.tsv`, `liste-wort.tsv` und `liste-figur.tsv`. Alle Listen verwenden dieselbe Produktionsstruktur mit gemeinsamen Spalten an festen Positionen und gruppenspezifischen Kernfeldern. Bei Orten und Aufgaben folgen auf die Zielwörter `phrase` als Minimalfassung und `phrase_story` als optionale ausführliche Erzählfassung. `col1`, `col2` usw. enthalten direkt vor `img` die hellen Ausgangsfarben für dunkle Karten; eine leere Spalte hinter `ai` trennt die anschließenden Metadaten sichtbar ab. Konkretisierte Karten haben derzeit die Stückzahl `1`; die internen IDs bleiben kleingeschrieben.

Alle Wortideen ohne Karten-ID stehen gemeinsam in `cards/liste-wortideen.tsv` getrennt vom konkretisierten Kartenbestand. Die zentrale Dokumentation für Spalten, Dateinamen, Bildpfade, Bewertungsskala und aktuelle Materialwerte steht in `cards/info-listen.md`.

## Bildquellen und Exporte

Jede Kartengruppe verwendet genau einen `img/`-Ordner für kleine, versionierte `.ai`-Originale und normale `.png`- oder `.jpg`-Exporte ohne Bleed. Dateinamen verwenden die Karten-ID in Großbuchstaben, zum Beispiel `E01_Wüste.ai` und `E01_Wüste-01.png`. Pfade werden in den jeweiligen Bildspalten nur eingetragen, wenn die Datei tatsächlich vorhanden ist.

Bleed-Exporte werden nicht vorgehalten. `cardmaker/wanderer-print.cmp` erzeugt dunkle Bridge-Printkarten mit vorhandenem Bild oder heller Schrift auf Schwarz. `cardmaker/wanderer-paper.cmp` erzeugt helle quadratische Karten von ungefähr 45 × 45 mm mit kleiner Typ-/ID-Kennung links oben und ohne eingezeichnete Crop-Zeichen; CardMakers PDF-Export ordnet bis zu 24 davon im 4 × 6-Raster auf A4 an. `cardmaker/text-version.json` schaltet beide Projekte gemeinsam zwischen Minimal- und Storyfassung um; leere Storytexte verwenden automatisch die Minimalphrase. Die erzeugten CSVs enthalten abschließend `format-hell` und `format-dunkel`.
