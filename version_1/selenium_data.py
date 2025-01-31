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



#### Constants : 
working  = False
progress_value  = 0
progress_text = "I am Progress Text"

# Here the Images to be imported : 
connect_button_image  = "connect.png"
more_button_image = "more.png"
second_connect_button  = "second_connect.png"
add_note_button   = "add_note.png"


# Threading Event which woudl be used to exit from the thread #### 
stop_event  = threading.Event()



class selenium_class():
    
    # Function to save the Errors in text file ### 
    def error_file_working(self , error_message):
        with open("error_file.txt", "w") as file:
                file.write(error_message + "\n")

    def __init__(self , username  , password  , waitseconds , keywords , page_numbers , message_string):

        self.username = username
        self.password  = password
        self.waitseconds  = waitseconds
        self.keywords  = keywords
        self.page_numebrs = int(page_numbers)
        self.link_list  = []
        self.failed_link_files = []
        self.message_string  = message_string



        options  = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        options.add_argument("--disable-webrtc")  # Disable WebRTC
        options.add_argument("--log-level=3")    # Reduce log verbosity

        self.driver = webdriver.Chrome(options=options)


        #### Try Catch block to Login 
        try:
            self.driver.get("https://www.linkedin.com/checkpoint/rm/sign-in-another-account")
            self.driver.maximize_window()
            username  = self.driver.find_element(By.ID , "username")
            username.send_keys(self.username)
            password  = self.driver.find_element(By.ID , "password")
            password.send_keys(self.password)
            sleep(waitseconds // 2)
            self.driver.find_element(By.XPATH , '//*[@id="organic-div"]/form/div[4]/button').click()
            sleep(waitseconds)
        except Exception as login_error:
            self.error_file_working(f"Login Error Unable to Login and Exiting Program :{login_error} ::  {time.time()}")
            sleep(waitseconds)
            self.driver.close()
            sys.exit()
        

        ### Try catch block to serach to the inserted keywords and then save the link in a list 

        try:
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
            
            self.link_list =  list(set(self.link_list))

            with open("link_file.txt", "w") as file:
                for line in self.link_list:
                    file.write(line + "\n")
        except Exception as link_error:
            self.error_file_working(f"Link Error {link_error} :: {time.time()}")
            sleep(waitseconds)
            self.driver.close()
            sys.exit()
        

        #### Iterate from list and with each item try to connect with the user with the custom message #### 
      
        for link in self.link_list:
                pyautogui.moveTo(300 , 300 , 1)
                sleep(1)
                self.driver.get(link)
                sleep(3)
                try:
                            name_element = self.driver.find_element(By.XPATH , '/html/body/div[7]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[1]/span[1]/a/h1')
                            name = name_element.get_attribute('innerText')
                            hi_text  = f"Hi {name},"
                except Exception as name_error:
                            self.error_file_working(f"Unable to get the name of the User : {link} :: {time.time()}")
                            hi_text = "Hi,"
                try:
                    location = pyautogui.locateOnScreen(connect_button_image , confidence=0.9)
                    if location:
                        pyautogui.moveTo(location.left + 50 , location.top + 40 , 1)
                        pyautogui.click()
                        pyautogui.moveTo(1283 , 532 , 1)
                        # note_location  = pyautogui.locateOnScreen(add_note_button , confidence=0.9)
                        # pyautogui.moveTo(note_location.left + 30 , note_location.top + 30 , 1)
                        pyautogui.click()
                        
                        sleep(2)
                        pyautogui.write(hi_text)
                        sleep(3)
                        pyautogui.press("enter")
                        sleep(2)
                        pyautogui.write(self.message_string)
                        sleep(5)
                        pyautogui.moveTo(1614 , 771, 1)
                        pyautogui.click()
                    else:
                        self.failed_link_files.append(link)
                    sleep(waitseconds)
                except Exception as connect_error:
                    sleep(1)
                    self.error_file_working(f"Unable to find the connect button : {connect_error} :: {time.time()}")
    

        ### Where connect button is not visible it saves those links in another list ###
        for link in self.failed_link_files:
            with open("failed_links.txt", "w") as file:
                for line in self.failed_link_files:
                    file.write(line + "\n")


        ### Failed links to be tried again with another button approach #### 
        for link in self.failed_link_files:
            pyautogui.moveTo(300 , 300 , 1)
            sleep(1)
            self.driver.get(link)
            sleep(3)
            try:
                        name_element = self.driver.find_element(By.XPATH , '/html/body/div[7]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[1]/span[1]/a/h1')
                        name = name_element.get_attribute('innerText')
                        hi_text  = f"Hi {name},"
            except Exception as name_error:
                        self.error_file_working(f"Unable to get the name of the User : {time.time()}")
                        hi_text = "Hi,"
            try:
                move_to_location = pyautogui.locateOnScreen(more_button_image , confidence=0.9)
                if move_to_location:
                    pyautogui.moveTo(move_to_location.left + 50 , move_to_location.top + 40 , 1)
                    pyautogui.click()
                    pyautogui.moveTo(910 ,1196 , 2)
                    another_location  = pyautogui.locateOnScreen(second_connect_button , confidence=0.9)
                    pyautogui.moveTo(another_location.left + 10 , another_location.top + 10 , 1)
                    pyautogui.click()
                    pyautogui.moveTo(1287 , 550 , 1)
                    pyautogui.click()
                    sleep(2)
                    pyautogui.write(hi_text)
                    sleep(3)
                    pyautogui.press("enter")
                    sleep(2)
                    pyautogui.write(self.message_string)
                    sleep(5)
                    pyautogui.moveTo(1614 , 771, 1)
                    pyautogui.click()
            except Exception as final_error:
                    self.error_file_working(f"Final Error : {final_error} :: {time.time()}")



    def closing_browser(self):
        self.driver.close()
        sys.exit()
        

def show_message(messsage, duration):
    toast = ToastNotification("Linkedin Bot" , message=messsage , duration=duration)
    toast.show_toast()


#### Function which is called from main script and parameters are passed into it :: which in turn calls the class with the specified arguments #### 
def selenium_bot(username, password , wait_seconds , keywords , page_numbers  , message_string):
    global working
    if not working:
        working = True
        show_message("Starting Bot :" , 2000)
        sleep(3)
        # threading.Thread(selenium_class(username=username , password=password , waitseconds=wait_seconds , keywords=keywords , page_numbers=page_numbers ) , daemon=True).start()
        selenium_class(username=username , password=password , waitseconds=wait_seconds  , keywords=keywords , page_numbers=page_numbers , message_string=message_string)

        # selenium_class(username=username , password=password , waitseconds=wait_seconds)
    else:
        show_message("Bot Already Working" , 3000)


### Function to stop the bot ### 
def stopping_bot():
    global working
    working  = False
    show_message("Stopping Linkedin Bot" , 3000)
    sys.exit()
    





