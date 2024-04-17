import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
import csv
import json
import os
import random
import string
import base64
# import mongoDB
import io

# Extract text from PDFs
def extractTextFromPDF(pdfPath):
    with open(pdfPath, "rb") as pdfFile:
        pdfReader = PyPDF2.PdfReader(pdfFile)
        text = ""
        for page in pdfReader.pages:
            text += page.extract_text()
        return text

def extractTextFromPDFMongoDB(pdf_data):
    # Create a BytesIO object from the binary data
    pdf_stream = io.BytesIO(pdf_data)
    
    # Open the PDF file using PyPDF2
    pdfReader = PyPDF2.PdfReader(pdf_stream)
    
    # Extract text from each page
    text = ""
    for page in pdfReader.pages:
        text += page.extract_text()
    
    return text

def generateRandomID(length):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# def oneJobDescriptionToAllResume(jobDescriptionFromUser, jsonFileName):
#     # Get all resumes from the database
#     data = mongoDB.getAllDataFromCollection("resumeDatabase")
#     resumePaths = convertPDFFromBinary(data)

#     result = rankingAllResume(resumePaths, jobDescriptionFromUser, jsonFileName)
#     return result

def allJobDescriptionsToOneResume(resumeFromUser, jobTitleFromUser, jobDescriptionFromUser):
    result = rankingOneResume(resumeFromUser, jobTitleFromUser, jobDescriptionFromUser)
    return result

def oneJobDescriptionToOneResume(resumeFromUser, jobDescriptionFromUser):
    # Extract job description features using TF-IDF
    tfidfVectorizer = TfidfVectorizer()

    # Rank resumes based on similarity
    resumeText = extractTextFromPDF(resumeFromUser)
    resumeVector = tfidfVectorizer.fit_transform([resumeText])
    jobDescVector = tfidfVectorizer.transform([jobDescriptionFromUser])
    similarity = cosine_similarity(jobDescVector, resumeVector)[0][0]

    # dictRankedResumes = {"similarity": similarity}
    # jsonFilename = "rankedOneResumesTest.json"
    # with open(jsonFilename, "w") as jsonfile:
    #     json.dump(dictRankedResumes, jsonfile, indent=4)
    return similarity

def rankingAllResume(resumePathsForRanking, jobDescriptionForRanking, jsonFileName):
    # Extract job description features using TF-IDF
    tfidfVectorizer = TfidfVectorizer()
    jobDescVector = tfidfVectorizer.fit_transform([jobDescriptionForRanking])

    # Rank resumes based on similarity
    rankedResumes = []
    for resumePath in resumePathsForRanking:
        resumeText = extractTextFromPDFMongoDB(resumePath)
        resumeVector = tfidfVectorizer.transform([resumeText])
        similarity = cosine_similarity(jobDescVector, resumeVector)[0][0]
        rankedResumes.append((similarity))

    rankedResumes.sort(reverse=True)
    
    dictRankedResumes = [{"rank": rank, "id":generateRandomID(6), "similarity": similarity} for rank, (similarity) in enumerate(rankedResumes, start=1)]
    jsonFilename = jsonFileName
    with open(jsonFilename, "w") as jsonfile:
        json.dump(dictRankedResumes, jsonfile, indent=4)
    return dictRankedResumes

def rankingOneResume(resumePathForRanking, jobTitleForRanking, jobDescriptionForRanking):
    # Extract job description features using TF-IDF
    tfidfVectorizer = TfidfVectorizer()

    # Rank resumes based on similarity
    resumeText = extractTextFromPDF(resumePathForRanking)
    resumeVector = tfidfVectorizer.fit_transform([resumeText])

    rankedJobDescription = []
    for jobTitle, jobDescription in zip(jobTitleForRanking, jobDescriptionForRanking):
        jobDescriptionVector = tfidfVectorizer.transform([jobDescription])
        similarity = cosine_similarity(resumeVector, jobDescriptionVector)[0][0]
        rankedJobDescription.append({"jobTitle": jobTitle, "similarity": similarity})

    rankedJobDescription.sort(key=lambda x: x["similarity"], reverse=True)

    top3RankedJobDescription = rankedJobDescription[:3]

    jsonFilename = "rankedOneResumesTest.json"
    with open(jsonFilename, "w") as jsonfile:
        json.dump(top3RankedJobDescription, jsonfile, indent=4)

    return top3RankedJobDescription

def convertPDFFromBinary(data):
    resume_paths = []
    for item in data:
        pdf_data_bytes = item["pdf_data"]
        resume_paths.append(pdf_data_bytes)
        
    return resume_paths

# def postDataTOCollection(resumeFile):
#     if resumeFile.filename.endswith(".pdf"):  # Check if the uploaded file is a PDF
#         # Read the uploaded PDF file as binary data
#         pdf_data = resumeFile.file.read()
        
#         # Construct data object to post to the collection
#         resume_data = {
#             "filename": resumeFile.filename,
#             "pdf_data": pdf_data
#         }
        
#         return resume_data
        # Post the resume data to the collection
        # response = mongoDB.postData("resumeDatabase", resume_data)
        
        # return response  # Return the response from the MongoDB operation
    
def getConcatenatedText(jobTitle, data):
    for category in data:
        for job in category["availableJobs"]:
            if job["jobTitle"] == jobTitle:
                concatenated_text = job["jobDescription"] + "\n" + "\n".join(job["jobSkills"])
                return concatenated_text
    return None  # Return None if job title is not found