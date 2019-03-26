from google.cloud import storage
from firebase import firebase 
import os
from oauth2client.client import GoogleCredentials
from google.cloud.storage import blob
    
storage_client = storage.Client.from_service_account_json('Notice-818fa150ed19.json')
firebase = firebase.FirebaseApplication('https://notice-64ce2.firebaseio.com/')
bucket = storage_client.get_bucket("notice-64ce2.appspot.com")

blobs = list(bucket.list_blobs())
for blob in blobs:
    print(blobs)
    blob.download_to_filename(blob.name)
print("done")
