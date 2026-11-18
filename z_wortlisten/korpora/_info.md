# Korpora und Referenzlisten

Namensschema: `JAHR_name-art_umfang`. Fehlt ein belegter Quellenname, wird
`local` verwendet. Fehlt ein belegtes Korpusjahr, steht das letzte
nachvollziehbare Bestandsjahr an erster Stelle.

| Verzeichnis | Inhalt | Provenienz |
| --- | --- | --- |
| `2011_leipzig-mixed-typical_1m/` | Leipzig-Korpus `deu_mixed-typical_2011_1M` | durch Korpuskennung belegt |
| `2021_local-wortfrequenz-pos_864k/` | lokale SQLite-Wortfrequenzliste mit STTS-Wortarten | ursprüngliche Korpusquelle unbekannt; Stand 2021 |
| `2024_brandenburg-grundwortschatz_685/` | amtlicher Grundwortschatz Brandenburg | belegt |
| `2026_local-haeufigkeitsliste_102k/` | historische Datei `leibnitz-100k` | Herkunft unbekannt; im Repo seit 2026 nachvollziehbar |

`leibnitz-100k` ist **nicht** dem Leipziger Mixed-Typical-Korpus zugeordnet.
Der Name ist nur ein historischer Dateiname und kein Herkunftsnachweis.

Jedes Korpusverzeichnis enthält `_info.md` mit Inhalt, Feldern, bestehender
Reihenfolge und sinnvollen Sortiermöglichkeiten. Große Rohdateien liegen
verlustfrei als `.gz` vor. `compression-manifest.tsv` dokumentiert
Originalgröße und SHA-256 von Original und Archiv.
