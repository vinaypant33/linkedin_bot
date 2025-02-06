import tkinter as tk 
from tkinter import ttk  
import ttkbootstrap as btk

from ttkbootstrap.toast import ToastNotification


class Settings():


    def save_details(self):
        self.current_username  = self.username_textbox.get()
        self.current_message  = self.messagebox.get("1.0", "end-1c")
        self.current_keywords = self.keywords_textbox.get()


        self.theme_value  = self.current_theme.get()

        with open("settings.txt" , "w") as settings_file:
            settings_file.write(self.current_username + ":" + self.current_message + ":" + self.current_keywords + ":" + str(self.theme_value))

        message = ToastNotification("Linkedin Bot" , "Values Saved in settings File" , 3000)
        message.show_toast()

        self.username_textbox.delete( 0 ,tk.END)
        self.password_box.delete( 0  , tk.END)
        self.keywords_textbox.delete(0 , tk.END)
        

       

    def value_change(self):

        # print(self.current_theme.get())
        if self.current_theme.get() == True:
            self.theme_checkbox.configure(text="Current Theme : Light")
        else:
            self.theme_checkbox.configure(text="Current Theme : Dark")
        
        ## Check the theme box for current theme : and save in the ehckbox variable for now the variable is dark theme


    def __init__(self , master , old_keyowrds_list  = [] , current_theme  = True):
        self.master = master
        self.keywords_list = []


        if current_theme == False:
            self.current_theme  = btk.BooleanVar(value  = False)
        else:
            self.current_theme = btk.BooleanVar(value=True)



        # This to be changed later Will replace this with the actual database : Sqlite
        for each in old_keyowrds_list:
            self.keywords_list.append(each)
        
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

        self.theme_checkbox  = btk.Checkbutton(self.master , bootstyle  = "square-toggle" , text="Current Theme :" , variable=self.current_theme  , command=self.value_change)

        self.messagebox  = btk.Text(self.master , height=20)

        self.save_button  = btk.Button(self.master , text="Save Details" , command=self.save_details )


        ## Pack and Place the data :
        self.username_textbox.pack(side=tk.LEFT , anchor=tk.NW , padx=10 , pady=10)
        self.password_box.pack(side=tk.LEFT , anchor=tk.NW , padx=10 , pady=10)
        self.keywords_textbox.pack(side=tk.LEFT , anchor=tk.NW , padx=10 , pady=10)
        self.theme_checkbox.place(x = 10 , y = 70)
        self.save_button.place(x = 10 , y = 120)
        self.messagebox.place(x = 10 , y  = 180)


