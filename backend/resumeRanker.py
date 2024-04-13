import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
import csv
import json
import os
import random
import string

# Extract text from PDFs
def extractTextFromPDF(pdfPath):
    with open(pdfPath, "rb") as pdfFile:
        pdfReader = PyPDF2.PdfReader(pdfFile)
        text = ""
        for page in pdfReader.pages:
            text += page.extract_text()
        return text

def generateRandomID(length):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def oneJobDescriptionToAllResume(pdfDirectoryFromUser, jobDescriptionFromUser):
    pdfDirectory = pdfDirectoryFromUser

    pdfFiles = os.listdir(pdfDirectory)

    resumePaths=[]

    for filename in pdfFiles:
        fullpath = os.path.join(pdfDirectory, filename)
        resumePaths.append(fullpath)

    # Sample job description
    jobDescription = jobDescriptionFromUser

    result = rankingAllResume(resumePaths, jobDescription)
    return result

def allJobDescriptionsToOneResume(resumeFromUser, jobTitleFromUser, jobDescriptionFromUser):
    result = rankingOneResume(resumeFromUser, jobTitleFromUser, jobDescriptionFromUser)
    return result

def rankingAllResume(resumePathsForRanking, jobDescriptionForRanking):
    # Extract job description features using TF-IDF
    tfidfVectorizer = TfidfVectorizer()
    jobDescVector = tfidfVectorizer.fit_transform([jobDescriptionForRanking])

    # Rank resumes based on similarity
    rankedResumes = []
    for resumePath in resumePathsForRanking:
        resumeText = extractTextFromPDF(resumePath)
        resumeVector = tfidfVectorizer.transform([resumeText])
        similarity = cosine_similarity(jobDescVector, resumeVector)[0][0]
        rankedResumes.append((similarity))

    rankedResumes.sort(reverse=True)
    
    dictRankedResumes = [{"rank": rank, "id":generateRandomID(6), "similarity": similarity} for rank, (similarity) in enumerate(rankedResumes, start=1)]
    jsonFilename = "ranked_resumes_test.json"
    with open(jsonFilename, "w") as jsonfile:
        json.dump(dictRankedResumes, jsonfile, indent=4)
    return dictRankedResumes

def rankingOneResume(resumePathForRanking, jobTitleForRanking, jobDescriptionForRanking):
    # Extract job description features using TF-IDF
    tfidfVectorizer = TfidfVectorizer()

    # Rank resumes based on similarity
    resumeText = extractTextFromPDF(resumePathForRanking)
    resumeVector = tfidfVectorizer.transform([resumeText])

    rankedJobDescription = []
    for jobTitle, jobDescription in zip(jobTitleForRanking, jobDescriptionForRanking):
        jobDescriptionVector = tfidfVectorizer.transform([jobDescription])
        similarity = cosine_similarity(jobDescriptionVector, resumeVector)[0][0]
        rankedJobDescription.append({"jobTitle": jobTitle, "jobDescription": jobDescription, "similarity": similarity})

    rankedJobDescription.sort(key=lambda x: x["similarity"], reverse=True)

    # jsonFilename = "ranked_resumes_test.json"
    # with open(jsonFilename, "w") as jsonfile:
    #     json.dump(rankedJobDescription, jsonfile, indent=4)
    return json.dump(rankedJobDescription, indent=4)
