#!/usr/bin/python3

import tkinter as tk  # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
import sshmul


top = tk.Tk()

from tkinter import messagebox


top.geometry("400x300")
top.wm_title("Welcome")
 
def transferFiles():     
   sshmul.connect()
   
B = tk.Button(top, text ="Copy from device", command = transferFiles)
B.place(x=50,y=50)


top.mainloop()
