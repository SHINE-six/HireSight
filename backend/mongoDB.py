from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

# ----------------- Connection to MongoDB Atlas ----------------- #
MONGODB_URI = os.getenv('MONGODB_URI')
client = MongoClient(MONGODB_URI)
db = client['HireSight']
print(db.list_collection_names())


# ----------------- Foundation Functions ----------------- #
def get_all_data_from_collection(collection):
    collection = db[collection]
    data = []
    for x in collection.find():
        data.append(x)
    return data

def get_data_with_uniqueSessionID(collection, uniqueSessionID):
    collection = db[collection]
    data = collection.find_one({"uniqueSessionID": uniqueSessionID}, {"_id": 0})
    
    return data

def post_data(collection, data):
    collection = db[collection]
    collection.insert_one(data)
    return {"status": 200, "message": "Data posted successfully!"}

def delete_data(collection, data):
    collection = db[collection]
    collection.delete_one(data)
    return {"status": 200, "message": "Data deleted successfully!"}

def update_data(collection, data):
    collection = db[collection]
    collection.update_one(data)
    return {"status": 200, "message": "Data updated successfully!"}

def append_data_to_document(collection, data: dict, uniqueSessionID: str):
    if (collection == 'conversationLog'):
        collection = db[collection]
        collection.update_one({"uniqueSessionID": uniqueSessionID}, {"$push": {"log": data}})
    elif (collection == 'combinedData'):
        collection = db[collection]
        collection.update_one({"uniqueSessionID": uniqueSessionID}, {"$push": {"sections": data}})


    return {"status": 200, "message": "Data appended successfully!"}

# ----------------- Specific Functions ----------------- #