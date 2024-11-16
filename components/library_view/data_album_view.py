import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk

from .data_disk_album import Data_Disk_Album
from .disk_view import Disk_View
from .data_list_song_album import Data_List_Song_Album

class Data_Album_View(tk.Frame):
    def __init__(self, parent, album):
        super().__init__(parent, background="#222222")
        
        # Create frames for the left and right side content
        self.left_side = tk.Frame(self, background="#222222")
        self.right_side = tk.Frame(self, background="#222222")
        
        # Initialize the components (disk info, disk view, and song list)
        self.disk_info = Data_Disk_Album(self.left_side, album)
        self.disk_view = Disk_View(self.right_side, album)  # Disk_View runs on a separate thread
        self.songs_listed = Data_List_Song_Album(self.left_side, album)

    def set_data_album_view(self):
        # Layout the components using grid
        self.pack(expand=True, fill="both")
        
        # Add left and right sides to the grid
        self.left_side.grid(row=0, column=0, sticky="nsew")
        self.right_side.grid(row=0, column=1, sticky="nsew")
        
        # Set up individual components
        self.disk_info.set_data_disk_album()
        self.disk_view.set_disk_view()
        self.songs_listed.set_data_list_song_album()
        
        # Configure grid weights for resizing
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
