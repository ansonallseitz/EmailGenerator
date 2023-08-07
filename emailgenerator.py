from tkinter import *
from tkinter import ttk

class EmailWindow:
    def __init__(self):
        window = Tk()
        window.title("Email Generator")

        def DetermineOS():
            selected = Os_Var.get()
            if selected == 1:
                WindowsContingencies()
            elif selected == 2:
                MacContingencies()

        def WindowsContingencies():
            print("You are using Windows")

        def MacContingencies():
            print("You are using Mac")

        # Title
        label1 = Label(window, text="This is the Email Generating Program")
        label1.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

        # Name Entry
        label2 = Label(window, text="Person's first name")
        NameEntry = Entry(window)
        label2.grid(row=1, column=0, padx=10, sticky="w")
        NameEntry.grid(row=1, column=1, padx=10, pady=5, columnspan=2, sticky="w")

        # Computer name entry
        label3 = Label(window, text="Computer Name")
        ComputerEntry = Entry(window)
        label3.grid(row=2, column=0, padx=10, sticky="w")
        ComputerEntry.grid(row=2, column=1, padx=10, pady=5, columnspan=2, sticky="w")

        # TaskNumberEntry
        label4 = Label(window, text="Task Number")
        TaskNumberEntry = Entry(window)
        label4.grid(row=3, column=0, padx=10, sticky="w")
        TaskNumberEntry.grid(row=3, column=1, padx=10, pady=5, columnspan=2, sticky="w")

        # OS Radio Button
        label5 = Label(window, text="Operating system")
        Os_Var = IntVar()
        label5.grid(row=4, column=0, padx=10, sticky="w")
        WindowsRadio = Radiobutton(window, text="Windows", variable=Os_Var, value=1)
        MacOSRadio = Radiobutton(window, text="MacOs", variable=Os_Var, value=2)
        WindowsRadio.grid(row=4, column=1, pady=5, sticky="w")
        MacOSRadio.grid(row=4, column=2, pady=5, sticky="w")

        # Dropdown box
        label6 = Label(window, text="What is the problem?")
        label6.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        problems = ["Disk Encrypted", "OS Firewall Enabled", "OS Patched", "OS Supported"]
        ProblemDropdown = ttk.Combobox(window, values=problems)
        ProblemDropdown.grid(row=5, column=1, columnspan=2, pady=5, sticky="w")

        # Generate Email Button 
        GenerateEmail = Button(window, text="Generate Email", command=DetermineOS)
        GenerateEmail.grid(row=6, column=3, padx=10, pady=10, sticky="w")

        # Email Output
        label7 = Label(window, text="Email Output")
        label7.grid(row=7, column=0, padx=10, pady=5, sticky="w")
        Email_Text = Text(window, borderwidth=2, relief="solid", height=10, width=60)
        Email_Text.grid(row=8, column=0, columnspan=3, padx=10, pady=5)

        window.mainloop()

if __name__ == "__main__":
    EmailWindow()
