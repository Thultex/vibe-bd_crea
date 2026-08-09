# Codex-Handoff: Emotronic v2.30

## Auftrag

Diese Übergabe beschreibt den aktuellen Stand der installierbaren Emotronic-PWA. Änderungen sollen direkt in `sp-emotron/tools/emotronic-pwa/index.html` erfolgen. Die App ist bewusst eine weitgehend eigenständige Einzeldatei mit eingebettetem CSS und JavaScript. Die laufende Veröffentlichungsfassung unter `share/apps/emotronic/` ist ein synchroner Spiegel der Laufzeitdateien.

## Relevante Dateien

- `sp-emotron/tools/emotronic-pwa/index.html` – maßgebliche Quelle
- `sp-emotron/tools/emotronic-pwa/Emotronic-v2.30.html` – versionierter Snapshot, nach Änderungen neu erzeugen
- `sp-emotron/tools/emotronic-pwa/generate_audio_assets.py` – reproduzierbarer Generator beider Soundsets
- `assets/audio/emotronic/` – Manifest sowie `8-bit` und `8-bit_soft`
- `sp-emotron/tools/emotronic-pwa/sw.js` – Service Worker und Cache-Version
- `sp-emotron/tools/emotronic-pwa/manifest.webmanifest` – PWA-Manifest
- `sp-emotron/tools/emotronic-pwa/README.md` – Nutzer- und Funktionsdokumentation
- `sp-emotron/tools/emotronic-pwa/validate_emotronic.js` – verbindliche Gesamtprüfung
- `share/apps/emotronic/` – veröffentlichter Spiegel der PWA-Laufzeitdateien

`sp-emotron/files/emotron.ai` und die Illustrator-Anwendung nur nach einer ausdrücklich darauf bezogenen Anweisung anfassen. Allgemeine Änderungsaufträge schließen sie nicht ein.

## Versionierung

- Aktuell: **Emotronic v2.30**
- `APP_META.version`: `2.30`
- `APP_META.revision`: `130`
- Service-Worker-Cache: `emotronic-v130`
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
- Neutral bleibt eine normale, beliebig oft wählbare Emotion und darf den Ausschalter nicht auslösen.
- Der erste Druck auf **Aus** leert den Replay-Verlauf und stellt **Bereit** her; erst der zweite Druck innerhalb des Bestätigungsfensters schaltet aus.
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

- Normaler Replay-Verlauf maximal 24 Einträge. Jede neue Eingabe entfernt bei vollem Verlauf den ältesten Schritt; Simons eigene Folge bleibt davon unberührt.
- Intensitätsänderungen ersetzen den letzten Schritt derselben Gefühlsauswahl.
- Erneute Klicks auf dieselbe Gefühlstaste erzeugen bewusst weitere Schritte, auch bei identischem Zustand.
- Replay-Start und Replay-Sharing synchronisieren den aktuellen Zustand ohne zusätzlichen Duplikatschritt.
- `R` startet Replay.
- Slow ist der Fragment-Tag `#slow=…` eines vollständigen Replay-Links. Sein codierter Datenteil ist identisch mit `#replay=…`; `applySharedPayload()` übergibt den erkannten Tag getrennt an `applyDecodedSharedPayload()`. Schrittfolge, Displayübergang und Abschluss verwenden dann über `replayTimingMultiplier()` standardmäßig Faktor 2. Die Emoji-Bewegung verwendet getrennt `replayEmojiTimingMultiplier()` und `slowEmojiMultiplier:1.15`.
- `state.slowReplay` bleibt beim erneuten `R` für denselben Verlauf erhalten, wird aber durch Gefühl-, Intensitäts- oder Kombi-Eingaben sowie Ausschalten/Replay-Löschen zurückgesetzt.
- Die graue Restanzahl steht während Replay neben `R`. Nach vollständiger Wiedergabe bleibt `items.length` über `showReplayCount()` als erneuter Abspielhinweis stehen; weil empfangene Replays ebenfalls `replayHistory()` verwenden, benötigen sie keinen Sonderpfad. Bricht `R` eine erneute Wiedergabe ab, ruft `cancelReplayToLatest()` `stopReplay(false,true)` auf und stellt anschließend ebenfalls die Gesamtzahl wieder her.
- Die 13-Pixel-Zahl sitzt mit `right:13px` näher bei `R` und verwendet dieselbe 0,38-Sekunden-Deckkraft-/Skalierungsbewegung wie die ausgeschalteten Tastenhinweise. `pressEmotion()` blendet sie über `hideReplayCount()` aus.
- `R` während Replay: nur abbrechen und neuesten gespeicherten Zustand wiederherstellen.
- **Aus** während Replay: abbrechen, Verlauf leeren, direkt zu Bereit; nicht Neutral und nicht Gerät ausschalten.
- Im Aus-Zustand setzt `render()` die Kombi-Taste auf `disabled` und `.offline`; das Kombi-Symbol blendet dabei vollständig aus und erst nach der Einschaltsequenz wieder ein.
- Normaler Neustart leert den Replay-Verlauf.
- Ein geteilter Replay-Link startet im Normalmodus automatisch.

## Sharing – Kerninvarianten

- Formate: `#share=<code>` für ein Gefühl, `#replay=<codes>` für normale Replays, `#slow=<dieselben-codes>` für langsame Replays und `#score=<scorecode>` für Game-over-Scores. Ein Base36-Zeichen `0` bis `w` codiert jeweils einen der 33 Zustände; Intensität und Kombination sind darin bereits enthalten.
- Alte Base64url-JSON-Links mit denselben ausgeschriebenen Fragmentnamen bleiben vollständig lesbar.
- Typ `emotion`: `{type:'emotion', item:...}`.
- Typ `replay`: `{type:'replay', items:[...]}`. Der Tag `#replay=` beziehungsweise `#slow=` wählt ausschließlich das Wiedergabetempo. Ältere Datensätze mit `slow:true` bleiben lesbar.
- Daten liegen nur im URL-Fragment und werden nicht als Query an einen Server gesendet.
- Bei `http:` oder `https:` vollständigen Link kopieren.
- Bei `file:` oder Android `content:` nur den portablen Kurzcode kopieren.
- UI-Text muss korrekt zwischen `Link kopiert` und `Code kopiert` unterscheiden.
- Telefon-Doppeltipp teilt konsistent den Replay-Verlauf.
- Wifi-/Sender-Doppeltipp teilt konsistent den vollständigen Replay-Verlauf unter `#slow=…`; Telefon teilt denselben Datensatz unter `#replay=…`.
- Die Doppeltipperkennung muss vor den Sonderfällen für Aus-, Simon- und Bereit-Direktlinks laufen; der erste Tipp darf den Direktlink auslösen, der zweite führt die feste Share-Aktion aus.
- Der jeweils erste Tipp erklärt die Doppeltipp-Geste für drei Sekunden in der kleinen Kategoriezeile.
- Eigene Touch-Doppeltipp-Erkennung beibehalten; nicht ausschließlich `dblclick` verwenden.
- Clipboard API plus `document.execCommand('copy')`-Fallback beibehalten.
- Fehler beim Kopieren dürfen keine normale Funktion blockieren.

## Kombinationen

Nur diese acht Paare sind gültig:

- Neugier + Zuneigung → Bewunderung
- Zuneigung + Freude → Dankbarkeit
- Freude + Wut → Streitlust
- Wut + Ekel → Abwertung
- Ekel + Scham → Unbehagen
- Scham + Trauer → Reue
- Trauer + Angst → Aufgeben
- Angst + Neugier → Überraschung

Bei aktiver Kombi-Taste zeigen gültige Partner-/Nachbartasten das resultierende Kombi-Emoji und dessen Kombinationsnamen als Vorschau. In „Bereit“ sowie bei Neutral zeigt `comboOverview` alle acht Ergebnisse auf dem äußeren Ring. Trotz Y-Spiegelung bleiben die Anker emotionsbezogen: Bewunderung liegt auf Zuneigung, Dankbarkeit auf Freude, Streitlust auf Wut, Abwertung auf Ekel, Unbehagen auf Scham, Reue auf Trauer, Aufgeben auf Angst und Überraschung auf Neugier. Beim Einstieg aus Neutral wird ausschließlich der letzte Neutral-Eintrag aus `state.history` entfernt und der sichtbare Zustand intern auf Bereit gesetzt, damit `replayHistory()` ihn nicht erneut synchronisiert. Ein Tipp übernimmt das Ergebnis auf der gedrückten Taste. Beim Abbruch werden die Grund-Emojis und übergeordneten Emotionsnamen wiederhergestellt; nach einer gültigen Wahl behält nur die gewählte Taste das echte Kombi-Emoji samt Namen. Außerhalb dieser Vorschau bleiben die normalen Tastenbeschriftungen unverändert.

Jede Sekundäremotion übernimmt eine passende Bewegungscharakteristik aus ihren benachbarten Grundzweigen. Scham besitzt eine eigene zurückhaltende Bewegung.

In Simon ist die Kombi-Taste deutlich abgedunkelt und ignoriert direkte Eingaben. Bei Simons Vorführung erhält sie nach dem ersten Symbol für dessen restliche Anzeigezeit `game-flash`. Beim eigenen Nachtippen leuchtet sie nach dem ersten richtigen Symbol für 0,15 Sekunden auf; eine falsche Eingabe löst kein Lichtsignal aus.

## Simon-Spiel – Kerninvarianten

- Bei ausgeschaltetem Gerät öffnet nur `R` die Schwierigkeitsauswahl.
- Freude = leicht, Neutral = normal, Trauer = Profi.
- Ruhig: 1 Leben, langsamer.
- Normal: 1 Leben.
- Profi: 1 Leben, schneller, startet bei 0 Punkten, 25 % Endbonus.
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
node sp-emotron/tools/emotronic-pwa/validate_emotronic.js
```

Der Validator prüft Syntax, 8+1-Datentabellen, eindeutige Begriffe und Emojis, Y-Spiegelung, Tastaturzuordnung, emotionsbezogene Kombi-Anker, WAV-Manifest und Soundsets, Version/Cache sowie Snapshot und Laufzeitspiegel.

Für ein auslieferbares ZIP vom Repository-Root aus:

```bash
rm -f emotronic-pwa-v2.30.zip
zip -rq emotronic-pwa-v2.30.zip sp-emotron/tools/emotronic-pwa
unzip -t emotronic-pwa-v2.30.zip
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
