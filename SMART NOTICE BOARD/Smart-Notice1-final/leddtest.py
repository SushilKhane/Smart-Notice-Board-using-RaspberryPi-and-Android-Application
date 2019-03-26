import paho.mqtt.client as mqtt
import os
import socket
import ssl
import json
import unicodedata


import time

import Adafruit_CharLCD as LCD

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
    print(notification)
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

    str_pad = " " * 16 
    message = str(notification)[0:40] +"% \n"
    message = str_pad + message 
    lcd.message(message)
    for i in range (0, len(message)):  
        lcd_byte(LCD_LINE_1, LCD_CMD)  
        lcd_text = message[i:(i+15)]  
        lcd_string(lcd_text,1)  
        time.sleep(0.4)  
        lcd_byte(LCD_LINE_1, LCD_CMD)  
        lcd_string(str_pad,1)
    
    

    
##    lcd.clear()
     
  
     
    


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

