import tkinter as tk
from tkinter import ttk

class Filter_Pop_Up(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Select an Option")
        self.geometry("300x150")
        self.transient(parent)
        self.grab_set()

        tk.Label(self, text="Select filter option:").pack(pady=10)

        options = ["by Albums", "by Artists"]
        
        selected_option = tk.StringVar()
        combo = ttk.Combobox(self, textvariable=selected_option, values=options, state="readonly")
        combo.pack(pady=5)

        combo.current(0)

