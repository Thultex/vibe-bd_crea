# Changelog Emotronic

## Stats

Ausgangsdatum: 2026-07-26

*Diese Woche (ca. 1,6h, 1 Tag, Inhalte):*
Emotronic-PWA übernommen, strukturiert, dokumentiert, Replay-Verlauf korrigiert sowie Versionsanzeige und interaktive Empfangssteuerung ergänzt.

*Letzte Woche (0h, 0 Tage, Inhalte):*
Keine Einträge.

*Dieser Monat (ca. 1,6h, 1 Tag, Inhalte):*
Erstübernahme von Emotronic samt PWA-Struktur, korrigierter Verlaufslogik sowie Versionsanzeige und interaktiver Empfangssteuerung.

*Letzter Monat (0h, 0 Tage, Inhalte):*
Keine Einträge.

*Jahr (ca. 1,6h, 1 Tag, Inhalte):*
Erstübernahme von Emotronic samt PWA-Struktur, korrigierter Verlaufslogik sowie Versionsanzeige und interaktiver Empfangssteuerung.

*Insgesamt (ca. 1,6h, 1 Tag, Inhalte):*
Erstübernahme von Emotronic samt PWA-Struktur, korrigierter Verlaufslogik sowie Versionsanzeige und interaktiver Empfangssteuerung.

## Log

### 2026-07-26 - emo, struktur, tools, pwa, replay, share, anzeige, audio, doku (ca. 1,6h)

- Summary: Vollständige Emotronic-PWA in die Repository-Struktur übernommen und einen getrennten öffentlichen App-Spiegel vorbereitet.
- Struktur: Projekt unter `sp-emotronic/` mit dem Kürzel `emo` und den vorgesehenen Dokumentations-, Asset-, Datei- und Toolbereichen angelegt.
- Tool: Maßgebliche PWA-Quelle unter `tools/emotronic-pwa/` mit HTML, Manifest, Service Worker, Icons, Snapshot, README und Handoff übernommen.
- PWA: Laufzeitdateien unter `/share/apps/emotronic/` für einen stabilen öffentlichen Unterpfad gespiegelt.
- Fix: Replay-Abbruch räumt die graue Restanzeige zuverlässig auf; der zuletzt gewählte Zustand bleibt sichtbar.
- Fix: Intensitätsänderungen aktualisieren nur den zuletzt gewählten Replay-Schritt; erneute Klicks auf dieselbe Gefühlstaste bleiben dagegen als eigenständige Schritte erhalten.
- Anzeige: Im Bereitschaftszustand zeigt die zweite Displayzeile dynamisch den Projektnamen und die aktuelle Version.
- Share: Eingehende Emotions- und Replay-Links warten ohne Zeitlimit mit ruhig weiterlaufendem Nachrichtensymbol im schlichten Hauptdisplay; Bildschirm oder Taste außer Aus startet Jingle und Wiedergabe.
- Audio: Den Empfangs-Jingle vollständig entfernt; der Starttipp beginnt Emotion oder Replay ohne zusätzlichen Empfangston.
- Bedienung: Aus bricht die laufende Empfangsphase oder Replay-Wiedergabe unmittelbar ab.
- Replay: Der Wechsel zu Bereit durch zweimaliges Drücken von Neutral leert den Replay-Verlauf vollständig.
- Datenschutz: Detaillierten lokalen Projektpfad aus dem Ruckpacken-Startskript entfernt und öffentliche Repository-/Share-Hinweise dokumentiert.
- Test: JavaScript-Syntax, Manifest, Icons, Service-Worker-Dateien, doppelte HTML-IDs, Versionsgleichlauf, mobile Breite und Browser-Smoke-Test geprüft.
- Doku: Übersicht, Anleitung, Design, Ideen, Plan, Installationshinweise und technische Übergabe ergänzt.
- Versionen: Emotronic v1.73.
