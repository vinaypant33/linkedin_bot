import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

from threading import Thread


#Libraries for the ustom title bar : 
import ctypes


def set_dark_titlebar(window):
    try:
        window.update_idletasks()
        hwnd  = ctypes.windll.user32.GetParent(window.winfo_id())
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, DWMWA_USE_IMMERSIVE_DARK_MODE, ctypes.byref(ctypes.c_int(1)), ctypes.sizeof(ctypes.c_int(1)))
    except Exception as Error:
        print(f"Error for changing the dark mode {Error}")


class Dashboard(ctk.CTk , Thread):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        self.title("Linkedin Bot")
        self.configure(fg_color= "#181818")
        self.resizable( 0 , 0)

        self.height  = 400
        self.width  = 700

        screen_width  = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_locaiton  = (screen_width // 2) - (self.width // 2 )
        y_location = (screen_height // 2) - (self.height // 2)


        self.geometry(f"{self.width}x{self.height}+{x_locaiton}+{y_location}")
        # set_dark_titlebar(self)

        self._set_appearance_mode("dark")
       

        ### The Titlebar of the applicaiton is to be changed to black as same as the application color : This only works in windows : 




        self.mainloop()





if __name__ == '__main__':
    Dashboard()
    # pass