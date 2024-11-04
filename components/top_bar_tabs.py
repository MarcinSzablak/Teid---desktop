import tkinter as tk
from tkinter import ttk

class Top_Bar_Tabs(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent,background="#1A1A1A",width=350,height=50)    
        self.details=tk.Button(self,text="Details")
        self.library=tk.Button(self,text="Library")
        self.disk=tk.Button(self,text="Disk")

        for button in (self.details, self.library, self.disk):
            button.config(background="#1A1A1A",
                          foreground="#FFFFFF",
                          highlightbackground="#1A1A1A",
                          bd=0)
            button.bind("<Enter>", lambda e, btn=button: self.on_enter(btn))
            button.bind("<Leave>", lambda e, btn=button: self.on_leave(btn))

    def set_center_top_menu(self,parent_height):
        self.config(pady=(parent_height()*0.20))

    def set_menu_buttons(self):
        self.pack()
        self.details.pack(side=tk.LEFT,padx=10,pady=3)
        self.library.pack(side=tk.LEFT,padx=10,pady=3)
        self.disk.pack(side=tk.LEFT,padx=10,pady=3)

    def on_enter(self,button):
        button.config(activebackground='#4B65A9',activeforeground="#FFFFFF")
    def on_leave(self,button):
        button.config(background="#1A1A1A")