# 2011 Leipzig Mixed Typical, 1 Million Sätze

## Inhalt

Rohbestand `deu_mixed-typical_2011_1M` der Leipzig Corpora Collection mit
Wort-, Satz-, Quellen-, Kookkurrenz- und Invertierungstabellen sowie einem
SQL-Importskript. Die direkt genutzte Worttabelle bleibt unkomprimiert. Die
drei größten Tabellen `inv_w`, `sentences` und `sources` sind verlustfrei als
`.gz` gespeichert.

## Felder und Reihenfolge

Die Texttabellen sind tabulatorgetrennt. Je nach Datei enthalten sie numerische
IDs, Wortformen, Häufigkeiten, Satztexte, Quellenkennungen oder Beziehungen
zwischen IDs. Die Originalreihenfolge wurde unverändert bewahrt und soll nicht
als einheitliche alphabetische oder pädagogische Rangfolge interpretiert
werden. Das genaue Tabellenschema steht in
`deu_mixed-typical_2011_1M-import.sql` und in der offiziellen
Formatbeschreibung.

Sinnvolle Sortierungen nach dem Import sind insbesondere:

- Wörter nach Häufigkeit absteigend oder Wortform alphabetisch
- Sätze und Quellen nach numerischer ID
- Kookkurrenzen nach Signifikanz beziehungsweise Häufigkeit
- Wortbeziehungen nach den jeweiligen Fremdschlüssel-IDs

Vor dem SQL-Import müssen die drei `.gz`-Dateien wieder unter den in
`compression-manifest.tsv` genannten Originalnamen entpackt werden. Das
Manifest enthält Original- und Archivgröße sowie beide SHA-256-Prüfsummen; die
Archive wurden vollständig dekomprimiert und bytegenau rückgetestet.

Formatbeschreibung: https://wortschatz.uni-leipzig.de/documents/Format_Download_File-deu.pdf

Die historische Datei `leibnitz-100k` gehört ausdrücklich nicht zu diesem
Verzeichnis, weil ihre Herkunft nicht belegt ist.
