import ttkbootstrap as btk
from ttkbootstrap.toast import  ToastNotification
from ttkbootstrap.tooltip import ToolTip
from threading import Thread
from time import sleep

from ttkbootstrap import * # For Temp basis code would be changed later as per the specific requirments

import os 
import sys
import ctypes

from PIL import Image , ImageTk




### Importing classes for the controls : 
import home_class

## Setting up current directory in which the script would run :
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
print(f"Current Directory  : {script_dir}")

sys.setrecursionlimit(1000)


### App Constants : 
window_width  = 1200
window_height  = 700
current_theme = "darkly"

connections_image  = Image.open("connections.png")
jobs_image  = Image.open("jobs.png")
settings_image  = Image.open("settings.png")

connections = connections_image.resize((30 , 30))
jobs  = jobs_image.resize((30 , 30))
settings = settings_image.resize((30 , 30))



### Function to set later :: 
'''
Function would be used to dynamically change the theme for the application
titlebar dark or light wouldbe done accordingly

'''
themename = "darkly"
button_theme  = "dark"
background_color  = "#241F1A"
success_theme = "success"


# Function to set the title of the application  :  Works only in windows : 
def set_dark_titlebar(window , mode_numeral = 1):
    try:
        window.update_idletasks()
        hwnd  = ctypes.windll.user32.GetParent(window.winfo_id())
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, DWMWA_USE_IMMERSIVE_DARK_MODE, ctypes.byref(ctypes.c_int(mode_numeral)), ctypes.sizeof(ctypes.c_int(1)))
    except Exception as Error:
        print(f"Facing Error in Changing the Theme of the Application {Error}")


def change_window(window_name):
    if window_name == "home_button" :
        first_screen.pack(side=tk.LEFT ,expand=True , fill=tk.X)
        second_screen.pack_forget()
        third_screen.pack_forget()
        # second_screen.pack(side=tk.LEFT ,expand=True , fill=tk.X)
        # third_screen.pack(side=tk.LEFT , expand=True , fill = tk.X)
    elif window_name == "jobs_button":
        # first_screen.pack(side=tk.LEFT ,expand=True , fill=tk.X)
        first_screen.pack_forget()
        third_screen.pack_forget()
        second_screen.pack(side=tk.LEFT ,expand=True , fill=tk.X)
        # third_screen.pack(side=tk.LEFT , expand=True , fill = tk.X)
    elif window_name == "settings_button":
        # first_screen.pack(side=tk.LEFT ,expand=True , fill=tk.X)
        # second_screen.pack(side=tk.LEFT ,expand=True , fill=tk.X)
        first_screen.pack_forget()
        second_screen.pack_forget()
        third_screen.pack(side=tk.LEFT , expand=True , fill = tk.X)
    else:
        error_toast  = ToastNotification("Linkedin Bot" , "Unable to open any Frame ")
        first_screen.pack(side=tk.LEFT  , expand=True , fill=tk.X)
        second_screen.pack_forget()
        third_screen.pack_forget()

def checkbuttonclicked():
        if checkvar.get() == True:
            password_entry.configure(show="")
           
        elif checkvar.get() == False:
            if password_entry.get() == "Enter Password":
                pass
            else:
                password_entry.configure(show="*")
        
def check_button_check(x):
        if checkvar.get() == True:
            password_entry.configure(show="")
           
        elif checkvar.get() == False:
            if password_entry.get() == "Enter Password":
                pass
            else:
                password_entry.configure(show="*")



## Main Window and Skeleton details : 
window  = btk.Window(themename=themename)



### Variables for the windows : 
username_var = btk.StringVar(value="Enter Username")
password_var = btk.StringVar(value="Enter Password")
checkvar  = btk.BooleanVar(value=False)
page_depth_variable_initial  = btk.IntVar(value=0)
page_depth_variable_final  = btk.IntVar(value = 3)
retries_variable  = btk.IntVar(value  = 10)
keywords_var  = btk.StringVar(value="Enter Keywords")

connections_icon = ImageTk.PhotoImage(connections)
jobs_icon  = ImageTk.PhotoImage(jobs)
settings_icon  = ImageTk.PhotoImage(settings)


x_location  = ( window.winfo_screenwidth() // 2 ) - (window_width // 2)
y_location  = (window.winfo_screenheight() // 2) - (window_height // 2)

window.title("Linkedin Bot")
window.iconbitmap(r"linkedin_icon.ico")
window.resizable(0 , 0)


set_dark_titlebar(window  = window , mode_numeral=1)
window.geometry(f"{window_width}x{window_height}")


### Styles : Window and Other Widgets : 
style = btk.Style()
style.configure("Custom.TFrame", background="#241F1A") 


sidebar  = btk.Frame(window , height=window_height , width=50 ,bootstyle ="primary")
first_screen  = btk.Frame(window , height=window_height , style="Custom.TFrame") # style="Custom.TFrame" this will be used later 
second_screen = btk.Frame(window , height=window_height , style="Custom.TFrame")
third_screen  = btk.Frame(window , height = window_height , style="Custom.TFrame")


## Three Buttons with the images in sidebar :
home_button_frame  = btk.Frame(sidebar , height=window_height / 3  , bootstyle  = button_theme )
jobs_button_frame  = btk.Frame(sidebar , height=window_height / 3 , bootstyle = button_theme)
settings_button_frame = btk.Frame(sidebar , height=window_height / 3 , bootstyle  = button_theme)

home_button_with_image  = btk.Button(home_button_frame  , image=connections_icon , compound="top" , bootstyle  = success_theme  , command= lambda :change_window("home_button"))
jobs_button_with_image  = btk.Button(jobs_button_frame , image=jobs_icon , compound="top" , bootstyle  = success_theme , command= lambda : change_window("jobs_button"))
settings_button_with_image  = btk.Button(settings_button_frame , image=settings_icon , compound="top" , bootstyle  = success_theme , command= lambda : change_window("settings_button"))

### Frame wise controls : 
username_entry  = btk.Entry(master=first_screen , textvariable=username_var , width=41)
password_entry  = btk.Entry(master = first_screen , textvariable=password_var , width=41)
showpasswordcheckbox = btk.Checkbutton(master = first_screen , text="Show Password" , variable=checkvar , command=checkbuttonclicked  ,bootstyle="square-toggle")






## Configuring Controls :
sidebar.pack_propagate(0)
first_screen.pack_propagate(0)
second_screen.pack_propagate(0)
third_screen.pack_propagate(0)
home_button_frame.pack_propagate(0)
jobs_button_frame.pack_propagate(0)
settings_button_frame.pack_propagate(0)




## Binding Functions : 
def sidebar_animation(expand , width):
    if expand and width < 100:
        width +=10
        sidebar.configure(width=width)
        window.after(30 , lambda : sidebar_animation(True , width))
    elif expand == False and width > 50:
        width-=5 
        sidebar.configure(width=width)
        window.after(30 , lambda : sidebar_animation(False , width))

def clear_password_box():
        password_entry.delete( 0 ,tk.END)
        sleep(1 / 4)
        password_entry.configure(show="*")

### Binding Controls  : 
sidebar.bind("<Enter>" , lambda x:sidebar_animation(expand=True , width=50))
sidebar.bind("<Leave>" , lambda x : sidebar_animation(expand=False , width=100))
home_button_frame.bind("<Enter>" , lambda x : sidebar_animation(expand=True , width=100))
jobs_button_frame.bind("<Enter>" , lambda x : sidebar_animation(expand=True , width=100))
settings_button_frame.bind("<Enter>" , lambda x : sidebar_animation(expand=True , width=100))

username_entry.bind("<FocusIn>" , lambda x : username_entry.delete(0 , 190))
password_entry.bind("<FocusIn>" , lambda x : clear_password_box())


## Tooltip for the widgets  : 
# connections_button_tooltip = ToolTip(home_button_with_image , text="Click for Connections Page" , bootstyle="danger")


# Packing Controls  :
sidebar.pack(side=tk.LEFT)
first_screen.pack(side=tk.LEFT ,expand=True , fill=tk.X)
# second_screen.pack(side=tk.LEFT ,expand=True , fill=tk.X)
# third_screen.pack(side=tk.LEFT , expand=True , fill = tk.X)




home_button_frame.pack(side=tk.TOP , expand=True , fill=tk.X)
jobs_button_frame.pack(side=tk.TOP , expand=True , fill=tk.X)
settings_button_frame.pack(side=tk.TOP , expand=True ,fill=tk.X)

home_button_with_image.pack(expand=True , fill=tk.BOTH)
jobs_button_with_image.pack(expand=True , fill=tk.BOTH)
settings_button_with_image.pack(expand=True , fill=tk.BOTH)






##### Packing Frame wise controls : 
username_entry.pack (side=tk.LEFT , anchor = tk.N , padx = 10 , pady=10)
password_entry.pack(side=tk.LEFT , anchor=tk.N , pady=10 , padx= 10)
showpasswordcheckbox.pack(side=tk.RIGHT , anchor=tk.N , pady=19 , padx=(0,30))


window.mainloop()
