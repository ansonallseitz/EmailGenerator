from tkinter import *
from tkinter import ttk
import tkinter as tk

class emailWindow():

    def __init__(self):
        window = Tk()
        #Title 
        window.title("Email Generator") # set title
        label1 = Label(text ="This is the Emal Generating Program")
        label1.grid(row = 1, column =1)
        

        #Name Entry 
        label2 = Label(text= "Persons first name")
        NameEntry = Entry()
        label2.grid(row =2, column =1)
        NameEntry.grid(row =2, column =2)
        
        #computer name entry 
        label3 = Label(text= "Computer name")       
        ComputerEntry = Entry()
        label3.grid(row =3, column =1)
        ComputerEntry.grid(row =3, column=2)

        #OS Radio Button 
        label4 = Label(text="Operating system")
        Os_Var=IntVar()
        label4.grid(row=4, column=1)
        WindowsRadio= Radiobutton(window, text ="windows", variable=Os_Var, value=1)
        MacOSRadio= Radiobutton(window, text="MacOs", variable=Os_Var, value=2 )
        WindowsRadio.grid(row=4, column=2)
        MacOSRadio.grid(row=4, column=3)


      
        
        #dropdown box
        label5 = Label(text= "what is the problem?")
        problems= ["Disk Encrypted", "OS Firewall Enabled", "OS Patched", "OS Supported"]
        ProblemDropdown = ttk.Combobox(window, values=problems )
        ProblemDropdown.grid(row=5, column=2)
        label5.grid(row=5, column=1)
    

        window.mainloop()
emailWindow()