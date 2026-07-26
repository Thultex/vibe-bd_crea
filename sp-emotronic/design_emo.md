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
- Der Query-Parameter `mode` unterstützt ausschließlich `on`, `off` und `simon`; ohne Parameter entspricht der Start `on`.
- Der direkte Simon-Link wartet auf weißem Display mit kleinem Spielsymbol auf eine Interaktion; danach starten Startjingle und der Aufbau von `SIMON FEELS` in normaler Intro-Schriftgröße. Die Schwierigkeitsauswahl bleibt sofort bedienbar und beendet den Titelaufbau bei Eingabe.
- Beim Neustart über die Aus-Taste beginnt der Aufbau mit Kirby-artigen ASCII-Gesichtern, schreibt Emotronic ruhig von links nach rechts und hält den vollständigen Schriftzug rund 0,8 Sekunden.

## Verlauf

- Eine Gefühlstaste erzeugt bei jedem Klick einen Replay-Schritt.
- Ein erneuter Klick auf dieselbe Gefühlstaste startet ihre Animation ohne die für Motivwechsel vorgesehene Überblendverzögerung.
- Intensitätsänderungen ersetzen nur den zuletzt erzeugten Schritt derselben Gefühlsauswahl.
- Replay-Start und Replay-Sharing synchronisieren den sichtbaren Endzustand, ohne ihn doppelt anzuhängen.
- Zweimaliges Drücken von Neutral wechselt zu Bereit und leert dabei den gesamten Replay-Verlauf.
- Eingehende Emotions- und Replay-Links zeigen bis zur nächsten Interaktion ein ruhig weiterlaufendes Nachrichtensymbol direkt im normalen Display.
- Ein Tipp auf den Bildschirm oder eine beliebige Taste außer Aus startet die Wiedergabe ohne zusätzlichen Empfangston.
- Aus bricht die wartende Empfangsphase oder eine laufende Replay-Wiedergabe unmittelbar ab.
- Ein einfacher Tipp auf Telefon oder Wifi ersetzt die kleine Kategoriezeile drei Sekunden lang durch einen passenden Hinweis auf die jeweilige Doppeltipp-Teilgeste.
- Score-Links enthalten Endstand, Simon-Modus und die vollständige gespielte Folge; ihre Empfangsanimation ergänzt das Nachrichtensymbol um einen kleinen Pokal und die wartende Punktzahl.
- Beim Game Over versucht die App den Score-Link automatisch zu kopieren; Telefon wiederholt dies manuell und `R` spielt die mitgeteilte Folge erneut ab.
- Die Telefontaste wird am Game Over ausdrücklich für das manuelle Kopieren freigeschaltet.
- Neutral bleibt am Game Over eingeblendet und startet direkt ein neues Spiel im zuletzt verwendeten Modus; die Hinweise benennen die Aktionen als `Neutral: Neustart`, `R: Replay` und `⏻: Schluss`.
- Aus führt vom Game Over zurück zur Simon-Titelauswahl und schaltet die App erst bei erneutem Drücken in dieser Auswahl aus.
- Der Geschafft-Jingle folgt mit rund 0,3 Sekunden Abstand auf den letzten korrekten Tastendruck.

## Datenschutz

Das Repository ist öffentlich. Lokale Benutzerpfade, private Kontaktangaben, Zugangsdaten und Geheimnisse werden nicht versioniert. Bewusste Urheberangaben dürfen bestehen bleiben.

Share-Daten liegen ausschließlich im URL-Fragment. Sie werden beim normalen Seitenabruf nicht an den Webserver gesendet, bleiben jedoch für Empfänger des vollständigen Links lesbar.

## Drittmaterial

OpenMoji-Grafiken werden zur Laufzeit geladen. Der ASCII-Fallback hält die Anwendung auch bei fehlgeschlagenen Grafik- oder Audiozugriffen bedienbar.
