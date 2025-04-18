# import ttkbootstrap as btk
# from threading import Thread
# from time import sleep

# from ttkbootstrap.constants import *

# import ctypes
# import os 



# ### Setting up the current directroy in which the script is running as the default directory  : 
# script_dir = os.path.dirname(os.path.abspath(__file__))
# os.chdir(script_dir)

# print(script_dir)


# ### Function for changing the default behaviour of the application : Change the color of the titlebar :
# def set_dark_titlebar(window , mode_numeral = 1):
#     try:
#         window.update_idletasks()
#         hwnd  = ctypes.windll.user32.GetParent(window.winfo_id())
#         DWMWA_USE_IMMERSIVE_DARK_MODE = 20
#         ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, DWMWA_USE_IMMERSIVE_DARK_MODE, ctypes.byref(ctypes.c_int(mode_numeral)), ctypes.sizeof(ctypes.c_int(1)))
#     except Exception as Error:
#         print(f"Facing Error in Changing the Theme of the Application {Error}")

# def change_theme(new_theme):
#     style.configure(new_theme)
#     main_window.tk.call("ttk::theme", "use", new_theme)


# ### App Constants for the application  : 
# window_width  = 900
# window_height = 600
# current_theme   = "darkly"


# ### Later it will read the data from the file and set the configuratins : 
# '''
# Function to set later : 
# the theme name the titlebar color and the background color  based on that : 

# '''
# ### Base Window for the application  : 
# main_window  = btk.Window(themename = current_theme)
# style = btk.Style()

# main_window.iconphoto = r"linkedin_bot.png"

# main_window.resizable(0,0)
# main_window.geometry(f"{window_width}x{window_height}")


# set_dark_titlebar(main_window , 1)


# side_titlebar  = btk.Frame(main_window , height=600 , width=100  ,bootstyle  = 'primary')

# main_frame_1  = btk.Frame(main_window , height=600 , bootstyle  = "warning")








# ### Configuring Controls :
# side_titlebar.pack_propagate(0)
# main_frame_1.pack_propagate(0)





# # Binding Functions :

# def side_titlebar_animation(x , method):
#     print(side_titlebar.winfo_width())

#     # if method  == "expand" and side_titlebar.winfo_width() < 200:
#     #     side_titlebar.confiure(side_titlebar.winfo_width + 1)
#     # side_titlebar_animation("expand")


# ## Binding the Controls : 

# side_titlebar.bind("<Enter>" , side_titlebar)



# ## Packing Controls : 
# side_titlebar.pack(side=btk.LEFT)
# main_frame_1.pack(expand=btk.TRUE , fill=btk.X)








# ### Starting the main Applicatin : 

# main_window.mainloop()



