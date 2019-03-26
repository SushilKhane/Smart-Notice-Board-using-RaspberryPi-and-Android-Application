import pymongo
import gridfs
import os
import glob

folder = os.path.join(r'D:\pics')
client = pymongo.MongoClient('localhost', 27017)
database = client.example

#print(folder)
for filename1 in os.listdir(folder):
    #print(filename1)
    file = os.path.join(folder,filename1)
    #print(file)
    datafile = open(file, 'rb')
    data = datafile.read()
    fs = gridfs.GridFS(database)
    stored = fs.put(data, filename=filename1)
    print(stored)
    database.my_collection.insert_one({"imagefile":filename1,"fileid":stored})

'''
outputdata = fs.get(stored).read()
outputfilename = 'outputtest.jpg'
output = open(outputfilename, 'wb')

output.write(outputdata)
output.close()'''

files = database.my_collection.find()

for item in files:
    #print(item.get('imagefile'))
    
    filename2 = item['imagefile']
    fid = item['fileid']
    outputdata = fs.get(fid).read()
    outputfilename = filename2 
    output = open(outputfilename, 'wb')

    output.write(outputdata)
        
    
client.drop_database('example')
client.close()
