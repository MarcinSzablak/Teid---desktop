import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk

from .data_disk_album import Data_Disk_Album

class Data_Album_View(tk.Frame):
    def __init__(self,parent,album):
        super().__init__(parent,background="#F2B112")
        self.left_side = tk.Frame(self,background="#22A112",width=self.winfo_width()*0.75)
        self.right_side = tk.Frame(self,background="#F2B1FF")
        self.disk_info = Data_Disk_Album(self.left_side,album)
    
    def set_data_album_view(self):
        self.pack(expand=True,fill="both")
        self.left_side.pack(side="left",expand=True,fill="both")
        self.right_side.pack(side="left",expand=True,fill="both")
        self.disk_info.set_data_disk_album()
        