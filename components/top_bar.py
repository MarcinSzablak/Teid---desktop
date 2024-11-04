import tkinter as tk
from tkinter import ttk

class Top_Bar(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.config(height=50)
        self.label = tk.Label(self,text="lala",background="#FE33A1")

    def set_top_bar(self):
        self.pack(fill='x')
        self.label.pack(pady=5)