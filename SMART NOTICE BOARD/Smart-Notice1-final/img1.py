from itertools import cycle
import tkinter as tk
import os
from PIL import Image, ImageTk

folder = 'D:\notice\s3-backup'

class slideshow_app(tk.Tk):
    def __init__(self, image_files, x, y):
        tk.Tk.__init__(self)
        self.geometry('+{}+{}'.format(x, y))
        self.picture_canvas = tk.Canvas(self)
        self.picture_canvas.bind("<ButtonPress-1>", self.show_slides)
        self.picture_canvas.pack()
        self.pictures = cycle((ImageTk.PhotoImage(file=image), image)
                              for image in image_files)
        self.picture_display = tk.Label(self.picture_canvas)
        self.picture_display.pack()

    def show_slides(self):
        img_object, img_name = next(self.picture)
        self.picture_display.config(image=img_object)
        self.title(img_name)

    def run(self):
        self.mainloop()


def slideshow(folder):

    pic_paths = []
    for a,b,c in os.walk(folder):
        pic_paths += [os.path.join(a,f) for f in c if f.lower().endswith(('.jpg','.jpeg','png'))]
    pic_paths.sort()

    x = 100
    y = 50

    app = slideshow_app(pic_paths, x, y)
    app.show_slides()
    app.run()

if __name__ == '__main__':
    slideshow(folder)


