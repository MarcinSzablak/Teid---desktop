import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
from ..album import Album

class Load_Files:
    def __init__(self,ask_directory=None):
        self.albums = []
        if ask_directory == None:
            self.asked_directory = filedialog.askdirectory(title="Select Folder with music folders")
            
            if self.asked_directory:
                self.search_for_music(self.asked_directory)
        else:
            self.search_for_music(ask_directory)

    def search_for_music(self, root_dir, file_extensions=["mp3", "flac", "wav", "ogg"]):
        self.albums = []

        for root, dirs, files in os.walk(root_dir):
            dirs_to_keep = []
            for d in dirs:
                if not d.startswith('.'):
                    dirs_to_keep.append(d)
            dirs[:] = dirs_to_keep

            album_name = os.path.basename(root)
            cover_image = None
            song_list = []

            for song in files:
                if song.startswith('.'):
                    continue

                file_extension = song.lower().split('.')[-1]

                if file_extension in [ext.lower() for ext in file_extensions]:
                    song_path = os.path.join(root, song)
                    song_list.append(song_path)

                if file_extension in ['png', 'jpg', 'jpeg',"wepp"] and not cover_image:
                    cover_image = os.path.join(root, song)

            if song_list:
                if cover_image and cover_image in song_list:
                    song_list.remove(cover_image)

                album = Album(album_name, cover_image, song_list)
                self.albums.append(album)

