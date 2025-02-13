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

from ttkbootstrap.tooltip import ToolTip


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
    page_depth_variable_initial  = btk.IntVar(value=0)
    page_depth_variable_final  = btk.IntVar(value = 3)
    retries_variable  = btk.IntVar(value  = 10)
   

    keywords_var  = btk.StringVar(value="Enter Keywords")


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


    def selenium_bot_starting():
        if username_entry.get() == "" or password_entry.get() == "":
            toast_message("Enter Username Password and other Fields to start the bot" , 3000)
        elif username_entry.get() == "Enter Username" or password_entry.get() == "Enter Password":
            toast_message("Enter the actual Username and Password to Start" , 3000)
        elif round(wait_seconds.get()) == 0:
            toast_message("Enter the waiting time also :" , 2000)
        else:
            username = username_entry.get()
            password  = password_entry.get()
            waiting_time  = round(wait_seconds.get())
            actual_message  = str(multiline_messagebox.get("1.0", "end-1c"))
           
            selenium_data.selenium_bot(username=username , password = password , wait_seconds=waiting_time , keywords=keywords_box.get() , page_numbers=page_depth_final.get() , message_string = actual_message)
            
    # Trial to stop the running bot ### 
    def stopping_selenium_bot():
        selenium_data.stopping_bot()
             
    def closing_application():
        selenium_data.stopping_bot()
        sys.exit()

    ######### ------ Initial App Details ##########
    application_width = 890
    application_height = 700

    window_height  = main_window.winfo_screenheight()
    window_width  = main_window.winfo_screenwidth()

    x_location  = ( window_width // 2 ) - ( application_width // 2)
    y_location  = (window_height // 2) - ( application_height // 2)

    main_window.geometry(f"{application_width}x{application_height}+{x_location}+{y_location}")


    ## UI Based Functions ( Only for the UI based data )
    upper_box  = btk.Frame(main_window , width=900 , height=70 , border = 1 )
    
    username_entry  = btk.Entry(upper_box , textvariable=username_var , width=31)
    password_entry  = btk.Entry(upper_box , textvariable=password_var , width=31)
    showpasswordcheckbox = btk.Checkbutton(upper_box , text="Show Password" , variable=checkvar , command=checkbuttonclicked  ,bootstyle="square-toggle")
    seperator = btk.Separator(orient=btk.HORIZONTAL)
    middle_box  = btk.Frame(main_window , width=900 , height=70 )


    page_depth_initial = btk.Spinbox(middle_box , from_=0 , to=1000 , textvariable=page_depth_variable_initial , width=12)
    page_depth_final  = btk.Spinbox(middle_box , from_=0 , to = 1000 , textvariable=page_depth_variable_final , width= 12)
    
    
    wait_seconds  = btk.Scale(middle_box , from_= 0 , to=60 , length=200 , command=seconds_scale_changed , value=6)
    wait_seconds_value  = btk.Label(middle_box , text=f"{wait_seconds.get()} Seconds" , width=10)
    retries_  = btk.Spinbox(middle_box , from_=0 , to=10 , width=12 , textvariable=retries_variable )

    seperator_2  = btk.Separator(orient=btk.HORIZONTAL)

    lower_middle_frame  = btk.Frame(main_window , width=900 , height=400)

    seperator_3  = btk.Separator(orient=btk.HORIZONTAL)

    keywords_box  = btk.Entry(lower_middle_frame ,textvariable=keywords_var , width=90)
    multiline_messagebox  = btk.Text(lower_middle_frame , width=85 , height=15 )

   
    start_button = btk.Button(main_window , text="Start" , bootstyle  = btk.SUCCESS , width=25 , command=selenium_bot_starting)
    stop_button = btk.Button(main_window , text="Stop" , bootstyle  = btk.DANGER , width=25 , command=stopping_selenium_bot)
    reset_button = btk.Button(main_window , text="Reset" , bootstyle  = btk.WARNING , width=25)

    # progressbar  = btk.Floodgauge(main_window , length=860 , maximum = 100 , value=10, orient=tk.HORIZONTAL , bootstyle="success-striped" , mode='determinate')
    progressbar  = btk.Floodgauge(main_window , maximum=100 , mask="Progress {}%" , length=860 , value=0, bootstyle="dark" , mode='determinate')
    
    


    ##############---------------- Configure Controls : 
    upper_box.pack_propagate(0)
    middle_box.pack_propagate(0)
    lower_middle_frame.pack_propagate(0)

    

    ################-------------  Binding Controls : 
    username_entry.bind("<FocusIn>" , lambda x : username_entry.delete(0 , 190))
    password_entry.bind("<FocusIn>" , lambda x : clear_password_box())
    keywords_box.bind("<FocusIn>" , lambda x :keywords_box.delete(0 , 100))
    password_entry.bind("<KeyRelease>" ,  check_button_check)


    #################------------- Binding Control to make a tooltip : 
    initial_depth_tooltip = ToolTip(page_depth_initial, text="Initial Page Count from Where the Count is to start" , bootstyle="light" , delay=500)
    final_page_tooltip  = ToolTip(page_depth_final , text="Final Page Count till then the Bot shall scrap Urls" , bootstyle="light" , delay=500)
    wait_seconds_tooltip = ToolTip(wait_seconds , text="Number of Seconds to Wait for Every Operation ( Login, Scrapping Etc.)" , bootstyle="light" , delay=500)
    retries_tooltip = ToolTip( retries_ , text="Number of retries browser does before throiwing error " , bootstyle="light" ,delay=500)
    multiline_messagebox_tooltip = ToolTip(multiline_messagebox , text="Enter Full Message Here with the spaces and Line Breaks ( Only Skip Hi, Hello it will be added by bot on its own ( with name ))" , bootstyle="light" , delay=500)


    
    ###########-------------- Packing Controls 
    upper_box.pack(padx=0 , pady=0 , anchor="n")
    username_entry.pack(side=tk.LEFT , anchor=tk.N , pady=10 , padx = 10)
    password_entry.pack(side=tk.LEFT , anchor=tk.N , pady=10 , padx= 10)
    showpasswordcheckbox.pack(side=tk.RIGHT , anchor=tk.N , pady=19 , padx=(0,30))
    seperator.pack(fill="x" , padx=10)

    middle_box.pack()
    page_depth_initial.pack(side=tk.LEFT , anchor=tk.N ,pady=10  ,padx = 10)
    page_depth_final.pack(side=tk.LEFT , anchor=tk.N , pady=10 , padx=10)
    wait_seconds_value.pack(side=tk.LEFT , anchor=tk.N , pady=16 , padx =10)
    wait_seconds.pack(side=tk.LEFT , anchor=tk.N ,pady=20  ,padx = 10)
    retries_.pack(side=tk.RIGHT , anchor=tk.N , padx=10 , pady=10)

    seperator_2.pack(fill=tk.X ,  padx=10)


    lower_middle_frame.pack()
    keywords_box.pack(padx=10 , pady=10)
    multiline_messagebox.pack(side=tk.LEFT , anchor=tk.NE  ,padx = 10 , pady = 10)
   
    seperator_3.pack(fill=tk.X , padx = 10)
    start_button.pack(side=tk.LEFT , padx=10 , pady=20 , anchor=tk.N)
    stop_button.pack(side=tk.LEFT , padx=10 , pady=20 , anchor=tk.N)
    reset_button.pack(side=tk.LEFT , padx=10 , pady=20 , anchor=tk.N)

    progressbar.place(x  = 10 , y = 620)

    main_window.protocol("WM_DELETE_WINDOW", closing_application)

    main_window.mainloop()






######___________ Main ( Initiation of the Code ) ___________#########
if __name__ == '__main__':
    main_thread  = threading.Thread(target=UI)
    main_thread.start()

    while WORKING == False:
        try:
            stop_event.set()
        except Exception as stop_event_error:
            toast_message(f"Stop Event Error {stop_event_error}")
