import os
from tkinter import filedialog
from ..album import Album

class Load_Files:
    def __init__(self, ask_directory=None):
        """
        Initialize and load music files from a specified or user-selected directory.
        """
        self.albums = []
        self.asked_directory = ask_directory or filedialog.askdirectory(title="Select Folder with Music Folders")
        
        if self.asked_directory:
            self.search_for_music(self.asked_directory)

    def search_for_music(self, root_dir, file_extensions=None):
        """
        Search for music and associated album metadata in the specified directory.

        Args:
            root_dir (str): The root directory to search for music.
            file_extensions (list): List of file extensions to include in the search. Defaults to common audio formats.
        """
        if file_extensions is None:
            file_extensions = ["mp3", "flac", "wav", "ogg"]

        # Clear existing album data
        self.albums.clear()

        # Normalize file extensions for case-insensitive matching
        valid_audio_exts = {ext.lower() for ext in file_extensions}
        valid_image_exts = {"png", "jpg", "jpeg", "webp"}

        # Walk through the directory tree
        for root, dirs, files in os.walk(root_dir):
            # Exclude hidden directories
            dirs[:] = [d for d in dirs if not d.startswith('.')]

            # Album metadata
            album_name = os.path.basename(root)
            cover_image = None
            song_list = []

            # Process files in the current directory
            for file_name in files:
                if file_name.startswith('.'):
                    continue

                file_extension = file_name.lower().split('.')[-1]
                file_path = os.path.join(root, file_name)

                # Classify files into songs or album cover
                if file_extension in valid_audio_exts:
                    song_list.append(file_path)
                elif file_extension in valid_image_exts and not cover_image:
                    cover_image = file_path

            # Create an Album instance if valid songs are found
            if song_list:
                # Remove cover image from song list if necessary
                if cover_image and cover_image in song_list:
                    song_list.remove(cover_image)

                album = Album(album_name, cover_image, song_list)
                self.albums.append(album)
