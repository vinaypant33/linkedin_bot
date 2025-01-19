from selenium import webdriver
from typing import Any
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from tqdm import tqdm
import os
import sys


import pyautogui
from bs4 import BeautifulSoup


#### Constants : 
working  = False
progress_value  = 0
progress_text = "I am Progress Text"

from ttkbootstrap.toast import ToastNotification # For showing the error messages



def show_message(messsage, duration):
    toast = ToastNotification("Linkedin Bot" , message=messsage , duration=duration)
    toast.show_toast()



def selenium_bot():
    global working

    if not working:
        working = True
        print("Starting Selenium : ")
    else:
        show_message("Bot Already Working" , 3000)


def stopping_bot():
    global working
    working  = False
    show_message("Stopping Linkedin Bot" , 3000)





