# CM – CardMaker für Ruckpacken

`cm` bezeichnet in diesem Projekt ausschließlich [nhmkdev/cardmaker](https://github.com/nhmkdev/cardmaker), nicht andere Programme mit dem Namen „CardMaker“.

- Upstream: `nhmkdev/cardmaker`
- Getestete Zielversion: `v1.4.0.0`
- Projektdatei: `ruckpacken.cmp`
- Datenquelle: `cards.csv`
- Kartenformat: Pokerkarte, 750 × 1050 px bei 300 DPI

## Verwendung

1. CardMaker `v1.4.0.0` starten.
2. `ruckpacken.cmp` öffnen.
3. Prüfen, ob `cards.csv` als Reference geladen ist.
4. Layout `Ruckpacken` auswählen und Karten bzw. PDF exportieren.

Die neun Bildelemente beziehen ihre Dateipfade aus `cards.csv`. Rotation und Größe werden pro Karte über CardMaker-Overrides gesetzt. Die ARASAAC-Bilder und ihre Attribution liegen vollständig unter `assets/images/arasaac/`.

## Daten neu erzeugen

```powershell
python build_cm_data.py ../nandeck/cards.csv cards.csv
```

Der nanDECK-Datensatz dient aktuell nur als Eingabematrix. Das erzeugte `cards.csv` ist die aktive CM-Datenquelle.
