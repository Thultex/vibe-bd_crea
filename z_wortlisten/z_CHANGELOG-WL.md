# Changelog WL

## Stats

Ausgangsdatum: 2026-11-18

*Diese Woche (ca. 1,5h, 1 Tag, Inhalte):*
Import, Wortbereinigung, zentrale Korpora, kurze Grundwörter und Prüftool.

*Letzte Woche (0,0h, 0 Tage, Inhalte):*
Keine Einträge.

*Dieser Monat (ca. 1,5h, 1 Tag, Inhalte):*
Import, erste allgemeine Pflege und Korpusabgleich der WL-Ressource.

*Letzter Monat (0,0h, 0 Tage, Inhalte):*
Keine Einträge.

*Jahr (ca. 1,5h, 1 Tag, Inhalte):*
Aufbau der allgemeinen WL-Ressource.

*Insgesamt (ca. 1,5h, 1 Tag, Inhalte):*
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
- Struktur: `Leibnitz 100k` aus Zeilenfuttern in den allgemeinen Ordner `korpora/` verschoben; Browser- und Textfassung bleiben zentral gemeinsam verfügbar.
- Quelle: Amtlichen Grundwortschatz Brandenburg 2024 als Original-PDF und als bereinigte Textfassung mit 685 eindeutigen Grundformen aufgenommen.
- Material: Einzelwortlisten besonders im Bereich zwei bis sechs Zeichen um amtliche Grundwörter und zusätzlich kuratierte konkrete Kurzbegriffe erweitert; Phrasen bleiben unverändert.
- Tool: Vorschau weist nun neben dem Leibnitz-Rang auch Treffer im Grundwortschatz Brandenburg aus.
- Versionen: build_wordlists v1.01.
