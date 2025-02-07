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


from datetime import datetime

from pubsub import pub  


### Importing classes for the controls : 
import home_class
import settings as settings_page

import selenium_script

## Setting up current directory in which the script would run :
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
print(f"Current Directory  : {script_dir}")

sys.setrecursionlimit(1000)


### App Constants : 
window_width  = 1050
window_height  = 680
current_theme = "darkly"


progressbar_value  = 0

connections_image  = Image.open("connections.png")
jobs_image  = Image.open("jobs.png")
settings_image  = Image.open("settings.png")

connections = connections_image.resize((30 , 30))
jobs  = jobs_image.resize((30 , 30))
settings = settings_image.resize((30 , 30))

global mode_numeral
global themename
global background_color
themename = "darkly"
button_theme  = "dark"
background_color  = "#241F1A"
secondary_theme = "secondary"
mode_numeral  = 1

global username_var
global password_var

# username_var = btk.StringVar(value="Enter Username")
# password_var = btk.StringVar(value="Enter Password")
# checkvar  = btk.BooleanVar(value=False)
# page_depth_variable_initial  = btk.IntVar(value=0)
# page_depth_variable_final  = btk.IntVar(value = 3)
# retries_variable  = btk.IntVar(value  = 10)
# keywords_var  = btk.StringVar(value="Enter Keywords")

### Function to set later :: 
'''
Function would be used to dynamically change the theme for the application
titlebar dark or light wouldbe done accordingly

'''

### Load file and Check for the details to be Preloaded in the application : 

try:
     with open("settings.txt" , "r") as file:

        # global keywords
        text = file.read()
        username  = text.split(":")[0]
        message = text.split(":")[1]
        keywords  = text.split(":")[2]
        print(f"The kwyrods as : {keywords}")
        theme = text.split(":")[3]
        
        if theme == "False":
            mode_numeral = 1
            current_theme = "darkly"
        elif theme == "True":
            mode_numeral = 0
            themename = "flatly"
            background_color = "#F7F7F7"
           
except Exception as Error:
    with open("error_file.txt" , "a") as file:
         file.write(f"Error Occured {Error} :: {datetime.now()}")
    print(f"Error Occured {Error}")



# Function to set the title of the application  :  Works only in windows : 
def set_dark_titlebar(window , mode_numeral):
    try:
        window.update_idletasks()
        hwnd  = ctypes.windll.user32.GetParent(window.winfo_id())
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, DWMWA_USE_IMMERSIVE_DARK_MODE, ctypes.byref(ctypes.c_int(mode_numeral)), ctypes.sizeof(ctypes.c_int(1)))
    except Exception as Error:
        with open("error_file.txt" , "a") as file:
            file.write(f"Facing Error in Changing the Theme of the Application {Error} :: {datetime.now()}")


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

def seconds_scale_changed(x):
        wait_seconds_value.configure(text=str(round(wait_seconds.get())) + " Seconds")  


def start_button_clicked():
    # global progressbar_value
    # progressbar_value+=10
    # progress_bar.step(0.3)
    # progress_bar.configure(value=progressbar_value)
    username = username_entry.get()
    password  = password_entry.get()
    keywords = keywords_box.get()
    message  = multiline_messagebox.get("1.0", "end-1c")
    final_range  = int(page_depth_final.get())
    final_wait_seconds = int(retries_.get())
    sleep_seconds = int(round(wait_seconds.get()))

    global selenium_thread
    selenium_thread  = selenium_script.Selenium_bot(name="Selenium_Thread" , username=username , password=password , keywords=keywords , 
                                                    message=message , final_range=final_range , waitseconds=final_wait_seconds , sleepseconds=sleep_seconds)
    selenium_thread.start()


    # main_thread = selenium_script.Selenium_bot(name  = "Thread-1" , username="vinaypant24@gmail.com" , password="HimanshuPant@2290"  , keywords="HR Ireland" , message="I am the message" , final_range=10 , waitseconds=5)

    # main_thread.start()

def stop_button_clicked():
     selenium_thread.stop()

def change_progressbar(value):
    progress_bar.step(value)

## Main Window and Skeleton details : 
window  = btk.Window(themename=themename)



### Variables for the windows : 

username_var = btk.StringVar(value="Enter Username")
username_var.set(username)
password_var = btk.StringVar(value="Enter Password")
checkvar  = btk.BooleanVar(value=False)
page_depth_variable_initial  = btk.IntVar(value=0)
page_depth_variable_final  = btk.IntVar(value = 3)
retries_variable  = btk.IntVar(value  = 10)
keywords_var  = btk.StringVar(value="Enter Keywords")


try:
    
    keywords_var.set(keywords)
except Exception as keywords_error:
     with open("error_file.txt" , "a") as file:
            file.writelines(f"Facing Error in Changing the Theme of the Application {keywords_error} :: {datetime.now()}")

connections_icon = ImageTk.PhotoImage(connections)
jobs_icon  = ImageTk.PhotoImage(jobs)
settings_icon  = ImageTk.PhotoImage(settings)


x_location  = ( window.winfo_screenwidth() // 2 ) - (window_width // 2)
y_location  = (window.winfo_screenheight() // 2) - (window_height // 2)

window.title("Linkedin Bot")
window.iconbitmap(r"linkedin_icon.ico")
window.resizable(0 , 0)


set_dark_titlebar(window  = window , mode_numeral=mode_numeral)
window.geometry(f"{window_width}x{window_height}")





sidebar  = btk.Frame(window , height=window_height , width=50 ,bootstyle ="primary")
first_screen  = btk.Frame(window , height=window_height ) # style="Custom.TFrame" this will be used later 
second_screen = btk.Frame(window , height=window_height)
third_screen  = btk.Frame(window , height = window_height )


## Three Buttons with the images in sidebar :
home_button_frame  = btk.Frame(sidebar , height=window_height / 3  , bootstyle  = button_theme )
jobs_button_frame  = btk.Frame(sidebar , height=window_height / 3 , bootstyle = button_theme)
settings_button_frame = btk.Frame(sidebar , height=window_height / 3 , bootstyle  = button_theme)

home_button_with_image  = btk.Button(home_button_frame  , image=connections_icon , compound="top" , bootstyle  = secondary_theme  , command= lambda :change_window("home_button"))
jobs_button_with_image  = btk.Button(jobs_button_frame , image=jobs_icon , compound="top" , bootstyle  = secondary_theme , command= lambda : change_window("jobs_button"))
settings_button_with_image  = btk.Button(settings_button_frame , image=settings_icon , compound="top" , bootstyle  = secondary_theme , command= lambda : change_window("settings_button"))

### Frame wise controls : 
username_entry  = btk.Entry(master=first_screen , textvariable=username_var , width=35)
password_entry  = btk.Entry(master = first_screen , textvariable=password_var , width=35)
showpasswordcheckbox = btk.Checkbutton(master = first_screen , text="Show Password" , variable=checkvar , command=checkbuttonclicked  ,bootstyle="square-toggle")


page_depth_initial = btk.Spinbox(first_screen , from_=0 , to=1000 , textvariable=page_depth_variable_initial , width=13)
page_depth_final  = btk.Spinbox(first_screen , from_=0 , to = 1000 , textvariable=page_depth_variable_final , width= 13)


wait_seconds  = btk.Scale(first_screen , from_= 0 , to=60 , length=200 , command=seconds_scale_changed , value=6)
wait_seconds_value  = btk.Label(first_screen , text=f"{wait_seconds.get()}:Seconds" , width=10)
retries_  = btk.Spinbox(first_screen , from_=0 , to=10 , width=13 , textvariable=retries_variable )

keywords_box  = btk.Entry(first_screen ,textvariable=keywords_var , width=95)
multiline_messagebox  = btk.Text(first_screen , width=95 , height=15 )
try:
    multiline_messagebox.insert("1.0" , message)
except Exception as message_exception:
     with open("error_file.txt" , "a") as file:
            file.writelines(f"Facing Error in Changing the Theme of the Application {message_exception} :: {datetime.now()}")

start_button = btk.Button(first_screen , text="Start" , bootstyle  = btk.SUCCESS , width=21 , command=start_button_clicked )
stop_button = btk.Button(first_screen , text="Stop" , bootstyle  = btk.DANGER , width=21 , command=stop_button_clicked )
reset_button = btk.Button(first_screen , text="Reset" , bootstyle  = btk.WARNING , width=21)
pause_button  = btk.Button(first_screen , text="Pause" , bootstyle = btk.INFO , width=21)

progress_bar  = btk.Progressbar(first_screen ,value= 0 , bootstyle  = "danger-striped" , length=960)

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
    global window_width
    if expand and width < 100:
        width +=10
        window_width+=10
        sidebar.configure(width=width)
        window.geometry(f"{window_width}x{window_height}")
        window.after(30 , lambda : sidebar_animation(True , width))
    elif expand == False and width > 50:
        width-=5 
        window_width-=5
        sidebar.configure(width=width)
        window.geometry(f"{window_width}x{window_height}")
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
password_entry.bind("<KeyRelease>" ,  check_button_check)
keywords_box.bind("<FocusIn>" , lambda x : keywords_box.delete( 0 , tk.END))

## Tooltip for the widgets  : 
# connections_button_tooltip = ToolTip(home_button_with_image , text="Click for Connections Page" , bootstyle="danger")
connection_button_tooltip = ToolTip(home_button_with_image , text='Click for Connections Page' , bootstyle="primary")
jobs_button_tooltip = ToolTip(jobs_button_with_image , text="Click for Jobs" , bootstyle="primary")
settings_button_tooltip = ToolTip(settings_button_with_image , text="Click for Settings" , bootstyle="primary")
initial_page_tooltip = ToolTip(page_depth_initial , text="Enter Initial Search Page Value" , bootstyle="primary")
final_page_tooltip = ToolTip(page_depth_final , text="Enter Final Search Page Value" , bootstyle="primary")
wait_seconds_tooltip = ToolTip(wait_seconds , text="Enter Sleep Time for Events to Happen" , bootstyle="primary")


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
showpasswordcheckbox.pack(side=tk.LEFT , anchor=tk.NW , pady=19 , padx=(16,30))

page_depth_initial.place(x = 10 , y = 70)
page_depth_final.place(x = 210 , y = 70)
wait_seconds_value.place(x = 400 , y = 78)
wait_seconds.place(x = 555 , y = 85)
retries_.place(x = 800 , y = 70)

keywords_box.place(x = 10 , y = 130)
multiline_messagebox.place(x = 10 , y = 190)

start_button.place(x = 10 , y = 600)
stop_button.place(x = 254 , y = 600)
reset_button.place(x = 494 , y  = 600)
pause_button.place(x = 734 , y = 600)

progress_bar.place(x = 10 , y = 650)


## Calling classes for the controls : 
settings_page.Settings(third_screen)


pub.subscribe(change_progressbar , "progressupdate")

window.mainloop()
