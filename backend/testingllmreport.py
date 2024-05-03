import mongoDB
import LLM_report
import time  
from datetime import datetime
import json

global uniqueSessionID
uniqueSessionID = "y6iet1gmocedfdphuolx68"

def concat_all_transcript():
    conversationLog = mongoDB.getDataWithUniqueSessionID("conversationLog", uniqueSessionID)
    log_full = ""
    for log in conversationLog['log']:
        if log['user'] == "applicant":
            log_format = "Candidate: " + log['text'] + ". "
            log_full += log_format
        elif log['user'] == "Ai - EVA":
            log_format = "HR: " + log['text']
            log_full += log_format
    return log_full 

mbti_type = "intj" 
concatTranscript = concat_all_transcript()
interviewDate = datetime.today().strftime('%B %d, %Y')
toStoreJson = {
    "InterveweeName": "Desdesdes",
    "InterveweeID": "122ed2",
    "OverallSuitability": 90,
    "InterviewPosition": "IT BUSINESS ANALYST (SUSTAINABILITY)- Fresh Graduates",
    "InterviewDate": interviewDate,
    "RadarChartSummary": "The candidate demonstrated strong technical expertise in ERP systems and toStoreJson analysis, particularly with tools like SAP S/4HANA, Power BI, and SQL. They were exceptionally prepared, showing a thorough understanding of our company's challenges and the wider industry. Their effective communication and collaborative skills, coupled with their adaptability and professionalism, make them a standout candidate and a potential asset to our team.",
}

try:
    ai_report = LLM_report.main(concatTranscript, mbti_type)
    # print(ai_report)
except Exception as e:
    print(f"An error occurred: {e}")
    print("Retrying in 5 seconds...")
    time.sleep(5)
    
toStoreJson["reportData"] = ai_report
print(mongoDB.postData("reportInfo", toStoreJson))