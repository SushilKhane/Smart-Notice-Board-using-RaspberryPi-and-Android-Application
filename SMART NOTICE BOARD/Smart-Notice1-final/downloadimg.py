import boto3
from botocore.client import Config
from PIL import Image
from PIL import ImageTk
from tkinter import *
from itertools import cycle
import io
import glob
import os
import sys

import PIL


self =Tk()

class app(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.config(bg='black')
        
        global img_list, image_files
        img_list, image_files = [], []

        self.downloading()
        self.image123()
    def downloading(self):
        ACCESS_KEY_ID = 'AKIAJ6PBFSE7ZKKIPSHQ'
        ACCESS_SECRET_KEY = '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'
        BUCKET_NAME = 'my-notice-board'

        DOWNLOAD_LOCATION_PATH = r"D://notice" + "//s3-backup//"
        if not os.path.exists(DOWNLOAD_LOCATION_PATH):
            print ("Making download directory")
            os.mkdir(DOWNLOAD_LOCATION_PATH)
                    
                
        # S3 Connect
        s3 = boto3.resource('s3',aws_access_key_id=ACCESS_KEY_ID,aws_secret_access_key=ACCESS_SECRET_KEY,config=Config(signature_version='s3v4'))
        
        
        my_bucket = s3.Bucket(BUCKET_NAME)
        for object in my_bucket.objects.all():
            file1 = object.key
            
            DOWNLOAD_LOCATION_PATH1 = r"D://notice" + "//s3-backup// " + file1
            img_list.append(DOWNLOAD_LOCATION_PATH1)
            s3.Bucket(BUCKET_NAME).download_file(file1, DOWNLOAD_LOCATION_PATH1)
            size = 300,300
            img2 = PIL.Image.open(DOWNLOAD_LOCATION_PATH1)
            img2.thumbnail(size,PIL.Image.ANTIALIAS)
            img2.save(DOWNLOAD_LOCATION_PATH1,'PNG')
            image_files = img_list
        return image_files
            
        self.after(6000,self.downloading)
      
    def image123(self):
        image_files = self.downloading()
        print("123")
        print (image_files)
        self.x = 256
        self.y = 256
        self.delay = 2000
        print("inside 123")
        print(image_files)
        picture_display.destroy()
        self.pictures = cycle((self.photo_image(image), image) for image in image_files)
        self.picture_display = Label(self)
        self.picture_display.pack()
        self.show_slides()
        self.after(6000, self.image123)

    def show_slides(self):

        img_object, img_name = next(self.pictures)
        self.picture_display.config(image=img_object)
        self.after(self.delay, self.show_slides)


    def photo_image(self, jpg_filename):

        with io.open(jpg_filename, 'rb') as ifh:
            pil_image = Image.open(ifh)
            return ImageTk.PhotoImage(pil_image)



# get a series of gif images you have in the working folder
# or use full path, or set directory to where the images are



self.mainloop()
