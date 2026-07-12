# Ruckpacken – Design v1.00

## Material

- 73 Symbolkarten im Pokerformat 63 × 88 mm
- 73 Gegenstandssymbole, jeweils neun Vorkommen
- neun Symbole je Karte
- geheime Aufgaben der Typen A, B und C

## Kartendesign

Die neun Positionen bilden eine organische Raute statt eines 3×3-Rasters:

```text
      1
   2     3
 4    5    6
   7     8
      9
```

Die Mitte ist größer als Innen- und Außenpositionen. Einzelne Symbole werden zufällig leicht gedreht. Karten dürfen als Ganzes gedreht und so überlappt werden, dass drei bis sechs Symbole verschwinden.

## Mathematischer Kern

Die Kartenmatrix bildet eine projektive Ebene der Ordnung 8: 73 Karten, neun Symbole pro Karte, neun Vorkommen jedes Symbols und genau ein gemeinsames Symbol je Kartenpaar. Symbol-ID und Bild sind getrennt; ein Motiv kann später ausgetauscht werden, ohne die Matrix neu zu berechnen.

## Produktionswerkzeug

`cm` bezeichnet ausschließlich [nhmkdev/cardmaker](https://github.com/nhmkdev/cardmaker). Das aktive Projekt liegt unter `tools/cm/` und verwendet eine CSV-Reference mit neun Graphic-Elementen. Rotation sowie Breite und Höhe werden je Karte über `override:[element]:[value]` gesteuert.

Das Layout nutzt 750 × 1050 px bei 300 DPI, entsprechend dem Pokerkartenformat 2,5 × 3,5 Zoll.
