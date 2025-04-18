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
from bs4 import BeautifulSoup

import random
import threading


pyautogui.FAILSAFE = False

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


        ### List to save the all links the completed links and the Uncompleted Links : 
        self.all_links  = []
        self.completeed_links  = []
        self.pending_links = []

        ### Import the images for the connect, More, buttons : 
        self.connect_button_image  = r"connect_button.png"
        self.add_button_image  = r"add_note_button.png"
        self.send_button_image  = r"send_button.png"
        self.keep_login_image  = r"keep_login.png"
        self.more_button = r"more_button.png"
        self.second_connect  = r"second_connect.png"




        ### Code for the thread for the selenium Bot : Threading :: 
        self.pause_event  = threading.Event()
        self.pause_event.set() ## Made the threading event as true as the thrad is runnin. 
        self.stop_event  = threading.Event()

        # Options for the Chrome Bot : 
        self.options  = webdriver.ChromeOptions()
        self.options.add_experimental_option('detach', True)
        self.options.add_argument("--disable-webrtc")  # Disable WebRTC
        self.options.add_argument("--log-level=3")    # Reduce log verbosity

    def refresh(self):
        self.bot.refresh()
        threading.Timer(10000 , self.refresh)


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
                        file.writelines(f"Error in Login {Login_Error} ::  {datetime.now()} \n")
                    print(f"First Error in Login :: {Login_Error}")
                    self.bot.close()
                    sys.exit

                
                ## Check for the remember me box and then click the singin button
                try:
                    # window_position = self.bot.get_window_size()
                    # click_location = self.bot.find_element(By.ID , "rememberMeOptIn-checkbox").location
                    click_location  = pyautogui.locateOnScreen(self.keep_login_image , confidence=0.9)
                    # x = click_location['x']
                    # y = click_location['y']
                    x  = click_location.left + 30
                    y = click_location.top +  30
                    pyautogui.moveTo( x ,  y , 2)
                    pyautogui.click()
                except Exception as Click_Error:
                    with open ("error_file.txt" , "a") as file:
                        file.writelines(f"Error in Login {Click_Error} :: {datetime.now()} \n")
                    print(f"Login Second Error  :: {Click_Error}")
                    

                try:
                    sleep(1)
                    self.bot.find_element(By.XPATH , '//*[@id="organic-div"]/form/div[4]/button').click()
                    sleep(1)
                except Exception as Button_Click_Error:
                    with open("error_file.txt" , "a") as file:
                        file.writelines(f"Error in Login {Click_Error} :: {datetime.now()} \n")
                    print(f"Login Button Error :: {Button_Click_Error}")
                    self.bot.close()
                    sys.exit

                sleep(self.sleep_seconds)

                ### For the specified range and the specified pages go through the pages and then update the progressbar: 


                try:
                    for i in range(1 , self.final_range + 1):
                        self.bot.get(f"https://www.linkedin.com/search/results/people/?keywords={self.keywords}&page={i}")
                        WebDriverWait(self.bot , self.wait_seconds).until( lambda d : d.execute_script("return document.readyState") == "complete")
                        sleep(3)
                        progress_Step = 50 // self.final_range
                        pub.sendMessage("progressupdate" ,value =  progress_Step)
                        ### Collect all the links from the page source and store it in the links list : 
                        source  = self.bot.page_source
                        soup  = BeautifulSoup(source ,'html.parser')
                        links = soup.find_all('a')
                        for link in links:
                            href = link.get('href')
                            if href:
                                if "www.linkedin.com/in/" in href:
                                    self.all_links.append(href)
                except Exception as page_load_error:
                    with open ("error_file.txt" , "a") as file:
                        file.writelines(f"Error in Login {page_load_error} :: {datetime.now()} \n")
                    print(f"Login Second Error  :: {page_load_error}")
                    self.bot.close()
                    sys.exit
                

                ### Remove the Duplicates from the link list and start sending requests : 
                self.all_links = list(set(self.all_links))
                for each in self.all_links:
                    with open("link_file.txt" ,"a") as links_file:
                        links_file.writelines(f"{each} +\n")



                ### Links Collected and saved to the file : Starting sending requests:
                for each in self.all_links:
                    self.bot.get(f"{each}")
                    pyautogui.moveTo(300 , 300 , 2)
                    # Here Introduce the random part so that it may refresh on ramdon basis : 
                    self.refresh()
                    # Get the name of the user : 
                    try:
                        current_name  = self.bot.find_element(By.XPATH , '/html/body/div[7]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[1]/span[1]/a/h1')
                        self.current_name  = current_name.get_attribute('innerText')
                        self.current_name = self.current_name.split(" ")[0]
                        self.hi_text  = f"Hi {self.current_name},"
                    except Exception as name_error:
                        try:
                            current_name  = self.bot.find_element(By.XPATH , "/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[1]/span[1]/a/h1")
                            self.current_name  = current_name.get_attribute('innerText')
                            self.current_name = self.current_name.split(" ")[0]
                            self.hi_text  = f"Hi {self.current_name},"
                        except Exception as Name_Error:
                            with open ("error_file.txt" , "a") as file:
                                file.writelines(f"Unable to find the name of the user  {Name_Error} :: {datetime.now()} \n")
                            print(f"Name Finding Error  :: {Name_Error}")
                            self.hi_text = "Hi,"
                
                    ### Check for the connect button and Move Mouse there if the button is available : 
                    try:
                        ## Check for the connect button image :
                        connect_location = pyautogui.locateOnScreen(self.connect_button_image , confidence=0.9)
                        pyautogui.moveTo(connect_location.left + 50 , connect_location.top + 50 , 2)
                        pyautogui.click()
                        sleep(1)
                        add_button = pyautogui.locateOnScreen(self.add_button_image , confidence=0.9)
                        pyautogui.moveTo(add_button.left + 50 , add_button.top + 50 , 2)
                        pyautogui.click()
                        sleep(1)
                        pyautogui.write(self.hi_text)
                        pyautogui.press("enter")
                        sleep(0.5)
                        pyautogui.write(self.message)
                        sleep(2)
                        send_coordinates  = pyautogui.locateOnScreen(self.send_button_image , confidence=0.9)
                        pyautogui.moveTo(send_coordinates.left + 30 , send_coordinates.top +  30 , 2)
                        pyautogui.click()
                        sleep(1)
                    except Exception as screen_error:
                        # Check for the other alternative for connect : and then connect to the second button :
                        try:
                            more_location  = pyautogui.locateOnScreen(self.more_button , confidence=0.9)
                            pyautogui.moveTo(more_location.left +  30 , more_location.top + 30 , 1)
                            pyautogui.click()
                            sleep(1)
                            another_connect_button  = pyautogui.locateOnScreen(self.second_connect ,  confidence=0.9)
                            pyautogui.moveTo(another_connect_button.left  + 20 , another_connect_button.top + 20 , 2 )
                            pyautogui.click()
                            sleep(1)
                            add_button = pyautogui.locateOnScreen(self.add_button_image , confidence=0.9)
                            pyautogui.moveTo(add_button.left + 50 , add_button.top + 50 , 2)
                            pyautogui.click()
                            sleep(1)
                            pyautogui.write(self.hi_text)
                            pyautogui.press("enter")
                            sleep(0.5)
                            pyautogui.write(self.message)
                            sleep(2)
                            send_coordinates  = pyautogui.locateOnScreen(self.send_button_image , confidence=0.9)
                            pyautogui.moveTo(send_coordinates.left + 30 , send_coordinates.top +  30 , 2)
                            pyautogui.click()
                            sleep(1)
                        except Exception as final_error:
                            with open("second_links.txt" , "a") as file:
                                file.writelines(f"{each} \n")
                            print("None Method Working")
                            with open ("error_file.txt" , "a") as file:
                                file.writelines(f"None of the methods are working ::  {final_error} :: {datetime.now()} \n")







                completion_toast  = ToastNotification("Linkedin Bot" , "Request Sending Completed" , 5000)
                completion_toast.show_toast()
                pub.sendMessage("completed")
                sleep(5)
                self.bot.close()
                sys.exit



                
            
    def stop(self):
        self.stop_event.set()
        self.bot.close()
        print("The Thread is stopped")
        sys.exit


