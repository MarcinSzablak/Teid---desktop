import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from .load_files import Load_Files

from ..library_view.album_view import Album_View

class Load_Albums(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, background="#222222")
        self.albums = []

        self.load_music = tk.Button(self, text="Load Music", background="#1A1A1A",
                                     foreground="#FFFFFF", highlightbackground="#1A1A1A",
                                     bd=0, relief="flat", font=font.Font(family="Arial", size=12),
                                     activebackground='#4B65A9', activeforeground="#FFFFFF")

        self.load_music.config(command=lambda: self.load_albums())

        self.scrollable = tk.Canvas(self)

        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.scrollable.yview)
        
        self.scrollable.configure(yscrollcommand=self.scrollbar.set)

        self.scrollable_holder = tk.Frame(self.scrollable)
        self.scrollable.create_window((0, 0), window=self.scrollable_holder, anchor="nw")

        self.parent_size = self.winfo_width()
        self.bind('<Configure>', lambda event: self.change_size(event.width))

    def load_albums(self):
        self.albums = Load_Files().albums
        if len(self.albums):
            self.load_music.pack_forget()
            self.scrollable.pack(side="left", fill="both", expand=True)
            self.scrollbar.pack(side="right", fill="y")
            self.set_album()
    
    def change_size(self,size):
        self.parent_size = size
        self.set_album()

    def set_album(self):
        for widget in self.scrollable_holder.winfo_children():
            widget.destroy()
        buttons_per_row = 5
        padding = 12

        button_size = (self.parent_size // buttons_per_row) - padding * 3
        

        for i in range(len(self.albums)):
            album_row = i // buttons_per_row
            album_col = i % buttons_per_row

            album_view = Album_View(self.scrollable_holder,self.albums[i],button_size)
            album_view.grid(row=album_row, column=album_col, padx=padding, pady=padding)

        total_rows = (len(self.albums) // buttons_per_row) + (1 if len(self.albums) % buttons_per_row != 0 else 0)
        total_height = total_rows * (button_size + padding * 3)

        self.scrollable.config(scrollregion=(0, 0, 0, total_height))
            
    def set_view_album(self):
        self.load_music.pack(expand=True)
        
        