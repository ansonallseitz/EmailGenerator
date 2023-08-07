from tkinter import *
from tkinter import ttk
import tkinter as tk

class emailWindow():

    def __init__(self):
        window = Tk()
        #Title 
        window.title("Email Generator") # set title
        label1 = Label(window, text ="This is the Email Generating Program")
        label1.grid(row = 0, column =1,columnspan=3, padx=10, pady=10)  

                
        
      #Name Entry 
        label2 = Label(window, text= "Persons first name")
        NameEntry = Entry(window)
        label2.grid(row=1, column =0, padx=10, sticky="w")
        NameEntry.grid(row =1, column =1, padx=10, pady=5, columnspan=2, sticky="w")
           

        #computer name entry 
        label3 = Label(window, text= "Computer name")       
        ComputerEntry = Entry(window)
        label3.grid(row =2, column =0, padx=10, sticky="w")
        ComputerEntry.grid(row =2, column=1, padx=10, pady=5, columnspan=2, sticky="w")

        #OS Radio Button 
        label4 = Label(window, text="Operating system")
        Os_Var=IntVar()
        label4.grid(row=3, column=0, padx=10, sticky="w")
        WindowsRadio= Radiobutton(window, text ="windows", variable=Os_Var, value=1)
        MacOSRadio= Radiobutton(window, text="MacOs", variable=Os_Var, value=2 )
        WindowsRadio.grid(row=3, column=1, pady=5, sticky="w")
        MacOSRadio.grid(row=3, column=2, pady=5, sticky="w")


        #dropdown box
        label5 = Label(window, text= "what is the problem?")
        label5.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        problems= ["Disk Encrypted", "OS Firewall Enabled", "OS Patched", "OS Supported"]
        ProblemDropdown = ttk.Combobox(window, values=problems )
        ProblemDropdown.grid(row=4, column=1, columnspan=2, pady=5, sticky="w")        

        #EmailOutput
        label6 =Label(window, text= "Email Output")
        label6.grid(row=5, column=0, padx=10, sticky="w")
        Email_Text = Text(window, borderwidth=2, relief="solid", height=10, width=60 )
        Email_Text.grid(row=6, column=0, columnspan=3, padx=10, pady=5)
    

        window.mainloop()
emailWindow()