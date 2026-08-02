# Emotron – verbindliche Illustrator-Referenz

Diese Datei ist die mitzuführende Referenz für `Emotron.ai` und die Emotronic-PWA. Änderungen an Namen, OpenMoji-Codes oder Farben werden immer gleichzeitig hier, in der Illustrator-Datei und in `../tools/emotronic-pwa/index.html` eingetragen.

## Illustrator-Ebenen

| Ebene | Verbindlicher Inhalt |
|---|---|
| `emoji_svg color` | Farbige OpenMoji-Vektoren der unten aufgeführten Codes |
| `emoji_svg sw` | Schwarzweiße OpenMoji-Vektoren derselben Codes und Positionen |
| `emoji_svg color faded` | Kopie der farbigen OpenMoji-Vektoren mit der vorhandenen Faded-Darstellung |
| `names` | Namen der acht Grundemotionen und `Neutral` in sichtbarer Radreihenfolge |
| `names for emoji` | Kurze Adjektive der Intensitätsstufen und einwortige Namen der Zwischenemotionen |
| `names for emoji - front` | Deckungsgleiche vordere Kopie von `names for emoji` |
| `Color` | Basisfarben des Rads |
| `Color faded` | Deckungsgleiche Kopie von `Color` mit den unten berechneten Faded-Farben |

Alle Emoji-Ebenen verwenden echte OpenMoji-SVG-Vektoren wie im Original, keine Text-Emoji. Jeder OpenMoji-Code kommt genau einmal vor; alle Motive zeigen Gesichter. Für Farbe gilt `https://openmoji.org/data/color/svg/<CODE>.svg`, für Schwarzweiß `https://openmoji.org/data/black/svg/<CODE>.svg`.

Die vorbereiteten Vektoren liegen parallel unter `openmoji/color/` und `openmoji/sw/`. Die Ringnummerierung lautet `1` Neugier, `2` Zuneigung, `3` Freude, `4` Wut, `5` Ekel, `6` Scham, `7` Trauer und `8` Angst. Zwischenemotionen verwenden beide Nachbarn, zum Beispiel `1-2_bewunderung.svg`; Grundstufen verwenden zusätzlich Stufe und Adjektiv, zum Beispiel `1_neugier_2_neugierig.svg`. Neutral heißt `0_neutral.svg`. `openmoji/manifest.json` hält dieselbe Reihenfolge maschinenlesbar fest.

Der vorbereitete Bestand wird ohne erneuten Download vom Repository-Stamm aus geprüft:

```powershell
python sp-emotron\tools\illustrator\download_openmoji_assets.py --check
```

`../tools/illustrator/inspect_emotron.jsx` kann später über Illustrators Befehl **Datei → Skripten → Anderes Skript** einen Ebenenbericht `Emotron.layers.txt` erzeugen, bevor die Vektoren und Farben eingesetzt werden.

## Grundemotionen, Namen, Emojis und Farben

`Color faded` wird wie in der PWA aus `30 % Basisfarbe + 70 % Weiß` berechnet. Das Rad und sämtliche zugehörigen Inhalte sind an der Y-Achse gespiegelt.

| Position | Grundemotion | schwach | Emoji | mittel | Emoji | stark | Emoji | Basisfarbe | Faded |
|---|---|---|---|---|---|---|---|---|---|
| oben links | Freude | zufrieden | `1F60C` 😌 | fröhlich | `1F60A` 😊 | begeistert | `1F602` 😂 | `#f5df6f` | `#fcf5d4` |
| oben Mitte | Zuneigung | freundlich | `1F609` 😉 | zugewandt | `1F917` 🤗 | verbunden | `1F970` 🥰 | `#f4b56d` | `#fce9d3` |
| oben rechts | Neugier | interessiert | `1F60F` 😏 | neugierig | `1FAE2` 🫢 | fasziniert | `1F929` 🤩 | `#83d4cf` | `#daf2f1` |
| Mitte links | Wut | gereizt | `1F612` 😒 | verärgert | `1F620` 😠 | wütend | `1F92C` 🤬 | `#ef938b` | `#fadfdc` |
| Mitte | Neutral | ausgeglichen | `1F610` 😐 | – | – | – | – | `#ddd9d0` | `#f5f4f1` |
| Mitte rechts | Angst | besorgt | `1F61F` 😟 | ängstlich | `1F628` 😨 | panisch | `1F631` 😱 | `#c2a8dc` | `#ede5f5` |
| unten links | Ekel | abgeneigt | `1F615` 😕 | angeekelt | `1F616` 😖 | übel | `1F922` 🤢 | `#6f9f68` | `#d4e2d2` |
| unten Mitte | Scham | verlegen | `1F605` 😅 | befangen | `1F633` 😳 | beschämt | `1FAE3` 🫣 | `#bfe36f` | `#ecf7d4` |
| unten rechts | Trauer | bedrückt | `1F641` 🙁 | traurig | `1F622` 😢 | trauernd | `1F62D` 😭 | `#6381d7` | `#d0d9f3` |

## Zwischenemotionen

Die Namen sind kurze, eindeutige Einwort-Nomen. Auch hier werden in `emoji_svg color` und `emoji_svg sw` dieselben OpenMoji-Codes verwendet.

| Nachbarpaar | Name | OpenMoji | Übersichtsposition |
|---|---|---|---|
| Neugier + Zuneigung | Bewunderung | `1F60D` 😍 | Zuneigung |
| Zuneigung + Freude | Dankbarkeit | `1F979` 🥹 | Freude |
| Freude + Wut | Streitlust | `1F608` 😈 | Wut |
| Wut + Ekel | Abwertung | `1F644` 🙄 | Ekel |
| Ekel + Scham | Unbehagen | `1F62C` 😬 | Scham |
| Scham + Trauer | Reue | `1F61E` 😞 | Trauer |
| Trauer + Angst | Aufgeben | `1F629` 😩 | Angst |
| Angst + Neugier | Überraschung | `1F632` 😲 | Neugier |

## Pflegecheck

- Keine doppelten Namen oder OpenMoji-Codes.
- Grundemotionen verwenden kurze Adjektive; Zwischenemotionen verwenden ein Wort.
- Farbiges und schwarzweißes OpenMoji behalten identische Geometrie, Code-Reihenfolge und Position.
- `Color faded` und `emoji_svg color faded` bleiben deckungsgleiche Kopien ihrer Ausgangsebenen.
- Bei jeder Änderung PWA, Illustrator-Datei, diese Referenz und den Validator gemeinsam aktualisieren.
