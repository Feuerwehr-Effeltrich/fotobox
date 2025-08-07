# Fotobox

Eine einfach zu bedienende Selfie-Box-Software für Events, Partys oder Fotoprojekte, speziell für Raspberry Pi.
Sie zeigt einen Live-Video-Feed einer angeschlossenen Digitalkamera (per Capturecard) im Browser an und ermöglicht es, per Knopfdruck Fotos über einen GPIO-Relais-geschalteten Auslöser aufzunehmen.
Die Steuerung erfolgt bequem über eine Weboberfläche – ideal für Touchscreens oder Tablets.

## Erste Schritte

Um die Fotobox lokal auszuführen:

```sh
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
./serve.sh
```

## Deploy

Für einfaches Deployment auf einen frischen Raspberry Pi stellen wir ein Ansible-Playbook bereit.
Schritte:

1. Ansible auf eigenem PC/Laptop installieren
2. PiOS (Full) auf SD-Karte flashen (mit Nutzererstellung, SSH und ggf Wifi)
3. SSH-Verbindung mit Keys einrichten (ggf. `ssh-keygen`, `ssh-copy-id`, SSH-Config anpassen)
4. Falls Host in der SSH-Config nicht `fotobox` genannt wurde, `HOST` in [deploy.sh](/deploy.sh) anpassen (Syntax: `[user@](host|ip)`)
5. `./deploy.sh`

Nach Ändern der Konfiguration muss nur Schritt 5 ausgeführt werden, das Playbook aktualisiert die Fotobox dann entsprechend.

## Konfiguration

Editiere die [cfg.py](/src/cfg.py).

| Einstellung | Effekt |
|---|---|
| `static_image` | Zeige ein statisches Bild (ein "Cookie-Banner") statt Video-Feed |
| `video_device` | Pfad zur Webcam/Capturecard, zB `/dev/v4l/by-id/...` |
| `addr` | Bind-Adresse des Webservers |
| `port` | Port des Webservers |
| `gpio_pin` | GPIO Pin für den Auslöser |

## Bilder

![Livefeed](/images/livefeed.png)

![Countdown](/images/countdown.png)
