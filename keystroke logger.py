"""
GUI-Based Keystroke Logging Demonstration
Educational & Consent-Based Project
"""

import tkinter as tk
from pynput import keyboard
from datetime import datetime
import os

# GET PROJECT FOLDER (where this .py file exists)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "keystrokes.txt")

listener = None
logging_active = False


def write_to_file(text):
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(text)


def on_press(key):
    if not logging_active:
        return

    try:
        write_to_file(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            write_to_file(" ")
        elif key == keyboard.Key.enter:
            write_to_file("\n")
        else:
            write_to_file(f"[{key.name}]")


def start_logging():
    global listener, logging_active
    if logging_active:
        return

    logging_active = True
    status_label.config(text="Status: Logging...", fg="green")

    write_to_file(
        f"\n\n--- Logging Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n"
    )

    listener = keyboard.Listener(on_press=on_press)
    listener.start()


def stop_logging():
    global listener, logging_active
    if not logging_active:
        return

    logging_active = False
    status_label.config(text="Status: Stopped", fg="red")

    if listener:
        listener.stop()

    write_to_file("\n--- Logging Ended ---\n")


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Keystroke Logging Demonstration")
root.geometry("450x300")
root.resizable(False, False)

tk.Label(root, text="Keystroke Logging Demo",
         font=("Arial", 16, "bold")).pack(pady=10)

status_label = tk.Label(root, text="Status: Stopped",
                        font=("Arial", 12), fg="red")
status_label.pack(pady=5)

tk.Button(root, text="Start Logging", width=22,
          bg="green", fg="white",
          command=start_logging).pack(pady=5)

tk.Button(root, text="Stop Logging", width=22,
          bg="red", fg="white",
          command=stop_logging).pack(pady=5)

tk.Label(
    root,
    text=f"Log file saved in project folder:\n{LOG_FILE}",
    font=("Arial", 9),
    wraplength=420,
    justify="center"
).pack(pady=10)

tk.Label(
    root,
    text="Educational purposes only.",
    font=("Arial", 9)
).pack(pady=5)

root.mainloop()
