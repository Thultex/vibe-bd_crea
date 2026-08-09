# Emotronic Audio

Dieser Ordner enthält die beiden reproduzierbaren Soundsets der Emotronic-PWA:

- `8-bit/`: harte Retro-Fassung auf Grundlage der ursprünglichen Web-Audio-Tonfolgen.
- `8-bit_soft/`: gleiche Tonhöhen und Rhythmen mit weicheren Hüllkurven und kurzem, dezentem Nachhall. Dieses Set ist in der PWA Standard.

Die Dateien werden mit `sp-emotron/tools/emotronic-pwa/generate_audio_assets.py` erzeugt. Neue Sounds werden zuerst in dessen Datentabellen ergänzt und anschließend für beide Ordner neu generiert. Der Generator entfernt dabei ausschließlich nicht mehr im Manifest enthaltene WAV-Dateien aus den beiden von ihm verwalteten Sets.

`manifest.json` dokumentiert alle Sound-IDs, Tonfolgen, Intensitäten und die empfohlene Auswahl. `APP_CONFIG.audio.soundSet` schaltet die PWA mit einem Wert zwischen `8-bit_soft` und `8-bit` um; die bisherige Web-Audio-Synthese bleibt als Fehler-Fallback erhalten.

Das aktuelle Modell enthält die acht Grundzweige Neugier, Zuneigung, Freude, Wut, Ekel, Scham, Trauer und Angst sowie die Kombinationen Bewunderung, Dankbarkeit, Streitlust, Abwertung, Unbehagen, Reue, Aufgeben und Überraschung. Wut bleibt mit 2/3/4 Tönen innerhalb der gemeinsamen Obergrenzen; größere Intervalle geben insbesondere der mittleren Stufe mehr Dynamik. Trauer bleibt harmonisch dunkler.
