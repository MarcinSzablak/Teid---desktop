import tkinter as tk
from tkinter import ttk
from tkinter import font

class Titlebar_Tabs(tk.Frame):
    def __init__(self,parent,change_to_details,change_to_library,change_to_disk):
        super().__init__(parent,background="#1A1A1A",width=350)    
        self.details=tk.Button(self,text="Details")
        self.library=tk.Button(self,text="Library")
        self.disk=tk.Button(self,text="Disk")

        self.config(pady=12)

        self.change_to_details = change_to_details
        self.change_to_library = change_to_library
        self.change_to_disk = change_to_disk

        for button in (self.details, self.library, self.disk):
            button.config(background="#1A1A1A",
                          foreground="#FFFFFF",
                          highlightbackground="#1A1A1A",
                          bd=0,
                          relief="flat",
                          font=font.Font(family="Arial",size=12))
            button.bind("<Enter>", lambda e, btn=button: self.on_enter(btn))
            button.bind("<Leave>", lambda e, btn=button: self.on_leave(btn))

    def set_menu_buttons(self):
        self.pack()
        self.details.config(command=lambda:self.change_to_details())
        self.library.config(command=lambda:self.change_to_library())
        self.disk.config(command=lambda:self.change_to_disk())
        self.details.pack(side=tk.LEFT,padx=10,pady=3)
        self.library.pack(side=tk.LEFT,padx=10,pady=3)
        self.disk.pack(side=tk.LEFT,padx=10,pady=3)

    def on_enter(self,button):
        button.config(activebackground='#4B65A9',activeforeground="#FFFFFF")
    def on_leave(self,button):
        button.config(background="#1A1A1A")