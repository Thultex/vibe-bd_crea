# Anleitung Emotronic

## Start

Emotronic wird im Browser über den Ordner `share/apps/emotronic/` geöffnet. Für die Installation als PWA muss die Seite über HTTPS oder lokal über `localhost` bereitgestellt werden.

Nach dem Start ist Emotronic eingeschaltet und zeigt **Bereit**. Eine der neun Gefühlstasten wählt einen Zustand. Die Pfeiltasten ändern die Intensität; Neutral bleibt auf Stufe `0`.

## Bedienung

- Telefon: Eigen-/Telefonseite aktivieren; Doppeltipp teilt konsistent den Replay-Verlauf.
- Wifi/Sender: andere Seite aktivieren; Doppeltipp kopiert konsistent den `#slow`-Direktlink für doppelt langsames Replay.

Beim Verstellen der Intensität auf der Telefon-/Empfängerseite zeigen alle nicht-neutralen Gefühlstasten gemeinsam die passende Emoji-Stufe. Der Hintergrund zeigt nur das angeklickte Gefühl. Auf der Wifi-Senderseite bleibt die Vorschau unverändert; in Simon erscheinen Motiv und Effekt erst beim Drücken.
- Im Wifi-/Sendermodus läuft `>>>` bei jeder Gefühlsbetätigung einschließlich eines erneuten Klicks auf dasselbe Gefühl, bei Intensitätsänderung und beim Aktivieren der Sendertaste.
- `R`: gespeicherte Zustände wiedergeben; erneuter Einzeldruck bricht ab.
- Nach einer vollständigen Wiedergabe bleibt die etwas größere Schrittzahl nahe bei `R` stehen, bis eine neue Gefühlstaste gedrückt wird. Bei Simon zeigt sie am Game Over die Rundenzahl.
- Kombinationstaste: gültige benachbarte Gefühle kombinieren.
- Aus: Gerät aus- oder einschalten; während Replay Verlauf löschen und zu **Bereit** zurückkehren.
- Direktlink `#slow`: normal eingeschaltet starten und Replays doppelt so langsam abspielen; die übrige Bedienung behält ihr normales Tempo.
- Ziffern `7 8 9 / 4 5 6 / 1 2 3`: sichtbare 3×3-Gefühlstasten bedienen.

## Teilen

Gefühle stehen im Fragment `#share=…`, Replays eindeutig in `#replay=…` und Game-over-Scores in `#score=…`. Unter HTTP/HTTPS kopiert Emotronic einen vollständigen Link. Bei lokalen Datei-Adressen wird nur der portable Fragment-Code kopiert.

Jede Person mit dem vollständigen Link kann den enthaltenen Gefühls- oder Replay-Datensatz decodieren. Vertrauliche Inhalte sollten deshalb nicht öffentlich geteilt werden.

## Gedächtnisspiel

Bei ausgeschaltetem Gerät öffnet `R` die Schwierigkeitsauswahl:

- Telefon: Ruhig
- Neutral: Normal
- Wifi: Profi

Die vollständigen Regeln und Funktionsdetails stehen in
[`tools/emotronic-pwa/README.md`](tools/emotronic-pwa/README.md).
