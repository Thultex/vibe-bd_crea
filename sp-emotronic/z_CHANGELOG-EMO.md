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
- Animation: Beim erneuten Drücken derselben Gefühlstaste startet die Animation sofort; die kurze Überblendverzögerung bleibt ausschließlich für tatsächliche Motivwechsel bestehen.
- Anzeige: Im Bereitschaftszustand zeigt die zweite Displayzeile dynamisch den Projektnamen und die aktuelle Version.
- Anzeige: Die zweizeilige Start-/Copyrightanzeige nutzt weiterhin die normale Detailzeilenhöhe; Überstand ist erlaubt, ohne App-Größe oder Seitenverhältnis beim Neustart zu verändern.
- Anzeige: Beim Neustart über Aus leiten Kirby-artige ASCII-Gesichter den ruhigen Aufbau von Emotronic von links nach rechts ein; der vollständige Name bleibt anschließend länger stehen.
- Link: Direkte Startmodi über `?mode=simon`, `?mode=on` und `?mode=off` ergänzt; ohne Parameter startet die App eingeschaltet.
- Simon: Die Schwierigkeitsauswahl erhält einen kurzen Startjingle und den kleinen animierten Aufbau von `SIMON FEELS`; Eingaben bleiben sofort möglich und brechen den Titelaufbau ab.
- Anzeige: `SIMON FEELS` verwendet dieselbe Schriftgröße wie die normale Introanzeige.
- Audio: Der Geschafft-Jingle beginnt rund 0,3 Sekunden nach dem letzten korrekten Tastendruck und kollidiert dadurch weniger mit dessen Ton.
- Link: `?mode=simon` wartet zunächst auf weißem Display mit kleinem Spielsymbol auf einen Tipp und startet erst danach Simon-Animation und -Ton.
- Bedienung: Ein einfacher Tipp auf Telefon oder Wifi zeigt drei Sekunden lang direkt unter der kleinen Emotionsanzeige den passenden Hinweis für Gefühl- beziehungsweise Replay-Teilen per Doppeltipp.
- Share: Eingehende Emotions-, Replay- und Score-Links warten ohne Zeitlimit mit ruhig weiterlaufendem Nachrichtensymbol im schlichten Hauptdisplay; Bildschirm oder Taste außer Aus startet die lautlose Wiedergabe.
- Score: Beim Simon-Game-Over wird ein Link mit Endstand, Modus und vollständiger Folge automatisch kopiert; Telefon kopiert ihn manuell erneut und `R` spielt die gesamte Folge noch einmal.
- Bedienung: Neutral bleibt am Game Over eingeblendet und startet direkt ein neues Spiel im zuletzt verwendeten Modus; die Hinweise lauten `Neutral: Neustart`, `R: Replay` und `⏻: Schluss`.
- Bedienung: Aus führt vom Game Over zunächst zur Simon-Titelauswahl zurück und schaltet die App von dort aus direkt aus.
- Anzeige: Die Score-Empfangsanimation zeigt zusätzlich einen kleinen Pokal und die Punktzahl in einer dezenten wartenden Bewegung.
- Audio: Den Empfangs-Jingle vollständig entfernt; der Starttipp beginnt Emotion oder Replay ohne zusätzlichen Empfangston.
- Bedienung: Aus bricht die laufende Empfangsphase oder Replay-Wiedergabe unmittelbar ab.
- Replay: Der Wechsel zu Bereit durch zweimaliges Drücken von Neutral leert den Replay-Verlauf vollständig.
- Datenschutz: Detaillierten lokalen Projektpfad aus dem Ruckpacken-Startskript entfernt und öffentliche Repository-/Share-Hinweise dokumentiert.
- Test: JavaScript-Syntax, Manifest, Icons, Service-Worker-Dateien, doppelte HTML-IDs, Versionsgleichlauf, mobile Breite und Browser-Smoke-Test geprüft.
- Doku: Übersicht, Anleitung, Design, Ideen, Plan, Installationshinweise und technische Übergabe ergänzt.
- Versionen: Emotronic v1.79.
