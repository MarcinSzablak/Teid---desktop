import tkinter as tk
from tkinter import ttk

from ...settings_dir.filter_settings import Filter_Settings

class Filter_Pop_Up(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Select an Option")
        self.geometry("300x150")
        self.transient(parent)
        self.grab_set()

        tk.Label(self, text="Select filter option:").pack(pady=2)

        options = ["by Albums", "by Artists"]
        self.selected_option = tk.StringVar(value=Filter_Settings.get_filter())

        self.select_box = tk.OptionMenu(self, self.selected_option, *options)
        self.select_box.pack(pady=2)

        self.selected_option.trace_add("write",self.selected_filter_option)

    def selected_filter_option(self, *args):
        Filter_Settings.write_filter(self.selected_option.get())



