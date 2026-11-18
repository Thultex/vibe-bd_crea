# Allgemeine Wortlisten (WL)

Kurzversion: `wl`

Die Wortlisten sind eine allgemeine Repo-Ressource und gehören zu keinem einzelnen Spiel. Die Dateien unter `BlinkRead/` enthalten jeweils einen Eintrag pro Zeile und können direkt in einfachen Lese- und Schnellleseprogrammen verwendet werden.

## Inhalt

- `de_2_Zeichen.txt` bis `de_9-10_Zeichen.txt`: deutsche Wörter nach Zeichenlänge
- `de_Phrasen_*.txt`: historische Wortgruppen und Sätze; ihre inhaltliche Pflege erfolgt getrennt von den Wortlisten
- `de_Spezial_Doppelkonsonanten.txt`: Wörter zum Üben von Doppelkonsonanten
- `BlinkRead/tools/build_wordlists.py`: reproduzierbare Bereinigung, Ergänzung und Prüfung der BlinkRead-Einzelwörter

## Auswahlregeln

- Keine Personen-, Orts-, Marken-, Partei-, Vereins- oder Institutionsnamen.
- Neue Wörter sind allgemein verständlich und bevorzugen konkrete, bildlich vorstellbare Alltagsbegriffe und Handlungen.
- Abstrakte Fach-, Verwaltungs- und Nachrichtensprache wird nicht neu aufgenommen.
- Schreibweise und Großschreibung folgen dem Deutschen; Dubletten werden unabhängig von Groß- und Kleinschreibung entfernt.
- Jede kuratierte Ergänzung wird nach der Längenzuordnung gegen den gesamten vorhandenen Einzelwortbestand abgeglichen; vorhandene Wörter werden nicht erneut aufgenommen.
- Zusätzlich zeigt die Vorschau den Fund und Häufigkeitsrang aus `sp-zeilenfuttern/tools/presets/leibnitz-100k.txt`. Ein fehlender Fund wird sichtbar markiert, aber nicht automatisch verworfen, weil konkrete Komposita in einer Häufigkeitsliste fehlen können.
- Umlaute zählen als ein Zeichen. Leerzeichen und Satzzeichen zählen bei Phrasen mit.

Die Phrasen werden bewusst nicht gemeinsam mit den Einzelwörtern überarbeitet, damit beide Materialarten getrennt geprüft und versioniert werden können.

## Pflege

Aus dem Repo-Root:

```powershell
python z_wortlisten\BlinkRead\tools\build_wordlists.py
python z_wortlisten\BlinkRead\tools\build_wordlists.py --apply
python z_wortlisten\BlinkRead\tools\build_wordlists.py --check
```

Das Werkzeug zeigt standardmäßig nur eine Vorschau: Entfernen, Verschieben und Ergänzen erscheinen vor dem Schreiben getrennt. Erst der ausdrückliche Schalter `--apply` wendet den vollständig angezeigten Plan ohne weitere Rückfrage an. Direkt davor legt das Werkzeug unter `BlinkRead/backups/` ein Zeitstempel-Backup an. Größere Verarbeitungsschritte zeigen einen sparsamen, kompakten Fortschrittsbalken.

Das Werkzeug ist idempotent: Wiederholtes Ausführen erzeugt weder Änderungen noch zusätzliche Backups. Die Bedienlogik folgt den allgemeinen Vorgaben aus `POWERSHELL-KONVENTIONEN.md`: Parameterbetrieb ohne Rückfragen, schreibende Massenaktion nur mit explizitem Anwenden, vorherige Vorschau, Sicherung, Fortschritt und Abschlusszusammenfassung.
