# CM-Validierung

- Zieltool: `nhmkdev/cardmaker` (`cm`)
- Zielversion: `v1.4.0.0`
- Layouts: 1
- Karten: 73
- Bildplätze im Layout: 9
- CSV-Zeilen/Karten: 73; dieselben neun Bildplätze werden je Zeile neu befüllt
- Eindeutige Bildassets: 73
- Endformat: 3,5″ × 5″; 1050 × 1500 px bei 300 dpi
- Vollbeschnitt: 1120 × 1570 px
- Sicherheitsfläche: 975 × 1425 px
- Rotation: bei jeder CardMaker-Übersetzung zufällig von 0° bis 359° um den festen Symbolmittelpunkt
- Skalierung: ein gemeinsamer JavaScript-Zufallswert von ungefähr 95 % bis 105 % steuert Breite und Höhe; X und Y werden relativ zur normalen Elementgeometrie passend nachgeführt
- Bildgröße: positionsabhängige Grundgröße plus ungefähr ±5 % Laufzeitvariation
- Seitenverhältnis: gesperrt (`lockaspect=true`), daher keine Bildverzerrung
- CSV: keine Transformationswerte
- CSV: 11 Spalten (`Count`, `card_id`, neun Bildpfade)
- Bildstatus: 73 farbige, freigestellte ARASAAC-PNGs
- Hintergrund: vollflächig weiß bis in den Beschnitt
- Editorhilfen: rote, ungefüllte Schnitt- und Sicherheitsrahmen; beim Export deaktiviert

Die rechnerischen 657 Bildbelegungen (`73 × 9`) sind keine 657 Layoutplätze oder Dateien. Das CM-Layout definiert nur neun Graphic-Elemente; CardMaker verwendet sie für jede der 73 Karten erneut.

Der Validator verlangt für alle neun Elemente `rotation="0"`, `centerimageonorigin="false"`, den JavaScript-Übersetzer sowie gekoppelte Laufzeit-Overrides für X, Y, Breite, Höhe und Rotation. Zusätzlich prüft er Vollbeschnitt, Schnittfläche, Sicherheitsfläche, weißen Hintergrund, proportionale Symbolgeometrie und exportfreie Editorrahmen.
