import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

class Load_Files:
    def __init__(self):
        self.asked_directory = filedialog.askdirectory(title="Select Folder with music folders")
        
        if self.asked_directory:
            self.search_for_music(self.asked_directory, ["mp3", "flac", "wav", "ogg"])

    def search_for_music(self, root_dir, file_extensions=None):
        if file_extensions is None:
            file_extensions = []

        for root, dirs, files in os.walk(root_dir):
            dirs_to_keep = []
            for d in dirs:
                if not d.startswith('.'):
                    dirs_to_keep.append(d)
            dirs[:] = dirs_to_keep

            for file in files:
                if file.startswith('.'):
                    continue

                file_extension = file.lower().split('.')[-1]

                if file_extensions:
                    match = False
                    for ext in file_extensions:
                        if file_extension == ext.lower():
                            match = True
                            break
                    if not match:
                        continue

                parent_dir = os.path.basename(root)

                print(f"{parent_dir} - {file.strip("."+file_extension)} - {os.path.join(root, file)}")