from tkinter import *
from tkinter import ttk

class EmailWindow:
    def __init__(self):
        window = Tk()
        window.title("Email Generator")
        #function that determines if its windows or Mac, this splits the 16 possibilities into 8. 
        def DetermineOS():
            selected = Os_Var.get()
            if selected == 1:
                WindowsContingencies()
            elif selected == 2:
                MacContingencies()

        def WindowsContingencies():
            selected_problem = ProblemDropdown.get()
            Email_Text.delete('1.0', END)
            first_name = NameEntry.get()
            computer_name = ComputerEntry.get()
            task_number = TaskNumberEntry.get()

            if selected_problem=="Disk Encrypted":
                email_template = f"Hi {first_name}\n\nI'm attempting to reach out because your Windows device named {computer_name} is showing as non-compliant in our database.\nThe issue is that the drive hasn't been encrypted. On Windows that service is called, \"BitLocker.\"\n\nIf you are able to set up BitLocker yourself, please let us know. You will need to have the computer connected to the ND network for 2 hours for it to show as compliant in our database.\n\nIf you need assistance you can call us here at the Help Desk at: 574-631-8111 please, or you can stop by in-person here on campus at 115 Debartolo Hall, our hours are:\nMonday - Thursday: 7:30 a.m. - 6:30 p.m.\nFriday: 7:30 a.m. - 5:00 p.m.\nSaturday: Closed\nSunday: 1:00 p.m. - 5:00 p.m.\n\nPlease refer to the TASK number below while contacting the Help Desk.\nIf neither of those work for you we can also send someone from Help Desk Dispatch to your office on-campus for in person assistance. Please let me know which option would work best for you through the link of the TASK below.\n\nTask Number = {task_number}"
                Email_Text.insert('1.0', email_template)

            elif selected_problem=="OS Firewall Enabled":
                email_template = f"Hi {first_name}\n\nI'm attempting to reach out because your Windows device named {computer_name} is showing as non-compliant in our database.\nThe issue is that the firewall hasn't been enabled.\n\nIf you are able to set up the firewall yourself, please let us know.\nYou will need to have the computer connected to the ND network for 2 hours for it to show as compliant in our database.\n\nIf you need assistance you can call us here at the Help Desk at: 574-631-8111 please, or you can stop by in-person here on campus at 115 Debartolo Hall, our hours are:\n\nMonday - Thursday: 7:30 a.m. - 6:30 p.m.\n\nFriday: 7:30 a.m. - 5:00 p.m.\n\nSaturday: Closed\n\nSunday: 1:00 p.m. - 5:00 p.m.\n\nPlease refer to the TASK number below while contacting the Help Desk. If neither of those work for you we can also send someone from Help Desk Dispatch to your office on-campus for in person assistance.\n\nPlease let me know which option would work best for you through the link of the TASK below.\n\nTask Number = {task_number}"
                Email_Text.insert('1.0', email_template)
            elif selected_problem =="OS Patched":
                email_template = f"Hi {first_name}\n\nI'm attempting to reach out because your Windows device named {computer_name} is showing as non-compliant in our database.\nThe issue is that the operating system hasn't been updated.\n\nIf you are able to update the computer yourself, please let us know. You will need to have the computer connected to the ND network for 2 hours for it to show as compliant in our database.\n\nIf you need assistance you can call us here at the Help Desk at: 574-631-8111 please, or you can stop by in-person here on campus at 115 Debartolo Hall, our hours are:\n\nMonday - Thursday: 7:30 a.m. - 6:30 p.m.\n\nFriday: 7:30 a.m. - 5:00 p.m.\n\nSaturday: Closed\n\nSunday: 1:00 p.m. - 5:00 p.m.\n\nPlease refer to the TASK number below while contacting the Help Desk. If neither of those work for you we can also send someone from Help Desk Dispatch to your office on-campus for in person assistance. Please let me know which option would work best for you through the link of the TASK below.\n\nTask Number = {task_number}"
                Email_Text.insert('1.0', email_template)
            elif selected_problem=="OS Supported":
                email_template = f"Hi {first_name}\n\nI'm attempting to reach out because your Windows device named {computer_name} is showing as non-compliant in our database.\nThe issue is that the operating system hasn't been updated.\n\nIf you are able to update the computer yourself, please let us know. You will need to have the computer connected to the ND network for 2 hours for it to show as compliant in our database.\n\nIf you need assistance you can call us here at the Help Desk at: 574-631-8111 please, or you can stop by in-person here on campus at 115 Debartolo Hall, our hours are:\n\nMonday - Thursday: 7:30 a.m. - 6:30 p.m.\n\nFriday: 7:30 a.m. - 5:00 p.m.\n\nSaturday: Closed\n\nSunday: 1:00 p.m. - 5:00 p.m.\n\nPlease refer to the TASK number below while contacting the Help Desk. If neither of those work for you we can also send someone from Help Desk Dispatch to your office on-campus for in person assistance. Please let me know which option would work best for you through the link of the TASK below.\n\nTask Number = {task_number}"
                Email_Text.insert('1.0', email_template)
 
        def MacContingencies():
            selected_problem = ProblemDropdown.get()
            Email_Text.delete('1.0', END)
            first_name = NameEntry.get()
            computer_name = ComputerEntry.get()
            task_number = TaskNumberEntry.get()
            if selected_problem=="Disk Encrypted":
                email_template = f"Hi {first_name}\n\nI'm attempting to reach out because your Mac OS device named {computer_name} is showing as non-compliant in our database.\nThe issue is that the drive hasn't been encrypted. On Mac that service is called, \"File Vault.\"\n\nIf you are able to set up File Vault yourself, please let us know. You will need to have the computer connected to the ND network for two hours for it to show as compliant in our database.\n\nIf you need assistance you can call us here at the Help Desk at: 574-631-8111 please, or you can stop by in-person here on campus at 115 Debartolo Hall, our hours are:\nMonday - Thursday: 7:30 a.m. - 6:30 p.m.\nFriday: 7:30 a.m. - 5:00 p.m.\nSaturday: Closed\nSunday: 1:00 p.m. - 5:00 p.m.\n\nPlease refer to the TASK number below while contacting the Help Desk. If neither of those work for you we can also send someone from Help Desk Dispatch to your office on-campus for in person assistance. Please let me know which option would work best for you through the link of the TASK below.\n\nTask Number = {task_number}"
                Email_Text.insert('1.0', email_template)               
            elif selected_problem=="OS Firewall Enabled":
                email_template = f"Hi {first_name}\n\nI'm attempting to reach out because your Mac OS device named {computer_name} is showing as non-compliant in our database.\nThe issue is that the firewall hasn't been enabled.\n\nIf you are able to set up the firewall yourself, please let us know. You will need to have the computer connected to the ND network for it to show as compliant in our database.\n\nIf you need assistance you can call us here at the Help Desk at: 574-631-8111"
                Email_Text.insert('1.0', email_template)
            elif selected_problem=="OS Patched":
                email_template = f"Hi {first_name}\n\nI'm attempting to reach out because your Mac OS device named {computer_name} is showing as non-compliant in our database.\nThe issue is that the drive hasn't been encrypted. On Mac that service is called, \"File Vault.\"\n\nIf you are able to set up File Vault yourself, please let us know. You will need to have the computer connected to the ND network for two hours for it to show as compliant in our database.\n\nIf you need assistance you can call us here at the Help Desk at: 574-631-8111 please, or you can stop by in-person here on campus at 115 Debartolo Hall, our hours are:\nMonday - Thursday: 7:30 a.m. - 6:30 p.m.\nFriday: 7:30 a.m. - 5:00 p.m.\nSaturday: Closed\nSunday: 1:00 p.m. - 5:00 p.m.\n\nPlease refer to the TASK number below while contacting the Help Desk. If neither of those work for you we can also send someone from Help Desk Dispatch to your office on-campus for in person assistance. Please let me know which option would work best for you through the link of the TASK below.\n\nTask Number = {task_number}"
                Email_Text.insert('1.0', email_template)
            elif selected_problem=="OS Supported":
                email_template = f"Hi {first_name}\n\nI'm attempting to reach out because your Mac OS device named {computer_name} is showing as non-compliant in our database.\nThe issue is that the computer's operating system is showing as not supported. To be compliant with University IT policy, Mac computers have to run Ventura 13.0.\n\nIf the device is currently in use, can you update it and make sure that it's connected to the ND network for at least 2 hours?\n\nIf the device is several years old, it might not be able to receive the supported OS version. In that case, the device will need to be phased out. Please contact the help desk using the instructions below.\n\nIf you need assistance you can call us here at the Help Desk at: 574-631-8111 please, or you can stop by in-person here on campus at 115 Debartolo Hall, our hours are:\nMonday - Thursday: 7:30 a.m. - 6:30 p.m.\nFriday: 7:30 a.m. - 5:00 p.m.\nSaturday: Closed\nSunday: 1:00 p.m. - 5:00 p.m.\n\nPlease refer to the TASK number below while contacting the Help Desk. If neither of those work for you we can also send someone from Help Desk Dispatch to your office on-campus for in person assistance. Please let me know which option would work best for you through the link of the TASK below.\n\nTask Number = {task_number}"
                Email_Text.insert('1.0', email_template)

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
