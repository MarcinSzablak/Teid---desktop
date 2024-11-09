import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from .load_files import Load_Files

from ..library_view.album_view import Album_View
from ..settings_dir.settings import Settings

class Load_Albums(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, background="#222222")
        self.albums = []

        self.load_music = tk.Button(self, text="Load Music", background="#1A1A1A",
                                     foreground="#FFFFFF", highlightbackground="#1A1A1A",
                                     bd=0, relief="flat", font=font.Font(family="Arial", size=12),
                                     activebackground='#4B65A9', activeforeground="#FFFFFF",padx=10,pady=10)

        self.load_music.config(command=lambda: self.load_albums_handler())

        self.scrollable = tk.Canvas(self, background="#222222", bd=0, highlightthickness=0)

        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.scrollable.yview,
                                      background="#222222", troughcolor="#222222", width=12,
                                      activebackground="#222222",highlightbackground="#222222")
        self.scrollable.configure(yscrollcommand=self.scrollbar.set)

        self.scrollable_holder = tk.Frame(self.scrollable, background="#222222")
        self.scrollable.create_window((0, 0), window=self.scrollable_holder, anchor="nw")

        self.parent_size = self.winfo_width()
        self.bind('<Configure>', lambda event: self.change_size(event.width))

        self.scrollable.bind_all("<MouseWheel>", self.on_mouse_wheel)
        self.scrollable.bind_all("<Button-4>", self.on_mouse_wheel)
        self.scrollable.bind_all("<Button-5>", self.on_mouse_wheel)

    def on_mouse_wheel(self, event):
        delta = event.delta if event.delta else 0
        if event.num == 5 or delta < 0:
            self.scrollable.yview_scroll(1, "units")
        elif event.num == 4 or delta > 0:
            self.scrollable.yview_scroll(-1, "units")

    def load_albums_handler(self):
        loaded_files = Load_Files()
        self.albums = loaded_files.albums
        Settings.set_directory(loaded_files.asked_directory)
        if len(self.albums):
            self.load_music.pack_forget()
            self.scrollable.pack(fill="both", expand=True,padx=(15,0)) # side="left", 
            # self.scrollbar.pack(side="right", fill="y")
            self.set_album()
    
    def change_size(self,size):
        self.parent_size = size
        self.set_album()

    def set_album(self):
        for widget in self.scrollable_holder.winfo_children():
            widget.destroy()
        
        buttons_per_row = 5
        padding = 12

        # Base button size based on the parent size
        button_size = (self.parent_size // buttons_per_row) - padding * 3

        # Calculate the maximum height of a button considering wrapped text
        max_text_lines = 3  # For example, we assume a max of 3 lines of text (adjust this based on your text)
        line_height = 20  # Example line height (adjust this based on font size and padding)

        # Total height of each button including text wrapping
        button_height_with_text = button_size + (line_height * max_text_lines)

        # Create buttons and add them to the grid
        for i in range(len(self.albums)):
            album_row = i // buttons_per_row
            album_col = i % buttons_per_row

            album_view = Album_View(self.scrollable_holder, self.albums[i], button_size)
            album_view.grid(row=album_row, column=album_col, padx=padding, pady=padding)

        # Calculate total rows needed (adjust for the number of albums)
        total_rows = (len(self.albums) // buttons_per_row) + (1 if len(self.albums) % buttons_per_row != 0 else 0)

        # Adjust total height to accommodate the wrapped buttons, with a small buffer at the bottom
        # (total_rows - 1) * padding is the vertical padding between rows
        buffer_bottom = padding * 2  # Add some extra space at the bottom of the scroll area
        total_height = total_rows * button_height_with_text + (total_rows - 1) * padding + buffer_bottom

        # Update the scrollable region based on the new button height and adjusted padding
        self.scrollable.config(scrollregion=(0, 0, 0, total_height))

    def set_view_album(self):
        if not Settings.check_directory():
            self.load_music.pack(expand=True)
        else:
            self.albums = Load_Files(ask_directory=Settings.get_directory()).albums
            self.scrollable.pack(fill="both", expand=True,padx=(15,0))

        
        