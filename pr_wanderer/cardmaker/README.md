# CardMaker für WND

Dieses Verzeichnis enthält das minimale CardMaker-Projekt für „Wanderer und Träumende Götter“. `build_cardmaker.py` liest die vier konkreten TSV-Kartenlisten aus `../cards/`, erzeugt je Kartentyp eine CSV-Referenz und baut `wanderer.cmp` mit genau einem Layout je Typ.

## Modus wechseln

Der Schalter steht in `cardmaker.json`:

```json
{
  "mode": "paper"
}
```

Zulässige Werte sind:

- `paper`: A4-Seite bei 300 dpi, weißer Hintergrund, eine mittig platzierte Bridge-Kartenfläche, dunkler zentrierter Text und acht Schnittmarken.
- `print`: Bridge-Format 675 × 1050 px bei 300 dpi. Vorhandene Bilder füllen die Karte; ohne vorhandenes Bild erscheint der formatierte Text hell und vertikal zentriert auf Schwarz.

Nach einer Änderung wird das Projekt neu gebaut:

```powershell
python build_cardmaker.py
python validate_cardmaker.py
```

Alternativ überschreibt `python build_cardmaker.py --mode print` den Schalter nur für diesen Lauf. `build-info.json` hält den tatsächlich erzeugten Modus fest.

## Dateien und Datenfluss

- `wanderer.cmp`: zu öffnendes CardMaker-Projekt.
- `ort.csv`, `aufgabe.csv`, `wort.csv`, `figur.csv`: erzeugte CardMaker-Referenzen; nicht von Hand pflegen.
- `cardmaker.json`: Modusschalter.
- `build_cardmaker.py`: TSV-Import, Bildprüfung, CSV- und Projektaufbau.
- `validate_cardmaker.py`: Schema-, Referenz-, Format- und Layoutprüfung.

`format_text` wird aus den TSV-Dateien direkt in CardMaker übernommen. CardMaker verwendet dafür `FormattedText`; farbige Schlüsselwörter stehen in der Form `<fc=0xRRGGBB>Wort</fc>`. Die Grundschrift ist `Arial Rounded MT Bold`. Falls sie auf einem Rechner fehlt, muss in CardMaker eine vergleichbare klare Rundschrift gewählt werden.

Ein Bild wird nur benutzt, wenn der in `img` eingetragene Pfad beim Bauen tatsächlich existiert. Relative Bildpfade dürfen vom jeweiligen Listenordner oder vom Projektordner `pr_wanderer/` ausgehen. Fehlende oder leere Bildpfade erzeugen im Print-Modus automatisch die schwarze Textkarte.

## Export

Die Layouts speichern 300 dpi sowie die passenden Exportmaße. Für PDF-Ausgaben muss CardMaker zusätzlich unter `Tools > Settings > PDF Export` auf A4 eingestellt sein. Im Paper-Modus wird pro Referenz eine vollständige A4-Seite mit Schnittmarken erzeugt; im Print-Modus wird jede Referenz als Bridge-Karte exportiert.
