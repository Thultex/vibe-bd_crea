# Changelog Emotronic

## Stats

Ausgangsdatum: 2026-07-26

*Diese Woche (ca. 1,3h, 1 Tag, Inhalte):*
Emotronic-PWA übernommen, strukturiert, dokumentiert, Replay-Verlauf korrigiert und Versionsanzeige im Bereitschaftszustand ergänzt.

*Letzte Woche (0h, 0 Tage, Inhalte):*
Keine Einträge.

*Dieser Monat (ca. 1,3h, 1 Tag, Inhalte):*
Erstübernahme von Emotronic samt PWA-Struktur, korrigierter Verlaufslogik und dynamischer Versionsanzeige.

*Letzter Monat (0h, 0 Tage, Inhalte):*
Keine Einträge.

*Jahr (ca. 1,3h, 1 Tag, Inhalte):*
Erstübernahme von Emotronic samt PWA-Struktur, korrigierter Verlaufslogik und dynamischer Versionsanzeige.

*Insgesamt (ca. 1,3h, 1 Tag, Inhalte):*
Erstübernahme von Emotronic samt PWA-Struktur, korrigierter Verlaufslogik und dynamischer Versionsanzeige.

## Log

### 2026-07-26 - emo, struktur, tools, pwa, replay, anzeige, doku (ca. 1,3h)

- Summary: Vollständige Emotronic-PWA in die Repository-Struktur übernommen und einen getrennten öffentlichen App-Spiegel vorbereitet.
- Struktur: Projekt unter `sp-emotronic/` mit dem Kürzel `emo` und den vorgesehenen Dokumentations-, Asset-, Datei- und Toolbereichen angelegt.
- Tool: Maßgebliche PWA-Quelle unter `tools/emotronic-pwa/` mit HTML, Manifest, Service Worker, Icons, Snapshot, README und Handoff übernommen.
- PWA: Laufzeitdateien unter `/share/apps/emotronic/` für einen stabilen öffentlichen Unterpfad gespiegelt.
- Fix: Replay-Abbruch räumt die graue Restanzeige zuverlässig auf; der zuletzt gewählte Zustand bleibt sichtbar.
- Fix: Intensitätsänderungen aktualisieren nur den zuletzt gewählten Replay-Schritt; erneute Klicks auf dieselbe Gefühlstaste bleiben dagegen als eigenständige Schritte erhalten.
- Anzeige: Im Bereitschaftszustand zeigt die zweite Displayzeile dynamisch den Projektnamen und die aktuelle Version.
- Datenschutz: Detaillierten lokalen Projektpfad aus dem Ruckpacken-Startskript entfernt und öffentliche Repository-/Share-Hinweise dokumentiert.
- Test: JavaScript-Syntax, Manifest, Icons, Service-Worker-Dateien, doppelte HTML-IDs, Versionsgleichlauf, mobile Breite und Browser-Smoke-Test geprüft.
- Doku: Übersicht, Anleitung, Design, Ideen, Plan, Installationshinweise und technische Übergabe ergänzt.
- Versionen: Emotronic v1.68.
