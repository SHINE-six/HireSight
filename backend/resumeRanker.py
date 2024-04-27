import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json


def convertBinaryToPdf(data):
    filename = f'resume/resume_out/resume_live.pdf'
    with open(filename, 'wb') as f:
        f.write(data)
        
    return filename

# Extract text from PDFs
def extractTextFromPDF(pdfBinary):
    pdfReader = PyPDF2.PdfReader(pdfBinary)
    text = ""
    for page in pdfReader.pages:
        text += page.extract_text()
    return text


def oneJobDescriptionToOneResume(resumeText, jobDetail):

    concantenatedJobDescription = jobDetail.jobDescription + "\n" + "\n".join(jobDetail.jobSkills)

    # Extract job description features using TF-IDF
    tfidfVectorizer = TfidfVectorizer()

    # Rank resumes based on similarity
    resumeVector = tfidfVectorizer.fit_transform([resumeText])
    jobDescVector = tfidfVectorizer.transform([concantenatedJobDescription])
    similarity = cosine_similarity(jobDescVector, resumeVector)[0][0]

    return similarity


def main_PdfToText(resumeBinary):
    pdfbi = convertBinaryToPdf(resumeBinary)
    text = extractTextFromPDF(pdfbi)
    return text

def main_ResumeSuitability(resumeBinary, jobDetail):
    pdfbi = convertBinaryToPdf(resumeBinary)
    text = extractTextFromPDF(pdfbi)
    return oneJobDescriptionToOneResume(text, jobDetail)


# def rankingOneResume(resumePathForRanking, jobTitleForRanking, jobDescriptionForRanking):
#     # Extract job description features using TF-IDF
#     tfidfVectorizer = TfidfVectorizer()

#     # Rank resumes based on similarity
#     resumeText = extractTextFromPDF(resumePathForRanking)
#     resumeVector = tfidfVectorizer.fit_transform([resumeText])

#     rankedJobDescription = []
#     for jobTitle, jobDescription in zip(jobTitleForRanking, jobDescriptionForRanking):
#         jobDescriptionVector = tfidfVectorizer.transform([jobDescription])
#         similarity = cosine_similarity(resumeVector, jobDescriptionVector)[0][0]
#         rankedJobDescription.append({"jobTitle": jobTitle, "similarity": similarity})

#     rankedJobDescription.sort(key=lambda x: x["similarity"], reverse=True)

#     top3RankedJobDescription = rankedJobDescription[:3]

#     jsonFilename = "rankedOneResumesTest.json"
#     with open(jsonFilename, "w") as jsonfile:
#         json.dump(top3RankedJobDescription, jsonfile, indent=4)

#     return top3RankedJobDescription

