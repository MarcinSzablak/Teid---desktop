import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk

class Data_Disk_Album(tk.Frame):
    def __init__(self, parent, album):
        super().__init__(parent)
        self.album = album

        # Tworzymy etykiety
        self.disk = tk.Label(self, text="Disk")
        self.time_of_songs = tk.Label(self, text="Time:")
        self.number_of_songs = tk.Label(self, text="Songs:")

    def set_data_disk_album(self):
        self.pack(fill="x")

        # Ustawienie rozmiaru kolumny, aby rozciągnęła się na całą szerokość
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        
        # Ustawiamy elementy w jednej linii z marginesami, na początku, środku i końcu
        self.disk.grid(row=0, column=0, padx=10, pady=5, sticky="w")          # wyrównanie do lewej
        self.time_of_songs.grid(row=0, column=1, padx=10, pady=5, sticky="n") # wyrównanie do środka
        self.number_of_songs.grid(row=0, column=2, padx=10, pady=5, sticky="e") #