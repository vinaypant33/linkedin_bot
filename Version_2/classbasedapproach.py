import ttkbootstrap as btk
from threading import Thread

import ctypes

import os


print(os.getcwd())

def set_dark_titlebar(window , mode_numeral = 1):
    try:
        window.update_idletasks()
        hwnd  = ctypes.windll.user32.GetParent(window.winfo_id())
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, DWMWA_USE_IMMERSIVE_DARK_MODE, ctypes.byref(ctypes.c_int(mode_numeral)), ctypes.sizeof(ctypes.c_int(1)))
    except Exception as Error:
        print(f"Error for changing the dark mode {Error}")





class Dashboard(btk.Window , Thread):

    def __init__(self, title="Linkedin Bot", themename="darkly", iconphoto='', size=None, position=None, minsize=None, maxsize=None, resizable=None, hdpi=True, scaling=None, transient=None, overrideredirect=False, alpha=1):
        super().__init__(title, themename, iconphoto, size, position, minsize, maxsize, resizable, hdpi, scaling, transient, overrideredirect, alpha)
        


        ## Configuring the windows : 
        self.configure(background="#202020")
        self.resizable(0 , 0)
        self.width  = 900
        self.height  = 600

        set_dark_titlebar(self , 1)
        
        print(themename)

        self.geometry(f"{self.width}x{self.height}")

        self.mainbuttin = Simple_button(self)
        self.mainbuttin.pack()


       
        
        self.mainloop()


class Simple_button(btk.Button):



    def __init__(self , parent):
        super.__init__(self , parent)
        self.button  = btk.Button(self , text="I am the button")
        self.button.pack()    


if __name__ == '__main__':
    Dashboard(iconphoto="ttkbootstrap\linkedin_bot.png")