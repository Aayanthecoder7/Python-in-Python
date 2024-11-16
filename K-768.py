import tkinter as tk
from tkinter import *


root = tk.Tk()
root.geometry("400x400")
root.title("Python in Python")
root.config(bg="Black")

def show_terminal():
    answer = get_entry.get()  
    try:
        result = exec(answer)  
    except Exception as e:
        answwer_label.config(text="Error") 

enter_code = Label(root, text="Enter Python code", bg="Black", fg="White")
enter_code.pack()

use_button = Button(root, text="Click", command=show_terminal)
use_button.pack()

answwer_label = Label(root, text="", bg="Black", fg="White")
answwer_label.pack()

get_entry = Entry(root)
get_entry.pack()

root.mainloop()