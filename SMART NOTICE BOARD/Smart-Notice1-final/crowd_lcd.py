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
    client.subscribe("Crowd_Policy" , 1 )

def on_message(client, userdata, msg):
    print("topic: "+msg.topic)
    print("Payload Data: "+str(msg.payload))
    global notification_json
    notification_json = json.loads(msg.payload)
    print(notification_json)
    global notification
    notification = notification_json["Crowd"]
    #print(notification)
    # Raspberry Pi pin configuration:
    lcd_rs        = 26  # Note this might need to be changed to 21 for older revision Pi's.
    lcd_en        = 19
    lcd_d4        = 13
    lcd_d5        = 06
    lcd_d6        = 05
    lcd_d7        = 11
    lcd_backlight = 4

    

    
    lcd_columns = 16
    lcd_rows    = 2

    
    # Initialize the LCD using the pins above.
    lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                               lcd_columns, lcd_rows, lcd_backlight)

   
    message = "Crowd is : " + str(notification)[0:2]+"% \n" +"In Coach"
    lcd.message(message)
    for i in range(lcd_columns-len(message)):
        time.sleep(0.5)
        lcd.move_right()
    for i in range(lcd_columns-len(message)):
        time.sleep(0.5)
        lcd.move_left()

    
##    lcd.clear()


mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message


# Define the AWS Host Key ; Thing Name defined in AWS IoT; Root Certificate Path; Certificate Path; Private Key Certificate Path
awshost = "a2fqllcdqkq0md.iot.ap-southeast-1.amazonaws.com"
# AWS Port(Default: 8883)
awsport = 8883
# Client ID
clientId = "Crowd_data"
# Thing Name defined in AWS IoT
thingName = "Crowd_data"
# Root Certificate Path
caPath = "crowdrootca.pem"
# Certificate Path
certPath = "b27cc67774-certificate.pem.crt"
# Private Key Certificate Path
keyPath = "b27cc67774-private.pem.key"

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
mqttc.connect(awshost, awsport, keepalive=60)

mqttc.loop_forever()

