# Anleitung Emotronic

## Start

Emotronic wird im Browser über den Ordner `share/apps/emotronic/` geöffnet. Für die Installation als PWA muss die Seite über HTTPS oder lokal über `localhost` bereitgestellt werden.

Nach dem Start ist Emotronic eingeschaltet und zeigt **Bereit**. Eine der neun Gefühlstasten wählt einen Zustand. Die Pfeiltasten ändern die Intensität; Neutral bleibt auf Stufe `0`.

## Bedienung

- Telefon: Eigen-/Telefonseite aktivieren; Doppeltipp teilt das aktuelle Gefühl.
- Wifi: andere Seite aktivieren; Doppeltipp teilt den Replay-Verlauf.
- `R`: gespeicherte Zustände wiedergeben; erneuter Einzeldruck bricht ab.
- Kombinationstaste: gültige benachbarte Gefühle kombinieren.
- Aus: Gerät aus- oder einschalten; während Replay Verlauf löschen und zu **Bereit** zurückkehren.
- Ziffern `7 8 9 / 4 5 6 / 1 2 3`: sichtbare 3×3-Gefühlstasten bedienen.

## Teilen

Gefühle und Replays stehen im Fragment `#share=…`, Game-over-Scores in `#score=…`. Unter HTTP/HTTPS kopiert Emotronic einen vollständigen Link. Bei lokalen Datei-Adressen wird nur der portable Fragment-Code kopiert.

Jede Person mit dem vollständigen Link kann den enthaltenen Gefühls- oder Replay-Datensatz decodieren. Vertrauliche Inhalte sollten deshalb nicht öffentlich geteilt werden.

## Gedächtnisspiel

Bei ausgeschaltetem Gerät öffnet `R` die Schwierigkeitsauswahl:

- Telefon: Ruhig
- Neutral: Normal
- Wifi: Profi

Die vollständigen Regeln und Funktionsdetails stehen in
[`tools/emotronic-pwa/README.md`](tools/emotronic-pwa/README.md).
