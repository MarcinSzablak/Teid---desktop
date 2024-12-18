import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
from .load_files import Load_Files
from .data_album_view import Data_Album_View
from .album_view import Album_View
from .artist_view import Artist_View
from ..settings_dir.settings import Settings
from .top_bar import Top_Bar
import threading
from ..settings_dir.filter_settings import Filter_Settings
from ..settings_dir.sort_settings import Sort_Settings
from ..settings_dir.search_settings import Search_Settings

class Library_View(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, background="#222222")
        self.albums = []
        self.unique_artist = []
        self.data_from_album = None
        self.parent_size = self.winfo_width()

        self.artist_albums_selected = None

        # Initialize and pack the Top_Bar
        self.top_bar = Top_Bar(self)
        self.top_bar.pack(side="top", fill="x")

        # Load music button
        self.load_music_button = tk.Button(
            self, text="Load Music", background="#1A1A1A", foreground="#FFFFFF",
            font=font.Font(family="Arial", size=12), bd=0, relief="flat",
            activebackground='#4B65A9', activeforeground="#FFFFFF",
            command=self.load_albums_handler, padx=10, pady=10
        )

        # Scrollable area for albums
        self.scrollable_canvas = tk.Canvas(self, background="#222222", bd=0, highlightthickness=0)
        self.scrollable_holder = tk.Frame(self.scrollable_canvas, background="#222222")
        self.scrollable_canvas.create_window((0, 0), window=self.scrollable_holder, anchor="nw")

        self.scrollbar = tk.Scrollbar(
            self, orient="vertical", command=self.scrollable_canvas.yview,
            background="#222222", troughcolor="#222222", width=12,
            activebackground="#222222", highlightbackground="#222222"
        )
        self.scrollable_canvas.configure(yscrollcommand=self.scrollbar.set)

        # Event bindings
        self.bind('<Configure>', self.on_resize)

        # Mouse wheel event binding
        self.scrollable_canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)
        self.scrollable_canvas.bind_all("<Button-4>", self.on_mouse_wheel)
        self.scrollable_canvas.bind_all("<Button-5>", self.on_mouse_wheel)

        # Thread management
        self.album_loading_thread = None  # Keep track of the album loading thread
        self.is_loading = False  # Flag to prevent redundant loading

        Filter_Settings.add_observer(self.on_filter_change)
        Sort_Settings.add_observer(self.on_sort_change)
        Search_Settings.add_observer(self.on_search_change)

        self.resize_timer = None

    def on_resize(self, event):
        """Handle resize event and delay layout update."""
        if self.resize_timer:
            self.after_cancel(self.resize_timer)  # Cancel the previous scheduled update

        # Clear all widgets immediately on resize
        self.clear_widgets()

        # Set a new update after a delay (e.g., 300 milliseconds)
        self.resize_timer = self.after(300, self.update_layout)

    def clear_widgets(self):
        """Clear the scrollable area widgets immediately when resizing."""
        for widget in self.scrollable_holder.winfo_children():
            widget.destroy()

    def update_layout(self):
        """Update layout dynamically after resizing."""
        self.parent_size = self.winfo_width()

        # Repopulate the content based on the current filter
        if Filter_Settings.get_filter() == "by Artists":
            if self.artist_albums_selected:
                self.display_albums(self.artist_albums_selected)
            else:    
                self.display_artists(self.unique_artist)
        elif Filter_Settings.get_filter() == "by Albums":
            self.display_albums(self.albums)

    def on_search_change(self, new_value_sort):
        if Search_Settings.get_filter() == "":
            self.on_filter_change(None)
        else:
            if Filter_Settings.get_filter() == "by Albums":
                matching_albums = [album for album in self.albums if album.album_name.lower().startswith(Search_Settings.get_filter().lower())]
                self.display_albums(matching_albums)
            elif Filter_Settings.get_filter() == "by Artists":
                matching_artist = [artist for artist in self.unique_artist if artist.lower().startswith(Search_Settings.get_filter().lower())]
                self.display_artists(matching_artist)

    def on_sort_change(self, new_value_sort):
        if Sort_Settings.get_filter() == "from A to Z":
            self.albums.sort(key=lambda album: album.album_name)
            self.unique_artist = sorted(self.unique_artist)
            self.on_filter_change(None)
        elif Sort_Settings.get_filter() == "from Z to A":
            self.albums.sort(key=lambda album: album.album_name, reverse=True)
            self.unique_artist = sorted(self.unique_artist, reverse=True)
            self.on_filter_change(None)

    def on_filter_change(self, new_value_filter):
        if Filter_Settings.get_filter() == "by Artists":
            self.display_artists(self.unique_artist)
        elif Filter_Settings.get_filter() == "by Albums":
            self.display_albums(self.albums)

    def on_mouse_wheel(self, event):
        """Handle mouse wheel scrolling for the scrollable canvas."""
        if event.delta > 0 or event.num == 4:
            self.scrollable_canvas.yview_scroll(-1, "units")  # Scroll up
        elif event.delta < 0 or event.num == 5:
            self.scrollable_canvas.yview_scroll(1, "units")  # Scroll down

    def load_albums_handler(self):
        """Handler to load albums when the 'Load Music' button is clicked."""
        if self.is_loading:
            return  # Prevent redundant loading
        self.is_loading = True
        self.load_music_button.config(state=tk.DISABLED)  # Disable button while loading

        # Start loading albums in a separate thread
        if self.album_loading_thread and self.album_loading_thread.is_alive():
            self.album_loading_thread.join()  # Ensure previous thread is completed before starting a new one

        self.album_loading_thread = threading.Thread(target=self.load_albums_thread)
        self.album_loading_thread.daemon = True  # Ensures the thread will close when the app is closed
        self.album_loading_thread.start()

    def load_albums_thread(self):
        loaded_files = Load_Files()
        self.albums = loaded_files.albums
        self.unique_artist = set(loaded_files.unique_artist)
        Settings.set_directory(loaded_files.asked_directory)
        self.after(0, self.update_ui_after_loading)  # Update UI after loading

    def update_ui_after_loading(self):
        """Update the UI after albums are loaded."""
        self.top_bar.clear_search_bar()
        self.is_loading = False  # Reset the loading flag
        if self.unique_artist:
            self.load_music_button.pack_forget()
            self.scrollable_canvas.pack(fill="both", expand=True, padx=(15, 0))
            self.display_artists(self.unique_artist)
        elif self.albums:
            self.load_music_button.pack_forget()
            self.scrollable_canvas.pack(fill="both", expand=True, padx=(15, 0))
            self.display_albums(self.albums)
        else:
            self.load_music_button.pack(expand=True)  # Redisplay button if no albums found

    def display_artists(self, setted_artists):
        """Populate the scrollable area with artist views."""
        buttons_per_row = 5
        padding = 12
        button_size = (self.parent_size // buttons_per_row) - padding * 3
        max_text_lines = 3
        line_height = 20
        button_height_with_text = button_size + (line_height * max_text_lines)

        for i, artist in enumerate(setted_artists):
            row, col = divmod(i, buttons_per_row)
            artist_view = Artist_View(self.scrollable_holder, artist, self.albums, button_size, self.show_albums_from_artist_view)
            artist_view.set_artist_view()
            artist_view.grid(row=row, column=col, padx=padding, pady=padding)

        total_rows = -(-len(setted_artists) // buttons_per_row)  # Ceiling division
        total_height = (total_rows * button_height_with_text + (total_rows - 1) * (padding*3))
        self.scrollable_canvas.config(scrollregion=(0, 0, 0, total_height))

    def display_albums(self, setted_albums):
        """Populate the scrollable area with album views."""
        buttons_per_row = 5
        padding = 12
        button_size = (self.parent_size // buttons_per_row) - padding * 3
        max_text_lines = 3
        line_height = 20
        button_height_with_text = button_size + (line_height * max_text_lines)

        for i, album in enumerate(setted_albums):
            row, col = divmod(i, buttons_per_row)
            album_view = Album_View(self.scrollable_holder, album, button_size, self.show_album_details)
            album_view.set_album_view()
            album_view.grid(row=row, column=col, padx=padding, pady=padding)

        total_rows = -(-len(setted_albums) // buttons_per_row)  # Ceiling division
        total_height = (total_rows * button_height_with_text + (total_rows - 1) * (padding*3))
        self.scrollable_canvas.config(scrollregion=(0, 0, 0, total_height))

    def show_albums_from_artist_view(self, albums):
        self.artist_albums_selected = albums
        self.display_albums(self.artist_albums_selected)
        self.top_bar.set_back_button(back_callback=lambda: self.return_albums_from_artist_view())
    
    def return_albums_from_artist_view(self):
        self.artist_albums_selected = None
        self.top_bar.unset_back_button()
        self.display_artists(self.unique_artist)

    def show_album_details(self, album):
        """Display the detailed view of a selected album."""
        self.top_bar.clear_search_bar()
        self.scrollable_canvas.pack_forget()
        self.data_from_album = Data_Album_View(self, album)
        self.data_from_album.set_data_album_view()

        self.top_bar.set_album_name(album)
        self.top_bar.set_back_button(back_callback=lambda: self.return_to_album_list())

    def return_to_album_list(self):
        """Return to the album list view from the album details view."""
        self.top_bar.clear_search_bar()
        if self.data_from_album:
            self.data_from_album.destroy()
            self.data_from_album = None

        self.scrollable_canvas.pack(fill="both", expand=True, padx=(15, 0))
        self.top_bar.unset_back_button()
        self.top_bar.set_back_button(back_callback=lambda: self.return_albums_from_artist_view())

    def set_view_album(self):
        """Initialize the album view."""
        if Settings.check_directory():
            loaded_files = Load_Files(ask_directory=Settings.get_directory())
            self.albums = loaded_files.albums
            self.unique_artist = set(loaded_files.unique_artist)
            self.scrollable_canvas.pack(fill="both", expand=True, padx=(15, 0))

            if Filter_Settings.get_filter() == "by Artists":
                self.display_artists(self.unique_artist)
            elif Filter_Settings.get_filter() == "by Albums":
                self.display_albums(self.albums)
        else:
            self.load_music_button.pack(expand=True)

    def clear_resources(self):
        """Clear unnecessary resources when transitioning away from the album view."""
        self.albums = []
        self.unique_artist = []
        self.scrollable_canvas.pack_forget()

    def get_all_albums(self):
        """Returns the list of all loaded albums."""
        return self.albums
