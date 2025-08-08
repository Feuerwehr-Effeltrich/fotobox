import cv2
import cfg
import subprocess

subprocess.run([
    "v4l2-ctl",
    "-d", cfg.video_device,
    "--set-fmt-video=width=1280,height=720,pixelformat=MJPG",
    "--set-parm=30"
], check=True)


# camera = cv2.VideoCapture(cfg.video_device)
# camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Open device with MJPEG fourcc
camera = cv2.VideoCapture(cfg.video_device)
camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
camera.set(cv2.CAP_PROP_FPS, 30)

def frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        # Still comes in decoded as NumPy array, so we just encode once (fast since it's already JPEG internally)
        _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 70])
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' +
               buffer.tobytes() + b'\r\n')
