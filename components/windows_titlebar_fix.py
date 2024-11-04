from ctypes import *

class Windows_Titlebar_fix:
    def __init__(self,root):
        root.update()
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        set_window_attribute = windll.dwmapi.DwmSetWindowAttribute # type: ignore
        get_parent = windll.user32.GetParent # type: ignore
        hwnd = get_parent(root.winfo_id())
        rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
        value = 2
        value = c_int(value)
        set_window_attribute(hwnd, rendering_policy, byref(value),
                            sizeof(value))