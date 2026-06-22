# Changelog ZEIFU

## Stats

Ausgangsdatum: 2026-06-21

*Diese Woche (ca. 2,7h, 2 Tage, 48 Inhalte):*
Zeifu: Grundstruktur angelegt, Spielinhalte direkt im Spielordner gebuendelt, README-/Changelog-Namen vereinheitlicht, Wortanalyse-Tool ergaenzt und erweitert, Regex101-Absprung ergaenzt, Eingabebereiche neu geordnet, Dateiimport und Textspeicherung ergaenzt, Textstandards `Nordwind & Sonne` und `Leibnitz 100k (mixed typical)` ergaenzt, Print-Cleanup und Cleanup-/Ausgabeoptionen ergaenzt, Print-Schriftauswahl ergaenzt, Basisschreibweise auf `=`/`#` umgestellt, Positionsmarker auf `p` umgestellt, gerichtete `c`-Kombos ergaenzt, `k` auf `#k` fuer Konsonanten reserviert, nummerierte Regex-Aufgaben ergaenzt, Copy-Buttons verschoben und gekuerzt, Standardtext gesetzt sowie Anleitung v1.08 und Designdokument v1.01 eingebunden.

*Letzte Woche (0,0h, 0 Tage, 0 Inhalte):*
Keine Eintraege.

*Dieser Monat (ca. 2,7h, 2 Tage, 48 Inhalte):*
Zeifu: Grundstruktur angelegt, Spielinhalte direkt im Spielordner gebuendelt, README-/Changelog-Namen vereinheitlicht, Wortanalyse-Tool ergaenzt und erweitert, Regex101-Absprung ergaenzt, Eingabebereiche neu geordnet, Dateiimport und Textspeicherung ergaenzt, Textstandards `Nordwind & Sonne` und `Leibnitz 100k (mixed typical)` ergaenzt, Print-Cleanup und Cleanup-/Ausgabeoptionen ergaenzt, Print-Schriftauswahl ergaenzt, Basisschreibweise auf `=`/`#` umgestellt, Positionsmarker auf `p` umgestellt, gerichtete `c`-Kombos ergaenzt, `k` auf `#k` fuer Konsonanten reserviert, nummerierte Regex-Aufgaben ergaenzt, Copy-Buttons verschoben und gekuerzt, Standardtext gesetzt sowie Anleitung v1.08 und Designdokument v1.01 eingebunden.

*Letzter Monat (0,0h, 0 Tage, 0 Inhalte):*
Keine Eintraege.

*Jahr (ca. 2,7h, 2 Tage, 48 Inhalte):*
Zeifu: Grundstruktur angelegt, Spielinhalte direkt im Spielordner gebuendelt, README-/Changelog-Namen vereinheitlicht, Wortanalyse-Tool ergaenzt und erweitert, Regex101-Absprung ergaenzt, Eingabebereiche neu geordnet, Dateiimport und Textspeicherung ergaenzt, Textstandards `Nordwind & Sonne` und `Leibnitz 100k (mixed typical)` ergaenzt, Print-Cleanup und Cleanup-/Ausgabeoptionen ergaenzt, Print-Schriftauswahl ergaenzt, Basisschreibweise auf `=`/`#` umgestellt, Positionsmarker auf `p` umgestellt, gerichtete `c`-Kombos ergaenzt, `k` auf `#k` fuer Konsonanten reserviert, nummerierte Regex-Aufgaben ergaenzt, Copy-Buttons verschoben und gekuerzt, Standardtext gesetzt sowie Anleitung v1.08 und Designdokument v1.01 eingebunden.

*Insgesamt (ca. 2,7h, 2 Tage, 48 Inhalte):*
Zeifu: Grundstruktur angelegt, Spielinhalte direkt im Spielordner gebuendelt, README-/Changelog-Namen vereinheitlicht, Wortanalyse-Tool ergaenzt und erweitert, Regex101-Absprung ergaenzt, Eingabebereiche neu geordnet, Dateiimport und Textspeicherung ergaenzt, Textstandards `Nordwind & Sonne` und `Leibnitz 100k (mixed typical)` ergaenzt, Print-Cleanup und Cleanup-/Ausgabeoptionen ergaenzt, Print-Schriftauswahl ergaenzt, Basisschreibweise auf `=`/`#` umgestellt, Positionsmarker auf `p` umgestellt, gerichtete `c`-Kombos ergaenzt, `k` auf `#k` fuer Konsonanten reserviert, nummerierte Regex-Aufgaben ergaenzt, Copy-Buttons verschoben und gekuerzt, Standardtext gesetzt sowie Anleitung v1.08 und Designdokument v1.01 eingebunden.

## Log

### 2026-06-22 - zeifu, memo #1 (ca. 0,7h)

- Tooling: Memo #1 umgesetzt; Basisschreibweise schreibt standardmaessig nicht mehr ins Aufgabenfeld, wird aber weiter intern fuer die Analyse verstanden.
- Tooling: Basisschreibweise auf `=` und `#` umgestellt; Positionsmarker wie `(d, t)=i`, Einzelmarker wie `(a)=i` sowie Kurzgruppen wie `#v=i` und `(#v, #u)=2` werden erkannt, alte `"`-Positionsmarker bleiben als Fallback gueltig.
- Tooling: Ausgabeoptionen getrennt; Wortausgaben koennen erzwungen klein oder gross geschrieben werden und Drucktabellen koennen optional ein Tabellengitter zeigen.
- Tooling: Namenlose Regex-Aufgaben koennen nun auch als nummerierte Zeilen wie `1. sch` oder `2) [aeiou]` eingegeben werden.
- Tooling: Aufgaben-Wortausgaben sortieren Trefferwoerter zuerst nach Treffergruppe, damit gleiche Buchstaben, Laute oder Silben zusammenbleiben.
- Tooling: Gerichtete Kombos ergaenzt; `(ch, a, o, u)=c+` erzeugt feste Reihenfolgen mit erstem Laut wie `cha`, `cho`, `chu`, waehrend `(a, o, u, ch)=c-` feste Reihenfolgen mit letztem Laut wie `ach`, `och`, `uch` erzeugt.
- Tooling: Kombomarker von `k` auf `c` umgestellt; `k` bleibt nur noch im Kuerzel `#k` fuer Konsonanten erhalten.
- Tooling: Verhalten von `c+` und `c-` getauscht; Plus steht nun fuer ersten festen Laut, Minus fuer letzten festen Laut.
- Tooling: Text kann nun per Dateiimport geladen werden; das Aufgabenfeld hat einen eigenen Leeren-Button.
- Tooling: Buttonbeschriftungen gekuerzt: `Regex101`, `Reset`, `Leeren`.
- Tooling: Sichtbare Konvertierung der Basisschreibweise ins Aufgabenfeld entfernt; Aufgaben bleiben in der eingegebenen Notation sichtbar und werden nur intern analysiert.
- Tooling: Monospace-Checkbox fuer Druckseiten durch speicherbare Schriftauswahl ersetzt; verfuegbar sind Sans, Mono, Serif, Arial Rounded, Verdana, Trebuchet MS, Century Gothic, Comic Sans MS und Consolas.
- Tooling: Positionsmarker von `i/m/f` auf `p` umgestellt; `p` und `p+` markieren initial, `p-` final, `p~` medialen Kontext sowie `p++`, `p--` und `p~~` die exklusiven Varianten.
- Tooling: Textfeld-Inhalt wird nun lokal zwischengespeichert; auch geladene Datei-Inhalte erscheinen beim erneuten Oeffnen wieder, soweit Browser-Speicher verfuegbar ist.
- Tooling: Standardauswahl fuer Texte in die Aktionszeile neben `Analysieren` und `Leeren` verschoben; Eintraege heissen nun `Nordwind & Sonne` und `Leibnitz 100k (mixed typical)`.
- Fix: Auswahl `Standard` laedt nun ebenfalls aktiv den Standardtext; eigener gespeicherter Text nutzt einen neutralen Dropdown-Zustand.
- Fix: `Leibnitz 100k (mixed typical)` nutzt zusaetzlich eine lokale JS-Fallbackdatei, damit das Preset auch ohne erfolgreichen `fetch` beim direkten Oeffnen der HTML-Datei geladen werden kann.
- Tooling: Case-sensitive Basisschreibweise mit `!` ergaenzt; z.B. `!A=i` oder `!(A, B)=i` erzwingen Gross-/Kleinschreibung fuer diese Basisteile, waehrend normale Aufgaben weiter case-insensitive bleiben.
- Versionen: word-task-analyzer v1.84.

### 2026-06-21 - zeifu, struktur, doku (ca. 1,4h)

- Struktur/Doku: Spielgeruest fuer Zeilenfuttern angelegt; README, Anleitung, Design, Ideen, Plan, Changelog sowie Material- und Toolordner sind vorbereitet.
- Doku: Spielanleitung v1.08 fuer Zeilenfutter eingebunden; Ziel, Material, Vorbereitung, Ablauf, Wortanlege-Regeln, Spielende, Wertung und Beispiele sind dokumentiert.
- Design: Designdokument v1.01 eingebunden; paedagogische Ziele, Phonetik-Schwerpunkte, Wortbildung, Sprachbewusstsein und Designprinzipien sind als Entwicklungsgrundlage erfasst.
- Struktur: Zwischenordner `game-zeifu/` entfernt; Anleitung, `assets/` und `tools/` liegen direkt unter `sp-zeilenfuttern/`.
- Struktur: README und Changelog auf die Praefix-Namen `z_README-ZEIFU.md` und `z_CHANGELOG-ZEIFU.md` umgestellt.
- Tooling: Offline nutzbares HTML5-Wortanalyse-Tool ergaenzt; es extrahiert Woerter ohne Punktuation, sortiert nach Laenge und Alphabet und zaehlt frei definierbare Regex-Aufgaben mit Buchstabenstatistik.
- Tooling: Wortanalyse-Tool erweitert; doppelte Woerter werden vor Sortierung und Bewertung entfernt, minimale und maximale Wortlaenge sind einstellbar, Ergebnisbereiche sind klappbar und die Aufgabenanalyse steht rechts neben Generelles/Wortliste.
- Tooling: Regex101-Link im Aufgabenbereich ergaenzt; der erste Aufgaben-Regex wird als Regex-Parameter und der Aufgabenblock als Test-String an `https://regex101.com/` uebergeben.
- Tooling: Eingabe im Wortanalyse-Tool neu geordnet; Text, Aufgaben und Optionen sind getrennte klappbare Kaesten, der Analysebutton steht direkt im Textbereich und die Wortlaengenoptionen stehen unter den Aufgaben.
- Tooling: Wortanalyse-Ausgabe angepasst; Generelles zeigt mittlere Wortlaenge statt Duplikatzaehler, fehlende Buchstaben sind als `(de)` markiert, die Laengenuebersicht zeigt nur Mengen und ein Print-Cleanup gibt die sortierten eindeutigen Woerter mit Copy-Buttons fuer Text und zweispaltige HTML-Tabelle aus.
- Tooling: Cleanup-Optionen fuer die Wortanalyse ergaenzt; Duplikatentfernung ist standardmaessig aktiv, Umlaute-zu-Doppelvokal, Diakritika entfernen, Bindestrichverbindung und Zahlen-an-Woertern sind optional.
- Tooling: Standardtext im Wortanalyse-Tool auf `Der Nordwind und die Sonne` gesetzt.
- Tooling: Copy-Buttons fuer Print-Wortliste und zweispaltige HTML-Tabelle aus dem Print-Cleanup in den Bereich `Generelles` verschoben.
- Tooling: Aufgabenanalyse nach Trefferwoertern absteigend sortiert und die Trefferzusammenfassung optisch hervorgehoben.
- Tooling: Aufgaben koennen Punkte im Namen fuehren, z. B. `Vokalkombo (2): regex`; Treffer werden ueberlappend gezaehlt und Punkte in der Trefferzeile summiert.
- Tooling: Aufgabenwertung angepasst; ohne Punkteangabe gilt 1 Punkt pro Treffer, Punkte werden nur bei expliziter oder abweichender Wertung angezeigt, `Enthalten:` wurde aus der Trefferzeile entfernt und die Standardaufgaben fassen `st/sp` mit 3 Punkten zusammen.
- Tooling: Aufgabenanalyse sortiert jetzt zuerst nach berechneten Punkten, auch wenn die Punkte wegen Standardwertung nicht sichtbar angezeigt werden.
- Tooling: Copy-Buttons fuer Wortliste und HTML-Tabelle stehen zusaetzlich direkt unter der Printversion; Tabellenbutton ist auf `Tabelle` gekuerzt.
- Tooling: Geschlossenen Hinweisbereich fuer Aufgabenformat und klassische Phonetik-Aufgaben ergaenzt; `sp` ist als Standardaufgabe mit 2 Punkten getrennt von `st` gesetzt.
- Tooling: Phonetik-Hinweise und Standardaufgaben entlang des Designdokuments erweitert; Positionsbeispiele enthalten jetzt vorne, Mitte und hinten sowie Lautgruppen, Kombos, Gegensaetze, Rechtschreibmuster, Umlaute und Affrikaten.
- Tooling: Aufgabenhilfe staerker phonetisch ausgerichtet; Rechtschreibmuster aus Standardaufgaben und Hinweisen entfernt, komplexere phonetische Muster bleiben nur als Beispiele in der Formathilfe.
- Tooling: Einfache Aufgabenlogik ergaenzt; `(d, t)`, `(d, t)"i`, `(d, t)"m` und `(d, t)"f` werden zu Regex fuer allgemein, initial, medial und final uebersetzt und vor den Regex-Beispielen erklaert.
- Tooling: Phonetik-Hilfe um Doppelkonsonanten, Konsonantenverbindungen und eine getrennte Liste inhaltlicher Gruppenideen wie Nasale, Liquide, Plosive, Frikative, Affrikaten, Diphthonge, Endungen und harte/weiche Paare erweitert.
- Tooling: Einfache Aufgabenlogik erweitert; Klammerlisten bleiben Oder-Verbindungen und `"k` markiert nun Kombos, bei denen die Elemente direkt nacheinander gesucht werden.
- Tooling: Einfache Aufgabenmuster werden beim Analysieren direkt im Aufgabenfeld zu Regex umgeschrieben, bevor Auswertung und Regex101-Link aktualisiert werden.
- Tooling: Umschreiben der Basisschreibweise zu Regex als standardmaessig aktive Option ergaenzt; bei deaktivierter Option bleibt die Basisschreibweise sichtbar und wird nur intern ausgewertet.
- Tooling: Format-Hilfe bereinigt; Basisschreibweise wird als intern uebersetzt beschrieben, Beispiele stehen oben einzeln und Gruppenideen sind zeilenweise getrennt.
- Tooling: Regex-Beispiele in der Phonetik-Hilfe auf ein Beispiel pro Zeile umgestellt und um weitere phonetisch/sprachlich interessante Muster wie offene/geschlossene Silbe, Endverhaertungsidee, Anfangscluster und Mehrfachkonsonanz erweitert.
- Tooling: Phonetik-Hilfe nach Recherche um konkrete Einzelbeispiele fuer Ich-/Ach-Laut-Kontexte, Endcluster, sch-/spr-/str-Anfangscluster, r-Kontexte, unbetonte Endungen und Diphthong-Konsonant-Verbindungen ergaenzt.
- Tooling: Grobe Silbenzaehlung ueber Vokalgruppen ergaenzt; Wortfilter fuer minimale/maximale Silbenzahl sowie Aufgabenkurzel `(3)`, `(2, 3)` und `(1-4)` werten geschaetzte Silbenbereiche aus.
- Tooling: Generelle Statistik zeigt mittlere Silbenzahl statt eigenem Fehlbuchstaben-Kasten; fehlende Buchstaben nennen ihre Anzahl in der Textzeile. Silbenkuerzel werden nur bei separater, standardmaessig deaktivierter Option ins Aufgabenfeld zu Regex umgeschrieben.
- Fix: Basisschreibweise-Umschreibung gegen rekursives Escaping gehaertet; vorhandene Regex-Gruppen wie `(?:p|b)` werden nicht mehr erneut umgeschrieben und bereits escaped Gruppen werden beim Analysieren repariert.
- Fix: Silbenkuerzel wie `(4)` und `test: (4)` bleiben bei aktiver Basisschreibweise-Umschreibung unveraendert, solange die separate Silben-Regex-Option aus ist.
- Tooling: Namenlose Aufgaben bekommen sprechende Kurznamen aus bekannter Notation, z.B. `Aufgabe 16: 4-Silber` oder `/ch/ initial`; Silbenaufgaben zeigen in den Details Silbenzahlen statt Buchstabenzaehlung.
- Tooling: Detailzeilen stellen Mengen voran, z.B. `Buchstaben (8): ...`; Silbenaufgaben listen die gezaehlten Silbenstuecke, waehrend Buchstabendetails bei mehr als 20 unterschiedlichen Eintraegen einklappbar sind.
- Tooling: Optionale Wortzuordnung fuer alle Aufgabentypen ergaenzt; Silbenaufgaben zaehlen wieder Silbentypen wie `2-Silber (3)` und Wortzuordnungen werden gruppiert als `Wörter (3): ...` dargestellt.
- Tooling: Tabellenbutton erzeugt druckbare HTML-Seiten im A4-Format mit konfigurierbarer Spaltenzahl und Schriftgroesse; Standard ist 3 Spalten bei Schriftgroesse 30, Links erscheinen kompakt als `Druckseiten: [1], [2]`.
- Tooling: Format-Hilfe gestrafft; Silbenkurzformen stehen in einer Zeile, Gruppenideen enthalten Vokale, Konsonanten, Umlaute und Konsonantenverbindungen, spezielle phonetische Aufgaben stehen getrennt davor.
- Tooling: Generelle Wort- und Buchstabenstatistiken basieren immer auf eindeutigen Woertern, unabhaengig von der Duplikat-Option fuer Ausgabe und Aufgaben.
- Tooling: Regex-Muster werden in der Aufgabenanalyse standardmaessig ausgeblendet und sind nur noch ueber die Debug-Option sichtbar.
- Tooling: Filter fuer minimale/maximale Wortlaenge und Silbenzahl starten standardmaessig bei `0`; `0` deaktiviert den jeweiligen Filter.
- Tooling: Bereich `Generelles` behaelt Mittelwerte und fehlende Buchstaben; die Kennzahlen fuer Woerter und Buchstaben zaehlen dort nur eindeutige Woerter bzw. eindeutige Buchstabentypen.
- Tooling: Trefferzeile und Buchstaben-/Silbendetails in Aufgaben sind nun optional ausblendbar, bleiben aber standardmaessig aktiv.
- Tooling: Standardaufgaben neu balanciert; phonetisch abwechslungsreiche Aufgaben erzielen beim Standardtext aehnlichere Punktbereiche.
- Tooling: Anzeigeoptionen fuer Aufgabenanalyse in eigenen Abschnitt `Anzeigen` verschoben; `Cleanup` enthaelt nur noch Aufbereitungsoptionen.
- Tooling: Punkte werden optional vorne in der fetten Trefferzeile angezeigt, z.B. `(22p): 10 Treffer in 9 Wörtern.`; Standardaufgaben sprachlich vereinfacht.
- Tooling: Zusaetzlichen `Analysieren`-Button unter den Optionen ergaenzt, damit Anzeige- und Filteraenderungen schneller angewendet werden koennen.
- Tooling: `Liquid plus Vokal` und `Vokal plus Liquid` in der Formathilfe von konkreten Aufgabenbeispielen zu Gruppenideen verschoben.
- Tooling: Gruppenideen in der Formathilfe auf kopierbare Basisschreibweise umgestellt; Kombi-Ideen werden als Bausteine mit `+` beschrieben und `R vor Konsonant` zu den Gruppenideen verschoben.
- Tooling: Formathilfe neu sortiert; Beispiele ohne Backticks dargestellt und in Buchstabentypen, Lautgruppen, Kombis/Positionen und Gruppenideen getrennt.
- Tooling: Formathilfe nachgeschärft; Diphthonge bleiben Lautgruppe, Kontextmuster wie initiales st/sp, Zischlaut vor t, Liquid vor Verschluss und Vokal vor sch stehen unter Spezialfaellen, `Mittleres sch` entfernt.
- Tooling: Abschnittsueberschriften in der Formathilfe fett gesetzt und Basisschreibweise-Hinweis in die Ueberschrift integriert.
- Tooling: Abschnitt `Kombis und Positionen` in der Formathilfe direkt hinter die Basisschreibweise und vor die Buchstabentypen verschoben.
- Tooling: Bezeichnung `Gruppenideen` in der Formathilfe zu `Gruppen` vereinfacht.
- Tooling: Doppelkonsonanten in der Formathilfe als gleiche Doppelungen wie `tt` oder `pp` dargestellt; unterschiedliche Folgen bleiben Konsonantenverbindungen.
- Tooling: Doppelkonsonanten-Beispiel wieder als Regex formuliert, aber auf gleiche Doppelungen wie `tt`, `pp` oder `ss` begrenzt.
- Tooling: Konsonantenverbindungen in der Formathilfe ebenfalls als Regex formuliert und `sch` dort entfernt, weil es als eigener Laut unter Lautgruppen steht.
- Tooling: Doppelkonsonanten-Regex auf Konsonantenklasse plus Rueckbezug umgestellt, damit nur echte Paare desselben Konsonanten zaehlen.
- Tooling: Konsonantenverbindungen-Regex ebenfalls auf Konsonantenklasse umgestellt; gezählt werden unterschiedliche Konsonantenpaare statt einer festen Einzelliste.
- Fix: Aufgabenanalyse wertet bei Regex mit Capture-Gruppen den ganzen Treffer aus, damit Doppelkonsonanten nicht als einzelne Konsonanten-Wortlisten erscheinen.
- Fix: Overlap-Auswertung nutzt keine zusätzliche Capture-Gruppe mehr; Backreferences wie `\1` bleiben dadurch in Nutzer-Regex unverändert gültig.
- Tooling: Optionen werden beim Analysieren lokal im Browser gespeichert und beim nächsten Öffnen wieder geladen; eigener Button setzt nur die Optionen auf Standard zurück.
- Tooling: Druckseiten-Links werden kompakt in einer Zeile gerendert; Druckseiten koennen optional mit Monospace-Schrift erzeugt werden.
- Tooling: Aufgabenfeld wird beim Analysieren ebenfalls lokal gespeichert und beim Neuladen wiederhergestellt; der Standardaufgaben-Button schreibt den Standard erneut in den Speicher.
- Tooling: Tabellenbutton erzeugt nur noch Druckseiten-Links und kopiert kein HTML mehr automatisch in die Zwischenablage.
- Tooling: Wortausgaben behalten Groß-/Kleinschreibung aus dem Eingabetext; Kleinschreibung wird nur noch intern fuer Buchstabenanalyse und Duplikatvergleich genutzt.
- Tooling: Basisschreibweise um Doppelungsmarker `"2` erweitert; z.B. `(r, s)"2` wird zu `([rs])\1` fuer `rr` oder `ss`.
- Tooling: Basisschreibweise um Gruppenkuerzel `("k)`, `("v)` und `("u)` fuer Konsonanten, Vokale und Umlaute erweitert; Positionen und Doppelung funktionieren damit ebenfalls.
- Tooling: Gruppenkuerzel funktionieren jetzt auch innerhalb von Listen, z.B. `("v, "u)` fuer Vokale plus Umlaute.
- Tooling: Option ergaenzt, um bei jeder Aufgabenkarte die Trefferwoerter direkt zu kopieren oder als eigene Druckseiten zu erzeugen.
- Tooling: Zahlenoption umgedreht; `Zahlen entfernen` ist jetzt standardmaessig aktiv statt Zahlen an Woertern zu behalten.
- Tooling: Lange Regex-Beispiele fuer Konsonantenverbindungen, Vokalkombo und Doppelkonsonanten durch Basisschreibweise mit Kuerzeln ersetzt.
- Doku/Tooling: Umlaute und deutsche Sonderzeichen sind in Dokumentation, Spieltexten, Materialdaten, Tool-Oberflaechen und Tool-Eingaben ausdruecklich erlaubt.
- Doku: Changelog-Dauer nach ttz-Vorbild von Platzhalter auf `ca.`-Schaetzung umgestellt.
- Versionen: word-task-analyzer v1.72.
