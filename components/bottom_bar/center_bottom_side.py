import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from ..music_operator.music_operator import Music_Operator

class Center_Bottom_Side(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, background="#1A1A1A")

        self.play_pause_button = tk.Button(self, command=self.set_play_pause_button, text="", background="#252525",height=45,width=45,state='disabled')
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

        self.left_skip_button = tk.Button(self, command=self.skip_to_previous_song, text="", background="#252525",height=45,width=45,state='disabled')
        self.left_skip_button.image = self.set_play_pause_image("assets/skipprevious.png")
        self.left_skip_button.config(image=self.left_skip_button.image)
        self.left_skip_button.config(
            background="#252525",
            foreground="#FFFFFF",
            activebackground="#4B65A9",
            activeforeground="#FFFFFF",
            highlightbackground="#1A1A1A",
            bd=0,
            relief="flat"
        )
        self.left_skip_button.bind("<Enter>", lambda e: self.left_skip_button.config(background="#4B65A9"))
        self.left_skip_button.bind("<Leave>", lambda e: self.left_skip_button.config(background="#252525"))

        self.right_skip_button = tk.Button(self, command=self.skip_to_next_song, text="", background="#252525",height=45,width=45,state='disabled')
        self.right_skip_button.image = self.set_play_pause_image("assets/skipnext.png")
        self.right_skip_button.config(image=self.right_skip_button.image)
        self.right_skip_button.config(
            background="#252525",
            foreground="#FFFFFF",
            activebackground="#4B65A9",
            activeforeground="#FFFFFF",
            highlightbackground="#1A1A1A",
            bd=0,
            relief="flat"
        )
        self.right_skip_button.bind("<Enter>", lambda e: self.right_skip_button.config(background="#4B65A9"))
        self.right_skip_button.bind("<Leave>", lambda e: self.right_skip_button.config(background="#252525"))

    def set_center_bottom_side(self):
        self.grid_columnconfigure((0,1,2), weight=1, uniform="equal")
        self.left_skip_button.grid(column=0,row=0)
        self.play_pause_button.grid(column=1,row=0)
        self.right_skip_button.grid(column=2,row=0)

    def skip_to_previous_song(self):
        Music_Operator.get_song_index()
        if(Music_Operator.song_index!=0):
            Music_Operator.set_song_by_index(Music_Operator.song_index-1)

    def skip_to_next_song(self):
        Music_Operator.get_song_index()
        if(Music_Operator.song_index<len(Music_Operator.album.songs_data_list)-1):
            Music_Operator.set_song_by_index(Music_Operator.song_index+1)

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
        
    def change_pause_play_button_clicked_in_list(self,value):
        if Music_Operator.is_paused:
            self.play_pause_button.image = self.set_play_pause_image("assets/playarrow.png")
            self.play_pause_button.config(image=self.play_pause_button.image)
        else:
            self.play_pause_button.image = self.set_play_pause_image("assets/pause.png")
            self.play_pause_button.config(image=self.play_pause_button.image)
        self.play_pause_button.config(state="normal")
        self.right_skip_button.config(state="normal")
        self.left_skip_button.config(state="normal")

    def set_play_pause_image(self, photo_uri):
        cover_image = Image.open(photo_uri)
        cover_image = cover_image.resize((40, 40))
        cover_photo = ImageTk.PhotoImage(cover_image)
        return cover_photo
