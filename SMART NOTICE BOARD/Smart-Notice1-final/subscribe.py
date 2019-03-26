import paho.mqtt.client as mqtt
import os
import socket
import ssl
import json
import unicodedata
import socket
import time

#import Adafruit_CharLCD as LCD
import sqlite3

db = sqlite3.connect('test.db;')
cursor = db.cursor()
cursor.execute("create table if not exists noticee(id INTEGER PRIMARY KEY, data TEXT)")                            



notification_json ={}
notification = ''
def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc) )
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    mqttc.subscribe("MyNotice", 1) 

def on_message(client, userdata, msg):
    #print("topic: "+msg.topic)
    #print("Payload Data: "+str(msg.payload))
    global notification_json
    d = (msg.payload).decode('utf-8')
    notification_json = json.loads(d)
    print(notification_json)
    global notification
    notification = notification_json["message"]
    #print(notification)
    
    cursor.execute("insert into noticee(data) values(?)", (notification,))
    db.commit()
    cursor.execute("select * from noticee ORDER BY id DESC LIMIT 1")
    user = cursor.fetchone()
    print(user[1])    
    '''
    # Raspberry Pi pin configuration:
    lcd_rs        = 26  # Note this might need to be changed to 21 for older revision Pi's.
    lcd_en        = 19
    lcd_d4        = 13
    lcd_d5        = 6
    lcd_d6        = 5
    lcd_d7        = 11
    lcd_backlight = 4

    

    
    lcd_columns = 16
    lcd_rows    = 2

    
    # Initialize the LCD using the pins above.
    lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                               lcd_columns, lcd_rows, lcd_backlight)

   
    message = str(notification)[0:40]
    lcd.message(message)
    for i in range(lcd_columns-len(message)):
        time.sleep(0.5)
        lcd.move_right()
    for i in range(lcd_columns-len(message)):
        time.sleep(0.5)
        lcd.move_left()
    
    
    
##    lcd.clear()
    



   '''
    
mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message


# Define the AWS Host Key ; Thing Name defined in AWS IoT; Root Certificate Path; Certificate Path; Private Key Certificate Path
awshost = "a3a5pcpsjom1dy.iot.ap-southeast-1.amazonaws.com"
# AWS Port(Default: 8883)
awsport = 8883
# Client ID
clientId = "notice_test"
# Thing Name defined in AWS IoT
thingName = "notice_test"
# Root Certificate Path
caPath = "root-CA.pem"
# Certificate Path
certPath = "aff2972e7a-certificate.pem.crt"
# Private Key Certificate Path
keyPath = "aff2972e7a-private.pem.key"

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
mqttc.connect(awshost, awsport, keepalive=60)

mqttc.loop_forever()

