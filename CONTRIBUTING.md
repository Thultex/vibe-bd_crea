# Contributing

## Repo-Struktur

Dieses Repository sammelt Boardgame-Materialien, Regeln, Designs und optionale Tools.

- Jedes Spiel liegt in einem Root-Ordner `sp-[name]`.
- Der Root-Ordner nutzt den vollen Spielnamen in lowercase, z. B. `sp-zeilenfuttern`.
- Innerhalb der Spielstruktur zaehlt die Kurzversion des Spiels.
- Platzhalter sind sinnbildlich: `[name]` ist lowercase, `[Name]` ist Titlecase, `[NAME]` ist uppercase. Die eckigen Klammern werden nie in Datei- oder Ordnernamen geschrieben.
- Umlaute und deutsche Sonderzeichen sind in Dokumentation, Spieltexten, Materialdaten, Tool-Oberflaechen und Tool-Eingaben erlaubt.
- Jedes Spiel hat eine eigene Uebersicht `z_README-[NAME].md`.
- Bild-, Video- und andere Medien-Assets liegen direkt im Spielordner unter `assets/`, bei Bedarf in Unterordnern wie `assets/images/`.
- Allgemeine Dateien wie CSV, ZIP, JSON sowie nicht ausfuehrbare JS-/Python-Quellen liegen direkt im Spielordner unter `files/`.
- Ausfuehrbare Spieltools und Hilfsskripte liegen direkt im Spielordner unter `tools/`.
- Allgemeinverstaendliche Spielregeln stehen direkt im Spielordner als `anleitung_[name].md`.
- Designdokumente heissen `design_[name].md` und enthalten Materiallisten, Spezifikationen, detaillierte Regeln und Spezialfaelle.
- Noch nicht eingebrachte Ideen stehen in `ideen_[name].md`.
- Naechste Schritte stehen in `plan_[name].md`.
- Das spielbezogene Changelog heisst `z_CHANGELOG-[NAME].md`.

Beispiel fuer `Zeilenfuttern` mit Kurzversion `zeifu`:

```text
sp-zeilenfuttern/
  z_README-ZEIFU.md
  z_CHANGELOG-ZEIFU.md
  design_zeifu.md
  ideen_zeifu.md
  plan_zeifu.md
  anleitung_zeifu.md
  assets/
  files/
  tools/
```

## Pflege & Versionierung

Jede inhaltliche Aenderung an einem Spiel wird an zwei Stellen dokumentiert:

- in der betroffenen Spiel-, Design-, Ideen-, Plan-, Material- oder Tool-Datei
- im passenden `z_CHANGELOG-[NAME].md` als Spielverlauf und Arbeitsprotokoll

Regeln:

- Vor Abschluss jeder inhaltlichen Aenderung aktiv pruefen, ob das passende `z_CHANGELOG-[NAME].md` den aktuellen Stand enthaelt.
- Changelog mit Datum, Dauer, Aenderungstyp und Wirkung ergaenzen.
- Changelog-Tagesbloecke nennen direkt nach dem Datum alle betroffenen Kategorien kommasepariert, z. B. `### 2026-06-21 - zeifu, struktur, doku (0,4h)`.
- Kategorien sind kurze Arbeitsbereiche wie Spielkuerzel, `regeln`, `design`, `assets`, `tools`, `struktur`, `doku`, `ideen` oder `plan`.
- Gleiche Tage im Changelog in einem Tagesblock zusammenziehen.
- Tests, Doku, Materialstand und Toolversionen im Tagesblock erwaehnen, wenn sie betroffen sind.
- Wenn Tools eigene Versionen fuehren, neue produktive Tools bei `v1.00` starten und bei jeder Aenderung fortlaufend hochzaehlen, z. B. `v1.01`, `v1.02`.
- Ausfuehrliche Aenderungslisten gehoeren ins Changelog, nicht in Tool-Kopfkommentare.
- Kommentare in Tools sollen Entscheidungen erklaeren, nicht offensichtliche Codezeilen wiederholen.

## Changelog-Format

- Datum, Kategorien und Dauer im Format `### YYYY-MM-DD - zeifu, design (2,3h)`; bei mehreren Sessions optional mit Anzahl, z. B. `(2,2h, 3x)`.
- Wenn Git-Zeitpunkte oder Commits den Arbeitszeitraum belastbar eingrenzen, die Dauer daraus ableiten und als `ca.` markieren, z. B. `(ca. 0,5h)`.
- Wenn eine Dauer genannt wird, diese uebernehmen.
- Wenn nur ein unklarer Arbeitsblock vorliegt, eine vorsichtige `ca.`-Schaetzung nutzen und nicht mit leeren Platzhaltern arbeiten.
- Unter `Stats` zuerst `Ausgangsdatum: YYYY-MM-DD` notieren.
- Danach feste Stats-Abschnitte nutzen: `Diese Woche`, `Letzte Woche`, `Dieser Monat`, `Letzter Monat`, `Jahr`, `Insgesamt`.
- Stats-Abschnitte im Format `*Abschnitt (Dauer, Tage, Inhalte):*` schreiben; darunter eine kurze spezifische Themenzeile, keine Tabelle.
- Stats-Inhalte nach Relevanz sortieren: verhaltensrelevante Spielaenderungen vor Doku/Formalia.
- Eintraege stehen unter `## Log`; jeder Tagesblock ist ein `###`-Punkt.
- Pro Arbeitsschritt kurze Stichpunkte schreiben.
- Datei, Material oder Tool nennen, wo es hilfreich ist.
- Normale Eintraege beginnen mit Typ, z. B. `Feature:`, `Fix:`, `Change:`, `Doku:`, `Test:`, `Refactor:`, `Struktur:` oder `Material:`.
- Issue direkt hinter das Thema setzen, z. B. `- Feature: Neuer Wertungsmodus (#12); Wirkung fuer die Partie beschreiben.`
- Ab 7 Punkten im Tagesblock als ersten Punkt eine kurze Zeile `Summary: ...` ergaenzen.
- Wirkung dokumentieren, nicht nur `Fix` oder `Update`.
- Versionsspruenge nicht als eigene Hauptpunkte fuehren.
- Versionen bei Bedarf immer als letzten Stichpunkt des Tages gesammelt nennen; pro Tool nur die neueste erreichte Version nennen, z. B. `- Versionen: zeifu-exporter v1.02.`

## Vorlage

```md
### 2026-06-21 - zeifu, regeln, design (0,4h)

- Summary: Kurze Tageszusammenfassung bei laengeren Tagesbloecken.
- Feature: Neue Regel ergaenzt; Wirkung fuer die Partie beschreiben.
- Material/Doku: Karte, Anleitung oder Designnotiz aktualisiert.
- Versionen: tool-name v1.02.
```
