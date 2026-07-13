# CM-Validierung

- Zieltool: `nhmkdev/cardmaker` (`cm`)
- Zielversion: `v1.4.0.0`
- Layouts: 1
- Karten: 73
- Grafiken je Karte: 9
- Bildreferenzen: vollständig
- Endformat: 3,5″ × 5″; 1050 × 1500 px bei 300 dpi
- Vollbeschnitt: 1120 × 1570 px
- Sicherheitsfläche: 975 × 1425 px
- Rotation: bei jeder CardMaker-Übersetzung zufällig von 0° bis 359°
- Bildgröße: positionsabhängige Grundgröße plus ungefähr ±5 % Laufzeitvariation
- Seitenverhältnis: gesperrt (`lockaspect=true`), daher keine Bildverzerrung
- CSV: keine Transformationswerte
- CSV: 11 Spalten (`Count`, `card_id`, neun Bildpfade)
- Bildstatus: 73 farbige, freigestellte ARASAAC-PNGs
- Hintergrund: vollflächig weiß bis in den Beschnitt
- Editorhilfen: rote, ungefüllte Schnitt- und Sicherheitsrahmen; beim Export deaktiviert

Der Validator verlangt für alle neun Elemente `rotation="0"` sowie die Incept-Overrides mit `#random;min;max#`. Zusätzlich prüft er Vollbeschnitt, Schnittfläche, Sicherheitsfläche, weißen Hintergrund, proportionale Symbolgeometrie und exportfreie Editorrahmen.
