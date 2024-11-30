import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import eyed3  # type: ignore

from .pop_ups.sort_pop_up import Sort_Pop_Up
from .pop_ups.filter_pop_up import Filter_Pop_Up

class Top_Bar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(height=50, background="#252525")

        # Back button (Initially hidden)
        self.back_image = ImageTk.PhotoImage(Image.open("assets/back.png").resize((40, 40)))
        self.back_image_holder = tk.Button(self, image=self.back_image,
                                           background="#252525", relief="flat",
                                           highlightbackground="#252525", bd=0,
                                           activebackground='#252525', command=self.on_back_button_clicked)
        self.back_image_holder.pack(side="left", pady=5, padx=(30, 0))
        self.back_image_holder.pack_forget()  # Initially hide the back button

        # Search bar
        self.search_bar_border = tk.Frame(self, background="#FFFFFF")
        self.search_bar = tk.Entry(self.search_bar_border, font=font.Font(family="Arial", size=16),
                                   background="#252525", foreground="#FFFFFF", relief="flat")
        self.search_bar.pack(pady=2, padx=2)

        # Swap button
        self.swap_image = ImageTk.PhotoImage(Image.open("assets/swap.png").resize((40, 40)))
        self.swap_image_holder = tk.Button(self, image=self.swap_image,
                                           background="#252525", relief="flat",
                                           highlightbackground="#252525", bd=0,
                                           activebackground='#252525',
                                           command=self.on_sort_button_clicked)
        

        # Filter button
        self.filter_image = ImageTk.PhotoImage(Image.open("assets/filter.png").resize((40, 40)))
        self.filter_image_holder = tk.Button(self, image=self.filter_image,
                                             background="#252525", relief="flat",
                                             highlightbackground="#252525", bd=0,
                                             activebackground='#252525',
                                             command=self.on_filter_button_clicked)
        

        # Album name label (Right side)
        self.name_of_album = tk.Label(self, text="",
                                      font=font.Font(family="Arial", size=20),
                                      background="#252525", foreground="#FFFFFF")
        
        self.search_bar_border.pack(side="left", pady=5, padx=(30, 3))
        self.filter_image_holder.pack(side="left", pady=5, padx=3)
        self.swap_image_holder.pack(side="left", pady=5, padx=3)

        self.name_of_album.pack(side="right", padx=30, pady=5)

    def on_filter_button_clicked(self):
        Filter_Pop_Up(self)

    def on_sort_button_clicked(self):
        Sort_Pop_Up(self)

    def on_back_button_clicked(self):
        """Handle back button click to return to the album list."""
        if self.back_callback:
            self.back_callback()

    def set_back_button(self, back_callback):
        """Set a callback for the back button."""
        self.back_callback = back_callback
        self.name_of_album.pack_forget()
        self.filter_image_holder.pack_forget()
        self.swap_image_holder.pack_forget()
        self.search_bar_border.pack_forget()

        self.back_image_holder.pack(side="left", pady=5, padx=(30, 0))
        
        self.name_of_album.pack(side="right", padx=30, pady=5)
        self.search_bar_border.pack(side="left", pady=5, padx=3)
        self.filter_image_holder.pack(side="left", pady=5, padx=3)
        self.swap_image_holder.pack(side="left", pady=5, padx=3)
        


    def unset_back_button(self):
        """Unset the back button and reset top bar for album list."""
        self.back_image_holder.pack_forget()

        self.filter_image_holder.pack_forget()
        self.swap_image_holder.pack_forget()
        self.search_bar_border.pack_forget()

        self.search_bar_border.pack(side="left", pady=5, padx=(30, 3))
        self.filter_image_holder.pack(side="left", pady=5, padx=3)
        self.swap_image_holder.pack(side="left", pady=5, padx=3)

        self.unset_album_name()
        

    def set_album_name(self, album):
        """Set album name when viewing album details."""
        audio_file = eyed3.load(album.song_list[0])
        if audio_file.tag:
            for tag in audio_file.tag.frame_set:
                frame = audio_file.tag.frame_set[tag][0]
                if tag == b'TALB':
                    album_title = audio_file.tag.album
                    self.name_of_album.config(text=str(album_title))

    def unset_album_name(self):
        """Unset album name when returning to album list."""
        self.name_of_album.config(text="")
