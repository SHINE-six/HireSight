from pymongo import MongoClient
import json


db = client['HireSight']
print("Connected to MongoDB Atlas database Successfully!")



# ----------------- Foundation Functions ----------------- #
def get_data(collection):
    collection = db[collection]
    data = []
    for x in collection.find():
        data.append(x)
    return data

def post_data(collection, data):
    collection = db[collection]
    collection.insert_one(data)
    return {"status": 200, "message": "Data posted successfully!"}

def delete_data(collection, data):
    collection.delete_one(data)
    return {"status": 200, "message": "Data deleted successfully!"}

def update_data(collection, data):
    collection.update_one(data)
    return {"status": 200, "message": "Data updated successfully!"}

def append_data_to_document(collection, data, document):
    collection.update_one(document, {"$push": data})
    return {"status": 200, "message": "Data appended successfully!"}

# ----------------- Specific Functions ----------------- #

