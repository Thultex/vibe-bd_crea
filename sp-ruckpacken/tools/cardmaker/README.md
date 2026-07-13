# CM – CardMaker für Ruckpacken

`cm` bezeichnet in diesem Projekt ausschließlich [nhmkdev/cardmaker](https://github.com/nhmkdev/cardmaker), nicht andere Programme mit dem Namen „CardMaker“.

- Upstream: `nhmkdev/cardmaker`
- Getestete Zielversion: `v1.4.0.0`
- Projektdatei: `ruckpacken.cmp`
- Datenquelle: `cards.csv`
- Endformat: 3,5″ × 5″ (89 × 127 mm)
- Produktionsdatei: 1120 × 1570 px Vollbeschnitt bei 300 dpi
- Hersteller: [MakePlayingCards – Custom Jumbo Cards](https://www.makeplayingcards.com/design/custom-3-5-x-5-game-cards.html)

## Verwendung

1. CardMaker `v1.4.0.0` starten.
2. `ruckpacken.cmp` öffnen.
3. Prüfen, ob `cards.csv` als Reference geladen ist.
4. Layout `Ruckpacken MPC Jumbo 3.5x5` auswählen und Karten bzw. PDF exportieren.

Die neun Bildelemente beziehen nur ihre Dateipfade aus `cards.csv`. Position und Grundgröße liegen in `ruckpacken.cmp`. CardMaker erzeugt bei jeder Übersetzung jedes Bildes eine neue Drehung über den vollständigen Kreis (0° bis 359°) und eine Größenabweichung von höchstens ungefähr ±5 %. Die Bilder bleiben dank `lockaspect="true"` unverzerrt.

Die Laufzeitvariation verwendet CardMakers Incept-Syntax direkt in der Elementdefinition:

```text
$[rotation:#random;0;359#]
$[width:#random;MIN;MAX#]
$[height:#random;MIN;MAX#]
```

Die XML-Attribute `rotation` bleiben deshalb alle auf `0`; es gibt keine pro Karte gespeicherten Transformationswerte in der CSV. Die ARASAAC-Bilder und ihre Attribution liegen unter `assets/images/arasaac/`.

## MPC-Flächen

| Fläche | Pixel bei 300 dpi | Umsetzung |
|---|---:|---|
| Vollbeschnitt | 1120 × 1570 | weißer Hintergrund bis zum Außenrand |
| Schnittfläche | 1050 × 1500 | roter, ungefüllter Editorrahmen bei 35 px Einzug |
| Sicherheitsfläche | 975 × 1425 | roter, ungefüllter Editorrahmen bei 72 px Einzug |

Die roten Rahmen werden nur im CardMaker-Editor angezeigt und beim Export automatisch deaktiviert. Dadurch gelangen keine Hilfslinien in die Druckdateien.

Die bisherigen Abstände der Symbolmittelpunkte zur Kartenmitte werden auf der X- und Y-Achse getrennt proportional zur neuen Schnittfläche skaliert. Die Symbolgrößen verwenden den kleineren der beiden Skalierungsfaktoren, damit das Muster nicht überfüllt wird.

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
