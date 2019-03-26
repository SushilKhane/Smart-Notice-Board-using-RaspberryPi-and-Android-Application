import boto3
from botocore.client import Config

ACCESS_KEY_ID = 'AKIAJ6PBFSE7ZKKIPSHQ'
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 'my-notice-board'
FILE_NAME = 'Banner.jpg'


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
