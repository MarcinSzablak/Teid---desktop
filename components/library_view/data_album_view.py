import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from .data_disk_album import Data_Disk_Album
from .disk_view import Disk_View

class Data_Album_View(tk.Frame):
    def __init__(self, parent, album):
        super().__init__(parent, background="#222222")
        self.left_side = tk.Frame(self, background="#222222")
        self.right_side = tk.Frame(self, background="#222222")
        self.disk_info = Data_Disk_Album(self.left_side, album)
        self.disk_view = Disk_View(self.right_side, album)

    def set_data_album_view(self):
        self.pack(expand=True, fill="both")
        self.left_side.pack(side="left", expand=True, fill="both")
        self.right_side.pack(side="left", expand=True, fill="both")
        self.disk_info.set_data_disk_album()
        self.disk_view.set_disk_view()
