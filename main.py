import tkinter as tk
from tkinter import ttk
import pygame

pygame.mixer.init()
sound = pygame.mixer.Sound('Rogue-Dreams.mp3')
sound.set_volume(0.2)
sound.play()

root = tk.Tk()
root.title("My Tkinter App")
root.geometry("1280x720")
root.minsize(960, 506)

frame_top = tk.Frame(root, background="white")
frame_top.pack(side="top", fill="x")

frame_bottom = tk.Frame(root, background="red")
frame_bottom.pack(side="bottom", fill="x")

frame_left = tk.Frame(root, background="yellow")
frame_left.pack(side="left", fill="y")

top_label = tk.Label(frame_left, text="lala", bg="brown")
top_label.pack(pady=10)

frame_right = tk.Frame(root, background="blue")
frame_right.pack(side="left", fill="y")

def set_frame_heights():
    total_height = root.winfo_height()
    total_width = root.winfo_width()
    top_height = int(total_height * 0.05)
    bottom_height = int(total_height * 0.10)
    left_width = int(total_width * 0.8)
    right_width = int(total_width * 0.21)

    frame_top.config(height=top_height)
    frame_bottom.config(height=bottom_height)
    frame_left.config(width=left_width)
    frame_right.config(width=right_width)


root.bind("<Configure>", lambda e: set_frame_heights())

set_frame_heights()

root.mainloop()
