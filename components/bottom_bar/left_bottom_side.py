import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import customtkinter as ctk

from ..music_operator.music_operator import Music_Operator

class Left_Bottom_Side(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent,background="#1A1A1A")

        self.settings = tk.Button(self,background="#1A1A1A",
            foreground="#FFFFFF",activebackground="#4B65A9",
            activeforeground="#FFFFFF",highlightbackground="#1A1A1A",
            bd=0,relief="flat",height=45,width=45)
        self.settings.image_name = self.set_volume_image("assets/settings.png")
        self.settings.config(image=self.settings.image_name)

        self.volume_image = tk.Label(self, bd=0, relief="flat",
                                      highlightbackground="#222222",
                                      background="#1A1A1A", activebackground="#1A1A1A")
        self.volume_image.image_name = None

        self.volume_bar = ctk.CTkSlider(self, from_=0, to=100, command=self.set_volume_of_sound,width=160,height=20)
        self.volume_bar.set(50)
        Music_Operator.set_music_value(0.5)

        self.set_volume_of_sound(50)

    def set_left_bottom_bar(self):
        self.settings.pack(side="left",padx=(10,0))
        self.volume_image.pack(side="left")
        self.volume_bar.pack(side="right")

    def set_volume_of_sound(self, value):
        value = int(value)
        if value < 25:
            image_path = "assets/volumemute.png"
        elif 25 <= value < 60:
            image_path = "assets/volumedown.png"
        else:
            image_path = "assets/volumeup.png"

        Music_Operator.set_music_value((value*0.01))

        Music_Operator.get_song_index()

        self.volume_image.image_name = self.set_volume_image(image_path)
        self.volume_image.config(image=self.volume_image.image_name)

    def set_volume_image(self, photo_uri):
        cover_image = Image.open(photo_uri)
        cover_image = cover_image.resize((40, 40))
        cover_photo = ImageTk.PhotoImage(cover_image)
        return cover_photo