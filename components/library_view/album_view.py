import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from .load_files import Load_Files

class Album_View(tk.Button):
    def __init__(self,parent,album,size):
        super().__init__(parent,
                         text=album.album_name,
                         width=size,height=size)
        
        if not album.cover:
            cover_image = Image.open("assets/defaultcover.png")
        else:
            cover_image = Image.open(album.cover)
        cover_image = cover_image.resize((size, size))
        cover_photo = ImageTk.PhotoImage(cover_image)
        self.config(image=cover_photo)
        self.image = cover_photo
        