import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import eyed3 # type: ignore
import mutagen # type: ignore
from mutagen.flac import FLAC # type: ignore
from mutagen.mp3 import MP3 # type: ignore
from tinytag import TinyTag # type: ignore
from PIL import Image, ImageTk
import io

class Album_View(tk.Frame):
    def __init__(self, parent, album, size, show_album_data):
        super().__init__(parent, bg="#222222")
        self.show_album_data = show_album_data
        self.album = album

        # Ensure size is valid (greater than 0)
        if size <= 0:
            self.size = 100  # Default size if invalid
        else:
            self.size = size  

        # Button to display cover image
        self.cover_button = tk.Button(self, text=self.album.album_name,
                                      width=self.size, height=self.size,
                                      bd=0, relief="flat",
                                      highlightbackground="#222222",
                                      background="#1A1A1A", activebackground="#1A1A1A")
        
        # Label to display album name
        self.album_name = tk.Label(self, text=self.album.album_name, justify="center")
        self.album_name.config(font=font.Font(family="Arial", size=12),
                               wraplength=self.size,
                               bg="#222222", fg="white")
        
        # Handle missing cover image by providing a default
        cover_image = self.load_cover_image()

        # Check the first song in the album and extract metadata if available
        self.extract_album_metadata()

        # Resize the image to the specified size
        cover_image = cover_image.resize((self.size, self.size))
        cover_photo = ImageTk.PhotoImage(cover_image)
        self.cover_button.config(image=cover_photo)
        self.cover_button.image = cover_photo

        # Bind the show album data action to the album view
        self.bind("<Button-1>", lambda e: self.show_album_data(self.album))
        self.cover_button.bind("<Button-1>", lambda e: self.show_album_data(self.album))
        self.album_name.bind("<Button-1>", lambda e: self.show_album_data(self.album))
    

    def load_cover_image(self):
        """Load cover image, use default if invalid or missing."""
        if not self.album.cover:
            # Use a default image if no cover is found
            try:
                cover_image = Image.open("assets/defaultcover.png")
            except FileNotFoundError:
                # If default image doesn't exist, create a simple placeholder
                cover_image = Image.new('RGB', (self.size, self.size), color='#CCCCCC')
        else:
            try:
                cover_image = Image.open(self.album.cover)
            except (FileNotFoundError, IOError):
                # If the cover image is invalid, use the default image
                cover_image = Image.open("assets/defaultcover.png")
        return cover_image

    def extract_album_metadata(self):
        """Update album metadata and cover art from the first song in the album's song list."""
        if not self.album.song_list:
            return
        audio_file_path = self.album.song_list[0]

        try:
            if audio_file_path.lower().endswith('.mp3'):
                audio_file = eyed3.load(audio_file_path)
                album_title = audio_file.tag.album if audio_file.tag else None
                band_name = audio_file.tag.artist if audio_file.tag else "None"
                cover_image = None
                if audio_file.tag:
                    for tag in audio_file.tag.frame_set:
                        frame = audio_file.tag.frame_set[tag][0]
                        if tag == b'APIC':
                            cover_image = Image.open(io.BytesIO(frame.image_data))

            elif audio_file_path.lower().endswith('.flac'):
                audio_file = FLAC(audio_file_path)
                album_title = audio_file.get('album', [None])[0]
                band_name = audio_file.get('artist', ['None'])[0]
                cover_image = None
                for tag in audio_file.tags.values():
                    if tag.FrameID == 'APIC':
                        cover_image = Image.open(io.BytesIO(tag.data))

            elif audio_file_path.lower().endswith('.ogg'):
                audio_file = mutagen.File(audio_file_path, easy=True)
                album_title = audio_file.get('album', None)
                band_name = audio_file.get('artist', 'None')
                cover_image = None
                if audio_file.pictures:
                    cover_image = Image.open(io.BytesIO(audio_file.pictures[0].data))

            elif audio_file_path.lower().endswith('.wav'):
                audio_file = TinyTag.get(audio_file_path)
                album_title = audio_file.title
                band_name = audio_file.artist
                cover_image = None

            else:
                album_title, band_name, cover_image = None, "None", None

            if album_title:
                self.album_name.config(text=album_title)

            self.album.band_name = band_name

            # Update cover image if available
            if cover_image:
                cover_image = cover_image.resize((self.size, self.size))
                cover_photo = ImageTk.PhotoImage(cover_image)
                self.cover_button.config(image=cover_photo)
                self.cover_button.image = cover_photo

        except Exception as e:
            pass

    def set_album_view(self):
        """Place the widgets (album cover and name) into the frame."""
        self.cover_button.pack(pady=5)
        self.album_name.pack()
