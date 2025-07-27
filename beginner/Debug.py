import tkinter as tk
from tkinter import ttk
import cv2
import threading
import numpy as np
from PIL import Image, ImageTk

# Load Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

class SurveillanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI CCTV Surveillance Grid")

        self.cameras = {
            "Laptop Camera": 0,
            "Camera 1 (Dummy)": 0,
            "Camera 2 (Dummy)": 0,
            "Camera 3 (Dummy)": 0
        }

        self.feeds = [None] * 4
        self.capture_threads = [None] * 4
        self.face_detection_enabled = [tk.BooleanVar(value=True) for _ in range(4)]
        self.create_ui()

    def create_ui(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Left Panel – Tree View
        self.left_panel = tk.Frame(self.main_frame, width=200, bg="#f0f0f0")
        self.left_panel.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(self.left_panel, text="Available Cameras", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        self.tree = ttk.Treeview(self.left_panel)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        for cam in self.cameras.keys():
            self.tree.insert('', tk.END, cam, text=cam)

        self.tree.bind("<Double-1>", self.assign_to_grid)

        # Right Panel – Grid Layout
        self.right_panel = tk.Frame(self.main_frame)
        self.right_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.video_labels = []
        self.checkboxes = []

        for i in range(4):
            frame = tk.Frame(self.right_panel, padx=5, pady=5)
            frame.grid(row=i // 2, column=i % 2, sticky="nsew")

            lbl = tk.Label(frame, bg="black")
            lbl.pack(fill=tk.BOTH, expand=True)
            self.video_labels.append(lbl)

            cb = tk.Checkbutton(frame, text="Face Detection", variable=self.face_detection_enabled[i])
            cb.pack()
            self.checkboxes.append(cb)

    def assign_to_grid(self, event):
        selected_cam = self.tree.selection()
        if not selected_cam:
            print("⚠️ No camera selected")
            return

        cam_name = self.tree.item(selected_cam[0], "text")
        if cam_name not in self.cameras:
            print(f"❌ Invalid selection: '{cam_name}'")
            return

        cam_source = self.cameras[cam_name]

        for i in range(4):
            if self.feeds[i] is None:
                self.feeds[i] = cam_source
                self.capture_threads[i] = threading.Thread(
                    target=self.show_stream_with_faces, args=(cam_source, i)
                )
                self.capture_threads[i].daemon = True
                self.capture_threads[i].start()
                break

    def show_stream_with_faces(self, source, index):
        cap = cv2.VideoCapture(source, cv2.CAP_DSHOW)  # Use CAP_DSHOW for stability on Windows

        if not cap.isOpened():
            print(f"Camera {source} could not be opened.")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                print(f"[Feed {index + 1}] Failed to read frame.")
                break

            frame = cv2.resize(frame, (480, 360))

            if self.face_detection_enabled[index].get():
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = ImageTk.PhotoImage(Image.fromarray(frame_rgb))

            def update():
                self.video_labels[index].configure(image=img)
                self.video_labels[index].image = img

            self.video_labels[index].after(10, update)

        cap.release() 

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = SurveillanceApp(root)
    root.mainloop()
