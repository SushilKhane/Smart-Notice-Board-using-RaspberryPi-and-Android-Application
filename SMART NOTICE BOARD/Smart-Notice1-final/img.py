from Tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()

L1 = Label( side =TOP, text = "Enter The Notice")
L1.pack(side = LEFT)
E1 = Entry(side =TOP ,bd =5)
E1.pack(side = RIGHT)
#img = ImageTk.PhotoImage(Image.open("assets/Newspaper.png"))
#imgLB1 = Label(root, image = img)
#imgLB1.place(relheight = 100 ,relwidth =100)
root.mainloop()
