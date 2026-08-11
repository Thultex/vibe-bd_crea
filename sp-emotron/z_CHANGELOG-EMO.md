# Changelog Emotronic

## Stats

Ausgangsdatum: 2026-07-26

*Diese Woche (ca. 2,0h, 1 Tag, Inhalte):*
Emotronic auf das neue funktionale 8+1-Rad umgebaut, Benennungen, Emojis, Kombinationen, Pastellfarben, Animationen und Soundsets erneuert sowie das vollständige Rad an der Y-Achse gespiegelt.

*Letzte Woche (ca. 3,0h, 2 Tage, Inhalte):*
Emotronic-PWA übernommen, strukturiert, dokumentiert, Replay-Verlauf sowie Intensitätszeiger korrigiert, Emoji-Intensitätsvorschau ergänzt und ausgeschaltete Bedientasten verfeinert.

*Dieser Monat (ca. 2,0h, 1 Tag, Inhalte):*
Vollständiger Neuaufbau des Emotionsmodells samt gespiegeltem Rad, eindeutigen Emojis, neuen Kombinationen, angepassten Bewegungen und reproduzierbaren Klangsets.

*Letzter Monat (0h, 0 Tage, Inhalte):*
Keine Einträge.

*Jahr (ca. 5,0h, 3 Tage, Inhalte):*
Erstübernahme und anschließender vollständiger Neuaufbau von Emotronic mit funktionalem 8+1-Rad.

*Insgesamt (ca. 5,0h, 3 Tage, Inhalte):*
Erstübernahme und anschließender vollständiger Neuaufbau von Emotronic mit funktionalem 8+1-Rad.

## Log

### 2026-08-11 - audio

- Audio: Gemäß Issue #11 wieder das ursprüngliche `8-bit`-Soundset als Standard eingebunden; `8-bit_soft` bleibt vollständig als auswählbare Alternative erhalten.
- Version: Emotronic v2.32 mit Cache-Revision 132.

### 2026-08-09 - simon, schwierigkeit

- Schwierigkeit: Profi startet bei 0 statt 5 Punkten; Leicht startet mit 1 Leben bei unverändert langsamerem Spieltempo.
- Zwischenanimation: Bonusmotive deutlich vergrößert und pro Frame dynamisch bewegt; ausschließlich ihre Standzeit ist in Leicht und Normal länger, Zehnerschritte erhalten eine zusätzliche Hervorhebung.
- Audio: Beide reproduzierbaren 40er-Soundsets geprüft und `8-bit_soft` als WAV-Standard eingebunden; ein einzelner Konfigurationswert wechselt vollständig auf `8-bit`, die bisherige Synthese bleibt als automatischer Fehler-Fallback erhalten.
- Version: Emotronic v2.31 mit Cache-Revision 131.

### 2026-08-02 - emo, modell, emojis, farben, animation, audio, pwa, doku (ca. 2,0h)

- Modell: Grundzweige auf Neugier, Zuneigung, Freude, Wut, Ekel, Scham, Trauer und Angst mit Neutral im Zentrum umgestellt.
- Spiegelung: Komplettes 3×3-Rad einschließlich Emojis, Beschriftungen, Pastellfarben und Ziffernsteuerung an der Y-Achse gespiegelt; sichtbare Reihenfolge ist Freude/Zuneigung/Neugier, Wut/Neutral/Angst, Ekel/Scham/Trauer.
- Begriffe: Kurze Adjektivreihen `interessiert/neugierig/fasziniert`, `freundlich/zugewandt/verbunden`, `zufrieden/fröhlich/begeistert`, `gereizt/verärgert/wütend`, `abgeneigt/angeekelt/übel`, `verlegen/befangen/beschämt`, `bedrückt/traurig/trauernd` und `besorgt/ängstlich/panisch` eingeführt.
- Kombinationen: Bewunderung, Dankbarkeit, Streitlust, Abwertung, Unbehagen, Reue, Aufgeben und Überraschung als einwortige Nomen mit eindeutigen Gesichts-Emojis und festen emotionsbezogenen Übersichtsankern umgesetzt; Streitlust verwendet wieder das alte Teufelsemoji, Unbehagen 😣 und Aufgeben das erschöpfte Gesicht 😩. Ekel verwendet 😬 in Intensität 1 und wie zuvor 😖 in Intensität 2.
- Emojis: Doppelte Motive entfernt; die klassischen Neugier- und Freude-Reihen wiederhergestellt und Bewunderung auf ein eigenes Herzaugen-Motiv umgestellt.
- Farben: Alte Pastellpalette und bestehende Intensitätsberechnung beibehalten, semantisch mit roter Wut, gelber Freude, grüner Scham, blauer Trauer, lavendelfarbener Angst, dunkelgrünem Ekel, orangener Zuneigung und türkiser Neugier neu zugeordnet.
- Animation: Eigene zurückhaltende Scham-Bewegung ergänzt; Sekundäremotionen übernehmen passende Bewegungscharakteristiken ihrer Grundzweige.
- Audio: Live-Synthese, Generator, Manifest und beide 40-teiligen WAV-Sets auf Scham und die acht neuen Kombinationen umgestellt; Wut mit 2/3/4 Tönen innerhalb der gemeinsamen Obergrenzen gehalten, die mittlere Wut-Stufe durch größere Sprünge dynamischer und Trauer harmonisch dunkler gestaltet.
- Bedienung: Neutral bleibt beliebig oft wählbar. Der erste Ausschalter-Klick leert den Replay-Verlauf und wechselt zu Bereit; erst der zweite Klick schaltet aus.
- Simon: Die diagonale Auswahl verwendet Freude für Leicht, Neutral für Normal und Trauer für Profi.
- PWA: Anwendung auf Emotronic v2.25, Revision 125 und Cache `emotronic-v125` angehoben; Snapshot und öffentlicher Laufzeitspiegel bytegleich synchronisiert.
- Grafik: `emotron.svg` als Illustrator-unabhängige Hauptquelle vollständig mit gespiegelten Farbflächen, 33 eingebetteten OpenMoji je Farb-, Schwarzweiß- und Faded-Gruppe sowie eindeutigen Beschriftungsgruppen neu aufgebaut; externe Bildverknüpfungen entfallen.
- Anzeige/Animation: Alle Grund-, Intensitäts- und Zwischenemotionen verwenden im Emotronic-Display kurze, eindeutige ASCII-Endmotive mit drei Frames und eigener Bewegungscharakteristik; Schriftgröße und zentrierte Position bleiben im bisherigen Displayraster.
- Sharing: Die ausgeschriebenen Fragmente `#share`, `#replay`, `#slow` und `#score` bleiben erhalten. Alle 33 Zustände werden im Datenteil mit je einem Base36-Zeichen codiert; Intensität und Kombination sind implizit, der Normalmodus im Score wird weggelassen und alte lange Links bleiben lesbar.
- Replay: Der normale Verlauf ist auf 24 Schritte begrenzt und entfernt bei jeder weiteren Eingabe den ältesten Eintrag; Simons eigene Spielfolge bleibt unverändert.
- Test: JavaScript-/Python-Syntax, eindeutige Emojis und Begriffe, Rad-/Tastaturspiegelung, Kombi-Anker, WAV-Struktur, Manifestgleichlauf, Versionsstand und bytegleiche Laufzeitspiegel geprüft.
- Versionen: Emotronic v2.30.

### 2026-07-26 - emo, struktur, tools, pwa, replay, share, anzeige, audio, doku (ca. 1,6h)

- Summary: Vollständige Emotronic-PWA in die Repository-Struktur übernommen und einen getrennten öffentlichen App-Spiegel vorbereitet.
- Struktur: Projekt unter `sp-emotron/` mit dem Kürzel `emo` und den vorgesehenen Dokumentations-, Asset-, Datei- und Toolbereichen angelegt.
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
- Anzeige: `R` und das normale Power-Zeichen bleiben nun auch ausgeschaltet erhalten; Videokassette und Lupe erscheinen stattdessen als kleine graue Hinweise rechts daneben.
- Fix: Beim Ausschalten wird neben dem internen Intensitätswert auch die sichtbare Zeigerposition unmittelbar auf `0` gesetzt.
- Fix: Der leere Bereit-Zustand wird nicht mehr irrtümlich als Kombinationsobjekt erkannt und bleibt nach Start, Neustart oder Ausschalten auf Intensität `0`; die erste Gefühlsauswahl beginnt wieder auf Stufe `1`.
- Anzeige: Die grauen Zusatzsymbole rechts neben `R` und Power wurden von 18 auf 21 Pixel vergrößert, ohne die feste Tastenhöhe zu verändern.
- Anzeige: Die Score-Empfangsvorschau verwendet den tatsächlich verlinkten OpenMoji-Pokal `1F3C6` statt eines plattformabhängigen Emoji-Zeichens.
- Design: OpenMoji ist künftig in Emotronic zu bevorzugen, wo Motiv und Darstellung sinnvoll passen; Text- und ASCII-Fallbacks bleiben erhalten.
- Versionen: Emotronic v2.01.

### 2026-07-27 - emo, tools, pwa, anzeige, animation, replay, simon, sharing, audio, doku, test (ca. 1,4h)

- Summary: Intensitätsvorschau und Beschriftungen verfeinert sowie leere Anzeigezustände und die ausgeschalteten Funktionstasten bereinigt.
- Fix: Die Zeigerposition wird als animierbare CSS-Zahl interpoliert, sodass die Nadel zwischen den Intensitäten wieder sichtbar gleitet und nachschwingt. Das gilt auch beim Wechsel zu Neutral und von Neutral zu einem Gefühl; die unabhängige `null`-Absicherung bleibt erhalten.
- Fix: Bereit setzt die Intensität sofort auf `0`, aktiviert die Transition danach aber wieder, damit die erste Auswahl nach Aus- und Einschalten nicht springt.
- Fix: Am linken Anschlag wird die sichtbare Position begrenzt und das zusätzliche Nachschwingen unterdrückt, damit die Nadel bei Neutral nicht über den Rand läuft.
- Fix: Das Nachschwingen startet nur noch bei einer tatsächlichen Positionsänderung und beginnt in der jeweiligen Bewegungsrichtung.
- Anzeige: Beim Verstellen im Telefon-/Empfängermodus zeigen nun alle nicht-neutralen Gefühlstasten ihre OpenMoji-Variante der aktuellen Intensität. Der Display-Hintergrund bleibt an das angeklickte Gefühl gebunden; Wifi/Sender und die erst beim Druck ausgelöste Simon-Dramaturgie bleiben unverändert.
- Anzeige: Die Beschriftungen der neun Gefühlstasten um zwei Pixel angehoben und ihre Zeilenhöhe leicht vergrößert, damit Unterlängen wie beim „g“ nicht mehr abgeschnitten erscheinen.
- Anzeige: Die Beschriftungen anschließend insgesamt vier Pixel tiefer gesetzt und ihre Zeilenbox nochmals leicht vergrößert; die Tastengröße bleibt unverändert und Unterlängen werden nicht abgeschnitten.
- Anzeige: Alle alleinstehenden `...`-Platzhalter aus den sichtbaren Initial- und Game-over-Anzeigen entfernt.
- Anzeige: Im ausgeschalteten Zustand stehen fünf Pixel näher neben `R` und Power nun die schwarzen Silhouetten des OpenMoji-Joysticks `1F579` und wieder der OpenMoji-Lupe `1F50D`.
- Anzeige/Bedienung: Im ausgeschalteten Zustand auch die mittlere Kombi-Taste deaktiviert und ihr Symbol vollständig ausgeblendet; nach der Einschaltsequenz wird sie weich wieder eingeblendet und freigegeben.
- Animation: Joystick und Lupe blenden beim Ausschalten weich ein und beim Einschalten wieder aus, während `R` und Power sichtbar bleiben.
- Fix/Animation: Die zuvor mögliche Resttransparenz, der Transparenzabfall in der Wechselmitte und ein harter Abschlusssprung beseitigt. Die über `APP_CONFIG.normalMode.keypadCrossfadeMs` definierbare Überblendung dauert standardmäßig 0,15 Sekunden: Das neue Motiv erreicht nach rund 0,12 Sekunden volle Deckkraft; das alte fadet ab etwa 0,08 Sekunden bis zum Ende weich aus.
- Fix: Kurz aufblitzende Textplatzhalter – besonders auf dem aktiven Emoji – verhindert. Das alte Motiv bleibt bis zum erfolgreichen Laden des neuen SVGs sichtbar; Alternativtext und großer grafischer Text-Ersatz entfallen, während die kleine Tastenbeschriftung erhalten bleibt.
- Anzeige/Bedienung: Bei aktiver Kombi-Taste zeigen gültige gestrichelt markierte Partner-/Nachbartasten das resultierende Kombi-Emoji. Beim Abbruch kehren alle Vorschauen zu den Grund-Emojis zurück; nach einer Wahl behält nur die gewählte Taste das echte Kombi-Emoji.
- Anzeige/Bedienung: Die Kombi-Vorschau ersetzt auf den gültigen Nachbartasten nun zusätzlich den übergeordneten Emotionsnamen durch den Namen der entstehenden Kombination. Beim Abbruch werden beide Vorschauanteile zurückgesetzt; normale Intensitätsvarianten behalten ihre übergeordneten Emotionsnamen.
- Anzeige/Bedienung: Bereit oder Neutral plus Kombi öffnet eine vollständige Übersicht aller acht Kombinationen auf dem äußeren Tastenring. Freude zeigt zuerst „lustig“, die übrigen Kombinationen folgen im Uhrzeigersinn und lassen sich direkt auswählen.
- Replay: Beim Öffnen der Kombiübersicht aus Neutral wird nur der aktuelle Neutral-Schritt aus dem Replay entfernt und der Zustand intern zu Bereit; frühere Schritte bleiben erhalten.
- Simon: Die Kombi-Taste ist deutlich abgedunkelt und nicht bedienbar. Bei Simons Vorführung leuchtet sie nach dem ersten Kombi-Symbol kurz auf; beim eigenen Nachtippen geschieht das für 0,15 Sekunden nur nach dem ersten richtigen Symbol.
- Sharing: Die Doppeltipp-Zuordnung getauscht und vor den zustandsabhängigen Direktlink-Aktionen ausgewertet: Telefon teilt konsistent den Replay-Verlauf, Wifi/Sender das aktuelle Gefühl. Die Einzeltipp-Hinweise wurden entsprechend angepasst.
- Sharing: Neue Replay-Links verwenden zur eindeutigen Erkennbarkeit `#replay=…`; Gefühle bleiben bei `#share=…`, Scores bei `#score=…`. Ältere Replay-Links unter `#share=…` werden weiterhin angenommen.
- Replay/Anzeige: Nach vollständiger lokaler oder empfangener Wiedergabe bleibt die Gesamtzahl der Schritte als erneuter Abspielhinweis neben `R` stehen. Sie wurde auf 13 Pixel vergrößert, näher an `R` gerückt und blendet beim nächsten Gefühlstastendruck wie die Ausschalthinweise weich aus.
- Replay/Anzeige: Wird `R` während einer erneuten Wiedergabe noch einmal gedrückt, bleibt die Gesamtzahl als Replay-Hinweis neben `R` erhalten.
- Replay/Timing: Slow als eigenen Fragment-Tag `#slow=…` eines vollständigen unveränderten Replay-Datensatzes umgesetzt. Der codierte Datenteil ist identisch zu `#replay=…`, sodass sich das Tempo durch direktes Ersetzen des Tag-Namens umschalten lässt.
- Replay/Timing: Schrittintervalle, Displayübergang und Abschlusszeit laufen unter `#slow=…` mit Faktor `2`, die Emoji-Bewegung getrennt davon nur minimal mit Faktor `1.15`.
- Replay/Timing: Die Slow-Markierung bleibt für erneutes Abspielen desselben empfangenen Verlaufs erhalten und wird bei der nächsten Gefühl-, Intensitäts- oder Kombi-Eingabe entfernt.
- Sharing: Der Wifi-/Sender-Doppeltipp teilt nun den vollständigen aktuellen Replay-Verlauf unter `#slow=…`; Telefon teilt exakt denselben Datensatz unter `#replay=…`.
- Simon/Anzeige: Am Game Over erscheint dieselbe Zahl sofort als Anzahl der gespeicherten Runden, obwohl das Score-Replay erst durch `R` gestartet wird. Empfangene Scores und die Rückkehr aus ihrem Replay verwenden denselben Hinweis.
- Sender/Animation: `>>>` startet nun bei jeder Gefühlsbetätigung einschließlich erneutem Klick auf dasselbe Gefühl, bei tatsächlicher Intensitätsänderung und beim Aktivieren der Wifi-/Sendertaste.
- Audio: Die bisher synthetisierten Tonfolgen als 40 reproduzierbare WAV-Sounds in `/assets/audio/emotronic/8-bit/` abgelegt und ein gleich aufgebautes Set `8-bit_soft/` mit weicheren Hüllkurven sowie kurzem dezentem Nachhall erzeugt.
- Audio: Beide Sets nur für den späteren Sound-Umbau vorbereitet. Die Live-PWA lädt sie noch nicht und verwendet unverändert ihre bestehende Web-Audio-Synthese; bei einer späteren Aktivierung ist `8-bit_soft` als Standard vorgesehen.
- Tool: `generate_audio_assets.py` und `manifest.json` als gemeinsame Pflege- und Generationsgrundlage für beide Soundordner ergänzt.
- Test: Den veröffentlichten Spiegel lokal im Browser mit Aus-/Einschaltzyklus sowie den Übergängen 0→1, 1→3, 3→Neutral und Neutral→1 geprüft.
- Test: JavaScript-/Python-Syntax, WAV-Struktur, Soundset-Gleichlauf, identische Replay-/Slow-Datenteile, getrennte Replay-/Emoji-Zeitfaktoren, Aus-/Ein-Zustand der Kombi-Taste, Versionsgleichlauf und bytegleichen Laufzeitspiegel für Emotronic v2.14 geprüft.
- Ausschalten/Anzeige: Die kleinen Joystick- und Lupenhinweise neben `R` und der Aus-Taste blenden erst nach dem vollständig abgeschlossenen Ausschaltprozess ein.
- Versionen: Emotronic v2.15.
