# Ruckpacken – Design v1.00

## Material

- 73 Symbolkarten im Format 57 × 88 mm
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

`cm` bezeichnet ausschließlich [nhmkdev/cardmaker](https://github.com/nhmkdev/cardmaker). Das aktive Projekt liegt unter `tools/cardmaker/` und verwendet eine schlanke CSV-Reference mit neun Bildpfaden. Position, Größe und Drehung der neun Graphic-Elemente sind im CM-Projekt gespeichert und nicht Teil der CSV.

Das Layout nutzt 673 × 1039 px bei 300 DPI, entsprechend 57 × 88 mm. Die organische Raute verwendet drei Größenstufen; die neun leichten Drehungen sind einmalig pseudo-zufällig festgelegt.
