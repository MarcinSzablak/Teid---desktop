import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk

class Top_Bar(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.config(height=50,background="#252525")
        self.name_of_album = tk.Label(self,text="lalaa llalala lalalall",# #FE33A1
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


    def set_top_bar(self):
        self.pack(fill='x')
        self.name_of_album.pack(pady=5,padx=30,side="right")
        self.back_image_holder.pack(pady=5,padx=(30,0),side="left")
        self.search_bar_border.pack(pady=5,padx=3,side="left")
        self.filter_image_holder.pack(pady=5,padx=3,side="left")
        self.swap_image_holder.pack(pady=5,padx=3,side="left")
        
        
