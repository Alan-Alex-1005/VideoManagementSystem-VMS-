import cv2

camera_urls = [
    "http://91.191.213.114:8080/mjpg/video.mjpg",  # example placeholder
    "http://87.98.219.198:8080/mjpg/video.mjpg",
    "http://213.109.145.167:8080/mjpg/video.mjpg",
    "http://213.226.254.135:8080/mjpg/video.mjpg"
]
caps = [cv2.VideoCapture(url) for url in camera_urls]

if caps.isOpened():
    print("✅ Stream is valid and supported")
else:
    print("❌ Could not open stream")

caps.release()
