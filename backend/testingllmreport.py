import mongoDB
import LLM_report_2
import LLM_report
import time  
from datetime import datetime

global uniqueSessionID
uniqueSessionID = "mc53tknse7nf4gliztva24"

def concat_all_transcript():
    t = mongoDB.getDataWithUniqueSessionID("reportData", uniqueSessionID)
    concatAllResult = t['concatAllResult']
    return concatAllResult 

mbti_type = "intj" #get from reportData
concatTranscript = concat_all_transcript()
interviewDate = datetime.today().strftime('%B %d, %Y')


toStoreJson={
    "overallSuitability": None,
    "RadarChartBinaryArray" : None,
    "RadarChartSummary": None,
    "MBTIBinaryArray": None
}

# put chenming formal and tidiness combinedData and get it to main()
try:
    aiReport = None
    if aiReport == None:
        # Vertex Ai    
        aiReport,TechnicalSkillScore, preparation_score, cultural_score, attitude_score, communication_score, adaptability_score = LLM_report.main(concatTranscript, mbti_type) 
        # Genmini Ai
        # ai_report = LLM_report.main(concatTranscript, mbti_type)
    toStoreJson["ai_report"] = aiReport
except Exception as e:
    print(f"An error occurred: {e}")
    print("Retrying in 5 seconds...")
    time.sleep(5)

print("\n\n\nAI Report: ", aiReport)

print("\n\n\nDataForReport + ai report in reportgeneration: ", toStoreJson)

technicalScore = toStoreJson["ai_report"]['TechnicalSkill']['TechnicalSkillScore']

print("technicalScore", technicalScore)

# print(mongoDB.postData("reportInfo", toStoreJson))