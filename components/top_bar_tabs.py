import tkinter as tk
from tkinter import ttk

class Top_Bar_Tabs(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent,background="purple",width=350,height=50)    
        self.details=tk.Button(self,text="Details")
        self.library=tk.Button(self,text="Library")
        self.disk=tk.Button(self,text="Disk")

    def set_center_top_menu(self,parent_height):
        self.config(pady=(parent_height()*0.02))

    def set_menu_buttons(self):
        self.pack()
        self.details.pack(side=tk.LEFT,padx=10,pady=3)
        self.library.pack(side=tk.LEFT,padx=10,pady=3)
        self.disk.pack(side=tk.LEFT,padx=10,pady=3)
