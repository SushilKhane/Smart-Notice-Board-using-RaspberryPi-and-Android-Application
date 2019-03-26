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


def download():
    
    ACCESS_KEY_ID = 'AKIAJ6PBFSE7ZKKIPSHQ'
    ACCESS_SECRET_KEY = '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'
    BUCKET_NAME = 'my-notice-board'

    DOWNLOAD_LOCATION_PATH = r"D://notice" + "//s3-backup//"
    if not os.path.exists(DOWNLOAD_LOCATION_PATH):
        print ("Making download directory")
        os.mkdir(DOWNLOAD_LOCATION_PATH)
                        
                    
    # S3 Connect
    s3 = boto3.resource('s3',aws_access_key_id=ACCESS_KEY_ID,aws_secret_access_key=ACCESS_SECRET_KEY,config=Config(signature_version='s3v4'))
            
    # Image download
    #s3.Bucket(BUCKET_NAME).download_file(FILE_NAME, 'downloads/Banner.jpg'); # Change the second part
    # This is where you want to download it too.
    my_bucket = s3.Bucket(BUCKET_NAME)
    for object in my_bucket.objects.all():
        file1 = object.key
        DOWNLOAD_LOCATION_PATH1 = r"D://notice" + "//s3-backup// " + file1
        if not os.path.exists(DOWNLOAD_LOCATION_PATH1):

            #img_list.append(DOWNLOAD_LOCATION_PATH1)
            s3.Bucket(BUCKET_NAME).download_file(file1, DOWNLOAD_LOCATION_PATH1)
            size = 300,300
            img2 = PIL.Image.open(DOWNLOAD_LOCATION_PATH1)
            img2.thumbnail(size,PIL.Image.ANTIALIAS)
            img2.save(DOWNLOAD_LOCATION_PATH1,'PNG')
            #image_files = img_list
            #print(DOWNLOAD_LOCATION_PATH1)
            return image_files

        else:
            #print("no download")
            print('downloading')

    self.after(6000,self.download)

