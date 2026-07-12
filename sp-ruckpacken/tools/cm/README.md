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

Die neun Bildelemente beziehen nur ihre Dateipfade aus `cards.csv`. Position, Größe und eine einmalig pseudo-zufällig festgelegte Drehung liegen vollständig in `ruckpacken.cmp`. Die ARASAAC-Bilder und ihre Attribution liegen unter `assets/images/arasaac/`.

## Daten neu erzeugen

```powershell
python build_cm_data.py cards.csv cards.csv
```

Die aktive CSV enthält ausschließlich `Count`, `card_id` und `slot_01` bis `slot_09`.
