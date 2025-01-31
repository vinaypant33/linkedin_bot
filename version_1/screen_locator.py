# import pyautogui
# from time import sleep


# connect_button  = "connect.png"






# sleep(5)


# # connect_locator  = pyautogui.locateOnScreen(connect_button ,confidence=0.8)

# # print(connect_locator.left)



# while True:
#     print(pyautogui.position())





# import pyautogui

# import time 

# current_time  = time.time()


# while time.time()  - current_time < 10:
#     print("Adasdf")
#     time.sleep(1)


# print("Time passed on")



import time
import pyautogui

# def locate_image_once_with_timeout( image_path, timeout=5):
#         time.sleep(3)
#         start_time = time.time()
#         location = None  # Initialize location to None
#         location = pyautogui.locateOnScreen(image_path)
#         while time.time() - start_time < timeout:
#             if location:  # If image is found, exit the loop
#                 break
#             time.sleep(0.1)  # Add a small delay to avoid busy-waiting
#         return location



# main_image  = "connect.png"


# locate_image_once_with_timeout(image_path=main_image , timeout=6)


print(pyautogui.size())
while True:
    time.sleep(1)
    print(pyautogui.mouseInfo())

