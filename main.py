import tkinter as tk
from tkinter import ttk
import pygame

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

        self.frame_top = tk.Frame(self, background="white")
        self.frame_bottom = tk.Frame(self, background="red")
        self.frame_left = tk.Frame(self, background="yellow")
        self.frame_right = tk.Frame(self, background="blue")

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