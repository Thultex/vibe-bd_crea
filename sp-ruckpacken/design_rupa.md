# Ruckpacken – Design v1.00

## Material

- 73 Symbolkarten im Endformat 3,5″ × 5″ (89 × 127 mm)
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

Die Mitte ist größer als Innen- und Außenpositionen. Einzelne Symbole erhalten beim Rendering eine zufällige Orientierung über 360° und bis ungefähr ±5 % Größenvariation. Karten dürfen als Ganzes gedreht und so überlappt werden, dass drei bis sechs Symbole verschwinden.

## Mathematischer Kern

Die Kartenmatrix bildet eine projektive Ebene der Ordnung 8: 73 Karten, neun Symbole pro Karte, neun Vorkommen jedes Symbols und genau ein gemeinsames Symbol je Kartenpaar. Symbol-ID und Bild sind getrennt; ein Motiv kann später ausgetauscht werden, ohne die Matrix neu zu berechnen.

## Produktionswerkzeug

`cm` bezeichnet ausschließlich [nhmkdev/cardmaker](https://github.com/nhmkdev/cardmaker). Das aktive Projekt liegt unter `tools/cardmaker/` und verwendet eine schlanke CSV-Reference mit neun Bildpfaden. Position und Grundgröße der neun Graphic-Elemente sind im CM-Projekt gespeichert; Transformationswerte sind nicht Teil der CSV.

Das Layout folgt dem [MPC-Jumboformat](https://www.makeplayingcards.com/design/custom-3-5-x-5-game-cards.html): 1050 × 1500 px Schnittfläche und 1120 × 1570 px Vollbeschnitt bei 300 dpi. Der weiße Hintergrund reicht bis zum Außenrand. Rote, ungefüllte Rahmen zeigen im Editor Schnitt- und Sicherheitsfläche und werden nicht exportiert.

Die organische Raute verwendet drei Größenstufen. Abstände zur Kartenmitte werden für X und Y getrennt proportional auf die neue Schnittfläche skaliert; die Symbolgrößen folgen dem kleineren Skalierungsfaktor. CardMakers JavaScript-Übersetzer erzeugt pro Rendering und Symbol eine Drehung von 0° bis 359° sowie eine einheitliche Größenvariation von ungefähr ±5 %. Die zugehörigen X-/Y-Werte werden aus demselben Größenwert neu berechnet, sodass Mittelpunkt und Seitenverhältnis erhalten bleiben.
