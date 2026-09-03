# Routine: Bilder importieren und zuordnen

Aus dem Repository-Root ausführen:

```powershell
python -B sp-ruckpacken/tools/cardmaker/sync_custom_images.py
```

Im CardMaker-Ordner genügt `python -B sync_custom_images.py`. Die Routine v1.00 benötigt nur die Python-Standardbibliothek und findet das Spielverzeichnis unabhängig vom aktuellen Arbeitsverzeichnis.

1. Neue Gegenstandsbilder unter `sp-ruckpacken/assets/img/` ablegen, beispielsweise unter `objects/`. Pro Motiv werden eine `.concepts`-Datei und ein gleichnamiger `.png`-Export im selben Ordner erwartet; auch die Schreibweise `.conzepts` wird erkannt. Die leere `_Size_709x709__Line_17-5px.txt` dient nur zur Orientierung und wird ignoriert.
2. Dateinamen wie `rp1_ball.concepts` und `rp1_ball.png` verwenden. Die Nummer entspricht der Gegenstandsliste, der Name muss dazu passen. Reine Gegenstandsnamen wie `Ball.png` sind ebenfalls möglich, ebenso Umlaute oder Umschreibungen wie `Giesskanne` und `Massband`.
3. Die Routine starten. Sie erkennt vollständige Paare rekursiv, prüft die Zuordnung und schreibt `files/data/custom-img_mapping.csv` mit allen 73 Gegenständen. Unvollständige Paare werden gemeldet und vorerst durch ARASAAC abgedeckt. Widersprüchliche Namen, mehrere Paare für denselben Gegenstand oder fehlende benötigte ARASAAC-Dateien stoppen den Abgleich vor dem Schreiben.
4. `ruckpacken.cmp` in CardMaker neu laden und exportieren. Die vorhandene Reference auf `cards.csv` verwendet nun direkt `assets/images/sym_1.png` bis `assets/images/sym_73.png`.

Der Bildsatz liegt vollständig im CardMaker-Ordner:

| Pfad relativ zu `tools/cardmaker/` | Inhalt |
|---|---|
| `assets/images/custom/sym_<Nr>.png` | unveränderte PNG-Kopien der eigenen Motive |
| `assets/images/arasaac/color/sym_<Nr zweistellig>.png` | bestehende ARASAAC-Quellen und Rückfallbilder |
| `assets/images/sym_<Nr>.png` | aktiver Bildsatz: eigenes Motiv bevorzugt, ansonsten ARASAAC |
| `cards.csv` | neun Bildreferenzen je Karte auf den aktiven Bildsatz direkt unter `assets/images/` |

Die CSV `files/data/custom-img_mapping.csv` hält `Nr`, `Gegenstand`, `Concepts`, `PNG`, `Quelle`, `CardMaker_Custom` und `CardMaker_Aktiv` fest. Alle Pfade darin sind relativ zu `sp-ruckpacken/`. Bei ARASAAC bleiben `Concepts` und `CardMaker_Custom` leer. Die Datei wird aus den Quellen neu erzeugt; Zuordnungen werden über die Dateinamen gepflegt.

Aktueller Stand: **Ball** aus `rp1_ball.concepts` / `rp1_ball.png`, dazu **72 ARASAAC-Motive**. Originale und ARASAAC-Attribution bleiben erhalten. Entfernte oder unvollständige eigene Paare führen im aktiven Bildsatz wieder zu ARASAAC; ältere Kopien im Unterordner `custom` bleiben erhalten und werden nicht mehr referenziert. Ein erneuter Lauf mit unveränderten Quellen schreibt keine Dateien neu.

Vorschau und Konsistenzprüfung aus dem CardMaker-Ordner:

```powershell
python -B sync_custom_images.py --dry-run
python -B sync_custom_images.py --check
python -B validate_cm_project.py
```

`--dry-run` zeigt anstehende Änderungen. `--check` verändert keine Dateien und liefert Exitcode 1, wenn Mapping, Bildkopien oder Kartenreferenzen aktualisiert werden müssen. Der Projektvalidator prüft ebenfalls diese Übereinstimmung. Die gezielten Regressionstests lassen sich mit `python -B test_sync_custom_images.py` ausführen.

## Abschluss eines Imports

- Die Zusammenfassung auf die erwartete Anzahl eigener Motive prüfen. Hinweise zu unvollständigen Paaren bearbeiten; die Routine erneut ausführen, sobald beide Dateien vorliegen.
- In [custom-img_mapping.csv](data/custom-img_mapping.csv) Gegenstand, Originalpaar, Quelle und aktiven Pfad prüfen. Die Zeilennummern folgen der Gegenstandsliste, nicht der Merkmalsliste.
- `python -B validate_cm_project.py` im CardMaker-Ordner ausführen. Damit werden die 73 Karten, 657 Bildreferenzen und der aktuelle Bild-/Mappingstand geprüft.
- Neue Bilder in CardMaker bei Originalgröße ansehen. Die Import-Routine kopiert PNGs unverändert; sie bearbeitet weder Motiv noch Transparenz, Auflösung oder Randabstände.
- Den Import im `z_CHANGELOG-RUPA.md` dokumentieren und Originalpaare, Mapping, aktualisierte Bildkopien und gegebenenfalls `cards.csv` gemeinsam committen und pushen.

Die ausführbare Routine liegt unter [`tools/cardmaker/sync_custom_images.py`](../tools/cardmaker/sync_custom_images.py). Sie importiert die Gegenstandsbilder für die bestehende 73-Symbol-Kartenmatrix. Merkmalszeichnungen benötigen eine eigene Zuordnung und dürfen nicht mit Gegenstandsnummern vermischt werden.
