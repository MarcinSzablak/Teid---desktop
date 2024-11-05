import tkinter as tk
from tkinter import ttk
import pygame
import platform

from components.windows_titlebar_fix import Windows_Titlebar_fix
from components.titlebar_tabs import Titlebar_Tabs
from components.main_content.tabs_views import Tabs_Views
from components.main_content.top_bar import Top_Bar

# pygame.mixer.init()
# sound = pygame.mixer.Sound('assets/Rogue-Dreams.mp3')
# sound.set_volume(0.2)
# sound.play()

class Main_Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Teid")
        self.geometry("1280x720")
        self.minsize(960, 506)
        if platform.system() == "Windows":
            Windows_Titlebar_fix(self)

        self.frame_top = tk.Frame(self, background="#1A1A1A")
        self.frame_bottom = tk.Frame(self, background="#1A1A1A")
        self.frame_left = tk.Frame(self, background="#252525")
        self.frame_right = tk.Frame(self, background="#111111")

        
        self.top_bar=Top_Bar(self.frame_left)
        self.tabs_views=Tabs_Views(self.frame_left)
        self.titlebar_menu=Titlebar_Tabs(self.frame_top,
                                   self.tabs_views.change_to_details,
                                   self.tabs_views.change_to_library,
                                   self.tabs_views.change_to_disk)

    def set_frame_expands(self):
        total_height = self.winfo_height()
        total_width = self.winfo_width()
        bottom_height = int(total_height * 0.10)
        left_width = int(total_width * 0.8)
        right_width = int(total_width * 0.21)

        self.frame_top.config(height=60)
        self.frame_bottom.config(height=bottom_height)
        self.frame_left.config(width=left_width)
        self.frame_right.config(width=right_width)
    
    def set_widgets(self):
        self.frame_top.pack(side="top", fill="x")
        self.frame_bottom.pack(side="bottom", fill="x")
        self.frame_left.pack(side="left", fill="y")
        self.frame_right.pack(side="left", fill="y")

        self.titlebar_menu.set_menu_buttons()
        self.top_bar.set_top_bar()
        self.tabs_views.set_tabs()
    
    def start_app(self):
        self.bind("<Configure>", lambda e: self.set_frame_expands())
        self.set_frame_expands()
        self.set_widgets()
        self.mainloop()

if __name__=="__main__":
    app = Main_Window()
    app.start_app()