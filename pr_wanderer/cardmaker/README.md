# CardMaker für WND

Dieses Verzeichnis enthält zwei feste CardMaker-Projekte für „Wanderer und Träumende Götter“. `build_cardmaker.py` liest die vier konkreten TSV-Kartenlisten aus `../cards/`, erzeugt je Kartentyp eine gemeinsame CSV-Referenz und baut beide Projekte mit genau einem Layout je Typ.

## Projekte

- `wanderer-print.cmp`: dunkle Bridge-Karten. Vorhandene Bilder füllen die Karte; ohne Bild erscheint heller, vertikal zentrierter Text auf Schwarz.
- `wanderer-paper.cmp`: kompakte quadratische Karten ohne Bilder. Dunkler, vertikal zentrierter Text steht auf Weiß; links oben steht klein die Kartenart mit verkürzter Anzeige-ID, beispielsweise `ORT · E1`.

Print verwendet das Bridge-Format 675 × 1050 px bei 300 dpi. Paper verwendet 531 × 531 px und damit ungefähr 45 × 45 mm bei 300 dpi. Es gibt keine eingezeichneten Crop-Zeichen. Der Paper-Export aktiviert lediglich den Kartenrand des CardMaker-Exports; die Kreuzgröße bleibt `0`.

## Erzeugen und prüfen

```powershell
python build_cardmaker.py
python validate_cardmaker.py
```

Der Generator schreibt `ort.csv`, `aufgabe.csv`, `wort.csv` und `figur.csv`. Diese Referenzen werden nicht von Hand gepflegt. `paper-label` enthält die kleine Paper-Kennung; die beiden letzten Spalten sind immer:

- `format-hell`: Text für helle Karten; die Farbwerte werden gegenüber der TSV-Ausgangsfarbe automatisch abgedunkelt.
- `format-dunkel`: Text für dunkle Karten; die helleren Ausgangsfarben aus `col1`, `col2` usw. werden unverändert verwendet.

Die TSV-Farbspalten enthalten ausschließlich Werte der Form `0xRRGGBB`, keine CardMaker-Tags. `col1` gehört zum ersten Zielwort beziehungsweise Einzelwort, `col2` zum zweiten Zielwort. Der Generator erkennt in Phrasen auch flektierte Formen wie `brennt`, `klaut` und `Bäume` und erzeugt daraus CardMakers `FormattedText`-Tags.

## Minimal- oder Storyfassung

Für Orte und Aufgaben enthält die TSV nach den Zielwörtern zwei Texte: `phrase` ist die kurze Minimalphrase, `phrase_story` der vollständige Erzähltext. Die zentrale Auswahl steht in `text-version.json`:

```json
{
  "text_version": "phrase"
}
```

Zulässig sind `phrase` und `phrase_story`. Ein leeres `phrase_story` fällt automatisch auf `phrase` zurück. Nach einer Änderung wird `python build_cardmaker.py` erneut ausgeführt; beide CardMaker-Projekte verwenden dann dieselbe gewählte Fassung. Für einen einmaligen Test kann die Konfiguration ohne Dateiänderung überschrieben werden:

```powershell
python build_cardmaker.py --text-version phrase_story
python validate_cardmaker.py --text-version phrase_story
```

Die Grundschrift ist `Arial Rounded MT Bold`. Falls sie auf einem Rechner fehlt, muss in CardMaker eine vergleichbare klare Rundschrift gewählt werden.

## A4-PDF für Paper

Die quadratischen Paper-Layouts sind auf eine dichte A4-Anordnung ausgelegt. Für A4 unter `Tools > Settings > PDF Export` einstellen:

- Seite: A4, Hochformat
- Breite: 210 mm
- Höhe: 297 mm
- horizontale Ränder: höchstens 12 mm
- vertikale Ränder: höchstens 10 mm
- Layouts automatisch auf der Seite zentrieren
- neue Seite je Layouttyp aktivieren
- Layout-Ränder exportieren; Crop-Kreuze deaktiviert lassen

Damit passen bis zu 24 Paper-Karten in einem 4 × 6-Raster auf eine A4-Seite. Die Projekte definieren Kartenformat, Auflösung, Exportdateinamen und Exportrand; das A4-Seitenformat selbst ist eine globale CardMaker-PDF-Einstellung und wird nicht in einer `.cmp`-Datei gespeichert.

Ein Bild wird nur benutzt, wenn der in `img` eingetragene Pfad beim Bauen tatsächlich existiert. Relative Bildpfade dürfen vom jeweiligen Listenordner oder vom Projektordner `pr_wanderer/` ausgehen.
Die Print-Layouts prüfen `img` direkt: ein leeres Feld zeigt die Textkarte, ein vorhandener Pfad die Bildkarte. Eine zusätzliche Hilfsvariable wird dafür nicht erzeugt.
