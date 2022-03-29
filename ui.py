from tkinter import *
from tkinter import ttk
import importlib


# Main tkinter window
x = Tk()
x.geometry("400x300")


# Label Widget
b = Label(x, bg="#f5f5f5", bd=4, relief=RAISED, text="With Separator")
b.place(relx=0.01, rely=0.1, relheight=0.8, relwidth=0.2)


# Separator object
separator = ttk.Separator(x, orient='vertical')
separator.place(relx=0.2, rely=0, relwidth=0.2, relheight=1)


# Label Widget
a = Label(x, bg="#f5f5f5", bd=4, relief=RAISED, text="With Separator")
a.place(relx=0.1, rely=0.2, relheight=0.8, relwidth=0.4)


importlib.reload(mainloop())
