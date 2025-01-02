import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from ..music_operator.music_operator import Music_Operator

class Bottom_Bottom_Side(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)

        self.long_of_song = ctk.CTkSlider(self, from_=0, to=100,width=50000,height=20,state="disable")
        self.long_of_song.set(0)
    
    def set_bottom_bottom_bar(self):
        self.long_of_song.pack(fill="x",expand=True,padx=30)

    def change_long_of_song_slider_clicked_in_list(self,value):
        self.long_of_song.configure(state="normal")
        self.slide_for_in_song()

    def slide_for_in_song(self):
        Music_Operator.get_song_index()
        song_played = Music_Operator.get_song_data(Music_Operator.song_index)

        try:
            duration_in_minutes = float(song_played['duration'])
            duration_in_seconds = duration_in_minutes * 60
            self.long_of_song.configure(to=duration_in_seconds)
        except:
            pass