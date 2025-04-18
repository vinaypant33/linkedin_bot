import ttkbootstrap as btk
import time
from threading import Thread






class Dashboard():

    def __init__(self , master ) -> None:


        ### Static variables for the controls  :
        self.username_var = btk.StringVar(value="Enter Username")
        self.password_var = btk.StringVar(value="Enter Password")
        self.checkvar  = btk.BooleanVar(value=False)
        self.page_depth_variable_initial  = btk.IntVar(value=0)
        self.page_depth_variable_final  = btk.IntVar(value = 3)
        self.retries_variable  = btk.IntVar(value  = 10)
        self.keywords_var  = btk.StringVar(value="Enter Keywords")
        
        ## Controls for the dashboard :
        self.username_box  = btk.Entry(master = master  , textvariable=self.username_var , width=31 )

        # Configuring Controls  : 
        # self.username_box.insert(0, self.username_var.get())
        self.username_box.insert(0, "Enter Username and the passwrod")

        ## Packing Controls : 
        self.username_box.pack()





if __name__ == "__main__":
    main_window  = btk.Window()
    Dashboard(master = main_window)

    main_window.mainloop()