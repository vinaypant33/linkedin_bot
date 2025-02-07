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
import time
import threading

import pyautogui
from bs4 import BeautifulSoup
from ttkbootstrap.toast import ToastNotification # For showing the error messages

from threading import Thread

from datetime import datetime

from pubsub import pub


class Selenium_bot(Thread):


    def __init__(self , name , username  = "" , password  = "" , keywords = "" , message  = "" , final_range  = 0 , waitseconds  = 10  , sleepseconds  = 10):
        super().__init__()

        self.name  = name
        self.username  = username
        self.password  = password
        self.keywords  = keywords
        self.message = message

        self.current_progress = 0

        self.final_range = final_range
        self.wait_seconds  = waitseconds
        self.sleep_seconds  = sleepseconds



        ### Code for the thread for the selenium Bot : Threading :: 
        self.pause_event  = threading.Event()
        self.pause_event.set() ## Made the threading event as true as the thrad is runnin. 
        self.stop_event  = threading.Event()

        # Options for the Chrome Bot : 
        self.options  = webdriver.ChromeOptions()
        self.options.add_experimental_option('detach', True)
        self.options.add_argument("--disable-webrtc")  # Disable WebRTC
        self.options.add_argument("--log-level=3")    # Reduce log verbosity

       


    def run(self):
        print(f"{self.name} started.")
        if not self.stop_event.is_set():
                self.bot  = webdriver.Chrome(options=self.options)

                ## Try to login to the linkedin : 
                try:
                    self.bot.get("https://www.linkedin.com/checkpoint/rm/sign-in-another-account")
                    WebDriverWait(self.bot, self.wait_seconds).until( lambda d: d.execute_script("return document.readyState") == "complete")
                    self.bot.maximize_window()
                    username  = self.bot.find_element(By.ID , "username")
                    username.send_keys(self.username)
                    password   = self.bot.find_element(By.ID , "password")
                    password.send_keys(self.password)
                except Exception as Login_Error:
                    with open ("error_file.txt" , "a") as file:
                        file.writelines(f"Error in Login {Login_Error} ::  {datetime.time} \n")
                    print(f"First Error in Login :: {Login_Error}")
                    self.bot.close()
                    sys.exit

                ## Check for the remember me box and then click the singin button
                try:
                    # window_position = self.bot.get_window_size()
                    click_location = self.bot.find_element(By.ID , "rememberMeOptIn-checkbox").location
                    x = click_location['x']
                    y = click_location['y']
                    pyautogui.moveTo(364 + x , 403 + y , 2)
                    pyautogui.click()
                    sleep(1)
                    self.bot.find_element(By.XPATH , '//*[@id="organic-div"]/form/div[4]/button').click()
                    sleep(1)
                except Exception as Click_Error:
                    with open ("error_file.txt" , "a") as file:
                        file.writelines(f"Error in Login {Click_Error} ::  {datetime.time} \n")
                    print(f"Login Second Error  :: {Click_Error}")
                    self.bot.close()
                    sys.exit

                sleep(self.sleep_seconds)

                ### For the specified range and the specified pages go through the pages and then update the progressbar: 


                try:
                    for i in range(1 , self.final_range):
                        self.bot.get(f"https://www.linkedin.com/search/results/people/?keywords={self.keywords}&page={i}")
                        WebDriverWait(self.bot , self.wait_seconds).until( lambda d : d.execute_script("return document.readyState") == "complete")
                        sleep(1)
                        progress_Step = 50 // self.final_range
                        pub.sendMessage("progressupdate" ,value =  progress_Step)
                except Exception as page_load_error:
                    with open ("error_file.txt" , "a") as file:
                        file.writelines(f"Error in Login {page_load_error} ::  {datetime.time} \n")
                    print(f"Login Second Error  :: {page_load_error}")
                    self.bot.close()
                    sys.exit


                
            
    def stop(self):
        self.stop_event.set()
        self.bot.close()
        print("The Thread is stopped")
        sys.exit





