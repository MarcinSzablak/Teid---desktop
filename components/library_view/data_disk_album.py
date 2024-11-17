import tkinter as tk
from tkinter import ttk
from tkinter import font

class Data_Disk_Album(tk.Frame):
    def __init__(self, parent, album):
        super().__init__(parent, background="#111111")
        self.album = album

        # Labels for displaying album info
        self.disk = tk.Label(self, text="Disk", background="#111111",
                             font=font.Font(family="Arial", size=12, weight="bold"),
                             foreground="#FFFFFF")
        self.time_of_songs = tk.Label(self, text="Time:", background="#111111",
                                      font=font.Font(family="Arial", size=12, weight="bold"),
                                      foreground="#FFFFFF")
        self.number_of_songs = tk.Label(self, text="Songs:", background="#111111",
                                        font=font.Font(family="Arial", size=12, weight="bold"),
                                        foreground="#FFFFFF")

        # Calculate total playtime
        all_time_seconds = 0
        for song in album.songs_data_list:
            # If duration is a string in MM:SS format, split it
            if isinstance(float(song["duration"]), str) and ":" in float(song["duration"]):
                minutes, seconds = map(int, float(song["duration"]).split(":"))
            else:
                minutes = int(float(song["duration"]))  # assuming it's in minutes
                seconds = int((float(song["duration"]) * 100) % 100)
            total_seconds = minutes * 60 + seconds
            all_time_seconds += total_seconds

        total_minutes = all_time_seconds // 60
        remaining_seconds = all_time_seconds % 60
        formatted_time = f"{total_minutes}:{remaining_seconds:02}"
        self.time_of_songs.config(text="Time: "+str(formatted_time))

        # Display number of songs
        self.number_of_songs.config(text="Songs: "+str(len(album.song_list)))

    def set_data_disk_album(self):
        # Use grid to organize the layout
        self.pack(fill="x", padx=20, pady=10, side="top")

        # Configure grid columns and rows
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # Place labels in the grid
        self.disk.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.time_of_songs.grid(row=0, column=1, padx=10, pady=5, sticky="n")
        self.number_of_songs.grid(row=0, column=2, padx=10, pady=5, sticky="e")
