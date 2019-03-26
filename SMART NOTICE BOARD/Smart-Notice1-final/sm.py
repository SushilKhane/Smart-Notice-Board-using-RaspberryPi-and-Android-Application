
# requirements
# requests, feedparser, traceback, Pillow

import sys
from tkinter import *
import locale
import threading
import time
import calendar
import requests
import json
import traceback
import feedparser
import datetime
import paho.mqtt.client as mqtt
import os
import socket
import ssl
import unicodedata
import sqlite3

global d


from PIL import Image, ImageTk
from contextlib import contextmanager

root = Tk()
def notice():
    
                #self.noticeContainer.destroy()
    d = StringVar()
    db = sqlite3.connect('test.db;')
    cursor = db.cursor()
    cursor.execute("select * from noticee ORDER BY id DESC LIMIT 1")
    user = cursor.fetchall()
    print(user[1])
    d = user[1]
    print(d)
    noticeLb2 = Label( root, text = d)
    noticeLb2.grid(row =2 ,column = 1 )


noticeLbl = Label( root, text = 'Notice')
noticeLbl.grid(row =1 ,column = 1 )


        #noticeLbl = Label( text = d, font=('Helvetica', medium_text_size), fg="white", bg="black")
        #noticeLbl.pack(side=TOP , anchor=S)

        
        
        #self.after(6000, self.get_notice)
        #notice
       # self.notice = notice(self.topFrame)
       # self.notice.pack(side=LEFT ,anchor=N , padx=60, pady=60)
        
    

root.mainloop()
