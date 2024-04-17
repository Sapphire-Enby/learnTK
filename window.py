#!/usr/bin/env python3

# ChatGPT
# ~2 minutes

    # To create a prompt for 
    # selecting a directory 
        # using Tkinter, 

    # you can use the tkinter.filedialog module. 
    # Here's a step-by-step guide on how to do it:

    # Import the required modules:

import tkinter as tk
from tkinter import filedialog

    # Create a Tkinter window:

root = tk.Tk()
root.geometry("800x600")#window dimensions

    # Define a function to handle the directory selection:
def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        print("Selected directory:", directory)
    else:
        print("No directory selected.")

    #Create a button to trigger the directory selection:

select_button = tk.Button(root, text="Select Directory", command=select_directory)
select_button.pack()

#
    #Run the Tkinter event loop:
root.mainloop()
    # This will create a window 
    # with a button labeled 
        #"Select Directory"
        
    #When you click the button, 
        #a directory selection dialog will open,  
        #After selecting a directory, 
        #the path will be printed to the console.
