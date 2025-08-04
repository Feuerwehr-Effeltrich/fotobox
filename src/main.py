#! /usr/bin/env python3

from flask import Flask, Response
from videofeed import frames
from gpio import gpio_capture

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/video_feed')
def video_feed():
    # image for testing
    return Response(open('static/cookie.webp', 'rb').read(), mimetype='image/webp')
    # return Response(frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.post('/capture')
def capture():
    try:
        gpio_capture()
    except Exception as e:
        print(f"Error during capture: {e}")
        return Response(status=500)
    return Response(status=204)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def catch_all(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
