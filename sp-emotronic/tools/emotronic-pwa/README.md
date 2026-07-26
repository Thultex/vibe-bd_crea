# Emotronic v1.77

Emotronic ist eine installierbare, offlinefähige PWA zur Auswahl, Darstellung, Kombination und Wiedergabe von Gefühlen. Die Oberfläche ist an ein kompaktes Retro-Handgerät angelehnt und für Touch, Maus und Tastatur ausgelegt.

Die maßgebliche PWA-Quelle liegt unter `sp-emotronic/tools/emotronic-pwa/`. Alle PWA-Pfade sind relativ, sodass dieselben Laufzeitdateien unter `share/apps/emotronic/` als öffentlicher App-Spiegel bereitgestellt werden können.

Wenn GitHub Pages den Branch `main` aus dem Repository-Root veröffentlicht, lautet der PWA-Link:

```text
https://thultex.github.io/vibe-bd_crea/share/apps/emotronic/
```

## Öffentliches Repository und Datenschutz

Das Repository `Thultex/vibe-bd_crea` ist öffentlich. Quelltexte, Dokumentation und Commit-Historie sind daher allgemein einsehbar; private Kontaktangaben, lokale Benutzerpfade und Zugangsdaten gehören nicht in die versionierten Dateien. Bewusste Urheber- und Namensnennungen bleiben davon unberührt.

Emotronic speichert keine Gefühls- oder Replay-Daten auf einem Server. Share-Daten stehen im URL-Fragment `#share=…`. Das Fragment wird beim normalen HTTP-Aufruf nicht an den Webserver übertragen, kann aber von jeder Person gelesen und decodiert werden, die den vollständigen Link erhält. Vertrauliche Inhalte sollten deshalb nicht über öffentlich zugängliche Kanäle geteilt werden.

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

- Simon-Says-Auswahl: `https://thultex.github.io/vibe-bd_crea/share/apps/emotronic/?mode=simon`
- Normal eingeschaltet: `https://thultex.github.io/vibe-bd_crea/share/apps/emotronic/?mode=on`
- Ausgeschaltet: `https://thultex.github.io/vibe-bd_crea/share/apps/emotronic/?mode=off`

Ohne `mode`-Parameter startet Emotronic wie `mode=on`.

## Dateien

| Datei | Zweck |
|---|---|
| `index.html` | Hauptanwendung mit Oberfläche, CSS und JavaScript |
| `Emotronic-v1.77.html` | Versionierte Kopie der Hauptanwendung |
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

Grundemotionen haben drei Intensitätsstufen. Neutral bleibt immer auf Intensität `0`. Andere Grundemotionen können nicht unter Intensität `1` fallen.

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
- `R` während des Replays bricht nur die Wiedergabe ab und zeigt wieder den neuesten Zustand.
- **Aus** während des Replays bricht ab, leert den Verlauf und geht direkt zu **Bereit**.
- Ein normaler Neustart leert den Replay-Verlauf vollständig.

## Sharing

Emotronic speichert geteilte Daten ausschließlich im URL-Fragment hinter `#share=`. Dadurch werden die Gefühlsdaten nicht automatisch an einen Server übertragen.

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
- Aus bricht den Empfang ab,
- ein geteilter Score zeigt in der Warteanimation zusätzlich klein Pokal und Punktzahl.

Die Zwischenablage verwendet zuerst die moderne Clipboard API und danach einen klassischen Android-kompatiblen Fallback. Ein Kopierfehler darf die übrige App-Funktion nicht unterbrechen.

## Gedächtnisspiel

Das Gedächtnisspiel wird bei ausgeschaltetem Gerät mit `R` geöffnet. Zuerst erscheint die Schwierigkeitsauswahl.

### Schwierigkeitsgrade

| Auswahl | Modus | Eigenschaften |
|---|---|---|
| Telefon | Ruhig | langsamer, 3 Leben, Wiederholen erlaubt |
| Neutral | Normal | Standardtempo, 1 Leben |
| Wifi | Profi | schneller, Start bei 5 Punkten, 25 % Endbonus |

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
- Bei 10, 20, 30 usw. Punkten wird ein zusätzliches Leben vergeben.
- Alle 5 Punkte läuft eine Kirby-artige Retro-Bonusanimation; ab 10 Punkten stehen zusätzliche Varianten bereit.
- Bei Spielende werden Punktzahl und Leistungs-Kommentar angezeigt.
- Im Profi-Modus wird die Endpunktzahl mit 25 % Bonus berechnet.
- Beim Game Over wird ein Link mit Score, Modus und vollständiger gespielter Folge automatisch in die Zwischenablage kopiert, soweit der Browser dies zulässt.
- Telefon kopiert denselben Score-Link auf dem Game-Over-Bildschirm erneut manuell.

### Steuerung im Spiel

- `R` während einer Runde fordert `NEUSTART?` an; ein zweites `R` bestätigt.
- Nach Game Over spielt `R` die vollständige gespielte Folge erneut ab und kehrt anschließend zum Score zurück.
- **Aus** fordert `AUS?` an; ein zweiter Druck bestätigt.
- Nach Game Over reagieren `R`, Telefon und **Aus**.

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
- Die aktuelle Cache-Version lautet `emotronic-v77`.
- Beim Aktivieren werden nur ältere Emotronic-Caches entfernt; Caches anderer Anwendungen auf derselben Domain bleiben erhalten.
- Nicht gecachte GET-Anfragen werden aus dem Netz geladen und anschließend gespeichert.
- Bei einem Netzfehler wird als Fallback `index.html` verwendet.

## Drittmaterial

Die Emoji-Grafiken werden von OpenMoji geladen. Copyright und Lizenzbedingungen von OpenMoji sind zu beachten. Die App zeigt beim Start `(c) OpenMoji` an.
