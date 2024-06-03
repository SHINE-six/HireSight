from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

# ----------------- Connection to MongoDB Atlas ----------------- #
MONGODB_URI = os.getenv('MONGODB_URI')
client = MongoClient(MONGODB_URI)
db = client['HireSight']
print("Connected to MongoDB Atlas!")

'''
Prepare for maintemance refactoring

join getAllDataFromCollection and getOneDataFromCollection and getCollectionCount
'''

# ----------------- Foundation Functions ----------------- #
def getAllDataFromCollection(collection_name, query: dict = None, count: bool = False, exclude: list = None):
    collection = db[collection_name]
    query = query or {}
    exclude = exclude or []

    projection = {"_id": 0}
    for field in exclude:
        projection[field] = 0

    if count:
        return collection.count_documents(query)
    else:        
        data = []
        for x in collection.find(query, projection):
            data.append(x)
        return data

def getOneDataFromCollection(collection, query: dict, exclude: list = None):
    collection = db[collection]
    query = query or {}
    exclude = exclude or []

    projection = {"_id": 0}
    for field in exclude:
        projection[field] = 0
    data = collection.find_one(query, projection)
    return data

def getDataWithUniqueSessionID(collection, uniqueSessionID):
    collection = db[collection]
    data = collection.find_one({"uniqueSessionID": uniqueSessionID}, {"_id": 0})
    
    return data

def postData(collection, data):
    collection = db[collection]
    collection.insert_one(data)
    return {"status": 200, "message": "Data posted successfully!"}

def updateData(collection, query: dict, data: dict):
    collection = db[collection]
    collection.update_one(query, {"$set": data})
    return {"status": 200, "message": "Data updated successfully!"}

def overwriteDocument(collection, query, data):
    collection = db[collection]
    collection.replace_one(query, data)
    return {"status": 200, "message": "Data overwritten successfully!"}

def appendDataToDocument(collection, data: dict, uniqueSessionID: str):
    if (collection == 'conversationLog'):
        collection = db[collection]
        collection.update_one({"uniqueSessionID": uniqueSessionID}, {"$push": {"log": data}})
    elif (collection == 'combinedData'):
        collection = db[collection]
        collection.update_one({"uniqueSessionID": uniqueSessionID}, {"$push": {"sections": data}})


    return {"status": 200, "message": "Data appended successfully!"}

# ----------------- Specific Functions ----------------- #
def getResumeDetailsNoPdf(jobTitle, stage):
    toReturn = {
        "data" : getAllDataFromCollection('resumeDatabase', {'jobPostitionApply': jobTitle, 'stage': stage}, exclude=['pdfData']),
        "count" : getAllDataFromCollection('resumeDatabase', {'jobPostitionApply': jobTitle, 'stage': stage}, count=True)
    }
    return toReturn

def getInterviewDetails(jobTitle, stage):
    resumedetails =  getResumeDetailsNoPdf(jobTitle, stage)
    unique_resume_ids = [resume['uniqueResumeId'] for resume in resumedetails['data']]
    interview_data_list = None
    for unique_id in unique_resume_ids:
        interview_data = getAllDataFromCollection('reportData', {'interviewPosition': jobTitle, 'uniqueResumeID': unique_id})
        if interview_data_list is None:
            interview_data_list = interview_data  # Assuming interview_data is a list
        else:
            interview_data_list.extend(interview_data)
    
    interview_count = getAllDataFromCollection('resumeDatabase', {'jobPostitionApply': jobTitle, 'stage': stage}, count=True)
    
    if interview_data_list is None:
        interview_data_list = []
    
    toReturn = {
        "data": interview_data_list,
        "count": interview_count
    }
    
    return toReturn
    
def getResumeCount(jobTitle):
    # possible stage : 'Ai detection', 'Resume Suitability', 'Interview-ai', 'Interview-hr', 'Offer', 'Rejected'
    Ai_detection_count = getAllDataFromCollection('resumeDatabase', {'jobPostitionApply': jobTitle, 'stage': 'Ai detection'}, count=True)
    Resume_suitability_count = getAllDataFromCollection('resumeDatabase', {'jobPostitionApply': jobTitle, 'stage': 'Resume Suitability'}, count=True)
    # Interview_ai_count = getAllDataFromCollection('resumeDatabase', {'jobPostitionApply': jobTitle, 'stage': 'Interview ai'}, count=True)
    # Interview_hr_count = getAllDataFromCollection('resumeDatabase', {'jobPostitionApply': jobTitle, 'stage': 'Interview hr'}, count=True)

    return {"Ai_detection": Ai_detection_count, "Resume_suitability": Resume_suitability_count}

#! For maintenance only, should not be connected to server
def deleteFirstTenData(collection):
    collection = db[collection]
    documents = collection.find().limit(22)    
    ids = [doc['_id'] for doc in documents]
    collection.delete_many({'_id': {'$in': ids}})
    return {"status": 200, "message": "Data deleted successfully!"}
