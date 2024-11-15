import tkinter as tk
from tkinter import ttk

class Data_List_Song_Album(tk.Frame):
    def __init__(self, parent, album):
        super().__init__(parent)
        self.album = album
        
        self.song_list = ttk.Treeview(self, columns=("name", "duration", "number"), show="headings")
        
        self.style = ttk.Style(self)
    
        self.style.configure("Custom.Treeview",
                             background="#222222",
                             foreground="#FFFFFF",
                             fieldbackground="#222222",
                             borderwidth=0,
                             relief="flat",
                             font=("Arial", 12))

        self.style.configure("Custom.Treeview.Heading",
                             background="#222222",
                             foreground="#FFFFFF",
                             font=("Arial", 12),
                             padding=(5, 5))

        self.style.map("Custom.Treeview.Heading",
                       background=[('active', '#222222')],
                       foreground=[('active', '#FFFFFF')])

        self.style.map("Custom.Treeview",
                       background=[('selected', '#222222')],
                       foreground=[('selected', '#FFFFFF')])

        self.song_list.configure(style="Custom.Treeview")
        
        self.song_list.heading("#0", text="", anchor=tk.W) 

        self.song_list.column("name", width=250, anchor=tk.W)
        self.song_list.column("duration", width=100, anchor=tk.W)
        self.song_list.column("number", width=50, anchor=tk.W)

        self.song_list.heading("name", text="Track Name", anchor=tk.W)
        self.song_list.heading("duration", text="Duration", anchor=tk.W)
        self.song_list.heading("number", text="Number", anchor=tk.W)

        self.album.songs_data_list.sort(key=lambda song: song['number'])

        for song in self.album.songs_data_list:
            self.song_list.insert("", tk.END, values=(song['title'], song['duration'], song['number']))

        self.song_list.bind("<ButtonRelease-1>", lambda e: self.select_music())

        self.style.configure("Custom.Treeview", rowheight=30)

    def select_music(self):
        selected_item = self.song_list.focus()

        item_values = self.song_list.item(selected_item)['values']
        
        print(f"Clicked item ID: {selected_item}")
        print(f"Item values: {item_values}")

        if item_values:
            for song in self.album.songs_data_list:
                if song["title"] == item_values[0]:
                    print(song["url"])

    def set_data_list_song_album(self):

        self.pack(expand=True, fill="both", padx=15, pady=(0, 15), side="bottom")
        self.song_list.pack(expand=True, fill="both")

