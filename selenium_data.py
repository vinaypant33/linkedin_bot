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

import threading


import pyautogui
from bs4 import BeautifulSoup





#### Constants : 
working  = False
progress_value  = 0
progress_text = "I am Progress Text"


stop_event  = threading.Event()

from ttkbootstrap.toast import ToastNotification # For showing the error messages




class selenium_class():

    def __init__(self , username  , password  , waitseconds , keywords , page_numbers):

        self.username = username
        self.password  = password
        self.waitseconds  = waitseconds
        self.keywords  = keywords
        self.page_numebrs = int(page_numbers)
        self.link_list  = []



        options  = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        options.add_argument("--disable-webrtc")  # Disable WebRTC
        options.add_argument("--log-level=3")    # Reduce log verbosity

        self.driver = webdriver.Chrome(options=options)

        try:
            self.driver.get("https://www.linkedin.com/checkpoint/rm/sign-in-another-account")
        except Exception as driver_error:
            show_message(f"Unable to Start Selenium Driver for Chrome {driver_error}")

        self.driver.maximize_window()

        try:
            username  = self.driver.find_element(By.ID , "username")
            username.send_keys(self.username)
            password  = self.driver.find_element(By.ID , "password")
            password.send_keys(self.password)
        except Exception as login_error:
            show_message(f"Login Error unable to find username or password filed {login_error}")
            sys.exit()

        try:
            rememberbox  = self.driver.find_element(By.ID , "rememberMeOptIn-checkbox")
            rememberbox.click()
        except Exception as remember_click:
            show_message("Unable to Click the Remember Box" , 3000)
        
        sleep(waitseconds)
        try:

            self.driver.find_element(By.XPATH , '//*[@id="organic-div"]/form/div[4]/button').click()
        except Exception as button_error:
            show_message("Unable to click the button ( Exiting Program )" , 2000)
            self.driver.close()
            sys.exit()
        

        try:
            self.driver.minimize_window()
        ### Searching pages for the Urls :
            for i in range(self.page_numebrs):
                self.driver.get(f"https://www.linkedin.com/search/results/people/?keywords={self.keywords}&page={i}")
                sleep(self.waitseconds / 3)
                source  = self.driver.page_source
                soup = BeautifulSoup(source, 'html.parser')
                links = soup.find_all('a')
                for link in links:
                    href = link.get('href')
                    if href :
                        if "www.linkedin.com/in/" in href:
                            self.link_list.append(href)
        except Exception as visit_error:
            show_message(f"Link Save Error : {visit_error}")
    
            

        self.link_list =  list(set(self.link_list))

        try:
            with open("link_file.txt", "w") as file:
                for line in self.link_list:
                    file.write(line + "\n")
        except Exception as save_file_error:
            show_message(f"Unable to save the file {save_file_error}")
        
        



        self.driver.close()

    




    def closing_browser(self):
        self.driver.close()
        sys.exit()
        
        

        






def show_message(messsage, duration):
    toast = ToastNotification("Linkedin Bot" , message=messsage , duration=duration)
    toast.show_toast()



def selenium_bot(username, password , wait_seconds , keywords , page_numbers):
    global working
    if not working:
        working = True
        show_message("Starting Bot :" , 2000)
        sleep(3)
        threading.Thread(selenium_class(username=username , password=password , waitseconds=wait_seconds , keywords=keywords , page_numbers=page_numbers ) , daemon=True).start()
        # selenium_class(username=username , password=password , waitseconds=wait_seconds)
    else:
        show_message("Bot Already Working" , 3000)


def stopping_bot():
    global working
    working  = False
    show_message("Stopping Linkedin Bot" , 3000)
    sys.exit()
    





