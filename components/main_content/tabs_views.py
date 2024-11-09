import tkinter as tk
from tkinter import ttk
from ..library_view.load_albums import Load_Albums

class Tabs_Views(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)

        self.details = tk.Frame(self, background="#222222")
        self.library = tk.Frame(self, background="#222222")
        self.disk = tk.Frame(self, background="#222222")


    def set_tabs(self):
        self.pack(expand=True, fill='both')

        self.details.pack(expand=True, fill='both')
        self.library.pack(expand=True, fill='both')
        self.disk.pack(expand=True, fill='both')

        self.details.pack_forget()
        self.disk.pack_forget()

        label1 = ttk.Label(self.details, text="1")
        label1.pack(pady=20)

        self.view_album = Load_Albums(self.library)
        self.view_album.pack(expand=True, fill='both')
        self.view_album.set_view_album()

        label2 = ttk.Label(self.disk, text="3")
        label2.pack(pady=20)

    def change_to_details(self):
        self.details.pack(expand=True, fill='both')
        self.library.pack_forget()
        self.disk.pack_forget()

    def change_to_library(self):
        self.details.pack_forget()
        self.library.pack(expand=True, fill='both')
        self.disk.pack_forget()

    def change_to_disk(self):
        self.details.pack_forget()
        self.library.pack_forget()
        self.disk.pack(expand=True, fill='both')