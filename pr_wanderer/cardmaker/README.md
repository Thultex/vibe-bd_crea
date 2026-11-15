# CardMaker für WND

Dieses Verzeichnis enthält zwei feste CardMaker-Projekte für „Wanderer und Träumende Götter“. `build_cardmaker.py` liest die vier konkreten TSV-Kartenlisten aus `../cards/`, erzeugt je Kartentyp eine gemeinsame CSV-Referenz und baut beide Projekte mit genau einem Layout je Typ.

## Projekte

- `wanderer-print.cmp`: dunkle Bridge-Karten. Vorhandene Bilder füllen die Karte; ohne Bild erscheint heller, vertikal zentrierter Text auf Schwarz.
- `wanderer-paper.cmp`: helle Bridge-Karten ohne Bilder. Dunkler, vertikal zentrierter Text steht auf Weiß.

Beide Projekte verwenden 675 × 1050 px bei 300 dpi. Es gibt keine eingezeichneten Crop-Zeichen. Der Paper-Export aktiviert lediglich den Kartenrand des CardMaker-Exports; die Kreuzgröße bleibt `0`.

## Erzeugen und prüfen

```powershell
python build_cardmaker.py
python validate_cardmaker.py
```

Der Generator schreibt `ort.csv`, `aufgabe.csv`, `wort.csv` und `figur.csv`. Diese Referenzen werden nicht von Hand gepflegt. Ihre beiden letzten Spalten sind immer:

- `format-hell`: Text für helle Karten; die Farbwerte werden gegenüber der TSV-Ausgangsfarbe automatisch abgedunkelt.
- `format-dunkel`: Text für dunkle Karten; die helleren Ausgangsfarben aus `col1`, `col2` usw. werden unverändert verwendet.

Die TSV-Farbspalten enthalten ausschließlich Werte der Form `0xRRGGBB`, keine CardMaker-Tags. `col1` gehört zum ersten Zielwort beziehungsweise Einzelwort, `col2` zum zweiten Zielwort. Der Generator erkennt in Phrasen auch flektierte Formen wie `brennt`, `klaut` und `Bäume` und erzeugt daraus CardMakers `FormattedText`-Tags.

Die Grundschrift ist `Arial Rounded MT Bold`. Falls sie auf einem Rechner fehlt, muss in CardMaker eine vergleichbare klare Rundschrift gewählt werden.

## A4-PDF für Paper

Die Paper-Layouts bleiben im echten Bridge-Format, damit CardMakers PDF-Export sie platzsparend auf einer Seite anordnet. Für A4 unter `Tools > Settings > PDF Export` einstellen:

- Seite: A4, Hochformat
- Breite: 210 mm
- Höhe: 297 mm
- horizontale Ränder: höchstens 12 mm
- vertikale Ränder: höchstens 6 mm
- Layouts automatisch auf der Seite zentrieren
- neue Seite je Layouttyp aktivieren
- Layout-Ränder exportieren; Crop-Kreuze deaktiviert lassen

Damit passen bis zu neun Bridge-Karten in einem 3 × 3-Raster auf eine A4-Seite. Die Projekte definieren Kartenformat, Auflösung, Exportdateinamen und Exportrand; das A4-Seitenformat selbst ist eine globale CardMaker-PDF-Einstellung und wird nicht in einer `.cmp`-Datei gespeichert.

Ein Bild wird nur benutzt, wenn der in `img` eingetragene Pfad beim Bauen tatsächlich existiert. Relative Bildpfade dürfen vom jeweiligen Listenordner oder vom Projektordner `pr_wanderer/` ausgehen.
