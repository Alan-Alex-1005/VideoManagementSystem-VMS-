import cv2
import numpy as np

# List your camera sources here:
# You can use '0', '1', etc. for local webcams
# Or use RTSP URLs like "rtsp://user:pass@ip:port/path"

cam_sources = [
    0,  # Default webcam
    1,  # Second webcam if available, else change to a stream
    "rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov",  # Public RTSP
    "rtsp://184.72.239.149/vod/mp4:BigBuckBunny_115k.mov"  # Another public RTSP
]

# Initialize video capture objects
cams = [cv2.VideoCapture(src) for src in cam_sources]

# Resize dimensions for each camera feed
width, height = 320, 240

while True:
    frames = []
    for cam in cams:
        ret, frame = cam.read()
        if ret:
            frame = cv2.resize(frame, (width, height))
        else:
            frame = np.zeros((height, width, 3), dtype=np.uint8)  # Black frame for unavailable feed
        frames.append(frame)

    # Build 2x2 grid
    top_row = np.hstack((frames[0], frames[1]))
    bottom_row = np.hstack((frames[2], frames[3]))
    grid = np.vstack((top_row, bottom_row))

    # Show the grid
    cv2.imshow("2x2 CCTV View (RTSP/Webcams)", grid)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release all cameras
for cam in cams:
    cam.release()

cv2.destroyAllWindows()
