import tkinter as tk
from tkinter import ttk
from ..library_view.load_albums import Load_Albums

class Tabs_Views(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Create tab frames
        self.tabs = {
            "details": tk.Frame(self, background="#222222"),
            "library": tk.Frame(self, background="#222222"),
            "disk": tk.Frame(self, background="#222222"),
        }

        # Active tab tracker
        self.active_tab = None

    def set_tabs(self):
        """
        Initialize and display the library tab by default.
        """
        self.pack(expand=True, fill="both")

        # Set up the tabs and hide all except "library"
        for name, frame in self.tabs.items():
            frame.pack(expand=True, fill="both")
            frame.pack_forget()

        # Add content to the tabs
        ttk.Label(self.tabs["details"], text="1").pack(pady=20)

        self.view_album = Load_Albums(self.tabs["library"])
        self.view_album.pack(expand=True, fill="both")
        self.view_album.set_view_album()

        ttk.Label(self.tabs["disk"], text="3").pack(pady=20)

        # Show library tab by default
        self.change_to_library()

    def change_to_tab(self, tab_name):
        """
        Show the specified tab and hide the others.
        """
        if self.active_tab:
            self.tabs[self.active_tab].pack_forget()
        self.tabs[tab_name].pack(expand=True, fill="both")
        self.active_tab = tab_name

    def change_to_details(self):
        self.change_to_tab("details")

    def change_to_library(self):
        self.change_to_tab("library")

    def change_to_disk(self):
        self.change_to_tab("disk")
