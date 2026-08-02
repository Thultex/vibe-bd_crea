# Anleitung Emotronic

## Start

Emotronic wird im Browser über den Ordner `share/apps/emotronic/` geöffnet. Für die Installation als PWA muss die Seite über HTTPS oder lokal über `localhost` bereitgestellt werden.

Nach dem Start ist Emotronic eingeschaltet und zeigt **Bereit**. Eine der neun Gefühlstasten wählt einen Zustand. Die Pfeiltasten ändern die Intensität; Neutral bleibt auf Stufe `0`.

Das an der Y-Achse gespiegelte Rad liegt sichtbar als `Freude · Zuneigung · Neugier / Wut · Neutral · Angst / Ekel · Scham · Trauer`. Emojis, Pastellfarben und Zifferntasten sind gemeinsam gespiegelt.

## Bedienung

- Telefon: Eigen-/Telefonseite aktivieren; Doppeltipp teilt konsistent den Replay-Verlauf.
- Wifi/Sender: andere Seite aktivieren; Doppeltipp teilt den vollständigen aktuellen Replay-Verlauf mit aktivierter langsamer Wiedergabe.

Beim Verstellen der Intensität auf der Telefon-/Empfängerseite zeigen alle nicht-neutralen Gefühlstasten gemeinsam die passende Emoji-Stufe. Der Hintergrund zeigt nur das angeklickte Gefühl. Auf der Wifi-Senderseite bleibt die Vorschau unverändert; in Simon erscheinen Motiv und Effekt erst beim Drücken.
- Im Wifi-/Sendermodus läuft `>>>` bei jeder Gefühlsbetätigung einschließlich eines erneuten Klicks auf dasselbe Gefühl, bei Intensitätsänderung und beim Aktivieren der Sendertaste.
- `R`: gespeicherte Zustände wiedergeben; erneuter Einzeldruck bricht ab.
- Nach einer vollständigen Wiedergabe bleibt die etwas größere Schrittzahl nahe bei `R` stehen, bis eine neue Gefühlstaste gedrückt wird. Bei Simon zeigt sie am Game Over die Rundenzahl.
- Kombinationstaste: gültige benachbarte Gefühle kombinieren.
- Aus: Der erste Druck löscht den Replay-Verlauf und wechselt zu **Bereit**; der zweite Druck schaltet aus. Neutral kann beliebig oft gewählt werden.
- Im ausgeschalteten Zustand ist auch die Kombi-Taste deaktiviert und ohne Symbol; nach dem Einschalten steht sie wieder zur Verfügung. Joystick und Lupe neben `R` und der Aus-Taste erscheinen erst, wenn der Ausschaltprozess vollständig beendet ist.
- Ein empfangener Slow-Replay-Link enthält denselben unveränderten Verlauf wie ein normaler Replay-Link. Nur dessen Wiedergabe läuft langsamer; eine neue Gefühlseingabe beendet den Slow-Zustand.
- Ziffern `7 8 9 / 4 5 6 / 1 2 3`: sichtbare 3×3-Gefühlstasten bedienen.

## Teilen

Neue Kurzlinks verwenden `#e=…` für Gefühle, `#r=…` für normale Replays, `#s=…` für langsame Replays und `#g=…` für Game-over-Scores. Ein Zeichen codiert jeweils einen Zustand samt Intensität oder Kombination; bei Slow muss nur `r` durch `s` ersetzt werden. Alte lange Links bleiben lesbar. Unter HTTP/HTTPS kopiert Emotronic einen vollständigen Link, bei lokalen Datei-Adressen nur den portablen Fragment-Code. Der normale Replay-Verlauf hält höchstens 24 Schritte und entfernt bei neuer Eingabe den ältesten; Simon ist davon nicht betroffen.

Jede Person mit dem vollständigen Link kann den enthaltenen Gefühls- oder Replay-Datensatz decodieren. Vertrauliche Inhalte sollten deshalb nicht öffentlich geteilt werden.

## Gedächtnisspiel

Bei ausgeschaltetem Gerät öffnet `R` die Schwierigkeitsauswahl:

- Freude: Leicht
- Neutral: Normal
- Trauer: Profi

Die vollständigen Regeln und Funktionsdetails stehen in
[`tools/emotronic-pwa/README.md`](tools/emotronic-pwa/README.md).
