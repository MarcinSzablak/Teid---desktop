import tkinter as tk
from PIL import Image, ImageDraw, ImageTk

class Disk_View(tk.Frame):
    def __init__(self, parent, album):
        super().__init__(parent, bd=0, relief="flat", padx=0, pady=0)
        self.angle = 0
        self.speed = 1
        self.move = False

        self.original_image = None
        try:
            self.original_image = Image.open(album.cover)
        except:
            self.original_image = Image.open("assets/basedvd.png")
        self.dvd_image = self.create_dvd_image(self.original_image)

        self.canvas = tk.Canvas(self, bg="#222222", bd=0, relief="flat", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<Configure>", self.on_resize)

        self.image = None
        self.image_id = None

        self.after(50, self.rotate_image)

    def create_dvd_image(self, image):
        """Create a circular image with a hole in the center."""
        size = min(image.width, image.height)
        image = image.resize((size, size))

        mask = Image.new("L", (size, size), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, size, size), fill=255)

        circular_image = Image.new("RGBA", (size, size))
        circular_image.paste(image, (0, 0), mask)

        hole_radius = size // 15
        center_x, center_y = size // 2, size // 2
        draw = ImageDraw.Draw(circular_image)

        colored_hole_radius = hole_radius + 15
        draw.ellipse(
            (center_x - colored_hole_radius, center_y - colored_hole_radius, 
             center_x + colored_hole_radius, center_y + colored_hole_radius),
            fill="#D8E3E7"
        )

        draw.ellipse(
            (center_x - hole_radius, center_y - hole_radius, 
             center_x + hole_radius, center_y + hole_radius),
            fill=(0, 0, 0, 0)
        )

        border_thickness = 3
        draw.ellipse(
            (center_x - size // 2, center_y - size // 2, 
            center_x + size // 2, center_y + size // 2),
            outline="#D8E3E7", width=border_thickness
        )

        return circular_image

    def rotate_image(self):
        """Rotate the disk image."""
        if self.move:
            self.angle = (self.angle + self.speed) % 360
            rotated_image = self.dvd_image.rotate(self.angle, expand=True)

            left_half = rotated_image.crop((0, 0, rotated_image.width // 2, rotated_image.height))

            self.image = ImageTk.PhotoImage(left_half)
        else:
            self.angle = self.angle % 360
            rotated_image = self.dvd_image.rotate(self.angle, expand=True)

            left_half = rotated_image.crop((0, 0, rotated_image.width // 2, rotated_image.height))

            self.image = ImageTk.PhotoImage(left_half)

        self.update_image()

        self.after(10, self.rotate_image)

    def update_image(self):
        """Update the canvas with the current image in the main thread."""
        if self.image_id:
            self.canvas.itemconfig(self.image_id, image=self.image)
        else:
            self.image_id = self.canvas.create_image(self.canvas.winfo_width(),
                                                     self.canvas.winfo_height() // 2, image=self.image, anchor="e")

    def on_resize(self, event):
        """Handle resizing of the canvas and adjust the image size accordingly."""
        new_width, new_height = event.width, event.height
        dvd_size = min(new_width, new_height)
        
        self.dvd_image = self.dvd_image.resize((dvd_size, dvd_size))

        self.image = ImageTk.PhotoImage(self.dvd_image)
        
        if self.image_id:
            self.canvas.itemconfig(self.image_id, image=self.image)
        else:
            self.image_id = self.canvas.create_image(new_width, new_height // 2, image=self.image, anchor="e")

        self.canvas.coords(self.image_id, new_width, new_height // 2)

    def set_disk_view(self):
        """Add the frame to the parent."""
        self.pack(side="right", fill=tk.BOTH, expand=True)

    def move_rotation(self,move):
        """Start the rotation of the disk."""
        self.move = move

