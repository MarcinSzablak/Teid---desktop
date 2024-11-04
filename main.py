import tkinter as tk
from tkinter import ttk
import pygame
from ctypes import *
import platform

from components.top_bar_tabs import Top_Bar_Tabs

pygame.mixer.init()
sound = pygame.mixer.Sound('assets/Rogue-Dreams.mp3')
sound.set_volume(0.2)
sound.play()

class Main_Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Teid")
        self.geometry("1280x720")
        self.minsize(960, 506)
        if platform.system() == "Windows":
            self.update()
            DWMWA_USE_IMMERSIVE_DARK_MODE = 20
            set_window_attribute = windll.dwmapi.DwmSetWindowAttribute
            get_parent = windll.user32.GetParent
            hwnd = get_parent(self.winfo_id())
            rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
            value = 2
            value = c_int(value)
            set_window_attribute(hwnd, rendering_policy, byref(value),
                                sizeof(value))

        self.frame_top = tk.Frame(self, background="#1A1A1A")
        self.frame_bottom = tk.Frame(self, background="#1A1A1A")
        self.frame_left = tk.Frame(self, background="#252525")
        self.frame_right = tk.Frame(self, background="#111111")

        self.top_menu=Top_Bar_Tabs(self.frame_top)
        self.top_menu.set_menu_buttons()
        self.top_menu.bind("<Configure>", lambda e: self.top_menu.set_center_top_menu(self.frame_top.winfo_height))

    def set_frame_expands(self):
        total_height = self.winfo_height()
        total_width = self.winfo_width()
        top_height = int(total_height * 0.08)
        bottom_height = int(total_height * 0.10)
        left_width = int(total_width * 0.8)
        right_width = int(total_width * 0.21)

        self.frame_top.config(height=top_height)
        self.frame_bottom.config(height=bottom_height)
        self.frame_left.config(width=left_width)
        self.frame_right.config(width=right_width)
    
    def set_widgets(self):
        
        self.frame_top.pack(side="top", fill="x")
        self.frame_bottom.pack(side="bottom", fill="x")
        self.frame_left.pack(side="left", fill="y")
        self.frame_right.pack(side="left", fill="y")
    
    def start_app(self):
        self.bind("<Configure>", lambda e: self.set_frame_expands())
        self.set_frame_expands()
        self.set_widgets()
        self.mainloop()

if __name__=="__main__":
    app = Main_Window()
    app.start_app()