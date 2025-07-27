import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

# Dummy credentials
USERNAME = "admin"
PASSWORD = "cctv123"

# Path to Donut.py
DONUT_PATH = os.path.join(os.path.dirname(__file__), "Donut.py")

# Function to launch main app
def launch_main_app():
    try:
        subprocess.Popen([sys.executable, DONUT_PATH])
        root.destroy()  # Close login window
    except Exception as e:
        messagebox.showerror("Error", f"Failed to launch Donut.py:\n{e}")

# Validate login
def validate_login():
    user = username_entry.get()
    pwd = password_entry.get()

    if user == USERNAME and pwd == PASSWORD:
        messagebox.showinfo("Login Success", "Welcome to AI CCTV Surveillance!")
        launch_main_app()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password!")

# Login GUI
root = tk.Tk()
root.title("Login - AI CCTV Surveillance")
root.geometry("350x200")
root.resizable(False, False)

tk.Label(root, text="Login", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text="Login", command=validate_login, bg="green", fg="white").pack(pady=10)

root.mainloop()
