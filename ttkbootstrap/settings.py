import tkinter as tk 
from tkinter import ttk  
import ttkbootstrap as btk




class Settings():

    def __init__(self , master):
        self.master = master

        '''
        Controls that would be added in the application would be :
        save username textbox
        save password 
        initial and final serach page value
        Delay seconds for the page visit
        keywords textbox and change the textboc from the main page to to combobox
        savebutton to save data to the textbox 


        Theme for the application : 
        dark or light 
        '''

        self.username_textbox = btk.Entry(self.master , width=30 )
        self.password_box  = btk.Entry(self.master , width=30)
        self.keywords_textbox = btk.Entry(self.master , width=30)

        self.theme_checkbox  = btk.Checkbutton(self.master , bootstyle  = "square-toggle" , text="Current Theme : Dark")
        self.save_button  = btk.Button(self.master , text="Save Details")





        ## Pack and Place the data :
        self.username_textbox.pack(side=tk.LEFT , anchor=tk.NW , padx=10 , pady=10)
        self.password_box.pack(side=tk.LEFT , anchor=tk.NW , padx=10 , pady=10)
        self.keywords_textbox.pack(side=tk.LEFT , anchor=tk.NW , padx=10 , pady=10)
        self.theme_checkbox.place(x = 10 , y = 70)
        self.save_button.place(x = 10 , y = 120)


