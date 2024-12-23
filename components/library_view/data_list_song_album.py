import tkinter as tk
from tkinter import ttk
from ..music_operator.music_operator import Music_Operator

class Data_List_Song_Album(tk.Frame):
    def __init__(self, parent, album):
        super().__init__(parent)
        self.album = album

        # Create the style for the Treeview widget
        self.style = ttk.Style(self)

        # Set the theme to 'clam' to allow custom styles to apply
        self.style.theme_use("clam")  # Ensure 'clam' theme is set to apply custom styles

        # Set background color and text color for the entire Treeview
        self.style.configure("Custom.Treeview",
                             background="#222222",  # Background color of the Treeview
                             foreground="#FFFFFF",  # Text color of the Treeview
                             fieldbackground="#222222",  # Background of the fields in Treeview
                             borderwidth=0,  # Set borderwidth to 0 to remove border
                             relief="flat",  # Set relief to flat to remove any raised effect
                             font=("Arial", 12),
                             highlightthickness=0,  # Remove the focus border
                             bd=0)  # Remove any border around the widget

        # Set style for the headers of the Treeview
        self.style.configure("Custom.Treeview.Heading",
                             background="#222222",  # Background color of the header
                             foreground="#FFFFFF",  # Text color of the header
                             font=("Arial", 12),
                             padding=(5, 5))

        # Update the header style when it's active
        self.style.map("Custom.Treeview.Heading",
                       background=[('active', '#222222')],  # Active header background
                       foreground=[('active', '#FFFFFF')])  # Active header text color

        # Create Treeview widget with columns
        self.song_list = ttk.Treeview(self, columns=("name", "duration", "number"), show="headings", style="Custom.Treeview")

        # Define column properties
        self.song_list.heading("#0", text="", anchor=tk.W)
        self.song_list.column("name", width=250, anchor=tk.W)
        self.song_list.column("duration", width=100, anchor=tk.W)
        self.song_list.column("number", width=50, anchor=tk.W)

        # Column headers
        self.song_list.heading("name", text="Track Name", anchor=tk.W)
        self.song_list.heading("duration", text="Duration", anchor=tk.W)
        self.song_list.heading("number", text="Number", anchor=tk.W)

        # Sort the songs by their number safely, handling None values
        self.album.songs_data_list.sort(key=lambda song: song['number'] if song['number'] is not None else float('inf'))

        # Insert songs into the Treeview
        for index, song in enumerate(self.album.songs_data_list):
            # Insert with a unique ID for each item (use index or a unique string)
            item_id = f"song_{index}"
            self.song_list.insert("", tk.END, item_id, values=(song['title'], song['duration'], song['number']))

        self.song_list.bind("<ButtonRelease-1>", lambda e: self.select_music())

        # Set row height for the Treeview
        self.style.configure("Custom.Treeview", rowheight=30)

        # Pack the Treeview widget into the frame
        self.song_list.pack(expand=True, fill="both")

        Music_Operator.add_observer(self.skip_to_song)

    def select_music(self):
        selected_item = self.song_list.focus()
        item_values = self.song_list.item(selected_item)['values']

        if item_values:
            for song in self.album.songs_data_list:
                if song["title"] == item_values[0]:
                    Music_Operator.source = song["url"]
                    Music_Operator.play_music()
                    Music_Operator.album=self.album
                    Music_Operator.notify_observers(True)

    def skip_to_song(self,value):
        Music_Operator.get_song_index()
        if(Music_Operator.song_index is not None):
            self.after(100, self.select_song_at_index)
            
    def select_song_at_index(self):
        try:
            item_id = f"song_{Music_Operator.song_index}"
            if item_id in self.song_list.get_children():
                self.song_list.selection_set(item_id)
        except:
            pass

    def set_data_list_song_album(self):
        self.pack(expand=True, fill="both", padx=15, pady=(0, 15), side="bottom")
        self.song_list.pack(expand=True, fill="both")
