# Codex-Handoff: Emotronic v2.11

## Auftrag

Diese Übergabe beschreibt den aktuellen Stand der installierbaren Emotronic-PWA. Änderungen sollen direkt in `sp-emotronic/tools/emotronic-pwa/index.html` erfolgen. Die App ist bewusst eine weitgehend eigenständige Einzeldatei mit eingebettetem CSS und JavaScript. Die laufende Veröffentlichungsfassung unter `share/apps/emotronic/` ist ein synchroner Spiegel der Laufzeitdateien.

## Relevante Dateien

- `sp-emotronic/tools/emotronic-pwa/index.html` – maßgebliche Quelle
- `sp-emotronic/tools/emotronic-pwa/Emotronic-v2.11.html` – versionierter Snapshot, nach Änderungen neu erzeugen
- `sp-emotronic/tools/emotronic-pwa/generate_audio_assets.py` – reproduzierbarer Generator beider Soundsets
- `assets/audio/emotronic/` – Manifest sowie `8-bit` und `8-bit_soft`
- `sp-emotronic/tools/emotronic-pwa/sw.js` – Service Worker und Cache-Version
- `sp-emotronic/tools/emotronic-pwa/manifest.webmanifest` – PWA-Manifest
- `sp-emotronic/tools/emotronic-pwa/README.md` – Nutzer- und Funktionsdokumentation
- `share/apps/emotronic/` – veröffentlichter Spiegel der PWA-Laufzeitdateien

## Versionierung

- Aktuell: **Emotronic v2.11**
- `APP_META.version`: `2.11`
- `APP_META.revision`: `111`
- Service-Worker-Cache: `emotronic-v111`
- Beim Aktivieren nur ältere Caches mit dem Präfix `emotronic-v` entfernen; andere Anwendungen können dieselbe Domain verwenden.
- Jede abgeschlossene Revision erhöht die Version um `0.01` und die Revision um `1`.
- Codekopf, `APP_META`, Service Worker, versionierte HTML-Datei, README und ZIP müssen synchron bleiben.

## Unveränderliche Struktur am Script-Anfang

Die Reihenfolge im JavaScript ist absichtlich:

1. kommentierter Codekopf
2. `APP_META`
3. `APP_CONFIG`
4. Ressourcen-Konstanten
5. Grundemotionstabelle `base`
6. Reihenfolge `order`
7. Kombinationstabelle `combos`
8. Soundtabellen
9. Funktionslogik

Globale Optionen nicht zwischen die Funktionslogik verteilen.

## Audio – Kerninvarianten

- `/assets/audio/emotronic/8-bit/` und `/assets/audio/emotronic/8-bit_soft/` enthalten dieselben 40 Sound-IDs; `manifest.json` ist die maschinenlesbare Übersicht.
- Neue oder geänderte Tonfolgen zuerst in `generate_audio_assets.py` pflegen und danach beide Ordner neu generieren.
- Die WAV-Dateien sind vorbereitet, aber noch nicht in die Live-PWA oder den Service-Worker-Cache eingebunden. `playEmotionSound`, `playComboSound` und `playSpecialSound` verwenden weiterhin ausschließlich `playTonePattern`.
- Bei der späteren Aktivierung soll `8-bit_soft` zunächst Standard sein und `8-bit` als Alternative erhalten bleiben.

## Öffentliches Repository und Datenschutz

- Das Repository `Thultex/vibe-bd_crea` ist öffentlich.
- Keine privaten Kontaktangaben, lokalen Benutzerpfade, Zugangsdaten oder anderen Geheimnisse einchecken; bewusste Urheber- und Namensnennungen dürfen bestehen bleiben.
- Share-Fragmente werden nicht automatisch an den Webserver gesendet, sind aber für jede Person mit dem vollständigen Link decodierbar.

## Normalmodus – Kerninvarianten

- Start eingeschaltet und direkt **Bereit**.
- Bereit hat keine Auswahl und Intensität `0`.
- Bereit darf niemals im Replay-Verlauf landen.
- Standardquelle ist `APP_CONFIG.normalMode.defaultSource === 'self'`, also Telefon.
- Grundemotionen außer Neutral haben mindestens Intensität `1`.
- Neutral bleibt Intensität `0`.
- Kombinationen haben immer Intensität `3`.
- Die Startanimation darf kein Neutral-Emoji als Zwischenbild zeigen.
- Telefonanimation bleibt zentriert und wirkt wie Klingeln, nicht wie ausgehende Pfeile.
- `>>>` gehört nur zur Wifi-/Sendeanimation.
- `triggerSenderStream()` läuft bei jeder Gefühlsbetätigung einschließlich erneutem Klick auf dasselbe Gefühl, bei tatsächlicher Intensitätsänderung und über `animateSource('other')` beim Aktivieren der Wifi-/Sendertaste.
- Nur im Telefon-/Empfängermodus spiegeln alle nicht-neutralen Tasten die aktuelle Intensitätsstufe vorab. Der Display-Hintergrund zeigt weiterhin das tatsächlich gewählte Gefühl; Wifi/Sender und Simon erhalten keine gemeinsame Vorschau.
- Die direkte Überblendung beim Intensitätswechsel läuft auf allen nicht-neutralen Empfängertasten und auf der aktuellen Wifi-Sendertaste. Ihre Gesamtdauer ist über `APP_CONFIG.normalMode.keypadCrossfadeMs` definierbar und beträgt standardmäßig 0,15 Sekunden. Das neue Motiv erreicht bei rund 0,12 Sekunden volle Deckkraft; das alte beginnt bei etwa 0,08 Sekunden auszufaden und endet bei 0,15 Sekunden. Dadurch dürfen weder Transparenzknick noch harter Abschlusssprung entstehen. Deckkraft- und Bewegungsanimation laufen unabhängig. Andere Sendertasten und der Display-Hintergrund erhalten keine zusätzliche Animation.
- Das alte aktive Tastenmotiv bleibt sichtbar, bis das neue SVG erfolgreich geladen ist. Tastenbilder verwenden leeren Alternativtext und keinen großen grafischen Text-Ersatz; bei einem Fehler bleibt die kleine Tastenbeschriftung als bedienbarer Fallback.
- In Simon werden Intensitätsmotiv und dramaturgischer Effekt weiterhin erst mit dem jeweiligen Tastendruck ausgelöst.

## Replay – Kerninvarianten

- Verlauf maximal 40 Einträge.
- Intensitätsänderungen ersetzen den letzten Schritt derselben Gefühlsauswahl.
- Erneute Klicks auf dieselbe Gefühlstaste erzeugen bewusst weitere Schritte, auch bei identischem Zustand.
- Replay-Start und Replay-Sharing synchronisieren den aktuellen Zustand ohne zusätzlichen Duplikatschritt.
- `R` startet Replay.
- `#slow` wird von `requestedStartupMode()` wie `#on` behandelt. Der normale Replay-Ablauf erhält für Schrittfolge, Displayübergang und Abschluss über `replayTimingMultiplier()` und `APP_CONFIG.replay.slowMultiplier` standardmäßig Faktor 2. Die Emoji-Bewegung verwendet getrennt `replayEmojiTimingMultiplier()` und `slowEmojiMultiplier:1.15`; normale Bedienung und Simon-Timing bleiben unverändert.
- Die graue Restanzahl steht während Replay neben `R`. Nach vollständiger Wiedergabe bleibt `items.length` über `showReplayCount()` als erneuter Abspielhinweis stehen; weil empfangene Replays ebenfalls `replayHistory()` verwenden, benötigen sie keinen Sonderpfad. Bricht `R` eine erneute Wiedergabe ab, ruft `cancelReplayToLatest()` `stopReplay(false,true)` auf und stellt anschließend ebenfalls die Gesamtzahl wieder her.
- Die 13-Pixel-Zahl sitzt mit `right:13px` näher bei `R` und verwendet dieselbe 0,38-Sekunden-Deckkraft-/Skalierungsbewegung wie die ausgeschalteten Tastenhinweise. `pressEmotion()` blendet sie über `hideReplayCount()` aus.
- `R` während Replay: nur abbrechen und neuesten gespeicherten Zustand wiederherstellen.
- **Aus** während Replay: abbrechen, Verlauf leeren, direkt zu Bereit; nicht Neutral und nicht Gerät ausschalten.
- Normaler Neustart leert den Replay-Verlauf.
- Ein geteilter Replay-Link startet im Normalmodus automatisch.

## Sharing – Kerninvarianten

- Formate: `#share=<base64url-json>` für Gefühle, `#replay=<base64url-json>` für Replays und `#score=<base64url-json>` für Game-over-Scores. Alte Replay-Datensätze unter `#share=` bleiben gültig.
- Typ `emotion`: `{type:'emotion', item:...}`.
- Typ `replay`: `{type:'replay', items:[...]}`.
- Daten liegen nur im URL-Fragment und werden nicht als Query an einen Server gesendet.
- Bei `http:` oder `https:` vollständigen Link kopieren.
- Bei `file:` oder Android `content:` nur den portablen `#share=...`-, `#replay=...`- beziehungsweise `#score=...`-Code kopieren.
- UI-Text muss korrekt zwischen `Link kopiert` und `Code kopiert` unterscheiden.
- Telefon-Doppeltipp teilt konsistent den Replay-Verlauf.
- Wifi-/Sender-Doppeltipp kopiert konsistent den `#slow`-Direktlink.
- Die Doppeltipperkennung muss vor den Sonderfällen für Aus-, Simon- und Bereit-Direktlinks laufen; der erste Tipp darf den Direktlink auslösen, der zweite führt die feste Share-Aktion aus.
- Der jeweils erste Tipp erklärt die Doppeltipp-Geste für drei Sekunden in der kleinen Kategoriezeile.
- Eigene Touch-Doppeltipp-Erkennung beibehalten; nicht ausschließlich `dblclick` verwenden.
- Clipboard API plus `document.execCommand('copy')`-Fallback beibehalten.
- Fehler beim Kopieren dürfen keine normale Funktion blockieren.

## Kombinationen

Nur diese acht Paare sind gültig:

- Freude + Zuneigung → verliebt
- Freude + Neugier → lustig
- Neugier + Wut → streitlustig
- Zuneigung + Angst → starr
- Ekel + Wut → abwertend
- Trauer + Ekel → bereuend
- Angst + Unsicherheit → genervt
- Unsicherheit + Trauer → verlegen

Bei aktiver Kombi-Taste zeigen gültige Partner-/Nachbartasten das resultierende Kombi-Emoji und dessen Kombinationsnamen als Vorschau. In „Bereit“ sowie bei Neutral zeigt `comboOverview` alle acht Ergebnisse auf dem äußeren Ring: Freude beginnt mit „lustig“, danach läuft die Zuordnung im Uhrzeigersinn. Beim Einstieg aus Neutral wird ausschließlich der letzte Neutral-Eintrag aus `state.history` entfernt und der sichtbare Zustand intern auf Bereit gesetzt, damit `replayHistory()` ihn nicht erneut synchronisiert. Ein Tipp übernimmt das Ergebnis auf der gedrückten Taste. Beim Abbruch werden die Grund-Emojis und übergeordneten Emotionsnamen wiederhergestellt; nach einer gültigen Wahl behält nur die gewählte Taste das echte Kombi-Emoji samt Namen. Außerhalb dieser Vorschau bleiben die normalen Tastenbeschriftungen unverändert.

`starr` verwendet eine eigene Rückzugs-/Erstarrbewegung in Normalmodus, Replay und Simon.

In Simon ist die Kombi-Taste deutlich abgedunkelt und ignoriert direkte Eingaben. Bei Simons Vorführung erhält sie nach dem ersten Symbol für dessen restliche Anzeigezeit `game-flash`. Beim eigenen Nachtippen leuchtet sie nach dem ersten richtigen Symbol für 0,15 Sekunden auf; eine falsche Eingabe löst kein Lichtsignal aus.

## Simon-Spiel – Kerninvarianten

- Bei ausgeschaltetem Gerät öffnet nur `R` die Schwierigkeitsauswahl.
- Telefon = ruhig, Neutral = normal, Wifi = Profi.
- Ruhig: 3 Leben, langsamer.
- Normal: 1 Leben.
- Profi: 1 Leben, schneller, startet bei 5 Punkten, 25 % Endbonus.
- Kein Eingabe-Timeout.
- Nächste Runde startet automatisch.
- Beschleunigung beginnt nach Punkt 5 und erreicht Maximum bei Punkt 20.
- Letzter Cue darf während Fade-out eingegeben werden.
- Intensität wird pro Sequenzschritt gespeichert und später nicht rückwirkend erhöht.
- Profi-Kombis ab 5; andere Modi ab `APP_CONFIG.simon.comboAt`.
- Bis 10 Punkte höchstens eine Profi-Kombi in der Folge.
- Kombi wird als erster Partner, schneller zweiter Partner und Kombi-Zustand auf zweiter Taste dargestellt.
- Leben: Das letzte sichtbare Herz darf auf 0 fallen; erst der folgende Fehler beendet das Spiel.
- Extra-Leben alle 10 Punkte.
- Bonusanimation alle 5 Punkte.
- Nach Game Over nur `R` und Aus aktiv.
- Am Game Over ruft die Anzeige `showReplayCount(validSharedGameSequence(g.sequence).length)` sofort auf, auch ohne gestartetes Score-Replay. `renderGame()` stellt denselben Rundenzähler für empfangene Scores und nach der Replay-Rückkehr wieder her.

## Mobile/PWA

- Proportionale Skalierung beibehalten; Oberfläche darf auf kleinen Browserhöhen nicht horizontal verrutschen.
- Kein äußerer rechteckiger App-Rahmen auf Mobilgeräten, interne Rahmen bleiben.
- App-Breite darf sich bei Intensität 2/3 nicht verändern.
- Service Worker nach jeder Revision aktualisieren, sonst sehen installierte PWAs alten Code.

## Prüfroutine nach jeder Änderung

```bash
cd sp-emotronic/tools/emotronic-pwa

python3 - <<'PY'
from pathlib import Path
text=Path('index.html').read_text()
start=text.index('<script>')+len('<script>')
end=text.index('</script>', start)
Path('emotronic_check.js').write_text(text[start:end])
PY

node --check emotronic_check.js
cp index.html Emotronic-vX.XX.html
rm emotronic_check.js
```

Für ein auslieferbares ZIP vom Repository-Root aus:

```bash
rm -f emotronic-pwa-v2.11.zip
zip -rq emotronic-pwa-v2.11.zip sp-emotronic/tools/emotronic-pwa
unzip -t emotronic-pwa-v2.11.zip
```

## Vorsicht bei Änderungen

- Keine alten Upload-Snapshots über die aktuelle Datei kopieren.
- Keine bestehende Timer-Abbruchlogik entfernen, ohne Replay, Boot und Simon separat zu testen.
- Keine `content://`-Adresse als teilbaren Browser-Link ausgeben.
- Keine Annahmen über sichtbare Android-Dateipfade treffen.
- Audio muss fail-safe bleiben.
- OpenMoji ist in Emotronic gegenüber plattformabhängigen Emoji-Zeichen zu bevorzugen, wenn Motiv und Darstellung sinnvoll passen.
- OpenMoji-Fehler dürfen die ASCII-Darstellung oder eine bedienbare Kernfunktion nicht verhindern.
- Keine ungültigen Kombinationspaare ergänzen.

## Bekannte Architektur

- Keine Build-Toolchain.
- Kein Framework.
- CSS und JavaScript sind in `index.html` eingebettet.
- Externe OpenMoji-SVGs werden zur Laufzeit geladen; Text- und ASCII-Fallbacks bleiben vorhanden.
- Der farbige Controller `1F3AE` kennzeichnet den direkten Simon-Einstieg. `R` und das normale Power-Zeichen bleiben immer erhalten; beim Ausschalten blenden direkt daneben 21 Pixel große schwarze Silhouetten des Joysticks `1F579` beziehungsweise der Lupe `1F50D` ein und beim Einschalten wieder aus. Die Score-Empfangsvorschau verwendet den Pokal `1F3C6`.
- Eine Kombinationsauswahl liegt nur bei einem tatsächlich vorhandenen Objekt vor; `null` darf weder den Kombi-Lock aktivieren noch die Intensität auf `3` setzen.
- Zustände liegen im zentralen `state`-Objekt.
- Simon-spezifischer Zustand liegt unter `state.game`.
- Timer des Spiels müssen über die vorhandenen Game-Timer-Helfer verwaltet werden.
