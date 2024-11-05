import tkinter as tk
from tkinter import ttk
from tkinter import font

class Top_Bar(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.config(height=50,background="#252525")
        self.name_of_album = tk.Label(self,text="lalaa llalala lalalall",# #FE33A1
                                      font=font.Font(family="Arial",size=18),
                                      background="#252525",
                                      foreground="#FFFFFF")

    def set_top_bar(self):
        self.pack(fill='x')
        self.name_of_album.pack(pady=5,padx=30,side="right")
