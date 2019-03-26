from tkinter import *
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json
import boto3
from botocore.client import Config
import sys



top = Tk()

d = {}
notice= ''

def publish():
    notice = E1.get()
    print(notice)
    myMQTTClient = AWSIoTMQTTClient("notice_test")
    # For Websocket connection
    # myMQTTClient = AWSIoTMQTTClient("myClientID", useWebsocket=True)
    # Configurations
    # For TLS mutual authentication
    myMQTTClient.configureEndpoint("a3a5pcpsjom1dy.iot.ap-southeast-1.amazonaws.com", 8883)
    # For Websocket
    # myMQTTClient.configureEndpoint("YOUR.ENDPOINT", 443)
    myMQTTClient.configureCredentials("root-CA.pem", "aff2972e7a-private.pem.key", "aff2972e7a-certificate.pem.crt")
    # For Websocket, we only need to configure the root CA
    # myMQTTClient.configureCredentials("YOUR/ROOT/CA/PATH")
    myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
    myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
    myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
    myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

    d = {'message': notice}
    data = json.dumps(d)
    myMQTTClient.connect()
    myMQTTClient.publish("MyNotice", data, 0)

    myMQTTClient.disconnect()

    
L1 = Label(top, text = 'Enter the notice:')
L1.grid(row=1,column=1)
E1 = Entry(top, bd =5)
E1.grid(row=1, column=2)


b1 = Button(top, text='Publish', command=publish)
b1.grid(row=2, column=1)

def upload():
    
    ACCESS_KEY_ID = 'AKIAJ6PBFSE7ZKKIPSHQ'
    ACCESS_SECRET_KEY = '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'
    BUCKET_NAME = 'my-notice-board'
    FILE_NAME = E2.get()


    data = open(FILE_NAME, 'rb')

    # S3 Connect
    s3 = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        config=Config(signature_version='s3v4')
    )

    # Image Uploaded
    s3.Bucket(BUCKET_NAME).put_object(Key=FILE_NAME, Body=data, ACL='public-read')

    print ("Done")

    

L2 = Label(top, text ='Upload Image')
L2.grid(row = 3 ,column = 1)
E2 = Entry(top,bd=5)
E2.grid(row=3, column=2)

b2 = Button(top, text='Upload',command =upload)
b2.grid(row=4, column=1)

       
top.mainloop()


#d = {'key': 'value'}
    
   
