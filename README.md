# Fotobox

Eine einfach zu bedienende Selfie-Box-Software für Events, Partys oder Fotoprojekte.
Sie zeigt einen Live-Video-Feed einer angeschlossenen Digitalkamera (per Capturecard) im Browser an und ermöglicht es, per Knopfdruck Fotos über einen GPIO-Relais-geschalteten Auslöser aufzunehmen.
Die Steuerung erfolgt bequem über eine Weboberfläche – ideal für Touchscreens oder Tablets.

## Erste Schritte

```sh
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
./serve.sh
```

## Konfiguration

Editiere die [cfg.py](/src/cfg.py).

| Einstellung | Effekt |
|---|---|
| `static_image` | Zeige ein statisches Bild (ein "Cookie-Banner") statt Video-Feed |
| `video_device` | Pfad zur Webcam/Capturecard, zB `/dev/v4l/by-id/...` |
| `addr` | Bind-Adresse des Webservers |
| `port` | Port des Webservers |

## Bilder

![Livefeed](/images/livefeed.png)

![Countdown](/images/countdown.png)
