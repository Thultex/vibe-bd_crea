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
- Die Modusfragmente `#on`, `#off` und `#simon` starten direkt im jeweiligen Zustand; ohne Modusfragment entspricht der Start `#on`.
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
- Replay-Start und Replay-Sharing synchronisieren den sichtbaren Endzustand, ohne ihn doppelt anzuhängen.
- Das normale Replay blendet Gefühl, Emotion und Intensität mit einem sehr leichten Fade während der Wiedergabe aus und danach wieder ein.
- Ein empfangenes Replay rendert vor seinem ersten Schritt nicht mehr kurz den gespeicherten Endzustand.
- Zweimaliges Drücken von Neutral wechselt zu Bereit und leert dabei den gesamten Replay-Verlauf.
- Eingehende Emotions- und Replay-Links zeigen bis zur nächsten Interaktion ein ruhig weiterlaufendes Nachrichtensymbol direkt im normalen Display.
- Ein Tipp auf den Bildschirm oder eine beliebige Taste außer Aus startet die Wiedergabe ohne zusätzlichen Empfangston.
- Nach dem Starttipp lässt die App rund 0,1 Sekunden Abstand, bevor der empfangene Inhalt beginnt.
- Aus bricht die wartende Empfangsphase oder eine laufende Replay-Wiedergabe unmittelbar ab.
- Ein einfacher Tipp auf Telefon oder Wifi ersetzt die kleine Kategoriezeile drei Sekunden lang durch einen passenden Hinweis auf die jeweilige Doppeltipp-Teilgeste.
- Score-Links enthalten Endstand, Simon-Modus und die vollständige gespielte Folge; ihre Empfangsanimation ergänzt das Nachrichtensymbol um einen kleinen Pokal und die wartende Punktzahl.
- Nach der Bestätigung eines Score-Links spielt die App die Folge automatisch. Währenddessen steht links die Punktzahl mit dem Abbruchhinweis darunter; jeder Tastenklick stellt sofort das Game Over wieder her.
- Gefühle und Replays verwenden ausschließlich `#share=…`; Game-over-Links verwenden ausschließlich `#score=…`.
- Beim Game Over versucht die App den Score-Link automatisch zu kopieren; Telefon wiederholt dies manuell und `R` spielt die mitgeteilte Folge erneut ab.
- Die Telefontaste wird am Game Over ausdrücklich für das manuelle Kopieren freigeschaltet.
- Am Game Over bleiben Neugier, Neutral und Unsicherheit eingeblendet und starten direkt ein neues Spiel in Leicht, Normal beziehungsweise Profi; `R` bleibt Replay und `⏻` Schluss.
- Während des Score-Replays entfällt der Game-over-Auswahlzustand: Die drei Modustasten werden wieder zu normalen Gefühlen und gemeinsam mit den übrigen inaktiven Tasten abgedunkelt.
- Aus führt vom Game Over zurück zur Simon-Titelauswahl und schaltet die App erst bei erneutem Drücken in dieser Auswahl aus.
- `R` auf der Simon-Titelauswahl stellt den letzten Game-over-Zustand samt Modus und Folge wieder her.
- Der Geschafft-Jingle folgt mit rund 0,2 Sekunden Abstand auf den letzten korrekten Tastendruck.

## Datenschutz

Das Repository ist öffentlich. Lokale Benutzerpfade, private Kontaktangaben, Zugangsdaten und Geheimnisse werden nicht versioniert. Bewusste Urheberangaben dürfen bestehen bleiben.

Geteilte Daten liegen ausschließlich in den URL-Fragmenten `#share=…` beziehungsweise `#score=…`. Sie werden beim normalen Seitenabruf nicht an den Webserver gesendet, bleiben jedoch für Empfänger des vollständigen Links lesbar.

## Drittmaterial

OpenMoji-Grafiken werden zur Laufzeit geladen. Der ASCII-Fallback hält die Anwendung auch bei fehlgeschlagenen Grafik- oder Audiozugriffen bedienbar.
