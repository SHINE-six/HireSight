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
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text

def generate_random_id(length):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def main(pdf_directory_from_user):
    pdf_directory = pdf_directory_from_user

    pdf_files = os.listdir(pdf_directory)

    resume_paths=[]

    for filename in pdf_files:
        fullpath = os.path.join(pdf_directory, filename)
        resume_paths.append(fullpath)

    # Sample job description
    job_description = "jobDescription:  Scrum Master is responsible for ensuring that the team follows the rules of Scrum, and helps the team to continuously improve their process. jobSkills :Scrum, Agile, Kanban, Jira."

    result = ranking(resume_paths, job_description)
    return result


def ranking(resume_paths_1, jd):
    # Extract job description features using TF-IDF
    tfidf_vectorizer = TfidfVectorizer()
    job_desc_vector = tfidf_vectorizer.fit_transform([jd])

    # Rank resumes based on similarity
    ranked_resumes = []
    for resume_path in resume_paths_1:
        resume_text = extract_text_from_pdf(resume_path)
        resume_vector = tfidf_vectorizer.transform([resume_text])
        similarity = cosine_similarity(job_desc_vector, resume_vector)[0][0]
        ranked_resumes.append((similarity))

    ranked_resumes.sort(reverse=True)



    dict_ranked_resumes = [{"rank": rank, "id":generate_random_id(6), "similarity": similarity} for rank, (similarity) in enumerate(ranked_resumes, start=1)]
    json_filename = "ranked_resumes_test.json"
    with open(json_filename, "w") as jsonfile:
        json.dump(dict_ranked_resumes, jsonfile, indent=4)
    return dict_ranked_resumes


