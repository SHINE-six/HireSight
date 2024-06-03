import time
import LLM_report
import radarChart
from datetime import date
def main(reportData):

    # "name": None, #reportPurpose
    # "id": None,  #reportPurpose
    # "overallSuitability": None, #reportPurpose
    # "interviewDate": None, #reportPurpose
    # "radarChartBinaryArray" : None, #reportPurpose
    # "radarChartSummary": None, #reportPurpose

    print("\n\n\nReportData in reportgeneration: ", reportData)
    dataForReport={
        "uniqueSessionID": reportData['uniqueSessionID'],
        "InterveweeName": reportData['email'],
        "InterveweeID": reportData['uniqueResumeID'],
        "InterviewPosition": reportData['interviewPosition'],
        "overallSuitability": None,
        "InterviewDate": date.today().isoformat(),
        "RadarChartBinaryArray" : None,
        "RadarChartSummary": None,
        "MBTIBinaryArray": None
    }

    print('date: ', dataForReport['InterviewDate'])

    try:
        aiReport = None
        if aiReport == None:
            # Vertex Ai    
            aiReport, TechnicalSkillScore, preparation_score, cultural_score, attitude_score, communication_score, adaptability_score = LLM_report.main(reportData['concatAllResult'], reportData['mbti']) 
            # Genmini Ai
            # ai_report = LLM_report.main(concatTranscript, mbti_type)
            dataForReport["aiReport"] = aiReport
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Retrying in 5 seconds...")
        time.sleep(5)

    print("\n\n\nAI Report: ", aiReport)


    print("\n\n\nDataForReport without ai report in reportgeneration: ", dataForReport)

    if(TechnicalSkillScore == None):
        TechnicalSkillScore = 6.0
    if(preparation_score == None):
        preparation_score = 6.0
    if(cultural_score == None):
        cultural_score = 6.0
    if(attitude_score == None):
        attitude_score = 6.0
    if(communication_score == None):
        communication_score = 6.0
    if(adaptability_score == None):
        adaptability_score = 6.0

    print("technicalScore", TechnicalSkillScore, '\n')
    print("preparationScore", preparation_score, '\n')
    print("culturalScore", cultural_score, '\n')
    print("attitudeScore", attitude_score, '\n')
    print("communicationScore", communication_score, '\n')
    print("adaptabilityScore", adaptability_score, '\n')

    print("technicalScoreType", type(TechnicalSkillScore), '\n')
    print("preparationScoreType", type(preparation_score), '\n')
    print("culturalScoreType", type(cultural_score), '\n')
    print("attitudeScoreType", type(attitude_score), '\n')
    print("communicationScoreType", type(communication_score), '\n')
    print("adaptabilityScoreType", type(adaptability_score), '\n')

    radarChartBinaryArray = radarChart.main(float(TechnicalSkillScore), float(preparation_score), float(cultural_score), float(attitude_score), float(communication_score), float(adaptability_score))

    print("\n\n\nRadarChartBinaryArray in reportgeneration: ", radarChartBinaryArray)

    print("\n\n\nDataForReport in reportgeneration: ", dataForReport)
    return dataForReport
    # Add more report generation scripts here