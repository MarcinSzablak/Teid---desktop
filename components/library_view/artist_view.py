import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import eyed3  # type: ignore
import io

class Artist_View(tk.Frame):
    def __init__(self,parent,artist,albums,size,show_albums_from_artist_view):
        super().__init__(parent, bg="#222222")
        self.artist = artist
        self.albums = albums
        self.size = size
        self.albums_from_artist = []
        self.sliced_albums_from_artist= []
        if size <= 0:
            self.size = 100  # Default size if invalid
        else:
            self.size = size

        self.artist_images_holder = tk.Frame(self,width=self.size, height=self.size, bg="#1A1A1A")
        for album in albums:
            if album.band == artist:
                self.albums_from_artist.append(album)

        self.limited_albums_from_artist = self.albums_from_artist[:4]

        match len(self.limited_albums_from_artist):
            case 1:
                cover_artist1 = self.set_images_in_places(self.limited_albums_from_artist[0], (int(self.size), int(self.size)))
                cover_artist1.pack()
            case 2:
                covers_size = int(self.size / 2)
                cover_artist1 = self.set_images_in_places(self.limited_albums_from_artist[0], (int(covers_size), int(self.size)))
                cover_artist2 = self.set_images_in_places(self.limited_albums_from_artist[1], (int(covers_size), int(self.size)))
                cover_artist1.pack(side='left')
                cover_artist2.pack(side='left')
            case 3:
                covers_size = int(self.size / 2)
                cover_artist1 = self.set_images_in_places(self.limited_albums_from_artist[0], (int(covers_size), int(covers_size)))
                cover_artist2 = self.set_images_in_places(self.limited_albums_from_artist[1], (int(covers_size), int(covers_size)))
                cover_artist3 = self.set_images_in_places(self.limited_albums_from_artist[2], (int(self.size), int(covers_size)))
                cover_artist1.grid(row=0, column=0)
                cover_artist2.grid(row=0, column=1)
                cover_artist3.grid(row=1, column=0, columnspan=2)
            case 4:
                covers_size = int(self.size / 2)
                cover_artist1 = self.set_images_in_places(self.limited_albums_from_artist[0], (int(covers_size), int(covers_size)))
                cover_artist2 = self.set_images_in_places(self.limited_albums_from_artist[1], (int(covers_size), int(covers_size)))
                cover_artist3 = self.set_images_in_places(self.limited_albums_from_artist[2], (int(covers_size), int(covers_size)))
                cover_artist4 = self.set_images_in_places(self.limited_albums_from_artist[3], (int(covers_size), int(covers_size)))
                cover_artist1.grid(row=0, column=0)
                cover_artist2.grid(row=0, column=1)
                cover_artist3.grid(row=1, column=0)
                cover_artist4.grid(row=1, column=1)
            case _:
                cover_artist1 = self.set_images_in_places(self.limited_albums_from_artist[0], (int(self.size), int(self.size)))
                cover_artist1.pack()

        self.artist_name = tk.Label(self, text=self.artist, justify="center")
        self.artist_name.config(font=font.Font(family="Arial", size=12),
                               wraplength=self.size,
                               bg="#222222", fg="white")
        
        self.artist_name.bind("<Button-1>", lambda e: show_albums_from_artist_view(self.albums_from_artist))

    

    def set_images_in_places(self,album,covers_size):
        '''Set sizes of album from artist'''
        cover_image = self.load_cover_image(album)
        cover_image = cover_image.resize(covers_size)
        cover_photo = ImageTk.PhotoImage(cover_image)
        image_holder = tk.Label(self.artist_images_holder,image=cover_photo, bd=0, relief="flat",
                                      highlightbackground="#222222",
                                      background="#1A1A1A", activebackground="#1A1A1A")
        image_holder.image_names = cover_photo
        return image_holder
    
    def load_cover_image(self,album):
        """Load cover image, use default if invalid or missing."""
        if not album.cover:
            # Use a default image if no cover is found
            try:
                cover_image = Image.open("assets/defaultcover.png")
            except FileNotFoundError:
                # If default image doesn't exist, create a simple placeholder
                cover_image = Image.new('RGB', (self.size, self.size), color='#CCCCCC')
        else:
            try:
                cover_image = Image.open(album.cover)
            except (FileNotFoundError, IOError):
                # If the cover image is invalid, use the default image
                cover_image = Image.open("assets/defaultcover.png")
        return cover_image

    def set_artist_view(self):
        self.artist_images_holder.pack(pady=5)
        self.artist_name.pack()