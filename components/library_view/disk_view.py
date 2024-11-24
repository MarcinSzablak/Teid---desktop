import tkinter as tk
from PIL import Image, ImageDraw, ImageTk

class Disk_View(tk.Frame):
    def __init__(self, parent, album):
        super().__init__(parent, bd=0, relief="flat", padx=0, pady=0)
        self.angle = 0
        self.speed = 1  # Reduced speed for slower rotation
        self.move = False  # Rotation initially stopped

        # Open and process the album cover image
        self.original_image = None
        try:
            self.original_image = Image.open(album.cover)
        except:
            self.original_image = Image.open("assets/basedvd.png")
        self.dvd_image = self.create_dvd_image(self.original_image)

        # Create canvas to display image
        self.canvas = tk.Canvas(self, bg="#222222", bd=0, relief="flat", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Bind resize event to handle canvas resizing
        self.canvas.bind("<Configure>", self.on_resize)

        self.image = None
        self.image_id = None

        # Start the rotation in the main thread using after() but rotation is initially stopped
        self.after(50, self.rotate_image)

    def create_dvd_image(self, image):
        """Create a circular image with a hole in the center."""
        size = min(image.width, image.height)
        image = image.resize((size, size))

        # Create a circular mask for the image
        mask = Image.new("L", (size, size), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, size, size), fill=255)

        # Apply the mask to create a circular image
        circular_image = Image.new("RGBA", (size, size))
        circular_image.paste(image, (0, 0), mask)

        # Draw the hole in the center of the disk
        hole_radius = size // 15
        center_x, center_y = size // 2, size // 2
        draw = ImageDraw.Draw(circular_image)

        colored_hole_radius = hole_radius + 15
        draw.ellipse(
            (center_x - colored_hole_radius, center_y - colored_hole_radius, 
             center_x + colored_hole_radius, center_y + colored_hole_radius),
            fill="#D8E3E7"
        )

        # Transparent hole in the middle
        draw.ellipse(
            (center_x - hole_radius, center_y - hole_radius, 
             center_x + hole_radius, center_y + hole_radius),
            fill=(0, 0, 0, 0)
        )

        return circular_image

    def rotate_image(self):
        """Rotate the disk image."""
        if self.move:  # Check if rotation is enabled
            self.angle = (self.angle + self.speed) % 360
            rotated_image = self.dvd_image.rotate(self.angle, expand=True)

            # Crop the left half of the rotated image
            left_half = rotated_image.crop((0, 0, rotated_image.width // 2, rotated_image.height))

            # Convert the image for tkinter display
            self.image = ImageTk.PhotoImage(left_half)
        else:
            # When stopped, show only the left half of the original (non-rotated) image
            left_half = self.dvd_image.crop((0, 0, self.dvd_image.width // 2, self.dvd_image.height))
            self.image = ImageTk.PhotoImage(left_half)

        # Update the canvas with the current image (whether rotating or static)
        self.update_image()

        # Continue checking for rotation (loop every 50ms)
        self.after(50, self.rotate_image)

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
        
        # Resize the image to fit the new canvas size, maintaining aspect ratio
        self.dvd_image = self.dvd_image.resize((dvd_size, dvd_size))

        # Update image
        self.image = ImageTk.PhotoImage(self.dvd_image)
        
        if self.image_id:
            self.canvas.itemconfig(self.image_id, image=self.image)
        else:
            self.image_id = self.canvas.create_image(new_width, new_height // 2, image=self.image, anchor="e")

        self.canvas.coords(self.image_id, new_width, new_height // 2)

    def set_disk_view(self):
        """Add the frame to the parent."""
        self.pack(side="right", fill=tk.BOTH, expand=True)

    def start_rotation(self):
        """Start the rotation of the disk."""
        self.move = True

    def stop_rotation(self):
        """Stop the rotation of the disk."""
        self.move = False
