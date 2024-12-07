import tkinter as tk
from tkinter import ttk
import platform

from components.windows_titlebar_fix import Windows_Titlebar_fix
from components.titlebar_tabs import Titlebar_Tabs
from components.main_content.tabs_views import Tabs_Views
from components.bottom_bar.bottom_bar import Bottom_Bar


class Main_Window(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Configure the main window
        self.title("Teid")
        self.geometry("1280x720")
        self.minsize(960, 506)
        self.config(background="#222222")
        
        # Apply Windows-specific title bar fix
        if platform.system() == "Windows":
            Windows_Titlebar_fix(self)
        
        # Initialize frames
        self.frame_top = tk.Frame(self, background="#1A1A1A", height=60)
        self.frame_bottom = tk.Frame(self, background="#1A1A1A")
        self.frame_left = tk.Frame(self, background="#252525")
        self.frame_right = tk.Frame(self, background="#111111")
        
        # Initialize custom components
        self.tabs_views = Tabs_Views(self.frame_left)
        self.titlebar_menu = Titlebar_Tabs(
            self.frame_top,
            self.tabs_views.change_to_details,
            self.tabs_views.change_to_library,
            self.tabs_views.change_to_disk,
        )
        self.bottom_bar = Bottom_Bar(self.frame_bottom)

        # Precompute layout ratios to avoid recalculating on every resize
        self.bottom_ratio = 0.13
        self.left_ratio = 0.8
        self.right_ratio = 0.21

    def set_frame_expands(self, event=None):
        """
        Dynamically adjusts the size of frames based on the window dimensions.
        """
        total_height = self.winfo_height()
        total_width = self.winfo_width()
        
        # Adjust frame dimensions
        self.frame_bottom.config(height=int(total_height * self.bottom_ratio))
        self.frame_left.config(width=int(total_width * self.left_ratio))
        self.frame_right.config(width=int(total_width * self.right_ratio))

    def set_widgets(self):
        """
        Pack the widgets into the main window and initialize subcomponents.
        """
        # Pack frames
        self.frame_top.pack(side="top", fill="x")
        self.frame_bottom.pack(side="bottom", fill="x")
        self.frame_left.pack(side="left", fill="y")
        self.frame_right.pack(side="left", fill="y")

        # Initialize custom component widgets
        self.titlebar_menu.set_menu_buttons()
        self.tabs_views.set_tabs()
        self.bottom_bar.set_bottom_bar()

    def start_app(self):
        """
        Starts the application and sets up dynamic resizing.
        """
        self.bind("<Configure>", self.set_frame_expands)  # Efficient event handling
        self.set_frame_expands()  # Set initial frame sizes
        self.set_widgets()  # Initialize and place widgets
        self.mainloop()


if __name__ == "__main__":
    app = Main_Window()
    app.start_app()
