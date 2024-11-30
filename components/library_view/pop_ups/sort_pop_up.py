import tkinter as tk
from tkinter import ttk
from tkinter import font
import platform

from ...windows_titlebar_fix import Windows_Titlebar_fix
from ...settings_dir.filter_settings import Filter_Settings

class Sort_Pop_Up(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Select an Option")
        self.geometry("150x70")
        self.transient(parent)
        self.grab_set()

        if platform.system() == "Windows":
            Windows_Titlebar_fix(self)

        self.config(background="#222222")

        tk.Label(self, text="Select filter option:",background="#222222",
                 font=font.Font(family="Arial", size=12),foreground="#FFFFFF").pack(pady=2)

        options = ["from A to Z (Album)", "from Z to A (Album)","from A to Z (Artist)", "from Z to A (Artist)"]
        self.selected_option = tk.StringVar(value=Filter_Settings.get_filter())

        self.select_box = tk.OptionMenu(self, self.selected_option, *options)
        self.select_box.pack(pady=2)

        self.select_box.config(background="#1A1A1A",
            foreground="#FFFFFF",
            activebackground="#4B65A9",
            activeforeground="#FFFFFF",
            highlightbackground="#1A1A1A",
            bd=0)
        self.select_box["menu"].config(background="#1A1A1A",
            foreground="#FFFFFF",
            activebackground="#4B65A9",
            activeforeground="#FFFFFF",
            bd=0)

        # When the value changes, call selected_filter_option()
        self.selected_option.trace_add("write", self.selected_filter_option)

    def selected_sort_option(self, *args):
        # Update the filter setting and notify observers
        new_filter = self.selected_option.get()
        Filter_Settings.write_filter(new_filter)
