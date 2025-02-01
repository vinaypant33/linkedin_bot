import ttkbootstrap as btk
from threading import Thread
from time import sleep

from ttkbootstrap import * # For Temp basis code would be changed later as per the specific requirments

import os 
import sys
import ctypes

## Setting up current directory in which the script would run :
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
print(f"Current Directory  : {script_dir}")



### App Constants : 
window_width  = 1200
window_height  = 700
current_theme = "darkly"

### Function to set later :: 
'''
Function would be used to dynamically change the theme fo the application
titlebar dark or light wouldbe done accordingly
'''


# Function to set the title of the application  :  Works only in windows : 
def set_dark_titlebar(window , mode_numeral = 1):
    try:
        window.update_idletasks()
        hwnd  = ctypes.windll.user32.GetParent(window.winfo_id())
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, DWMWA_USE_IMMERSIVE_DARK_MODE, ctypes.byref(ctypes.c_int(mode_numeral)), ctypes.sizeof(ctypes.c_int(1)))
    except Exception as Error:
        print(f"Facing Error in Changing the Theme of the Application {Error}")


## Main Window and Skeleton details : 
window  = btk.Window(themename="darkly")


x_location  = ( window.winfo_screenwidth() // 2 ) - (window_width // 2)
y_location  = (window.winfo_screenheight() // 2) - (window_height // 2)

window.title("Linkedin Bot")
window.iconbitmap(r"linkedin_icon.ico")
window.resizable(0 , 0)


set_dark_titlebar(window  = window , mode_numeral=1)
window.geometry(f"{window_width}x{window_height}")






window.mainloop()
