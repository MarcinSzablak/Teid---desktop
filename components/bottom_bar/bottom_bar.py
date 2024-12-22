import tkinter as tk
from tkinter import ttk
from .left_bottom_side import Left_Bottom_Side
from .center_bottom_side import Center_Bottom_Side
from .right_bottom_side import Right_Bottom_Side
from ..music_operator.music_operator import Music_Operator

class Bottom_Bar(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)

        self.left_bottom_side = Left_Bottom_Side(self)
        self.center_bottom_side = Center_Bottom_Side(self)
        self.right_bottom_side = Right_Bottom_Side(self)

        self.left_bottom_side.set_left_bottom_bar()
        self.center_bottom_side.set_center_bottom_side()

        Music_Operator.add_observer(self.center_bottom_side.change_pause_play_button_clicked_in_list)


    def set_bottom_bar(self):
        self.pack(fill="x",pady=10)
        self.grid_columnconfigure((0,1,2), weight=1, uniform="equal")
        self.left_bottom_side.grid(column=0,row=0)
        self.center_bottom_side.grid(column=1,row=0)
        self.right_bottom_side.grid(column=2,row=0)