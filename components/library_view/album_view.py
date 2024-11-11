import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
import eyed3 # type: ignore
import io

class Album_View(tk.Frame):
    def __init__(self,parent,album,size):
        super().__init__(parent,bg="#222222")

        self.cover_button = tk.Button(self,text=album.album_name,
                                    width=size,height=size,
                                    bd=0,relief="flat",
                                    highlightbackground="#222222",
                                    background="#1A1A1A",activebackground="#1A1A1A")
        
        self.album_name = tk.Label(self, text=album.album_name, justify="center")
        self.album_name.config(font=font.Font(family="Arial", size=12),
                               wraplength=size,
                               bg="#222222", fg="white")
        
        if not album.cover:
            cover_image = Image.open("assets/defaultcover.png")
        else:
            cover_image = Image.open(album.cover)
        
        audio_file = eyed3.load(album.song_list[0])
        if audio_file.tag:
            for tag in audio_file.tag.frame_set:
                frame = audio_file.tag.frame_set[tag][0]
                if tag == b'APIC':
                    image_data = frame.image_data
                    cover_image = Image.open(io.BytesIO(image_data))

                if tag == b'TALB':
                    album_title = audio_file.tag.album
                    self.album_name.config(text=album_title)
                
                if tag == b'TPE1':
                    band_name = audio_file.tag.artist
                    album.band_name=str(band_name)
                

        cover_image = cover_image.resize((size, size))
        cover_photo = ImageTk.PhotoImage(cover_image)
        self.cover_button.config(image=cover_photo)
        self.cover_button.image = cover_photo

        self.cover_button.pack()
        self.album_name.pack()
        