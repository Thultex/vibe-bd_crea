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
- Bedienung: Im Telefon-/Selbstmodus bleibt die Intensität beim Gefühlswechsel erhalten; im Wifi-Sendemodus startet das neue Gefühl wieder auf Stufe 1. Neutral setzt in beiden Modi auf 0.
- Animation: Beim erneuten Drücken derselben Gefühlstaste startet die Animation sofort; die kurze Überblendverzögerung bleibt ausschließlich für tatsächliche Motivwechsel bestehen.
- Anzeige: Im Bereitschaftszustand zeigt die zweite Displayzeile dynamisch den Projektnamen und die aktuelle Version.
- Anzeige: Die zweizeilige Start-/Copyrightanzeige nutzt weiterhin die normale Detailzeilenhöhe; Überstand ist erlaubt, ohne App-Größe oder Seitenverhältnis beim Neustart zu verändern.
- Anzeige: Beim Neustart über Aus leiten Kirby-artige ASCII-Gesichter den ruhigen Aufbau von Emotronic von links nach rechts ein; der vollständige Name bleibt anschließend länger stehen.
- Link: Direkte Startmodi verwenden `#simon`, `#on` und `#off`; ohne Modusfragment startet die App eingeschaltet.
- Simon: Die Schwierigkeitsauswahl erhält einen kurzen Startjingle und den animierten Aufbau von `Simon Feels!`; Eingaben bleiben sofort möglich und brechen den Titelaufbau ab.
- Simon: Die Auswahl erfolgt nun über Neugier für Leicht, Neutral für Normal und Unsicherheit für Profi statt über Telefon, Neutral und Wifi.
- Anzeige: Der Titel wird als `Simon Feels!` in derselben Schriftgröße wie die normale Introanzeige aufgebaut.
- Anzeige: `Simon Feels!` sitzt gegenüber der normalen Mittelposition nur drei Pixel tiefer.
- Anzeige: `Simon Feels!` zusätzlich um drei Viertel seiner eigenen Schrifthöhe nach unten versetzt, ohne Größe oder übrige Simon-Anzeigen zu ändern.
- Audio: Der Geschafft-Jingle beginnt rund 0,2 Sekunden nach dem letzten korrekten Tastendruck und kollidiert dadurch weniger mit dessen Ton.
- Link: `#simon` wartet zunächst auf weißem Display mit kleinem Spielsymbol auf einen Tipp und startet erst danach Simon-Animation und -Ton.
- Link: Telefon kopiert in Bereit, auf der Simon-Auswahl und im ausgeschalteten Zustand ohne Hinweistext den passenden Direktlink.
- Bedienung: Ein einfacher Tipp auf Telefon oder Wifi zeigt drei Sekunden lang direkt unter der kleinen Emotionsanzeige den passenden Hinweis für Gefühl- beziehungsweise Replay-Teilen per Doppeltipp.
- Share: Eingehende Emotions-, Replay- und Score-Links warten ohne Zeitlimit mit ruhig weiterlaufendem Nachrichtensymbol im schlichten Hauptdisplay; Bildschirm oder Taste außer Aus startet die lautlose Wiedergabe.
- Share: Nach dem Starttipp beginnt der empfangene Inhalt mit rund 0,1 Sekunden kurzem Abstand.
- Score: Beim Simon-Game-Over wird ein Link mit Endstand, Modus und vollständiger Folge automatisch kopiert; Telefon kopiert ihn manuell erneut und `R` spielt die gesamte Folge noch einmal.
- Score: Empfangene Score-Links spielen ihre Folge automatisch; links stehen Punktzahl und Replay-Abbruchhinweis, und jeder Tastenklick kehrt sofort zum Game Over zurück.
- Link: Gefühle und Replays verwenden ausschließlich `#share=…`; Game-over-Links verwenden ausschließlich `#score=…`.
- Fix: Die zuvor durch den Spielmodus blockierte Telefontaste ist am Game Over wieder klickbar und kopiert den Score-Link manuell.
- Bedienung: Am Game Over stehen Neugier, Neutral und Unsicherheit wieder als direkte Auswahl für Leicht, Normal und Profi bereit; `R` bleibt Replay und `⏻` Schluss.
- Fix: Während des Score-Replays werden Leicht, Normal und Profi wieder als normale Gefühle dargestellt und wie alle übrigen inaktiven Tasten abgedunkelt.
- Bedienung: `R` auf der Simon-Titelauswahl kehrt zum letzten Game-over-Bildschirm samt Modus und Folge zurück.
- Bedienung: Aus führt vom Game Over zunächst zur Simon-Titelauswahl zurück und schaltet die App von dort aus direkt aus.
- Anzeige: Die Score-Empfangsanimation zeigt zusätzlich einen kleinen Pokal und die Punktzahl in einer dezenten wartenden Bewegung.
- Audio: Den Empfangs-Jingle vollständig entfernt; der Starttipp beginnt Emotion oder Replay ohne zusätzlichen Empfangston.
- Bedienung: Aus bricht die laufende Empfangsphase oder Replay-Wiedergabe unmittelbar ab.
- Replay: Der Wechsel zu Bereit durch zweimaliges Drücken von Neutral leert den Replay-Verlauf vollständig.
- Replay: Im Normalmodus werden Gefühl, Emotion und Intensität mit einem sehr leichten Fade während der Wiedergabe aus- und danach wieder eingeblendet.
- Fix: Empfangene Replays beginnen direkt beim ersten Schritt, ohne den Endzustand zuvor kurz einzublenden und in das erste Bild zu überblenden.
- Datenschutz: Detaillierten lokalen Projektpfad aus dem Ruckpacken-Startskript entfernt und öffentliche Repository-/Share-Hinweise dokumentiert.
- Test: JavaScript-Syntax, Manifest, Icons, Service-Worker-Dateien, doppelte HTML-IDs, Versionsgleichlauf, mobile Breite und Browser-Smoke-Test geprüft.
- Doku: Übersicht, Anleitung, Design, Ideen, Plan, Installationshinweise und technische Übergabe ergänzt.
- Anzeige: Der direkte Simon-Einstieg verwendet weiterhin den farbigen OpenMoji-Controller `1F3AE`; im ausgeschalteten Zustand ersetzt nun die farbige Videokassette `1F4FC` das `R`.
- Anzeige: Der Aus-Knopf verwendet das farbige OpenMoji-Symbol `1F50D`.
- Anzeige: Die beiden nur im ausgeschalteten Zustand sichtbaren OpenMoji-Symbole verwenden die schwarz-weißen Varianten und wurden mit reduziertem Innenabstand auf 36 Pixel vergrößert, ohne die Tastenhöhe zu verändern.
- Fix: Videokassette und Lupe erscheinen nur noch im ausgeschalteten Zustand; eingeschaltet werden wieder `R` und das normale Power-Zeichen dargestellt.
- Bedienung: Beim Ausschalten wird die Intensität samt Zeiger sofort auf `0` gesetzt.
- Fix: Die untere Funktionstastenreihe besitzt trotz der 36-Pixel-Symbole eine feste, inklusive Rahmen berechnete Höhe von 43 Pixeln und wächst beim Ausschalten nicht mehr.
- Anzeige: Die Score-Empfangsvorschau verwendet den tatsächlich verlinkten OpenMoji-Pokal `1F3C6` statt eines plattformabhängigen Emoji-Zeichens.
- Design: OpenMoji ist künftig in Emotronic zu bevorzugen, wo Motiv und Darstellung sinnvoll passen; Text- und ASCII-Fallbacks bleiben erhalten.
- Versionen: Emotronic v1.97.
