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

## Verlauf

- Eine Gefühlstaste erzeugt bei jedem Klick einen Replay-Schritt.
- Intensitätsänderungen ersetzen nur den zuletzt erzeugten Schritt derselben Gefühlsauswahl.
- Replay-Start und Replay-Sharing synchronisieren den sichtbaren Endzustand, ohne ihn doppelt anzuhängen.
- Eingehende Emotions- und Replay-Links zeigen vor der Wiedergabe 750 ms lang eine animierte Nachricht.
- Während der Empfangsphase sind alle Bedientasten außer Aus gesperrt; Aus bricht die aktuelle Aktion unmittelbar ab.

## Datenschutz

Das Repository ist öffentlich. Lokale Benutzerpfade, private Kontaktangaben, Zugangsdaten und Geheimnisse werden nicht versioniert. Bewusste Urheberangaben dürfen bestehen bleiben.

Share-Daten liegen ausschließlich im URL-Fragment. Sie werden beim normalen Seitenabruf nicht an den Webserver gesendet, bleiben jedoch für Empfänger des vollständigen Links lesbar.

## Drittmaterial

OpenMoji-Grafiken werden zur Laufzeit geladen. Der ASCII-Fallback hält die Anwendung auch bei fehlgeschlagenen Grafik- oder Audiozugriffen bedienbar.
