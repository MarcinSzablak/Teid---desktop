import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
import io
import eyed3  # type: ignore

class Disk_View(tk.Frame):
    def __init__(self, parent, album):
        super().__init__(parent)
        self.angle = 0
        self.speed = 5
        self.move = False

        # Load cover image
        cover_image = album.cover
        audio_file = eyed3.load(album.song_list[0])
        if audio_file.tag:
            for tag in audio_file.tag.frame_set:
                frame = audio_file.tag.frame_set[tag][0]
                if tag == b'APIC':
                    image_data = frame.image_data
                    cover_image = io.BytesIO(image_data)

        self.original_image = Image.open(cover_image)
        self.dvd_image = self.create_dvd_image(self.original_image)

        # Create background image
        self.background_image = Image.open("assets/basedvd.png")
        self.background_image = self.create_background_image(self.background_image)

        # Initialize canvas with a fixed size for the canvas
        self.canvas = tk.Canvas(self, bg="#4287f5")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Bind resize event to handle resizing images
        self.canvas.bind("<Configure>", self.on_resize)

        # Variables for storing image references
        self.image = None
        self.image_background = None
        self.image_id = None
        self.background_image_id = None

        # Initialize rotation (after the canvas is ready)
        self.rotate_image()

    def create_dvd_image(self, image):
        size = min(image.width, image.height)
        image = image.resize((size, size))

        mask = Image.new("L", (size, size), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, size, size), fill=255)

        circular_image = Image.new("RGBA", (size, size))
        circular_image.paste(image, (0, 0), mask)

        draw = ImageDraw.Draw(circular_image)
        inner_circle_radius = size // 10
        center_x, center_y = size // 2, size // 2
        draw.ellipse(
            (center_x - inner_circle_radius, center_y - inner_circle_radius,
             center_x + inner_circle_radius, center_y + inner_circle_radius),
            fill=(0, 0, 0, 0)
        )

        return circular_image

    def create_background_image(self, image):
        size = min(self.dvd_image.width, self.dvd_image.height)
        new_size = int(size * 0.8)
        image = image.resize((new_size, new_size))
        return image

    def rotate_image(self):
        self.angle = (self.angle + self.speed) % 360
        rotated_image = self.dvd_image.rotate(self.angle, expand=True)
        self.image = ImageTk.PhotoImage(rotated_image)

        if self.image_id:
            self.canvas.itemconfig(self.image_id, image=self.image)

        # Call rotate_image every 25ms
        self.after(25, self.rotate_image)

    def on_resize(self, event):
        new_width, new_height = event.width, event.height

        # Resize DVD image to maintain aspect ratio
        dvd_size = min(new_width, new_height) # DVD image should take half of the smallest dimension
        self.dvd_image = self.create_dvd_image(self.original_image)
        self.dvd_image = self.dvd_image.resize((dvd_size, dvd_size))

        # Resize background image to fit proportionally
        self.background_image = self.create_background_image(self.background_image)
        self.background_image = self.background_image.resize((new_width, new_height))

        # Update image references
        self.image = ImageTk.PhotoImage(self.dvd_image)
        self.image_background = ImageTk.PhotoImage(self.background_image)

        # If image ID hasn't been created, create it now
        if not self.image_id:
            self.background_image_id = self.canvas.create_image(new_width // 2, new_height // 2, image=self.image_background)
            self.image_id = self.canvas.create_image(new_width // 2, new_height // 2, image=self.image)
        else:
            # If images already exist, just update them
            self.canvas.itemconfig(self.image_id, image=self.image)
            self.canvas.itemconfig(self.background_image_id, image=self.image_background)

        # Center the DVD image after resizing
        self.canvas.coords(self.image_id, new_width // 2, new_height // 2)
        self.canvas.coords(self.background_image_id, new_width // 2, new_height // 2)

    def set_disk_view(self):
        self.pack(side="right", fill=tk.BOTH, expand=True)
