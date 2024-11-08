import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from ..library_view.load_files import Load_Files

class View_Album(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent,background="#222222")
        # print(parent.winfo_width())

        self.albums=[]

        self.load_music = tk.Button(self,text="Load Music",background="#1A1A1A",
                          foreground="#FFFFFF",
                          highlightbackground="#1A1A1A",
                          bd=0,relief="flat",
                          font=font.Font(family="Arial",size=12),
                          activebackground='#4B65A9',
                          activeforeground="#FFFFFF")
        
        self.load_music.config(command= lambda:(self.load_albums()))

    
    def load_albums(self):
        self.albums = Load_Files().albums
        self.load_music.pack_forget()
        print(len(self.albums))
        
        for i in range(len(self.albums)):
            album_row = i // 5
            album_col = i % int(len(self.albums) / 5)
            print(f"Index: {i}, Row: {album_row}, Col: {album_col}, Album: {self.albums[i].album_name}")
            print(self.albums[i].cover)
            
            label = tk.Button(self, text=f"{self.albums[i].album_name}", width=120, height=120)
            
            if self.albums[i].cover:
                cover_image = Image.open(self.albums[i].cover)
                cover_image = cover_image.resize((120, 120))
                cover_photo = ImageTk.PhotoImage(cover_image)

                label.config(image=cover_photo)
                label.image = cover_photo
            
            label.grid(row=album_row, column=album_col,padx=12,pady=12)
            

    def set_view_album(self):
        self.load_music.pack(expand=True)
        