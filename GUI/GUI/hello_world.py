import tkinter as tk
from tkinter import ttk  # Import ttk for themed widgets such as Button, Label, etc.


root = tk.Tk() # Create the main window

greet_button = ttk.Button(root, text="Greet", command=lambda: print("Hello, World!"))  # Create a button that prints a greeting
greet_button.pack(side="left",fill="both", expand=True) # Pack the button into the window

quite_button = ttk.Button(root, text="Quit", command=root.destroy)  # Create a button that closes the application
quite_button.pack(side="left", fill="both", expand=True)  # Pack the quit button into the window


root.title("Hello World GUI")  # Set the title of the window
root.geometry("300x200")  # Set the size of the window
root.mainloop() # Start the Tkinter event loop




