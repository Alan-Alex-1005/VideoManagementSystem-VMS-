import tkinter as tk
from tkinter import ttk

class DragDropCameraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Drag & Drop CCTV Assignment")

        self.cameras = {
            "Laptop Cam": "0",
            "Cam 1 (Dummy)": "1",
            "Cam 2 (Dummy)": "2",
            "Cam 3 (Dummy)": "3"
        }

        self.dragged_cam = None
        self.create_ui()

    def create_ui(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # TreeView on Left
        self.left_panel = tk.Frame(self.main_frame, width=200, bg="#f0f0f0")
        self.left_panel.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(self.left_panel, text="Available Cameras", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
        self.tree = ttk.Treeview(self.left_panel)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=5)

        for cam_name in self.cameras.keys():
            self.tree.insert('', tk.END, text=cam_name)

        self.tree.bind("<ButtonPress-1>", self.start_drag)

        # Grid on Right
        self.grid_panel = tk.Frame(self.main_frame, bg="white")
        self.grid_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.grid_slots = []
        for i in range(4):
            lbl = tk.Label(self.grid_panel, text=f"Feed {i+1}", bg="black", fg="white",
                           width=40, height=10, relief="raised", bd=2)
            lbl.grid(row=i//2, column=i%2, padx=5, pady=5)
            lbl.bind("<Enter>", self.drop_here)
            self.grid_slots.append(lbl)

    def start_drag(self, event):
        item_id = self.tree.identify_row(event.y)
        if item_id:
            self.dragged_cam = self.tree.item(item_id, 'text')
            print(f"Dragging: {self.dragged_cam}")

    def drop_here(self, event):
        if self.dragged_cam:
            lbl = event.widget
            lbl.config(text=f"{self.dragged_cam}", bg="#003300")
            print(f"Dropped {self.dragged_cam} into feed.")
            self.dragged_cam = None

# Run it
if __name__ == "__main__":
    root = tk.Tk()
    app = DragDropCameraApp(root)
    root.mainloop()
