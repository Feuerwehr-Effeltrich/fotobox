# Fotobox



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
| `video_device` | Pfad zur Webcam/Capturecard, zB auch `dev/v4l/by-id/...` |
| `addr` | Bind-Adresse des Webservers |
| `port` | Port des Webservers |

## Bilder

![Livefeed](/images/livefeed.png)

![Countdown](/images/countdown.png)
