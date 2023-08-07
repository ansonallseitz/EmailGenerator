import tkinter as tk

def print_selection():
    selected = var.get()
    if selected == 1:
        print("It's Windows")
    elif selected == 2:
        print("It's MacOS")

# Create the main window
root = tk.Tk()
root.title("Operating System Selection")

# Create a IntVar to store the selected radio button's value
var = tk.IntVar()

# Create the radio buttons
windows_radio = tk.Radiobutton(root, text="Windows", variable=var, value=1)
macos_radio = tk.Radiobutton(root, text="MacOS", variable=var, value=2)

# Pack the radio buttons horizontally
windows_radio.pack(side=tk.LEFT)
macos_radio.pack(side=tk.LEFT)

# Create a button to trigger the print function
print_button = tk.Button(root, text="Print Selection", command=print_selection)
print_button.pack()

root.mainloop()
