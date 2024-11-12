import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
import eyed3 # type: ignore

class Top_Bar(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.config(height=50,background="#252525")
        self.name_of_album = tk.Label(self,text="",# #FE33A1
                                      font=font.Font(family="Arial",size=20),
                                      background="#252525",
                                      foreground="#FFFFFF")
        
        self.swap_image = ImageTk.PhotoImage(Image.open("assets/swap.png").resize((40, 40)))
        self.swap_image_holder = tk.Button(self,image=self.swap_image,
                                          background="#252525",relief="flat",
                                          highlightbackground="#252525",bd=0,
                                          activebackground='#252525')
        
        self.filter_image = ImageTk.PhotoImage(Image.open("assets/filter.png").resize((40, 40)))
        self.filter_image_holder = tk.Button(self,image=self.filter_image,
                                          background="#252525",relief="flat",
                                          highlightbackground="#252525",bd=0,
                                          activebackground='#252525')
        
        self.search_bar_border = tk.Frame(self,background="#FFFFFF")
        
        self.search_bar = tk.Entry(self.search_bar_border,font=font.Font(family="Arial",size=16),
                                   background="#252525",
                                   foreground="#FFFFFF",
                                   relief="flat").pack(pady=2,padx=2)
        
        self.back_image = ImageTk.PhotoImage(Image.open("assets/back.png").resize((40, 40)))
        self.back_image_holder = tk.Button(self,image=self.back_image,
                                          background="#252525",relief="flat",
                                          highlightbackground="#252525",bd=0,
                                          activebackground='#252525')

    def set_album_name(self,album):
        audio_file = eyed3.load(album.song_list[0])
        if audio_file.tag:
            for tag in audio_file.tag.frame_set:
                frame = audio_file.tag.frame_set[tag][0]
                if tag == b'TALB':
                    album_title = audio_file.tag.album
                    self.name_of_album.config(text=str(album_title))
    def unset_album_name(self):
        self.name_of_album.config(text="")

    def back_to_albums(self,albums_list,album_data):
        albums_list.pack(fill="both", expand=True,padx=(15,0))
        album_data.pack_forget()
        self.unset_back_button()
        self.unset_album_name()

    def set_top_bar(self):
        self.pack(fill='x')
        self.name_of_album.pack(pady=5,padx=30,side="right")
        self.back_image_holder.pack(pady=5,padx=(30,0),side="left")
        self.search_bar_border.pack(pady=5,padx=(30,3),side="left")
        self.filter_image_holder.pack(pady=5,padx=3,side="left")
        self.swap_image_holder.pack(pady=5,padx=3,side="left")

    def set_back_button(self):
        self.back_image_holder.pack(pady=5,padx=(30,0),side="left")
        self.search_bar_border.pack_forget()
        self.filter_image_holder.pack_forget()
        self.swap_image_holder.pack_forget()
        self.name_of_album.pack_forget()
        self.search_bar_border.pack(pady=5,padx=3,side="left")
        self.filter_image_holder.pack(pady=5,padx=3,side="left")
        self.swap_image_holder.pack(pady=5,padx=3,side="left")
        self.name_of_album.pack(pady=5,padx=30,side="right")

    def unset_back_button(self):
        self.back_image_holder.pack_forget()
        self.search_bar_border.pack(pady=5,padx=(30,3),side="left")
        self.filter_image_holder.pack(pady=5,padx=3,side="left")
        self.swap_image_holder.pack(pady=5,padx=3,side="left")
        self.name_of_album.pack(pady=5,padx=30,side="right")

        
    