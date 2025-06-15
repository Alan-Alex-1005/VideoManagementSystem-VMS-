import cv2
import numpy as np

# Open default webcam (index 0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Cannot access the webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame.")
        break

    # Resize frame for grid layout (e.g., 320x240)
    small_frame = cv2.resize(frame, (320, 240))

    # Create a 2x2 grid by stacking the same frame
    top_row = np.hstack((small_frame, small_frame))
    bottom_row = np.hstack((small_frame, small_frame))
    grid_frame = np.vstack((top_row, bottom_row))

    # Display the simulated CCTV grid
    cv2.imshow('Simulated CCTV Grid (2x2)', grid_frame)

    # Press ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
 