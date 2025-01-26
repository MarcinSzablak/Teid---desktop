import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from ..music_operator.music_operator import Music_Operator

class Bottom_Bottom_Side(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)

        self.song_duration = 0
        self.long_of_song = ctk.CTkSlider(self, from_=0, to=100,width=50000,height=20,state="disable")
        self.long_of_song.set(self.song_duration)

        self.long_of_song.bind("<Button-1>",self.click_change_song_duration)
    
    def click_change_song_duration(self,value):
        duration_now = int(int(self.long_of_song._to)*self.long_of_song._value)
        self.song_duration = duration_now
        self.long_of_song.set(duration_now)
        Music_Operator.set_song_position(duration_now)

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
            duration_in_seconds = (int(duration_in_minutes) * 60)+((float(duration_in_minutes)-int(duration_in_minutes))*100)
            self.long_of_song.configure(to=duration_in_seconds)
            self.after(1000,self.change_duration_slider)
        except:
            pass
    
    def change_duration_slider(self):
        self.song_duration+=1
        self.long_of_song.set(self.song_duration)
        if (int(self.long_of_song._to)!=int(self.song_duration)):
            self.after(1000,self.change_duration_slider)
        