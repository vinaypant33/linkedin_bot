from time import sleep
import os
import sys
import tkinter as tk
import pyautogui
import keyboard
import selenium
import threading


import ttkbootstrap as btk
from ttkbootstrap.toast import ToastNotification



import selenium_data

####__________ Constants __________________####
NORMAL_SLEEP_TIME = 10
MICRO_SLEEP_TIME  = 2
WORKING  = True


stop_event  = threading.Event()


def toast_message(text , duration):
    toast = ToastNotification("Linkedin Bot" , message=text , duration=duration)
    toast.show_toast()



########### ___________ Function for Multiprocessing ____________##########
def UI():

    def clear_password_box():
        password_entry.delete( 0 ,190)
        sleep(1 / 4)
        password_entry.configure(show="*")
    
    main_window  = btk.Window(title="Linkedin Bot" , themename="darkly" , resizable=(0 , 0))



    username_var = btk.StringVar(value="Enter Username")
    password_var = btk.StringVar(value="Enter Password")
    checkvar  = btk.BooleanVar(value=False)
    page_depth_variable  = btk.StringVar(value="Search Number of Pages")
    retries_variable = btk.StringVar(value="Number of Retries")

    keywords_var  = btk.StringVar(value="Enter Keywords")


    def checkbuttonclicked():
    
        if checkvar.get() == True:
            password_entry.configure(show="")
           
        elif checkvar.get() == False:
            if password_entry.get() == "Enter Password":
                pass
            else:
                password_entry.configure(show="*")
    
    def seconds_scale_changed(x):
        wait_seconds_value.configure(text=str(round(wait_seconds.get())) + " Seconds")           

    
    application_width = 890
    application_height = 900

    window_height  = main_window.winfo_screenheight()
    window_width  = main_window.winfo_screenwidth()

    x_location  = ( window_width // 2 ) - ( application_width // 2)
    y_location  = (window_height // 2) - ( application_height // 2)

    main_window.geometry(f"{application_width}x{application_height}+{x_location}+{y_location}")

    ### Styles for te UI Controls : 
    




    ## UI Based Functions ( Only for the UI based data )
    upper_box  = btk.Frame(main_window , width=900 , height=70 , border = 1 )
    
    username_entry  = btk.Entry(upper_box , textvariable=username_var , width=31)
    password_entry  = btk.Entry(upper_box , textvariable=password_var , width=31)
    showpasswordcheckbox = btk.Checkbutton(upper_box , text="Show Password" , variable=checkvar , command=checkbuttonclicked  ,bootstyle="square-toggle")
    seperator = btk.Separator(orient=btk.HORIZONTAL)
    middle_box  = btk.Frame(main_window , width=900 , height=70 )


    page_depth  = btk.Spinbox(middle_box , from_=0 , to=1000  , textvariable=page_depth_variable)
    wait_seconds_value  = btk.Label(middle_box , text="0 Seconds" , width=10)
    wait_seconds  = btk.Scale(middle_box , from_= 0 , to=60 , length=200 , command=seconds_scale_changed)
    retries_  = btk.Spinbox(middle_box , from_=0 , to=10 , textvariable=retries_variable )

    seperator_2  = btk.Separator(orient=btk.HORIZONTAL)

    lower_middle_frame  = btk.Frame(main_window , width=900 , height=400)

    seperator_3  = btk.Separator(orient=btk.HORIZONTAL)

    keywords_box  = btk.Entry(lower_middle_frame ,textvariable=keywords_var , width=84)
    multiline_messagebox  = btk.Text(lower_middle_frame , width=30 , height= 30)

   
    start_button = btk.Button(main_window , text="Start" , bootstyle  = btk.SUCCESS , width=25)
    stop_button = btk.Button(main_window , text="Stop" , bootstyle  = btk.DANGER , width=25)
    reset_button = btk.Button(main_window , text="Reset" , bootstyle  = btk.WARNING , width=25)

    


    # Configure Controls : 
    upper_box.pack_propagate(0)
    middle_box.pack_propagate(0)
    lower_middle_frame.pack_propagate(0)

    

    # Binding Controls : 
    username_entry.bind("<FocusIn>" , lambda x : username_entry.delete(0 , 190))
    password_entry.bind("<FocusIn>" , lambda x : clear_password_box())


    
    # Pack the controls
    upper_box.pack(padx=0 , pady=0 , anchor="n")
    username_entry.pack(side=tk.LEFT , anchor=tk.N , pady=10 , padx = 10)
    password_entry.pack(side=tk.LEFT , anchor=tk.N , pady=10 , padx= 10)
    showpasswordcheckbox.pack(side=tk.RIGHT , anchor=tk.N , pady=19 , padx=(0,30))
    seperator.pack(fill="x" , padx=10)

    middle_box.pack()
    page_depth.pack(side=tk.LEFT , anchor=tk.N ,pady=10  ,padx = 10)
    wait_seconds_value.pack(side=tk.LEFT , anchor=tk.N , pady=16 , padx =10)
    wait_seconds.pack(side=tk.LEFT , anchor=tk.N ,pady=20  ,padx = 10)
    retries_.pack(side=tk.RIGHT , anchor=tk.N , padx=10 , pady=10)

    seperator_2.pack(fill=tk.X ,  padx=10)


    lower_middle_frame.pack()
    keywords_box.pack(side=tk.LEFT , padx=10 , pady=10 , anchor=tk.N)
   
    seperator_3.pack(fill=tk.X , padx = 10)
    start_button.pack(side=tk.LEFT , padx=10 , pady=20 , anchor=tk.N)
    stop_button.pack(side=tk.LEFT , padx=10 , pady=20 , anchor=tk.N)
    reset_button.pack(side=tk.LEFT , padx=10 , pady=20 , anchor=tk.N)

    main_window.mainloop()






######___________ Main Code ___________#########
if __name__ == '__main__':
    main_thread  = threading.Thread(target=UI)
    main_thread.start()

    while WORKING == False:
        try:
            stop_event.set()
        except Exception as stop_event_error:
            toast_message(f"Stop Event Error {stop_event_error}")
