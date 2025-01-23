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

stop_event  = threading.Event()





class selenium_class():

    def locate_image_once_with_timeout(self , image_path, timeout=5):
        start_time = time.time()
        location = None  # Initialize location to None
        location = pyautogui.locateOnScreen(image_path)
        while time.time() - start_time < timeout:
            if location:  # If image is found, exit the loop
                break
            time.sleep(0.1)  # Add a small delay to avoid busy-waiting
        return location

    def __init__(self , username  , password  , waitseconds , keywords , page_numbers ):

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
            self.driver.maximize_window()
            username  = self.driver.find_element(By.ID , "username")
            username.send_keys(self.username)
            password  = self.driver.find_element(By.ID , "password")
            password.send_keys(self.password)
            sleep(waitseconds)
            self.driver.find_element(By.XPATH , '//*[@id="organic-div"]/form/div[4]/button').click()
        except Exception as login_error:
            show_message(f"Login Error Unable to login Exiting Program" , 4000)
            sleep(waitseconds)
            sys.exit()
        
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
            show_message(f"Link Error {link_error}" , 5000)
            sleep(waitseconds)
            sys.exit()
        

      
        for link in self.link_list:
                self.driver.get(link)
                try:
                    location = pyautogui.locateOnScreen(connect_button_image , confidence=0.9)
                    pyautogui.moveTo(location.left + 30 , location.top + 30 , 3)
                    pyautogui.click()
                    # print(location)
                    sleep(waitseconds)
                except Exception as connect_error:
                    show_message(f"Unable to find the connect button trying second method : {connect_error}" , 5000)
                    try:
                        more_button_location  = pyautogui.locateCenterOnScreen(more_button_image , confidence=0.9)
                        pyautogui.moveTo(more_button_location.left + 30, more_button_location.top + 30 , 2)
                        pyautogui.click()
                        # print(more_button_location)
                        sleep(waitseconds)
                    except Exception as move_to_error:
                        show_message(f"Unable to locate any buttons {move_to_error}" , 5000)
                        
    




        # try:
        #     self.driver.get("https://www.linkedin.com/checkpoint/rm/sign-in-another-account")
        # except Exception as driver_error:
        #     show_message(f"Unable to Start Selenium Driver for Chrome {driver_error}")

        # self.driver.maximize_window()

        # try:
        #     username  = self.driver.find_element(By.ID , "username")
        #     username.send_keys(self.username)
        #     password  = self.driver.find_element(By.ID , "password")
        #     password.send_keys(self.password)
        # except Exception as login_error:
        #     show_message(f"Login Error unable to find username or password filed {login_error}")
        #     sys.exit()

        # try:
        #     rememberbox  = self.driver.find_element(By.ID , "rememberMeOptIn-checkbox")
        #     rememberbox.click()
        # except Exception as remember_click:
        #     show_message("Unable to Click the Remember Box" , 3000)
        
        # sleep(waitseconds)
        # try:

        #     self.driver.find_element(By.XPATH , '//*[@id="organic-div"]/form/div[4]/button').click()
        # except Exception as button_error:
        #     show_message("Unable to click the button ( Exiting Program )" , 2000)
        #     self.driver.close()
        #     sys.exit()
        

        # try:
        #     self.driver.minimize_window()
        # ### Searching pages for the Urls :
        #     for i in range(self.page_numebrs):
        #         self.driver.get(f"https://www.linkedin.com/search/results/people/?keywords={self.keywords}&page={i}")
        #         sleep(self.waitseconds / 3)
        #         source  = self.driver.page_source
        #         soup = BeautifulSoup(source, 'html.parser')
        #         links = soup.find_all('a')
        #         for link in links:
        #             href = link.get('href')
        #             if href :
        #                 if "www.linkedin.com/in/" in href:
        #                     self.link_list.append(href)
        # except Exception as visit_error:
        #     show_message(f"Link Save Error : {visit_error}")
    
            

        # self.link_list =  list(set(self.link_list))

        # try:
        #     with open("link_file.txt", "w") as file:
        #         for line in self.link_list:
        #             file.write(line + "\n")
        # except Exception as save_file_error:
        #     show_message(f"Unable to save the file {save_file_error}")
        
        # self.driver.maximize_window()

        # try:
        #     for link in self.link_list:
        #         self.driver.get(link)
        #         # sleep(2)
        #         try:
        #             location = pyautogui.locateCenterOnScreen(connect_button_image , confidence=0.9 , minSearchTime=1)
        #         except Exception as error:
        #             show_message("Link Search Error" , 2000)
        #         if location:
        #             print("Found Data")
        #         else:
        #             print("Not Found")
        #         location = None
        # except Exception as link_error:
        #     show_message(f"Link Error : {link_error}" , 2000)
        
        

        # try:
        #     for link in self.link_list:
        #         self.driver.get(link)
        #         current_time  = time.time()
        #         while time.time() - current_time < 10:
        #             print("Cecking it ")
        #         print("Time Up and done")
        # except Exception as link_error:
        #     show_message(f"Link Error :{link_error}")
    
    # def sending_requestes(self):
    #     try:
    #         for link in self.link_list:
    #             self.driver.get(link)
    #             sleep(2)
    #             location  = self.locate_image_once_with_timeout(connect_button_image , 5)
    #             if location:
    #                 print("Found Data")
    #             else:
    #                 print("Not Found")
    #             start_time  = time.time()
    #             while time.time() - start_time < 10 :
    #                 connect_button_coordinates  = pyautogui.locateOnScreen(connect_button_image , confidence=0.9)
    #                 if connect_button_coordinates:
    #                     pyautogui.moveTo(connect_button_coordinates.left , connect_button_coordinates.top , duration=2)
    #                 else:
    #                     pyautogui.moveTo(848 , 936 , duration=2)
                
    #             try:
    #                 start_time  = time.time()  ### making a timeput as the pyautogui keeps on searching for the button and takes a lot of time in that
    #                 while time.time() - start_time < 10:
    #                     connect_coordinates  = pyautogui.locateOnScreen(connect_button_image , confidence=0.9 , region=(412 , 835 , 652 , 979))
    #                     pyautogui.moveTo(connect_coordinates.left , connect_coordinates.top , duration=2)
    #                     pyautogui.click()
    #                 show_message("Timeout Reached Moving to another profile :" , 2000)
    #             except Exception as connect_button_error:
    #                 show_message(f"Connect Button Error  {connect_button_error}")
    #                 try:
    #                     while time.time() - start_time  < 10:
    #                         more_button_coordinates  = pyautogui.locateOnScreen(more_button_image , confidence=0.9 , region=(412 , 835 , 652 , 979))
    #                         print(more_button_coordinates)
    #                     show_message("Timeout Reached Unable to find the connect button" , 2000)    
    #                 except Exception as more_button_error:
    #                     show_message(f"More Button Error : {more_button_error}")
    #     except Exception as link_error:
    #         show_message("Link Error"  ,2000)



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
        # threading.Thread(selenium_class(username=username , password=password , waitseconds=wait_seconds , keywords=keywords , page_numbers=page_numbers ) , daemon=True).start()
        selenium_class(username=username , password=password , waitseconds=wait_seconds  , keywords=keywords , page_numbers=page_numbers)

        # selenium_class(username=username , password=password , waitseconds=wait_seconds)
    else:
        show_message("Bot Already Working" , 3000)


def stopping_bot():
    global working
    working  = False
    show_message("Stopping Linkedin Bot" , 3000)
    sys.exit()
    





