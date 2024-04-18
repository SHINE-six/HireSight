from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

# ----------------- Connection to MongoDB Atlas ----------------- #
MONGODB_URI = os.getenv('MONGODB_URI')
client = MongoClient(MONGODB_URI)
db = client['HireSight']
print("Connected to MongoDB Atlas!")


# ----------------- Foundation Functions ----------------- #
def getAllDataFromCollection(collection):
    collection = db[collection]
    data = []
    for x in collection.find():
        data.append(x)
    return data

def getDataWithResume(collection, job_position):
    collection = db[collection]
    data = collection.find_one({"jobPositionApply": job_position})
    
    return data

def getDataWithUniqueSessionID(collection, uniqueSessionID):
    collection = db[collection]
    data = collection.find_one({"uniqueSessionID": uniqueSessionID}, {"_id": 0})
    
    return data

def postData(collection, data):
    collection = db[collection]
    collection.insert_one(data)
    return {"status": 200, "message": "Data posted successfully!"}

def updateData(collection, data):
    collection = db[collection]
    collection.update_one(data)
    return {"status": 200, "message": "Data updated successfully!"}

def appendDataToDocument(collection, data: dict, uniqueSessionID: str):
    if (collection == 'conversationLog'):
        collection = db[collection]
        collection.update_one({"uniqueSessionID": uniqueSessionID}, {"$push": {"log": data}})
    elif (collection == 'combinedData'):
        collection = db[collection]
        collection.update_one({"uniqueSessionID": uniqueSessionID}, {"$push": {"sections": data}})


    return {"status": 200, "message": "Data appended successfully!"}

# ----------------- Specific Functions ----------------- #
#! For maintenance only, should not be connected to server
def deleteFirstTenData(collection):
    collection = db[collection]
    documents = collection.find().limit(10)    
    ids = [doc['_id'] for doc in documents]
    collection.delete_many({'_id': {'$in': ids}})
    return {"status": 200, "message": "Data deleted successfully!"}

