import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

from threading import Thread




class Dashboard(ctk.CTk , Thread):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        self.title("Linkedin Bot")
        self.configure(fg_color= "black")
        



        self.mainloop()





if __name__ == '__main__':
    Dashboard()