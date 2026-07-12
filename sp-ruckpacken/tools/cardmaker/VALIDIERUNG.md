# CM-Validierung

- Zieltool: `nhmkdev/cardmaker` (`cm`)
- Zielversion: `v1.4.0.0`
- Layouts: 1
- Karten: 73
- Grafiken je Karte: 9
- Bildreferenzen: vollständig
- Kartengröße: 57 × 88 mm; 673 × 1039 px bei 300 DPI
- Rotation: bei jeder CardMaker-Übersetzung zufällig von −20° bis +20°
- Bildgröße: positionsabhängige Grundgröße plus ungefähr ±5 % Laufzeitvariation
- Seitenverhältnis: gesperrt (`lockaspect=true`), daher keine Bildverzerrung
- CSV: keine Transformationswerte
- CSV: 11 Spalten (`Count`, `card_id`, neun Bildpfade)
- Bildstatus: 73 farbige, freigestellte ARASAAC-PNGs

Der Validator verlangt für alle neun Elemente `rotation="0"` sowie die Incept-Overrides mit `#random;min;max#`. Damit fallen erneut hart codierte Drehungen sofort auf.
