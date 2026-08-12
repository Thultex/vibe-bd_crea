# Emotronic Audio

Dieser Ordner enthält die optionale reproduzierbare Soft-Soundvariante der Emotronic-PWA:

- `8-bit_soft/`: gleiche Tonhöhen und Rhythmen mit weicheren Hüllkurven und kurzem, dezentem Nachhall. Dieses Set bleibt als Alternative verfügbar.

Die Dateien werden mit `sp-emotron/tools/emotronic-pwa/generate_audio_assets.py` erzeugt. Neue Sounds werden zuerst in dessen Datentabellen ergänzt und anschließend für den Soft-Ordner neu generiert. Der Generator entfernt dabei ausschließlich nicht mehr im Manifest enthaltene WAV-Dateien aus dem von ihm verwalteten Set.

`manifest.json` dokumentiert alle Sound-IDs, Tonfolgen, Intensitäten, den klassischen Wiedergabestandard und die optionale Soft-Auswahl. `APP_CONFIG.audio.soundSet` steht standardmäßig auf `classic` und kann nur für die weichere Variante auf `8-bit_soft` umgestellt werden; die klassische Web-Audio-Synthese bleibt dann auch Fehler-Fallback.

Das aktuelle Modell enthält die acht Grundzweige Neugier, Zuneigung, Freude, Wut, Ekel, Scham, Trauer und Angst sowie die Kombinationen Bewunderung, Dankbarkeit, Streitlust, Abwertung, Unbehagen, Reue, Aufgeben und Überraschung. Wut bleibt mit 2/3/4 Tönen innerhalb der gemeinsamen Obergrenzen; größere Intervalle geben insbesondere der mittleren Stufe mehr Dynamik. Trauer bleibt harmonisch dunkler.
