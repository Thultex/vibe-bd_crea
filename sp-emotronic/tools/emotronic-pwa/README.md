# Emotronic v1.94

Emotronic ist eine installierbare, offlinefähige PWA zur Auswahl, Darstellung, Kombination und Wiedergabe von Gefühlen. Die Oberfläche ist an ein kompaktes Retro-Handgerät angelehnt und für Touch, Maus und Tastatur ausgelegt.

Die maßgebliche PWA-Quelle liegt unter `sp-emotronic/tools/emotronic-pwa/`. Alle PWA-Pfade sind relativ, sodass dieselben Laufzeitdateien unter `share/apps/emotronic/` als öffentlicher App-Spiegel bereitgestellt werden können.

Wenn GitHub Pages den Branch `main` aus dem Repository-Root veröffentlicht, lautet der PWA-Link:

```text
https://thultex.github.io/vibe-bd_crea/share/apps/emotronic/
```

## Öffentliches Repository und Datenschutz

Das Repository `Thultex/vibe-bd_crea` ist öffentlich. Quelltexte, Dokumentation und Commit-Historie sind daher allgemein einsehbar; private Kontaktangaben, lokale Benutzerpfade und Zugangsdaten gehören nicht in die versionierten Dateien. Bewusste Urheber- und Namensnennungen bleiben davon unberührt.

Emotronic speichert keine Gefühls-, Replay- oder Score-Daten auf einem Server. Gefühle und Replays stehen im URL-Fragment `#share=…`, Game-over-Daten in `#score=…`. Das Fragment wird beim normalen HTTP-Aufruf nicht an den Webserver übertragen, kann aber von jeder Person gelesen und decodiert werden, die den vollständigen Link erhält. Vertrauliche Inhalte sollten deshalb nicht über öffentlich zugängliche Kanäle geteilt werden.

## Schnellstart

1. Den gesamten Ordner auf einen Webserver mit **HTTPS** laden.
2. `index.html` öffnen.
3. Im Browser „Zum Startbildschirm hinzufügen“ beziehungsweise „App installieren“ wählen.
4. Für rein lokale Tests einen lokalen HTTP-Server verwenden. Direkt geöffnete `file://`- oder Android-`content://`-Dateien sind nicht vollwertig teilbar.

Beispiel für einen lokalen Testserver:

```bash
cd sp-emotronic/tools/emotronic-pwa
python3 -m http.server 8080
```

Danach im Browser `http://localhost:8080` öffnen.

## Direktlinks

- Simon-Says-Auswahl: `https://thultex.github.io/vibe-bd_crea/share/apps/emotronic/index.html#simon`
- Normal eingeschaltet: `https://thultex.github.io/vibe-bd_crea/share/apps/emotronic/index.html#on`
- Ausgeschaltet: `https://thultex.github.io/vibe-bd_crea/share/apps/emotronic/index.html#off`

Ohne Modusfragment startet Emotronic wie `#on`.

Ein Druck auf Telefon kopiert in **Bereit**, auf der `Simon Feels!`-Auswahl oder im ausgeschalteten Zustand still den jeweils passenden Direktlink. Dabei erscheint bewusst kein Hinweistext.

## Dateien

| Datei | Zweck |
|---|---|
| `index.html` | Hauptanwendung mit Oberfläche, CSS und JavaScript |
| `Emotronic-v1.94.html` | Versionierte Kopie der Hauptanwendung |
| `manifest.webmanifest` | PWA-Metadaten und Installationskonfiguration |
| `sw.js` | Service Worker für Offline-Cache |
| `icon-192.png`, `icon-512.png` | PWA-Symbole |
| `icon-maskable-512.png` | Maskierbares Android-Symbol |
| `favicon.png`, `apple-touch-icon.png` | Browser- und iOS-Symbole |
| `HANDOFF-CODEX.md` | Technische Übergabe für Codex oder andere Entwickler |
| `README-INSTALLATION.txt` | Kurze Installationshinweise |

## Share-Spiegel

Für die öffentliche PWA werden folgende Laufzeitdateien bytegleich nach `../../../share/apps/emotronic/` gespiegelt:

- `index.html`
- `manifest.webmanifest`
- `sw.js`
- `favicon.png`
- `apple-touch-icon.png`
- `icon-192.png`
- `icon-512.png`
- `icon-maskable-512.png`

Der versionierte Snapshot und die ausführlichen Entwicklungsdokumente bleiben in dieser maßgeblichen Quelle.

## Normalmodus

### Startzustand

- Die App startet eingeschaltet im Zustand **Bereit**.
- Die Intensität ist dabei `0`.
- Standardmäßig ist die Telefonseite aktiv.
- Während des Starts wird kurz der Schriftzug **Emotronic** aufgebaut.
- Zwischen Startanimation und Bereit-Zustand wird kein Neutral-Emoji eingeblendet.

### Gefühle

Die neun Tasten sind wie folgt angeordnet:

| Position | Gefühl |
|---|---|
| oben links | Neugier |
| oben Mitte | Freude |
| oben rechts | Zuneigung |
| Mitte links | Wut |
| Mitte | Neutral |
| Mitte rechts | Angst |
| unten links | Ekel |
| unten Mitte | Trauer |
| unten rechts | Unsicherheit |

Grundemotionen haben drei Intensitätsstufen. Im Telefon-/Selbstmodus bleibt die aktuelle Intensität beim Wechsel zwischen nicht-neutralen Gefühlen erhalten. Im Wifi-Sendemodus beginnt das neue Gefühl nach einem Wechsel wieder auf Mindeststufe `1`. Neutral setzt in beiden Modi auf `0`.

### Intensität

- `–` verringert die Intensität.
- `+` erhöht die Intensität.
- Kombinationen sind fest auf Intensität `3` eingestellt.
- Die Anzeige, Hintergrundfarbe, ASCII-Mimik, OpenMoji-Grafik, Bewegung und Ton reagieren auf die Intensität.

### Gefühls-Kombinationen

Die Kombinationstaste verwendet die aktuell gewählte Grundemotion als ersten Partner. Danach wird eine gültige Nachbar-Emotion gewählt.

| Kombination | Ergebnis |
|---|---|
| Freude + Zuneigung | verliebt |
| Freude + Neugier | lustig |
| Neugier + Wut | streitlustig |
| Zuneigung + Angst | starr |
| Ekel + Wut | abwertend |
| Trauer + Ekel | bereuend |
| Angst + Unsicherheit | genervt |
| Unsicherheit + Trauer | verlegen |

Die Animation von **starr** ist eine kurze Rückzugs- und Erstarrbewegung.

### Telefon und Wifi

- **Telefon** aktiviert den Telefon-/Eigenmodus und zeigt eine zentrierte Klingelanimation.
- **Wifi** aktiviert die andere Seite. Bei neu ausgewählten Gefühlen kann dort die `>>>`-Sendeanimation erscheinen.
- Ein einfacher Telefon-Tipp zeigt unter der kleinen Emotionsanzeige `Gefühl teilen: Zweimal ☎ klicken.`.
- Ein einfacher Wifi-Tipp zeigt dort `Replay teilen: Zweimal 📶 klicken.`.
- Die normale Auswahlfunktion bleibt auch bei einem Doppeltipp erhalten.

### Verlauf und Replay

- Jede neue gültige Gefühlsauswahl wird in einem Verlauf gespeichert.
- Eine anschließende Intensitätsänderung aktualisiert diesen letzten Schritt, statt zusätzliche Zwischenstufen zu speichern.
- Ein erneuter Klick auf dieselbe Gefühlstaste speichert bewusst einen weiteren Schritt, auch wenn Gefühl und Intensität gleich bleiben.
- Replay-Start und Replay-Sharing fügen den bereits aktuellen Zustand nicht nochmals hinzu.
- Maximal 40 Zustände werden gehalten.
- **Bereit** wird nie als Replay-Schritt gespeichert.
- `R` startet den Replay-Verlauf.
- Während des Replays zeigt eine kleine graue Zahl neben `R`, wie viele Zustände noch offen sind.
- Im normalen Replay werden Gefühl, Emotion und Intensität mit einem sehr leichten Fade aus- und anschließend wieder eingeblendet, damit nur die Wiedergabe selbst im Mittelpunkt steht.
- Ein empfangenes Replay beginnt direkt mit seinem ersten Schritt, ohne zuvor kurz den gespeicherten Endzustand einzublenden.
- `R` während des Replays bricht nur die Wiedergabe ab und zeigt wieder den neuesten Zustand.
- **Aus** während des Replays bricht ab, leert den Verlauf und geht direkt zu **Bereit**.
- Ein normaler Neustart leert den Replay-Verlauf vollständig.

## Sharing

Emotronic speichert geteilte Daten ausschließlich im URL-Fragment. Gefühle und Replays verwenden `#share=`, Game-over-Scores verwenden `#score=`. Dadurch werden die Daten nicht automatisch an einen Server übertragen.

### Gefühl teilen

- Telefon zweimal kurz tippen.
- Das aktuelle Gefühl wird als Share-Datensatz kopiert.
- Unter `http://` oder `https://` wird ein vollständiger anklickbarer Link erzeugt.
- Unter `file://` oder Android-`content://` wird nur der portable `#share=…`-Code kopiert, weil diese lokalen Adressen in anderen Browsern oder Geräten nicht funktionieren.

### Replay teilen

- Wifi zweimal kurz tippen.
- Der aktuelle Verlauf mit bis zu 40 Zuständen wird kopiert.
- Bei Intensitätsänderungen enthält der Verlauf nur die zuletzt eingestellte Stufe; wiederholte Gefühlsklicks bleiben als einzelne Schritte erhalten.
- Unter `http://` oder `https://` entsteht ein vollständiger Link.
- Bei lokalen Dateiadressen entsteht ein portabler Share-Code.

### Rückmeldung

Die kleine Zeile unter dem Gefühlsnamen zeigt kurz eine der folgenden Meldungen:

- `Gefühl-Link kopiert`
- `Replay-Link kopiert`
- `Gefühl-Code kopiert`
- `Replay-Code kopiert`
- eine verständliche Fehlermeldung, falls die Zwischenablage blockiert ist

### Link öffnen

Beim Öffnen eines gültigen Share-Links:

- erscheint zuerst die ruhig weiterlaufende Nachrichtenanimation,
- ein Tipp auf Bildschirm oder eine Taste außer Aus öffnet Gefühl, Replay oder Score,
- nach diesem Tipp wartet die App rund 0,1 Sekunden, bevor Gefühl, Replay oder Score tatsächlich starten,
- Aus bricht den Empfang ab,
- ein geteilter Score zeigt in der Warteanimation zusätzlich klein den OpenMoji-Pokal `1F3C6` und die Punktzahl.

Die Zwischenablage verwendet zuerst die moderne Clipboard API und danach einen klassischen Android-kompatiblen Fallback. Ein Kopierfehler darf die übrige App-Funktion nicht unterbrechen.

## Gedächtnisspiel

Das Gedächtnisspiel wird bei ausgeschaltetem Gerät über die farbige OpenMoji-Videokassette `1F4FC` auf der sonstigen `R`-Taste geöffnet. Zuerst erscheint die Schwierigkeitsauswahl. Der Aus-Knopf trägt das farbige OpenMoji-Symbol `1F50D`.

Beim Einstieg baut sich oben `Simon Feels!` in derselben Schriftgröße wie die normale Introanzeige auf und ein kurzer Startjingle erklingt. Die Auswahl bleibt dabei sofort bedienbar; jede Spielaktion beendet den Titelaufbau. Der Direktlink `#simon` wartet zunächst auf einem weißen Bildschirm mit dem farbigen OpenMoji-Controller `1F3AE` auf einen Tipp, damit Animation und Ton erst nach dieser Interaktion starten.

### Schwierigkeitsgrade

| Auswahl | Modus | Eigenschaften |
|---|---|---|
| Neugier | Leicht | langsamer, 3 Leben, Wiederholen erlaubt |
| Neutral | Normal | Standardtempo, 1 Leben |
| Unsicherheit | Profi | schneller, Start bei 5 Punkten, 25 % Endbonus |

### Spielablauf

1. Die App zeigt eine Folge von Gefühlstasten.
2. Der Spieler tippt dieselbe Folge nach.
3. Nach einer korrekten Runde beginnt automatisch die nächste.
4. Es gibt kein Eingabe-Zeitlimit.
5. Die Folge wird bis Punkt 5 gleich schnell gezeigt und danach schrittweise bis Punkt 20 beschleunigt.
6. Die letzte Taste kann bereits während ihres Ausblendens eingegeben werden.

### Intensität im Spiel

- Schritte 1 bis 5 verwenden Intensität 1.
- Ab 5 Punkten werden neu hinzugefügte Schritte mit Intensität 2 gespeichert.
- Ab 10 Punkten werden neu hinzugefügte Schritte mit Intensität 3 gespeichert.
- Frühere Schritte behalten ihre ursprüngliche Intensität.

### Kombis im Spiel

- Im Profi-Modus können Kombinationen ab 5 Punkten auftreten.
- In den anderen Modi beginnen Kombinationen später.
- Bis 10 Punkte ist im Profi-Modus höchstens eine Kombination in der Folge erlaubt.
- Eine Kombination wird als zwei aufeinanderfolgende Emotionen gezeigt; die zweite Taste zeigt anschließend das Kombi-Emoji.
- Der Spieler gibt dieselben zwei Emotionen ein.

### Leben, Bonus und Spielende

- Ruhig startet mit 3 Leben; Normal und Profi mit 1 Leben.
- Ein sichtbares Herz entspricht einem erlaubten Fehler.
- Nach dem Verlust des letzten sichtbaren Herzens darf mit 0 Herzen weitergespielt werden; der nächste Fehler beendet das Spiel.
- Beim Lebensverlust erscheinen eine große Herzanimation und ein eigener Ton.
- Der Geschafft-Jingle beginnt rund 0,2 Sekunden nach dem letzten korrekten Tastendruck, damit beide Töne klarer getrennt bleiben.
- Bei 10, 20, 30 usw. Punkten wird ein zusätzliches Leben vergeben.
- Alle 5 Punkte läuft eine Kirby-artige Retro-Bonusanimation; ab 10 Punkten stehen zusätzliche Varianten bereit.
- Bei Spielende werden Punktzahl und Leistungs-Kommentar angezeigt.
- Im Profi-Modus wird die Endpunktzahl mit 25 % Bonus berechnet.
- Beim Game Over wird ein Link mit Score, Modus und vollständiger gespielter Folge automatisch in die Zwischenablage kopiert, soweit der Browser dies zulässt.
- Telefon kopiert denselben Score-Link auf dem Game-Over-Bildschirm erneut manuell.
- Game-over-Links verwenden ausschließlich `#score=…`; `#share=…` akzeptiert nur Gefühle und Replays.
- Die Telefontaste bleibt dafür am Game Over sichtbar bedienbar.
- Nach dem Öffnen eines Score-Links startet die gespeicherte Folge automatisch. Währenddessen steht links die Punktzahl und darunter `Replay · Abbruch bei Klick auf irgendeine Taste`; jeder Tastenklick kehrt sofort zum Game Over zurück.

### Steuerung im Spiel

- `R` während einer Runde fordert `NEUSTART?` an; ein zweites `R` bestätigt.
- Nach Game Over spielt `R` die vollständige gespielte Folge erneut ab und kehrt anschließend zum Score zurück.
- Während dieses Score-Replays werden die drei Modustasten wieder als normale Gefühle dargestellt und wie die übrigen inaktiven Tasten abgedunkelt.
- **Aus** fordert `AUS?` an; ein zweiter Druck bestätigt.
- Nach Game Over reagieren `R`, Telefon und **Aus**.
- Nach Game Over bleiben Neugier, Neutral und Unsicherheit als direkte Auswahl für Leicht, Normal und Profi sichtbar.
- Die Hinweise nennen dort die drei Modi sowie `R: Replay` und `⏻: Schluss`.
- **Aus** führt vom Game Over zunächst zurück zur Simon-Titelauswahl; dort schaltet **Aus** die App direkt aus.
- `R` auf der Simon-Titelauswahl kehrt zum zuletzt gespeicherten Game-over-Bildschirm zurück; ohne vorheriges Game Over geschieht nichts.

## Ton

- Jede Grundemotion hat eigene 8-Bit-Klangfolgen je Intensität.
- Kombinationen, Erfolg, Fehler, Lebensverlust, Lebensgewinn sowie Ein- und Ausschalten haben eigene Signale.
- Der Ton ist optional und über `APP_CONFIG.audio` abschaltbar.
- Fehlt Web Audio oder blockiert der Browser Audio, läuft die App ohne Funktionsverlust weiter.

## Tastatur

Die Ziffern entsprechen der sichtbaren 3×3-Anordnung:

```text
7 8 9
4 5 6
1 2 3
```

Damit lassen sich die neun Emotionen auch über Haupttastatur oder Ziffernblock bedienen.

## Zentrale Konfiguration

Ganz oben im JavaScript stehen:

1. `APP_META` mit Name, Version, Revision und Autor.
2. `APP_CONFIG` mit Start, Audio, Normalmodus, Replay, Bestätigungen und Spielparametern.
3. Danach die Datentabellen für Ressourcen, Grundemotionen, Kombinationen und Sounds.

Diese Reihenfolge soll bei weiteren Änderungen erhalten bleiben.

## Offline/PWA

- Der Service Worker cached die Kernressourcen.
- Die aktuelle Cache-Version lautet `emotronic-v94`.
- Beim Aktivieren werden nur ältere Emotronic-Caches entfernt; Caches anderer Anwendungen auf derselben Domain bleiben erhalten.
- Nicht gecachte GET-Anfragen werden aus dem Netz geladen und anschließend gespeichert.
- Bei einem Netzfehler wird als Fallback `index.html` verwendet.

## Drittmaterial

Wo es gestalterisch und semantisch passt, sind OpenMoji-Grafiken gegenüber plattformabhängigen Emoji-Zeichen zu bevorzugen. Dazu gehören derzeit insbesondere der Controller `1F3AE`, die Videokassette `1F4FC`, das Symbol `1F50D` auf dem Aus-Knopf und der Pokal `1F3C6`. Bedienbare Kernfunktionen behalten einen einfachen Text- oder ASCII-Fallback. Copyright und Lizenzbedingungen von OpenMoji sind zu beachten. Die App zeigt beim Start `(c) OpenMoji` an.
