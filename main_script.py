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

    main_window  = btk.Window(title="Linkedin Bot" , themename="darkly" , resizable=(0 , 0))

    
    main_window.geometry(f"300x300")




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
