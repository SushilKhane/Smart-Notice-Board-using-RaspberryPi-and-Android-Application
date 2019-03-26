from tkinter import *
from itertools import cycle

class WindowOne(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()
        self.CreateBut = Button(text = "Add Window",
                                command = self.addWindow)
        self.CreateBut.pack()

    def addWindow(self):
        newWindow = Tk()
        appTwo = WindowTwo(newWindow)


class WindowTwo(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()
        Label(text = "This is WindowTwo").pack()

root = Tk()
app = WindowOne(root)
root.mainloop()
