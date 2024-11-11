import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk

class Data_Album_View(tk.Frame):
    def __init__(self,parent,album):
        super().__init__(parent,background="#F2B112",width=parent.winfo_width()//1.5)
        self.disk_info = tk.Label(self,text="lala",background="#F2B112")
    
    def set_data_album_view(self):
        self.pack(pady=15,expand=True,fill="x")
        self.disk_info.pack(pady=5,expand=True,fill="x")