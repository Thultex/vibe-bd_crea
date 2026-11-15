# Wanderer und Träumende Götter

Kurzversion: `wnd`

## Dateien

- `anleitung_wnd.md`: Spielanleitung v1.09.
- `design_wnd.md`: Design- und Entwicklungsdokument v1.15.
- `material_wnd.md`: konkreter Kartenbestand und Prototypplanung v1.05.
- `cards/`: gemeinsame TSV-Kartenlisten pro Kartengruppe und zugehörige Bildordner.
- `z_CHANGELOG-WND.md`: Arbeits- und Versionsverlauf.
- `z_referenzen/gfx/`: grafische Referenzen.

## Kartendaten

Orte, Aufgaben, Wörter und Figuren liegen jeweils in einer gemeinsamen TSV-Liste ihrer Kartengruppe. Jede Liste beginnt mit `anzahl` und `subtyp`; konkretisierte Karten haben derzeit die Stückzahl `1`. Die internen IDs bleiben kleingeschrieben, etwa `e01`, `ag01` und `wn01`.

Kandidaten ohne Karten-ID stehen in `cards/wort/liste-wörter-kandidaten.tsv` getrennt vom konkretisierten Kartenbestand. Einzelheiten zu Spalten, Dateinamen und Bildpfaden stehen in `cards/README.md`.

## Bildquellen und Exporte

Jede Kartengruppe verwendet genau einen `img/`-Ordner für kleine, versionierte `.ai`-Originale und normale `.png`- oder `.jpg`-Exporte ohne Bleed. Dateinamen verwenden die Karten-ID in Großbuchstaben, zum Beispiel `E01_Wüste.ai` und `E01_Wüste-01.png`. Pfade werden in den TSV-Spalten `bild_png` und `bild_ai` nur eingetragen, wenn die jeweilige Datei tatsächlich vorhanden ist.

Bleed-Exporte werden nicht vorgehalten; ein späterer Cardmaker soll sie bei Bedarf erzeugen. Ein Cardmaker ist noch nicht Teil dieses Projektstands.
