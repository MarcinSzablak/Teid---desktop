import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk

class Album_View(tk.Frame): #eyed3 dla wyczytywania metadanych
    def __init__(self,parent,album,size):
        super().__init__(parent,bg="#222222")

        self.cover_button = tk.Button(self,text=album.album_name,
                                    width=size,height=size,
                                    bd=0,relief="flat",
                                    highlightbackground="#222222",
                                    background="#1A1A1A",activebackground="#1A1A1A")
        
        if not album.cover:
            cover_image = Image.open("assets/defaultcover.png")
        else:
            cover_image = Image.open(album.cover)
        cover_image = cover_image.resize((size, size))
        cover_photo = ImageTk.PhotoImage(cover_image)
        self.cover_button.config(image=cover_photo)
        self.cover_button.image = cover_photo
        self.cover_button.pack()

        self.album_name = tk.Label(self, text=album.album_name, justify="center")
        self.album_name.config(font=font.Font(family="Arial", size=12),
                               wraplength=size, # Set the wrap length (width of the area)
                               bg="#222222", fg="white")
        self.album_name.pack()
        