import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from ..music_operator.music_operator import Music_Operator

class Center_Bottom_Side(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, background="#1A1A1A")

        self.play_pause_button = tk.Button(self, command=self.set_play_pause_button, text="", background="#252525",height=45,width=45)
        self.play_pause_button.image = self.set_play_pause_image("assets/playarrow.png")
        self.play_pause_button.config(image=self.play_pause_button.image)
        self.play_pause_button.config(
            background="#252525",
            foreground="#FFFFFF",
            activebackground="#4B65A9",
            activeforeground="#FFFFFF",
            highlightbackground="#1A1A1A",
            bd=0,
            relief="flat"
        )
        self.play_pause_button.bind("<Enter>", lambda e: self.play_pause_button.config(background="#4B65A9"))
        self.play_pause_button.bind("<Leave>", lambda e: self.play_pause_button.config(background="#252525"))

    def set_center_bottom_side(self):
        self.play_pause_button.pack()

    def set_play_pause_button(self):
        if not Music_Operator.is_paused:
            Music_Operator.pause_music()
            self.play_pause_button.image = self.set_play_pause_image("assets/playarrow.png")
            self.play_pause_button.config(image=self.play_pause_button.image)
            Music_Operator.notify_observers(False)
        else:
            Music_Operator.unpause_music()
            self.play_pause_button.image = self.set_play_pause_image("assets/pause.png")
            self.play_pause_button.config(image=self.play_pause_button.image)
            Music_Operator.notify_observers(True)

    def set_play_pause_image(self, photo_uri):
        cover_image = Image.open(photo_uri)
        cover_image = cover_image.resize((40, 40))
        cover_photo = ImageTk.PhotoImage(cover_image)
        return cover_photo
