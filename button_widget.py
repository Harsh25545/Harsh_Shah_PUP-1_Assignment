from cgitb import text
from doctest import master
from tkinter import CENTER, NE, mainloop
from tkinter.tix import Tk
from tkinter.ttk import Button

#creating Tk window
master =Tk()
#setting geometry of Tk window
master.geometry("200x200")
#button widget
b1=Button(master,text="Click me!")
b1.place(relx=1,x=2,y=2,anchor=NE)
#button widget
b2=Button(master,text="GFG")
b2.place(relx=0.5,rely=0.5,anchor=CENTER)
mainloop()
