#! /usr/bin/env bash

zenity --timeout=5 --info --text="Fotobox startet..." &

cd $(dirname $0)
cd ..

# ./serve.sh >> fotobox.log 2>&1 &
./serve.sh >> fotobox.log 2>&1

# sleep 3

# unclutter &

# xscreensaver -no-splash
# xset s off
# xset -dpms
# xset s noblank

# video decoding seems very slow, use our laptop for now
# chromium "http://localhost:5000" --start-fullscreen --kiosk --incognito --noerrdialogs --no-first-run --disk-cache-dir=/dev/null --ignore-gpu-blocklist --enable-features=UseOzonePlatform,WaylandWindowDecorations
