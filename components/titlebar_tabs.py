import tkinter as tk
from tkinter import font

class Titlebar_Tabs(tk.Frame):
    def __init__(self, parent, change_to_details, change_to_library, change_to_disk):
        super().__init__(parent, background="#1A1A1A", width=350)
        
        # Set padding for the frame
        self.config(pady=12)

        # Store tab change callback functions
        self.change_to_details = change_to_details
        self.change_to_library = change_to_library
        self.change_to_disk = change_to_disk

        # Create and configure buttons
        self.details = self.create_button("Details", self.change_to_details)
        self.library = self.create_button("Library", self.change_to_library)
        self.disk = self.create_button("Disk", self.change_to_disk)

    def create_button(self, text, command):
        """
        Helper method to create and configure a button with common properties.
        """
        button = tk.Button(self, text=text, command=command, font=font.Font(family="Arial", size=12))
        button.config(
            background="#1A1A1A",
            foreground="#FFFFFF",
            activebackground="#4B65A9",
            activeforeground="#FFFFFF",
            highlightbackground="#1A1A1A",
            bd=0,
            relief="flat"
        )
        button.bind("<Enter>", lambda e: button.config(background="#4B65A9"))
        button.bind("<Leave>", lambda e: button.config(background="#1A1A1A"))
        return button

    def set_menu_buttons(self):
        """
        Pack buttons into the title bar.
        """
        self.pack()
        for button in (self.details, self.library, self.disk):
            button.pack(side=tk.LEFT, padx=10, pady=3)
