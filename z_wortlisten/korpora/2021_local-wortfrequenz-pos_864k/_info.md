# 2021 Local Wortfrequenz mit POS, 864k

## Inhalt

- `worte.sqlite3.gz`: verlustfrei komprimierte SQLite-Datenbank mit 864.609
  Zeilen in der Tabelle `worte_pos`
- `worte-2-6.tsv`: Arbeitsauszug mit 39.960 alphabetischen Wortformen von zwei
  bis sechs Zeichen; `NE`-Eigennamen und `FM`-Fremdmaterial sind ausgeschlossen
- `worte.sqbpro`: ursprüngliche DB-Browser-Projektdatei
- `worte.sqlite3-journal`: mitgelieferte kleine Journaldatei
- `compression-manifest.tsv`: Größen und SHA-256 von Originaldatenbank und
  Archiv

Die Dateizeitstempel und die Projektdatei datieren von 2021. Die ursprüngliche
Korpusquelle ist nicht dokumentiert; `local` und `2021` kennzeichnen deshalb
Quelle und letzten nachvollziehbaren Stand, nicht ein behauptetes Korpusjahr.

## Felder und Reihenfolge

`worte_pos` enthält `id`, `wort`, `count`, `percent`, `types` und `desc`.
`types` verwendet das Stuttgart-Tübingen-Tagset (STTS). Die SQLite-Tabelle ist
primär nach ihrer vorhandenen ID nutzbar; der Export `worte-2-6.tsv` enthält
`wort`, `haeufigkeit` und `wortarten` und ist nach Häufigkeit absteigend,
anschließend nach Wortform sortiert.

Sinnvolle Sortierungen und Filter sind:

- Häufigkeit absteigend für gebräuchliche Wörter
- Wortform alphabetisch oder nach Zeichenlänge
- Wortarten, etwa `NN` für Nomen oder Verb-Tags
- Ausschluss von `NE`, `FM`, Abkürzungen und nichtalphabetischen Formen

BlinkRead übernimmt aus dieser Quelle nichts automatisch. Nur manuell geprüfte,
allgemein verständliche Wörter werden eingebaut. Zur direkten SQLite-Nutzung
`worte.sqlite3.gz` zunächst als `worte.sqlite3` entpacken.
