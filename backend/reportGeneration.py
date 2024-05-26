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
    aiReport = LLM_report.main(reportData.concatAllResult, reportData.mbti)

    technicalScore = aiReport['TechnicalSkill']['TechnicalSkillScore']
    preparationScore = aiReport['SoftSkill']['PreparationSkill']['PreparationScore']
    culturalScore = aiReport['SoftSkill']['CulturalFitSkill']['CulturalFitScore']
    attitudeScore = aiReport['SoftSkill']['AttitudeSkill']['AttitudeScore']
    communicationScore = aiReport['SoftSkill']['CommunicationSkill']['CommunicationSkillScore']
    adaptabilityScore = aiReport['SoftSkill']['AdaptabilitySkill']['AdaptabilityScore']

    radarChartBinaryArray = radarChart.main(technicalScore, preparationScore, culturalScore, attitudeScore, communicationScore, adaptabilityScore)

    dataForReport={
        "email": reportData.email,
        "id": reportData.uniqueResumeID,
        "InterviewPosition": reportData.interviewPosition,
        "overallSuitability": None,
        "interviewDate": date.today(),
        "radarChartBinaryArray" : radarChartBinaryArray,
        "radarChartSummary": None,
        "aiReport": aiReport
    }
    return dataForReport
    # Add more report generation scripts here