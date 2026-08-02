# Emotronic v2.27

Emotronic ist eine installierbare, offlinefähige PWA zur Auswahl, Darstellung, Kombination und Wiedergabe von Gefühlen. Die Oberfläche ist an ein kompaktes Retro-Handgerät angelehnt und für Touch, Maus und Tastatur ausgelegt.

Die maßgebliche PWA-Quelle liegt unter `sp-emotron/tools/emotronic-pwa/`. Alle PWA-Pfade sind relativ, sodass dieselben Laufzeitdateien unter `share/apps/emotronic/` als öffentlicher App-Spiegel bereitgestellt werden können.

Wenn GitHub Pages den Branch `main` aus dem Repository-Root veröffentlicht, lautet der PWA-Link:

```text
https://thultex.github.io/vibe-bd_crea/share/apps/emotronic/
```

## Öffentliches Repository und Datenschutz

Das Repository `Thultex/vibe-bd_crea` ist öffentlich. Quelltexte, Dokumentation und Commit-Historie sind daher allgemein einsehbar; private Kontaktangaben, lokale Benutzerpfade und Zugangsdaten gehören nicht in die versionierten Dateien. Bewusste Urheber- und Namensnennungen bleiben davon unberührt.

Emotronic speichert keine Gefühls-, Replay- oder Score-Daten auf einem Server. Neue Links verwenden die kurzen Fragmente `#e=…`, `#r=…`, `#s=…` und `#g=…`; alte lange Formate bleiben lesbar. Das Fragment wird beim normalen HTTP-Aufruf nicht an den Webserver übertragen, kann aber von jeder Person gelesen und decodiert werden, die den vollständigen Link erhält. Vertrauliche Inhalte sollten deshalb nicht über öffentlich zugängliche Kanäle geteilt werden.

## Schnellstart

1. Den gesamten Ordner auf einen Webserver mit **HTTPS** laden.
2. `index.html` öffnen.
3. Im Browser „Zum Startbildschirm hinzufügen“ beziehungsweise „App installieren“ wählen.
4. Für rein lokale Tests einen lokalen HTTP-Server verwenden. Direkt geöffnete `file://`- oder Android-`content://`-Dateien sind nicht vollwertig teilbar.

Beispiel für einen lokalen Testserver:

```bash
cd sp-emotron/tools/emotronic-pwa
python3 -m http.server 8080
```

Danach im Browser `http://localhost:8080` öffnen.

## Direktlinks

- Simon-Says-Auswahl: `https://thultex.github.io/vibe-bd_crea/share/apps/emotronic/index.html#simon`
- Normal eingeschaltet: `https://thultex.github.io/vibe-bd_crea/share/apps/emotronic/index.html#on`
- Ausgeschaltet: `https://thultex.github.io/vibe-bd_crea/share/apps/emotronic/index.html#off`

Ohne Modusfragment startet Emotronic wie `#on`. `#s=…` ist der langsame Tag eines vollständigen Replay-Links: Sein Datenteil ist identisch zu `#r=…`, sodass man zwischen beiden Tempi durch Ersetzen des Tag-Buchstabens umschalten kann.

Ein Druck auf Telefon kopiert in **Bereit**, auf der `Simon Feels!`-Auswahl oder im ausgeschalteten Zustand still den jeweils passenden Direktlink. Dabei erscheint bewusst kein Hinweistext.

## Dateien

| Datei | Zweck |
|---|---|
| `index.html` | Hauptanwendung mit Oberfläche, CSS und JavaScript |
| `Emotronic-v2.27.html` | Versionierte Kopie der Hauptanwendung |
| `manifest.webmanifest` | PWA-Metadaten und Installationskonfiguration |
| `sw.js` | Service Worker für Offline-Cache |
| `icon-192.png`, `icon-512.png` | PWA-Symbole |
| `icon-maskable-512.png` | Maskierbares Android-Symbol |
| `favicon.png`, `apple-touch-icon.png` | Browser- und iOS-Symbole |
| `HANDOFF-CODEX.md` | Technische Übergabe für Codex oder andere Entwickler |
| `README-INSTALLATION.txt` | Kurze Installationshinweise |
| `validate_emotronic.js` | Gesamtprüfung von Modell, Spiegelung, Emojis, Audio, Version und Laufzeitspiegel |

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
| oben links | Freude |
| oben Mitte | Zuneigung |
| oben rechts | Neugier |
| Mitte links | Wut |
| Mitte | Neutral |
| Mitte rechts | Angst |
| unten links | Ekel |
| unten Mitte | Scham |
| unten rechts | Trauer |

Die vollständige Anordnung einschließlich Emojis, Beschriftungen und Farben ist gegenüber der ersten Neufassung an der Y-Achse gespiegelt.

Die acht Grundzweige verwenden kurze Adjektive und jeweils drei eindeutige OpenMoji-Motive:

| Grundemotion | schwach | mittel | stark |
|---|---|---|---|
| Neugier | interessiert | neugierig | fasziniert |
| Zuneigung | freundlich | zugewandt | verbunden |
| Freude | zufrieden | fröhlich | begeistert |
| Wut | gereizt | verärgert | wütend |
| Ekel | abgeneigt | angeekelt | übel |
| Scham | verlegen | befangen | beschämt |
| Trauer | bedrückt | traurig | trauernd |
| Angst | besorgt | ängstlich | panisch |

Die Basisfarben stammen aus der bisherigen Pastellpalette und werden wie zuvor für die drei Intensitäten aufgehellt beziehungsweise abgedunkelt. Wut bleibt rot, Freude gelb, Scham grün, Trauer blau, Angst lavendel, Ekel dunkelgrün, Zuneigung orange und Neugier türkis.

Grundemotionen haben drei Intensitätsstufen. Im Telefon-/Selbstmodus bleibt die aktuelle Intensität beim Wechsel zwischen nicht-neutralen Gefühlen erhalten. Im Wifi-Sendemodus beginnt das neue Gefühl nach einem Wechsel wieder auf Mindeststufe `1`. Neutral setzt in beiden Modi auf `0`.

Im Telefon-/Empfängermodus zeigen alle nicht-neutralen Gefühlstasten die OpenMoji-Variante der aktuell eingestellten Intensität. So ist beim Verstellen sofort die gesamte Auswahl für diese Stufe sichtbar. Der große Display-Hintergrund zeigt weiterhin nur das tatsächlich gewählte Gefühl. Im Wifi-Sendemodus bleibt die Intensitätsdarstellung auf die ausgewählte Taste beschränkt; in Simon erscheinen Intensitätsmotiv und dramaturgischer Effekt weiterhin erst mit dem jeweiligen Tastendruck.

### Intensität

- `–` verringert die Intensität.
- `+` erhöht die Intensität.
- Kombinationen sind fest auf Intensität `3` eingestellt.
- Die Anzeige, Hintergrundfarbe, ASCII-Mimik, OpenMoji-Grafik, Bewegung und Ton reagieren auf die Intensität.
- Beim Intensitätswechsel überblenden alle nicht-neutralen Empfängertasten und die aktuelle Wifi-Sendertaste das alte und neue Emoji direkt miteinander. Die Gesamtdauer ist über `APP_CONFIG.normalMode.keypadCrossfadeMs` definierbar und beträgt standardmäßig 0,15 Sekunden. Das neue Motiv wird innerhalb von rund 0,12 Sekunden vollständig sichtbar; das alte beginnt nach etwa 0,08 Sekunden weich auszufaden und verschwindet bis zum Ende. So entstehen weder ein Transparenzknick in der Mitte noch ein harter Sprung am Schluss. Bewegung und Überblendung laufen unabhängig voneinander. Andere Sendertasten und der Display-Hintergrund behalten ihre bisherige Reaktion.
- Während SVGs wechseln, bleibt insbesondere auf der aktiven Taste das alte Motiv bis zum erfolgreichen Laden des neuen sichtbar. Alternativtext und große grafische Textplatzhalter werden dort nicht eingeblendet; die normale kleine Tastenbeschriftung bleibt als bedienbarer Fallback erhalten.

### Gefühls-Kombinationen

Die Kombinationstaste verwendet die aktuell gewählte Grundemotion als ersten Partner. Danach wird eine gültige Nachbar-Emotion gewählt. Während die Kombi-Taste aktiv ist, zeigen die gültigen gestrichelt markierten Nachbartasten bereits das jeweils entstehende Kombi-Emoji und dessen Kombinationsnamen.

Im Zustand **Bereit**, also ohne gewähltes Gefühl, sowie bei gewähltem Neutral zeigt die Kombi-Taste stattdessen alle acht Kombinationen auf den äußeren Gefühlstasten. Jede Taste zeigt den Übergang von ihrem gegen den Uhrzeigersinn benachbarten Zweig; zusammen ergibt sich die vollständige Übersicht des neuen Emotionsrads. Beim Öffnen aus Neutral wird dieser aktuelle Neutral-Schritt aus dem Replay entfernt und der Grundzustand intern zu Bereit; frühere Replay-Schritte bleiben erhalten. Ein Tipp wählt die Kombination auf der jeweiligen Taste aus. Beim Abbruch kehren alle Vorschauen zu ihren Grund-Emojis und übergeordneten Emotionsnamen zurück. Nach einer gültigen Wahl behält nur die gewählte Taste das nun echte Kombi-Emoji samt Namen. Im normalen Modus bleiben die Beschriftungen unverändert bei den übergeordneten Emotionen, da deren Motive lediglich Intensitätsabstufungen darstellen.

| Kombination | Ergebnis | Übersicht auf |
|---|---|---|
| Neugier + Zuneigung | Bewunderung | Zuneigung |
| Zuneigung + Freude | Dankbarkeit | Freude |
| Freude + Wut | Streitlust | Wut |
| Wut + Ekel | Abwertung | Ekel |
| Ekel + Scham | Unbehagen | Scham |
| Scham + Trauer | Reue | Trauer |
| Trauer + Angst | Aufgeben | Angst |
| Angst + Neugier | Überraschung | Neugier |

Jede Kombination übernimmt eine zu ihrer Bedeutung passende Bewegung aus den benachbarten Grundzweigen.

### Telefon und Wifi

- **Telefon** aktiviert den Telefon-/Eigenmodus und zeigt eine zentrierte Klingelanimation.
- **Wifi** aktiviert die andere Seite. Bei neu ausgewählten Gefühlen kann dort die `>>>`-Sendeanimation erscheinen.
- Im Wifi-/Sendermodus startet `>>>` außerdem beim erneuten Klick auf dasselbe Gefühl, bei einer tatsächlichen Intensitätsänderung und unmittelbar beim Aktivieren der Wifi-/Sendertaste.
- Ein einfacher Telefon-Tipp zeigt unter der kleinen Emotionsanzeige `Replay teilen: Zweimal ☎ klicken.`.
- Ein einfacher Wifi-Tipp zeigt dort `Slow-Replay teilen: Zweimal 📶 klicken.`.
- Die normale Auswahlfunktion bleibt auch bei einem Doppeltipp erhalten.

### Verlauf und Replay

- Jede neue gültige Gefühlsauswahl wird in einem Verlauf gespeichert.
- Eine anschließende Intensitätsänderung aktualisiert diesen letzten Schritt, statt zusätzliche Zwischenstufen zu speichern.
- Ein erneuter Klick auf dieselbe Gefühlstaste speichert bewusst einen weiteren Schritt, auch wenn Gefühl und Intensität gleich bleiben.
- Replay-Start und Replay-Sharing fügen den bereits aktuellen Zustand nicht nochmals hinzu.
- Maximal 24 Zustände werden gehalten. Bei einer neuen Eingabe im vollen Verlauf fällt jeweils der älteste Schritt heraus; Simon verwendet weiterhin seine eigene unbegrenzte Spielfolge.
- **Bereit** wird nie als Replay-Schritt gespeichert.
- `R` startet den Replay-Verlauf.
- Ein über `#s=…` empfangener Replay-Datensatz läuft mit doppelter Dauer pro Schritt; seine Emoji-Bewegung ist nur 15 Prozent langsamer. Eine neue Gefühl-, Intensitäts- oder Kombi-Eingabe beendet die Slow-Markierung.
- Während des Replays zeigt eine kleine graue Zahl neben `R`, wie viele Zustände noch offen sind.
- Nach der vollständigen Wiedergabe bleibt dort die Gesamtzahl der Schritte als Hinweis stehen, dass `R` dasselbe Replay erneut abspielt. Das gilt automatisch auch nach einem empfangenen Replay, da beide denselben Wiedergabeweg nutzen.
- Die Zahl ist etwas größer und näher an `R` positioniert. Erst eine neue Gefühlstaste blendet sie mit derselben weichen Deckkraft-/Skalierungsbewegung wie die Hinweise im Ausschaltzustand aus.
- Im normalen Replay werden Gefühl, Emotion und Intensität mit einem sehr leichten Fade aus- und anschließend wieder eingeblendet, damit nur die Wiedergabe selbst im Mittelpunkt steht.
- Ein empfangenes Replay beginnt direkt mit seinem ersten Schritt, ohne zuvor kurz den gespeicherten Endzustand einzublenden.
- `R` während des Replays bricht nur die Wiedergabe ab, zeigt wieder den neuesten Zustand und behält die Gesamtzahl als erneuten Replay-Hinweis bei.
- Der erste Druck auf **Aus** bricht gegebenenfalls ein Replay ab, leert den gesamten Verlauf und wechselt zu **Bereit**. Neutral bleibt dabei unberührt und kann beliebig oft gewählt werden.
- Ein zweiter Druck innerhalb des Bestätigungsfensters schaltet das Gerät aus.
- Ein normaler Neustart leert den Replay-Verlauf vollständig.
- Bei ausgeschaltetem Gerät ist auch die Kombi-Taste deaktiviert und ihr Symbol ausgeblendet; nach der Einschaltsequenz erscheint und funktioniert sie wieder.

## Sharing

Emotronic speichert geteilte Daten ausschließlich im URL-Fragment. Neue Links verwenden `#e=` für ein Gefühl, `#r=` für Replays, `#s=` für langsame Replays und `#g=` für Game-over-Scores. Jeder Gefühlszustand benötigt nur ein Base36-Zeichen; Intensität und Kombination sind darin bereits codiert. Die alten Formate `#share=`, `#replay=`, `#slow=` und `#score=` bleiben lesbar. Dadurch werden die Daten nicht automatisch an einen Server übertragen.

### Slow-Replay-Link teilen

- Wifi/Sender zweimal kurz tippen.
- Der vollständige aktuelle Replay-Verlauf wird unverändert unter dem Tag `#s=…` kopiert.
- Die codierten Daten sind dieselben wie bei `#r=…`; im Link muss nur `r` gegen `s` getauscht werden.
- Unter `http://` oder `https://` wird ein vollständiger anklickbarer `#s=…`-Link erzeugt; bei einer lokalen Datei wird der portable `#s=…`-Code kopiert.

### Replay teilen

- Telefon zweimal kurz tippen.
- Der aktuelle Verlauf mit bis zu 24 Zuständen wird kopiert.
- Bei Intensitätsänderungen enthält der Verlauf nur die zuletzt eingestellte Stufe; wiederholte Gefühlsklicks bleiben als einzelne Schritte erhalten.
- Unter `http://` oder `https://` entsteht ein vollständiger Link.
- Bei lokalen Dateiadressen entsteht ein portabler Share-Code.

### Rückmeldung

Die kleine Zeile unter dem Gefühlsnamen zeigt kurz eine der folgenden Meldungen:

- `Slow-Replay-Link kopiert`
- `Slow-Replay-Code kopiert`
- `Replay-Link kopiert`
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

Das Gedächtnisspiel wird bei ausgeschaltetem Gerät weiterhin mit `R` geöffnet. Direkt neben dem `R` blendet erst nach dem vollständig abgeschlossenen Ausschaltprozess die kleine schwarze Silhouette des OpenMoji-Joysticks `1F579` ein. Auch das normale Power-Zeichen bleibt erhalten und erhält dann direkt daneben wieder die schwarze Silhouette der OpenMoji-Lupe `1F50D`. Beim Einschalten blenden beide Hinweise weich aus. Sie sind 21 Pixel groß. Beim Ausschalten springen Intensitätswert und Zeiger sofort sichtbar auf `0`. Der leere Bereit-Zustand bleibt intern ebenfalls bei `0`, sodass die erste Gefühlsauswahl nach Start oder Neustart auf Mindeststufe `1` statt fälschlich auf `3` beginnt.

Beim Einstieg baut sich oben `Simon Feels!` in derselben Schriftgröße wie die normale Introanzeige auf und ein kurzer Startjingle erklingt. Die Auswahl bleibt dabei sofort bedienbar; jede Spielaktion beendet den Titelaufbau. Der Direktlink `#simon` wartet zunächst auf einem weißen Bildschirm mit dem farbigen OpenMoji-Controller `1F3AE` auf einen Tipp, damit Animation und Ton erst nach dieser Interaktion starten.

Die Kombi-Taste ist in Simon deutlich abgedunkelt und nicht bedienbar. Erwartet Simon eine Kombination, leuchtet die Taste nach dem ersten richtig gedrückten Symbol kurz auf und wird danach wieder dunkel.

Am Game Over zeigt die Zahl neben `R` sofort die Anzahl der gespeicherten Runden, obwohl das Score-Replay erst nach einem Druck auf `R` beginnt. Das gilt ebenso für empfangene Scores und nach der Rückkehr aus deren Replay.

### Schwierigkeitsgrade

| Auswahl | Modus | Eigenschaften |
|---|---|---|
| Freude | Leicht | langsamer, 3 Leben, Wiederholen erlaubt |
| Neutral | Normal | Standardtempo, 1 Leben |
| Trauer | Profi | schneller, Start bei 5 Punkten, 25 % Endbonus |

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
- Neue Game-over-Links verwenden `#g=…`, normale Replay-Links `#r=…`, langsame Replay-Links mit identischen Daten `#s=…` und Gefühlslinks `#e=…`. Alle bisherigen langen Fragmentformate werden weiterhin gelesen.
- Die Telefontaste bleibt dafür am Game Over sichtbar bedienbar.
- Nach dem Öffnen eines Score-Links startet die gespeicherte Folge automatisch. Währenddessen steht links die Punktzahl und darunter `Replay · Abbruch bei Klick auf irgendeine Taste`; jeder Tastenklick kehrt sofort zum Game Over zurück.

### Steuerung im Spiel

- `R` während einer Runde fordert `NEUSTART?` an; ein zweites `R` bestätigt.
- Nach Game Over spielt `R` die vollständige gespielte Folge erneut ab und kehrt anschließend zum Score zurück.
- Während dieses Score-Replays werden die drei Modustasten wieder als normale Gefühle dargestellt und wie die übrigen inaktiven Tasten abgedunkelt.
- **Aus** fordert `AUS?` an; ein zweiter Druck bestätigt.
- Nach Game Over reagieren `R`, Telefon und **Aus**.
- Nach Game Over bleiben Freude, Neutral und Trauer als direkte Auswahl für Leicht, Normal und Profi sichtbar.
- Die Hinweise nennen dort die drei Modi sowie `R: Replay` und `⏻: Schluss`.
- **Aus** führt vom Game Over zunächst zurück zur Simon-Titelauswahl; dort schaltet **Aus** die App direkt aus.
- `R` auf der Simon-Titelauswahl kehrt zum zuletzt gespeicherten Game-over-Bildschirm zurück; ohne vorheriges Game Over geschieht nichts.

## Ton

- Jede Grundemotion hat eigene Klangfolgen je Intensität. Kombinationen, Erfolg, Fehler, Lebensverlust, Lebensgewinn sowie Ein- und Ausschalten besitzen eigene Signale.
- Alle 40 Klangereignisse liegen unter `assets/audio/emotronic/` in zwei vollständigen WAV-Sets:
  - `8-bit/` erhält den härteren ursprünglichen Retro-Charakter.
  - `8-bit_soft/` verwendet dieselben Tonhöhen und Rhythmen, aber weichere Ein-/Ausläufe sowie einen kurzen dezenten Nachhall.
- `generate_audio_assets.py` erzeugt beide Ordner und `manifest.json` reproduzierbar. Neue Sounds werden zuerst in den Datentabellen des Generators ergänzt und anschließend für beide Sets generiert.
- Die WAV-Sets sind nur vorbereitet und werden von der Live-PWA noch nicht geladen oder gecached. Ihre Audioausgabe bleibt bis zur gesonderten Aktivierung bei der bestehenden Web-Audio-Synthese.
- Für die spätere Aktivierung ist `8-bit_soft` als Standard und `8-bit` als wählbare Alternative vorgesehen.
- Der laufende Ton ist optional und über `APP_CONFIG.audio.enabled` abschaltbar. Fehlt Web Audio oder blockiert der Browser Audio, läuft die App ohne Funktionsverlust weiter.

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
- Die aktuelle Cache-Version lautet `emotronic-v127`.
- Beim Aktivieren werden nur ältere Emotronic-Caches entfernt; Caches anderer Anwendungen auf derselben Domain bleiben erhalten.
- Nicht gecachte GET-Anfragen werden aus dem Netz geladen und anschließend gespeichert.
- Bei einem Netzfehler wird als Fallback `index.html` verwendet.

## Prüfung

Vom Repository-Root aus prüft `node sp-emotron/tools/emotronic-pwa/validate_emotronic.js` die JavaScript-Syntax, das gespiegelte Rad samt Ziffernsteuerung, alle kurzen Begriffe und eindeutigen Emojis, die acht emotionsbezogenen Kombi-Anker, beide WAV-Sets, Version/Cache sowie die bytegleichen HTML- und Service-Worker-Spiegel.

## Drittmaterial

Wo es gestalterisch und semantisch passt, sind OpenMoji-Grafiken gegenüber plattformabhängigen Emoji-Zeichen zu bevorzugen. Dazu gehören derzeit insbesondere der Controller `1F3AE`, die schwarzen Silhouetten von Joystick `1F579` und Lupe `1F50D` im Ausschaltzustand sowie der Pokal `1F3C6`. Bedienbare Kernfunktionen behalten einen einfachen Text- oder ASCII-Fallback. Copyright und Lizenzbedingungen von OpenMoji sind zu beachten. Die App zeigt beim Start `(c) OpenMoji` an.
