# CM – CardMaker für Ruckpacken

`cm` bezeichnet in diesem Projekt ausschließlich [nhmkdev/cardmaker](https://github.com/nhmkdev/cardmaker), nicht andere Programme mit dem Namen „CardMaker“.

- Upstream: `nhmkdev/cardmaker`
- Getestete Zielversion: `v1.4.0.0`
- Projektdatei: `ruckpacken.cmp`
- Datenquelle: `cards.csv`
- Kartenformat: 57 × 88 mm, 673 × 1039 px bei 300 DPI

## Verwendung

1. CardMaker `v1.4.0.0` starten.
2. `ruckpacken.cmp` öffnen.
3. Prüfen, ob `cards.csv` als Reference geladen ist.
4. Layout `Ruckpacken` auswählen und Karten bzw. PDF exportieren.

Die neun Bildelemente beziehen nur ihre Dateipfade aus `cards.csv`. Position und Grundgröße liegen in `ruckpacken.cmp`. CardMaker erzeugt bei jeder Übersetzung jedes Bildes eine neue Drehung von −20° bis +20° und eine kleine Größenabweichung von ungefähr ±5 %. Die Bilder bleiben dank `lockaspect="true"` unverzerrt.

Die Laufzeitvariation verwendet CardMakers Incept-Syntax direkt in der Elementdefinition:

```text
$[rotation:#random;-20;20#]
$[width:#random;MIN;MAX#]
$[height:#random;MIN;MAX#]
```

Die XML-Attribute `rotation` bleiben deshalb alle auf `0`; es gibt keine pro Karte gespeicherten Transformationswerte in der CSV. Die ARASAAC-Bilder und ihre Attribution liegen unter `assets/images/arasaac/`.

## Daten neu erzeugen

```powershell
python build_cm_data.py cards.csv cards.csv
```

Die aktive CSV enthält ausschließlich `Count`, `card_id` und `slot_01` bis `slot_09`.

Nach Layoutänderungen lassen sich die Laufzeittransformationen reproduzierbar neu eintragen und prüfen:

```powershell
python configure_runtime_transforms.py
python validate_cm_project.py
```
