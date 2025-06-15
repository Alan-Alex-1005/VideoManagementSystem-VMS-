import cv2
import tkinter as tk
from PIL import Image, ImageTk
import threading

class MultiCamApp:
    def __init__(self, root, sources):
        self.root = root
        self.sources = sources
        self.captures = [cv2.VideoCapture(src) for src in sources]
        self.frames = [None] * len(sources)
        self.labels = []
        self.running = False

        self.setup_ui()

    def setup_ui(self):
        self.root.title("Multi-Camera Surveillance")
        self.root.configure(bg='black')

        # Grid of video labels
        rows = cols = int(len(self.sources) ** 0.5)
        for i in range(len(self.sources)):
            label = tk.Label(self.root)
            label.grid(row=i // cols, column=i % cols, padx=5, pady=5)
            self.labels.append(label)

        # Control buttons
        control_frame = tk.Frame(self.root, bg='black')
        control_frame.grid(row=rows + 1, column=0, columnspan=cols)

        tk.Button(control_frame, text="Start", command=self.start).pack(side=tk.LEFT, padx=10)
        tk.Button(control_frame, text="Stop", command=self.stop).pack(side=tk.LEFT, padx=10)
        tk.Button(control_frame, text="Exit", command=self.exit_app).pack(side=tk.LEFT, padx=10)

    def start(self):
        self.running = True
        self.update_frames()

    def stop(self):
        self.running = False

    def update_frames(self):
        if not self.running:
            return

        for i, cap in enumerate(self.captures):
            ret, frame = cap.read()
            if not ret:
                frame = cv2.cvtColor(cv2.imread(""), cv2.COLOR_BGR2RGB)
            else:
                frame = cv2.resize(frame, (320, 240))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.labels[i].imgtk = imgtk
            self.labels[i].configure(image=imgtk)

        self.root.after(10, self.update_frames)

    def exit_app(self):
        self.running = False
        for cap in self.captures:
            cap.release()
        self.root.destroy()

# Simulate 4 cameras with laptop cam (replace 0 with IP/RTSP for real)
camera_sources = [0, 0, 0, 0]

root = tk.Tk()
app = MultiCamApp(root, camera_sources)
root.mainloop()
