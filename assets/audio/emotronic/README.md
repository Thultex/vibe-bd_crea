# Emotronic Audio

Dieser Ordner enthält die beiden reproduzierbaren Soundsets der Emotronic-PWA:

- `8-bit/`: harte Retro-Fassung auf Grundlage der ursprünglichen Web-Audio-Tonfolgen.
- `8-bit_soft/`: gleiche Tonhöhen und Rhythmen mit weicheren Hüllkurven und kurzem, dezentem Nachhall. Dieses Set ist für eine spätere Aktivierung empfohlen.

Die Dateien werden mit `sp-emotronic/tools/emotronic-pwa/generate_audio_assets.py` erzeugt. Neue Sounds werden zuerst in dessen Datentabellen ergänzt und anschließend für beide Ordner neu generiert.

`manifest.json` dokumentiert alle Sound-IDs, Tonfolgen, Intensitäten und die empfohlene spätere Auswahl. Die PWA verwendet diese WAV-Dateien noch nicht; ihre bisherige Web-Audio-Ausgabe bleibt in der Live-Version unverändert.
