# Design Emotronic

## Ziel

Emotronic ist eine eigenständige, installierbare Webanwendung ohne Framework oder Build-Toolchain. Oberfläche, CSS und JavaScript liegen gemeinsam in `index.html`; Manifest, Service Worker und Icons ergänzen die PWA.

## Quellen- und Veröffentlichungsstruktur

- Maßgebliche Quelle: `tools/emotronic-pwa/`
- Öffentlicher Laufzeitspiegel: `../share/apps/emotronic/`
- Installationspfad: `/share/apps/emotronic/`

Der Laufzeitspiegel enthält ausschließlich `index.html`, Manifest, Service Worker und die benötigten Icons. Änderungen werden zuerst in der maßgeblichen Quelle vorgenommen, dort getestet und anschließend bytegleich in den Share-Pfad gespiegelt.

## PWA

- Alle URLs sind relativ zum jeweiligen PWA-Ordner.
- `manifest.webmanifest` verwendet `./index.html` und Scope `./`.
- Der Service Worker cached die App-Shell und zur Laufzeit geladene Ressourcen.
- Cache-Namen beginnen mit `emotronic-v`; beim Aktivieren werden nur ältere Emotronic-Caches gelöscht.
- Jede abgeschlossene Revision synchronisiert Codekopf, `APP_META`, Snapshot, README, Handoff und Cache-Version.
- Die zweizeilige Start-/Copyrightanzeige behält die normale einzeilige Detailhöhe; möglicher Überstand verändert weder App-Höhe noch Seitenverhältnis auf Handybildschirmen.
- Die Modusfragmente `#on`, `#off` und `#simon` starten direkt im jeweiligen Zustand; ohne Modusfragment entspricht der Start `#on`. `#slow` startet ebenfalls eingeschaltet, skaliert aber ausschließlich Schrittintervalle, Emoji-Bewegung, Displayübergang und Abschlusszeit des normalen Replays mit Faktor 2.
- Der direkte Simon-Link `#simon` wartet auf weißem Display mit kleinem Spielsymbol auf eine Interaktion; danach starten Startjingle und der Aufbau von `Simon Feels!` in normaler Intro-Schriftgröße. Die Schwierigkeitsauswahl bleibt sofort bedienbar und beendet den Titelaufbau bei Eingabe.
- Telefon kopiert in Bereit, auf der Simon-Auswahl und im ausgeschalteten Zustand still den passenden Direktlink `#on`, `#simon` beziehungsweise `#off`.
- `Simon Feels!` steht gegenüber seiner bisherigen Position zusätzlich um drei Viertel der eigenen Schrifthöhe tiefer; andere Simon-Anzeigen bleiben unverändert.
- Die Simon-Auswahl verwendet drei Emotionstasten: Neugier für Leicht, Neutral für Normal und Unsicherheit für Profi; Telefon und Wifi sind dort keine Auswahl mehr.
- Beim Neustart über die Aus-Taste beginnt der Aufbau mit Kirby-artigen ASCII-Gesichtern, schreibt Emotronic ruhig von links nach rechts und hält den vollständigen Schriftzug rund 0,8 Sekunden.

## Verlauf

- Eine Gefühlstaste erzeugt bei jedem Klick einen Replay-Schritt.
- Ein erneuter Klick auf dieselbe Gefühlstaste startet ihre Animation ohne die für Motivwechsel vorgesehene Überblendverzögerung.
- Intensitätsänderungen ersetzen nur den zuletzt erzeugten Schritt derselben Gefühlsauswahl.
- Im Telefon-/Selbstmodus bleibt die Intensität beim Wechsel zwischen nicht-neutralen Gefühlen erhalten. Im Wifi-Sendemodus startet das neue Gefühl wieder auf Stufe 1. Neutral setzt in beiden Modi auf 0.
- Im Telefon-/Empfängermodus spiegeln alle nicht-neutralen Gefühlstasten die aktuelle Intensitätsstufe über ihre jeweilige OpenMoji-Variante. Der Display-Hintergrund bleibt die Rückmeldung auf das tatsächlich gewählte Gefühl. Im Wifi-Sendemodus bleibt die Tastenvorschau auf die Auswahl beschränkt; in Simon werden Motiv und dramaturgischer Effekt erst durch den Tastendruck ausgelöst.
- Die Wifi-/Senderanimation `>>>` startet bei jeder Gefühlsbetätigung einschließlich eines erneuten Klicks auf dasselbe Gefühl, bei jeder tatsächlichen Intensitätsänderung und beim Aktivieren der Wifi-/Sendertaste.
- Ein Intensitätswechsel überblendet auf allen nicht-neutralen Empfängertasten und auf der aktuellen Wifi-Sendertaste das alte und neue Emoji direkt miteinander. Die in `APP_CONFIG.normalMode.keypadCrossfadeMs` definierbare Gesamtdauer beträgt standardmäßig 0,15 Sekunden. Das neue Motiv erreicht nach rund 0,12 Sekunden volle Deckkraft; das alte bleibt zunächst stehen, beginnt nach etwa 0,08 Sekunden weich auszufaden und ist am Ende verschwunden. Dadurch bleiben Mitte und Abschluss ohne Transparenzknick oder harten Bildsprung. Die Überblendung läuft unabhängig von der Bewegung; andere Sendertasten und der Display-Hintergrund erhalten keine zusätzliche Animation.
- Tastenbilder sind dekorativ und besitzen keinen sichtbaren Alternativtext; die separate Tastenbeschriftung liefert den Namen. Das alte aktive Motiv bleibt bis zum erfolgreichen Laden des neuen SVGs sichtbar. Dadurch blitzen weder beim Wechsel noch bei einem Ladefehler große Textplatzhalter im Emoji-Feld auf.
- Bei aktiver Kombi-Taste zeigen alle gültigen gestrichelt markierten Partner-/Nachbartasten das jeweils entstehende Kombi-Emoji samt dessen Kombinationsnamen. In „Bereit“ sowie bei gewähltem Neutral öffnet die Kombi-Taste stattdessen eine Übersicht aller acht Kombinationen auf den äußeren Tasten: Freude beginnt mit „lustig“, die übrigen Ergebnisse folgen im Uhrzeigersinn. Beim Einstieg aus Neutral wird der aktuelle Neutral-Schritt aus dem Replay entfernt und der Grundzustand intern auf „Bereit“ gesetzt; frühere Replay-Schritte bleiben bestehen. Ein Tipp übernimmt die angezeigte Kombination auf dieser Taste. Beim Abbruch kehren sämtliche Vorschauen zu den Grund-Emojis und übergeordneten Emotionsnamen zurück; nach einer Wahl behält nur die gewählte Taste das nun echte Kombi-Emoji samt Namen.
- Im Simon-Modus ist die Kombi-Taste deutlich abgedunkelt und nicht bedienbar. Bei einer erwarteten Kombi-Aktion leuchtet sie nach dem ersten richtigen Symbol kurz auf.
- Replay-Start und Replay-Sharing synchronisieren den sichtbaren Endzustand, ohne ihn doppelt anzuhängen.
- Nach einem vollständig abgespielten lokalen oder empfangenen Replay bleibt die Gesamtzahl seiner Schritte etwas größer und näher bei `R` als erneuter Abspielhinweis sichtbar. Erst der nächste Druck auf eine Gefühlstaste blendet die Zahl mit derselben weichen Skalierungs-/Deckkraftbewegung wie die ausgeschalteten Tastenhinweise aus.
- Wird `R` während der erneuten Wiedergabe zum Abbruch gedrückt, bleibt die Gesamtzahl ebenfalls sichtbar.
- `#slow` verwendet denselben Replay-Ablauf und dieselben Inhalte, verlängert dessen zeitliche Komponenten aber über `APP_CONFIG.replay.slowMultiplier` standardmäßig exakt auf das Doppelte.
- Das normale Replay blendet Gefühl, Emotion und Intensität mit einem sehr leichten Fade während der Wiedergabe aus und danach wieder ein.
- Ein empfangenes Replay rendert vor seinem ersten Schritt nicht mehr kurz den gespeicherten Endzustand.
- Zweimaliges Drücken von Neutral wechselt zu Bereit und leert dabei den gesamten Replay-Verlauf.
- Eingehende Emotions- und Replay-Links zeigen bis zur nächsten Interaktion ein ruhig weiterlaufendes Nachrichtensymbol direkt im normalen Display.
- Ein Tipp auf den Bildschirm oder eine beliebige Taste außer Aus startet die Wiedergabe ohne zusätzlichen Empfangston.
- Nach dem Starttipp lässt die App rund 0,1 Sekunden Abstand, bevor der empfangene Inhalt beginnt.
- Aus bricht die wartende Empfangsphase oder eine laufende Replay-Wiedergabe unmittelbar ab.
- Ein einfacher Tipp auf Telefon oder Wifi ersetzt die kleine Kategoriezeile drei Sekunden lang durch einen passenden Hinweis auf die jeweilige Doppeltipp-Teilgeste.
- Ein Telefon-Doppeltipp teilt immer den Replay-Verlauf; ein Wifi-/Sender-Doppeltipp kopiert immer den `#slow`-Direktlink. Die Erkennung läuft vor den zustandsabhängigen Direktlink-Aktionen, damit die Zuordnung auch in Bereit, Aus und Simon konsistent bleibt.
- Score-Links enthalten Endstand, Simon-Modus und die vollständige gespielte Folge; ihre Empfangsanimation ergänzt das Nachrichtensymbol um einen kleinen Pokal und die wartende Punktzahl.
- Nach der Bestätigung eines Score-Links spielt die App die Folge automatisch. Währenddessen steht links die Punktzahl mit dem Abbruchhinweis darunter; jeder Tastenklick stellt sofort das Game Over wieder her.
- Gefühle verwenden `#share=…`, Replays `#replay=…` und Game-over-Links `#score=…`. Ältere Replay-Links unter `#share=…` bleiben lesbar.
- Beim Game Over versucht die App den Score-Link automatisch zu kopieren; Telefon wiederholt dies manuell und `R` spielt die mitgeteilte Folge erneut ab.
- Die Telefontaste wird am Game Over ausdrücklich für das manuelle Kopieren freigeschaltet.
- Am Game Over bleiben Neugier, Neutral und Unsicherheit eingeblendet und starten direkt ein neues Spiel in Leicht, Normal beziehungsweise Profi; `R` bleibt Replay und `⏻` Schluss.
- Während des Score-Replays entfällt der Game-over-Auswahlzustand: Die drei Modustasten werden wieder zu normalen Gefühlen und gemeinsam mit den übrigen inaktiven Tasten abgedunkelt.
- Aus führt vom Game Over zurück zur Simon-Titelauswahl und schaltet die App erst bei erneutem Drücken in dieser Auswahl aus.
- `R` auf der Simon-Titelauswahl stellt den letzten Game-over-Zustand samt Modus und Folge wieder her.
- In Simon zeigt dieselbe Zahl neben `R` am Game Over sofort die Anzahl der gespeicherten Runden, obwohl das Score-Replay erst durch `R` gestartet wird. Auch empfangene Scores und die Rückkehr nach deren Replay verwenden denselben Hinweis.

## Audio

- Alle 40 Klangereignisse liegen reproduzierbar in zwei WAV-Sets unter `/assets/audio/emotronic/`: `8-bit` bewahrt die harte Retro-Fassung, `8-bit_soft` verwendet dieselben Tonhöhen und Rhythmen mit weicheren Hüllkurven und kurzem Nachhall.
- `generate_audio_assets.py` erzeugt beide Sets und `manifest.json` aus einer gemeinsamen Datengrundlage. Neue Sounds werden dort ergänzt und stets für beide Ordner generiert.
- Die Sets sind für den späteren Sound-Umbau vorbereitet, aber noch nicht in die Live-PWA eingebunden. Diese verwendet unverändert die bestehende Web-Audio-Synthese.
- Bei der späteren Aktivierung ist `8-bit_soft` als erste Standardauswahl vorgesehen; `8-bit` bleibt als alternative Fassung erhalten.
- Der Geschafft-Jingle folgt mit rund 0,2 Sekunden Abstand auf den letzten korrekten Tastendruck.

## Datenschutz

Das Repository ist öffentlich. Lokale Benutzerpfade, private Kontaktangaben, Zugangsdaten und Geheimnisse werden nicht versioniert. Bewusste Urheberangaben dürfen bestehen bleiben.

Geteilte Daten liegen ausschließlich in den URL-Fragmenten `#share=…`, `#replay=…` beziehungsweise `#score=…`. Sie werden beim normalen Seitenabruf nicht an den Webserver gesendet, bleiben jedoch für Empfänger des vollständigen Links lesbar.

## Drittmaterial

OpenMoji-Grafiken werden zur Laufzeit geladen und sind in Emotronic gegenüber plattformabhängigen Emoji-Zeichen zu bevorzugen, wo Motiv und Darstellung sinnvoll passen. Der Controller `1F3AE` erscheint farbig am direkten Simon-Einstieg. `R` und das normale Power-Zeichen bleiben auf den unteren Tasten erhalten; beim Ausschalten blenden direkt daneben klein die schwarzen Silhouetten des Joysticks `1F579` beziehungsweise der Lupe `1F50D` ein und beim Einschalten wieder aus. Die Score-Vorschau verwendet den Pokal `1F3C6`. Text- und ASCII-Fallbacks halten die Anwendung auch bei fehlgeschlagenen Grafik- oder Audiozugriffen bedienbar.
