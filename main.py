import tkinter as tk
from tkinter import ttk
import pygame

pygame.mixer.init()
sound = pygame.mixer.Sound('Rogue-Dreams.mp3')
sound.play()

root = tk.Tk()
root.title("My Tkinter App")
root.geometry("1280x720")
root.minsize(960, 506)

label3 = tk.Label(root, text="Hello, World!", background="white")
label3.pack(side="top",fill="both")

label = tk.Label(root, text="Hello, World!", background="red")
label.pack(side="bottom",fill="both")

label2 = tk.Label(root, text="Hello, World!", background="yellow")
label2.pack(side="left",expand=True,fill="both")

label4 = tk.Label(root, text="Hello, World!", background="blue")
label4.pack(side="left",expand=True,fill="both")

root.mainloop()
