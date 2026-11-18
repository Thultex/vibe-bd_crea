# Changelog WL

## Stats

Ausgangsdatum: 2026-11-18

*Diese Woche (ca. 1,0h, 1 Tag, Inhalte):*
Import, Wortbereinigung, 2-Zeichen-Liste, konkrete Wortergänzungen und Prüftool.

*Letzte Woche (0,0h, 0 Tage, Inhalte):*
Keine Einträge.

*Dieser Monat (ca. 1,0h, 1 Tag, Inhalte):*
Import und erste allgemeine Pflege der WL-Ressource.

*Letzter Monat (0,0h, 0 Tage, Inhalte):*
Keine Einträge.

*Jahr (ca. 1,0h, 1 Tag, Inhalte):*
Aufbau der allgemeinen WL-Ressource.

*Insgesamt (ca. 1,0h, 1 Tag, Inhalte):*
Aufbau der allgemeinen WL-Ressource.

## Log

### 2026-11-18 - wl, material, tools, doku (ca. 1,0h)

- Summary: Historische BlinkRead-Listen separat übernommen und anschließend zunächst die Einzelwörter für eine allgemeine, spielunabhängige Nutzung gepflegt.
- Material: Bestehende Listen als unveränderten Ausgangsstand importiert.
- Change: Erkannte Personen-, Orts-, Marken-, Partei-, Vereins- und Institutionsnamen sowie veraltete Korpusreste entfernt.
- Feature: Neue Liste für Wörter mit zwei Zeichen ergänzt.
- Material: Viele konkrete, allgemein verständliche Alltagswörter und Handlungen ergänzt; Phrasen bleiben für einen getrennten Arbeitsschritt unverändert.
- Fix: Leere Zeilen und Dubletten unabhängig von Groß- und Kleinschreibung bereinigt.
- Tool: Reproduzierbare Bereinigung, Ergänzung und Validierung mit `BlinkRead/tools/build_wordlists.py` ergänzt; Ergänzungen werden gegen Bestand und `leibnitz-100k.txt` abgeglichen, Änderungen schrittweise vorab angezeigt, vor dem Schreiben gesichert und bei längeren Läufen mit Fortschrittsbalken begleitet.
- Doku: Zweck, Kürzel `wl`, Auswahlregeln und Pflegeablauf beschrieben.
- Versionen: build_wordlists v1.00.
