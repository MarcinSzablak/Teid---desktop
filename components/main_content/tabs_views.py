import tkinter as tk
from tkinter import ttk

class Tabs_Views(ttk.Notebook):
    def __init__(self,parent):
        super().__init__(parent)

        self.details = tk.Frame(self, background="#252525")
        self.library = tk.Frame(self, background="#252525")
        self.disk = tk.Frame(self, background="#252525")

    def set_tabs(self):
        self.pack(expand=True, fill='both')
        style = ttk.Style()
        style.layout('TNotebook.Tab', [])
        style.configure("TNotebook", borderwidth=0)
        style.configure("TNotebook.Tab", borderwidth=0)

        self.add(self.details)
        self.add(self.library)
        self.add(self.disk)

        label1 = ttk.Label(self.details, text="1")
        label1.pack(pady=20)

        label2 = ttk.Label(self.library, text="2")
        label2.pack(pady=20)

        label2 = ttk.Label(self.disk, text="3")
        label2.pack(pady=20)

    def change_to_details(self):
        self.select(self.details)

    def change_to_library(self):
        self.select(self.library)

    def change_to_disk(self):
        self.select(self.disk)