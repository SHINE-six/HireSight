import google.generativeai as genai
from dotenv import load_dotenv
import os
import re
import json

#  set GOOGLE_APPLICATION_CREDENTIALS= C:\HireMeModel\HireSight\backend\GOOGLE_APPLICATION_CRED.json changign to the vertex ai
load_dotenv()
 
# Configure the SDK with your API key by recovering the API key from a config file
GENAI_API_KEY = os.getenv('GENAI_API_KEY')
genai.configure(api_key= GENAI_API_KEY)
 
# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.6,
  "top_k": 1,
  "max_output_tokens": 200,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config)
                              #safety_settings=safety_settings)

def generate_technical(text):
    prompt = f"""
    TechnicalSkill Content:
    1. Rate the Technical Skills Rating 1 to 5 marks with one decimal.
    2. Generate a fifty words assessment summary about Tehcnical Skills of the following interview conversation: {text}. The assessment summary only can write pronoun as 'the applicant' and 'his/her'.
    3. TechnicalSkillScore and TechnicalSkillSummary should not be empty.
    "TechnicalSkillScore": ,  
    "TechnicalSkillSummary": ""
    """
    summary = model.generate_content(prompt)
    # print(summary)
    technical_assessment = summary.text
    # print(technical_assessment)
    match1 = re.search(r'"TechnicalSkillScore": (\d+(\.\d+)?)', technical_assessment)
    TechnicalSkillScore = float(match1.group(1))
    match2 = re.search(r'"TechnicalSkillSummary": "(.*)"', technical_assessment)
    TechnicalSkillSummary = match2.group(1)
    # print("TechnicalSkillScore:", TechnicalSkillScore)
    # print("TechnicalSkillSummary:", TechnicalSkillSummary)
    return TechnicalSkillScore, TechnicalSkillSummary

def generate_preparation(text):
    prompt = f"""
    PreparationSkill Content:
    1. Make the PreparationScore by calculate the PreparationScore = [(Knowledge of the Company, Role, and Industry Rating * 30%) + (Quality of Questions for the Interviewer Rating * 25%) + (Alignment of Skills and Experiences with Job Requirements Rating * 25%) + (Formal and Appropriate Attire Rating * 10%) + (Grooming and Tidiness Rating * 10%)]
    2. Rate the Knowledge of the Company, Role, and Industry 1 to 5 marks by evaluate how well the candidate understands the company's mission, the specifics of the role, and industry dynamics.
    3. Rate the Quality of Questions for the Interviewer 1 to 5 marks by evaluate the depth and relevance of the questions asked by the candidate, indicating their engagement and preparation. If the candidate have not ask any question will be 0.
    4. Rate the Alignment of Skills and Experiences with Job Requirements 1 to 5 marks by evaluate the candidate's ability to articulate how their background aligns with the role's requirements. 
    5. Only the PreparationScore with one decimal. The Knowledge of the Company, Role, and Industry, Quality of Questions for the Interviewer, Alignment of Skills and Experiences with Job Requirements, Formal and Appropriate Attire and Grooming and Tidiness are integer.
    6. Generate a fifty words assessment summary for Soft Skills of the following interview conversation: {text}. The assessment summary only can write pronoun as 'the applicant' and 'his/her'.
    7. PreparationScore, Knowledge of the Company, Role, and Industry, Quality of Questions for the Interviewer,Alignment of Skills and Experiences with Job Requirements, PreparationSummary should not be empty.
    "PreparationScore": ,
    "Knowledge of the Company, Role, and Industry": ,
    "Quality of Questions for the Interviewer": ,
    "Alignment of Skills and Experiences with Job Requirements": ,
    "PreparationSummary": ""
    """
    summary = model.generate_content(prompt)
    # print(summary)
    preparation_skill = summary.text
    # print(preparation_skill)
    match3 = re.search(r'"PreparationScore": (\d+(\.\d+)?)', preparation_skill)
    preparation_score = float(match3.group(1))
    match4 = re.search(r'"Knowledge of the Company, Role, and Industry": (\d+(\.\d+)?)', preparation_skill)
    if match4:
        knowledge_company_role_industry = match4.group(1)
    match5 = re.search(r'"Quality of Questions for the Interviewer": (\d+(\.\d+)?)', preparation_skill)
    if match5:
        quality_of_questions = match5.group(1)
    match6 = re.search(r'"Alignment of Skills and Experiences with Job Requirements": (\d+(\.\d+)?)', preparation_skill)
    if match6:
        alignment_with_job_requirements = match6.group(1)
    # match7 = re.search(r'"Formal and Appropriate Attire": (\d+(\.\d+)?)', preparation_skill)
    # if match7:
    #     formal_attire = match7.group(1)
    # match8 = re.search(r'"Grooming and Tidiness": (\d+(\.\d+)?)', preparation_skill)
    # if match8:
    #     grooming_tidiness = match8.group(1)
    match9 = re.search(r'"PreparationSummary": "([^"]+)"', preparation_skill)
    if match9:
        preparation_summary = match9.group(1)
    # print("Preparation Score:", preparation_score)
    # print("Knowledge of the Company, Role, and Industry:", knowledge_company_role_industry)
    # print("Quality of Questions for the Interviewer:", quality_of_questions)
    # print("Alignment of Skills and Experiences with Job Requirements:", alignment_with_job_requirements)
    # print("Formal and Appropriate Attire:", formal_attire)
    # print("Grooming and Tidiness:", grooming_tidiness)
    # print("Preparation Summary:", preparation_summary)
    return preparation_score, knowledge_company_role_industry, quality_of_questions, alignment_with_job_requirements, preparation_summary

def generate_culturalfit(text):
    prompt = f"""
    CulturalFitSkill Content:
    1. Make the CulturalFitScore with one decimal by calculate the CulturalFitScore = [(Alignment with Core Company Values * 30%) + (Professionalism and Work Ethic * 20%) + (Teamwork and Collaboration Style * 20%) + (Adaptability to Work Environment Preferences * 15%) + (Problem-Solving and Decision-Making Style * 15%)].
    2. Generate the Alignment with Core Company Values Ranking 1 to 5 marks by assessing the comprehension of the company's fundamental principles in professional behavior and choices.
    3. Generate the Professionalism and Work Ethic Ranking 1 to 5 marks by evaluating dedication, reliability, and responsibility in a professional environment, including meeting commitments and deadlines.
    4. Generate the Teamwork and Collaboration Style Ranking 1 to 5 marks by assessing preference for collaborative or solitary work, communication effectiveness, and contribution to team goals.
    5. Generate the Adaptability to Work Environment Preferences Ranking 1 to 5 marks by evaluating adaptability to different work settings (remote, hybrid, or on-site) and ability to maintain productivity.
    6. Generate the Problem-Solving and Decision-Making Style Ranking 1 to 5 marks by assessing problem-solving approach, creativity, critical thinking, and conflict resolution.
    7. Only the CulturalFitScore with one decimal. The Alignment with Core Company Values, Professionalism and Work Ethic, Teamwork and Collaboration Style, Adaptability to Work Environment Preferences and Problem-Solving and Decision-Making Style are integer.
    8. Generate a fifty words assessment summary for Cultural Fit of the following interview conversation: {text}. The assessment summary only can write pronoun as 'the applicant' and 'his/her'.
    9. CulturalFitScore, Alignment with Core Company Values, Professionalism and Work Ethic, Teamwork and Collaboration Style, Adaptability to Work Environment Preferences and Problem-Solving and Decision-Making Style should not be empty.
    "CulturalFitScore": ,
    "Alignment with Core Company Values" : ,
    "Professionalism and Work Ethic" : ,
    "Teamwork and Collaboration Style" : ,
    "Adaptability to Work Environment Preferences" : ,
    "Problem-Solving and Decision-Making Style" : ,
    "CulturalFitSummary": ""
    """
    summary = model.generate_content(prompt)
    # print(summary)
    culturalfit_skill = summary.text
    print(culturalfit_skill)
    cultural_score = None
    alignment_with_company_values = None
    professionalism_work_ethic = None
    teamwork_collaboration = None
    adaptability_work_environment = None
    problem_solving_decision_making = None
    cultural_summary = None
    match10 = re.search(r'"CulturalFitScore": (\d+(\.\d+)?)', culturalfit_skill)
    if match10:
        cultural_score = float(match10.group(1))
    match11 = re.search(r'"Alignment with Core Company Values": (\d?)', culturalfit_skill)
    if match11:
        alignment_with_company_values = match11.group(1)
    match12 = re.search(r'"Professionalism and Work Ethic": (\d?)', culturalfit_skill)
    if match12:
        professionalism_work_ethic  = match12.group(1)
    match13 = re.search(r'"Teamwork and Collaboration Style": (\d?)', culturalfit_skill)
    if match13:
        teamwork_collaboration  = match13.group(1)
    match14 = re.search(r'"Adaptability to Work Environment Preferences": (\d?)', culturalfit_skill)
    if match14:
        adaptability_work_environment  = match14.group(1)
    match15 = re.search(r'"Problem-Solving and Decision-Making Style": (\d?)', culturalfit_skill)
    if match15:
        problem_solving_decision_making  = match15.group(1)
    match16 = re.search(r'"CulturalFitSummary": "([^"]+)"', culturalfit_skill)
    if match16:
        cultural_summary  = match16.group(1)
    # print("Alignment with Core Company Values:", alignment_with_company_values)
    return cultural_score,alignment_with_company_values,professionalism_work_ethic,teamwork_collaboration,adaptability_work_environment,problem_solving_decision_making,cultural_summary

def generate_attitude(text):
    prompt = f"""
    AtitudeSkill Content:
    1. Make the AtitudeScore with one decimal by calculate the AtitudeScore = [(Professionalism * 25%) + (Positivity and Enthusiasm * 25%) + (Resilience and Response to Challenges * 25%) + (Motivation and Work Ethic * 25%)].
    2. Generate the Professionalism Ranking 1 to 5 marks by evaluate the candidate’s conduct during the interview, including adherence to interview norms, respectful communication, and overall demeanor. 
    3. Generate the Positivity and Enthusiasm Ranking 1 to 5 marks by Evaluate he lettel of enthusiasm and positive outlook the candidate displays about the opportunity and their responses to questions. 
    4. Generate the Resilience and Response to Challenges Ranking 1 to 5 marks by evaluate the candidate's ability to discuss past challenges constructively and demonstrate learning and resilience. 
    5. Generate the Motivation and Work Ethic Ranking 1 to 5 marks by evaluate the candidate’s eagerness to contribute to the team and company, as evidenced by their energy levels, commitment to achieving goals, and feedback from references. 
    6. Only the AtitudeScore with one decimal. The Professionalism, Positivity and Enthusiasm, Resilience and Response to Challenges and Motivation and Work Ethic are integer.
    7. Generate a fifty words assessment summary for Attitude of the following interview conversation: {text}. The assessment summary only can write pronoun as 'the applicant' and 'his/her'.
    8. AtitudeScore, Professionalism, Positivity and Enthusiasm, Resilience and Response to Challenges and Motivation and Work Ethicshould not be empty.
    "AtitudeScore": ,
    "Professionalism": ,
    "Positivity and Enthusiasm": ,
    "Resilience and Response to Challenges": ,
    "Motivation and Work Ethic": ,
    "AtitudeSummary": ""
    """
    summary = model.generate_content(prompt)
    # print(summary)
    attitude_skill = summary.text
    # print(attitude_skill)
    attitude_score = None
    professionalism = None
    positivity_enthusiasm = None
    resilience_response = None
    motivation_work_ethic = None
    attitude_summary = None
    match17 = re.search(r'"AtitudeScore": (\d+(\.\d+)?)', attitude_skill)
    if match17:
        attitude_score = float(match17.group(1))
    match18 = re.search(r'"Professionalism": (\d+(\.\d+)?)', attitude_skill)
    if match18:
        professionalism = match18.group(1)
    match19 = re.search(r'"Positivity and Enthusiasm": (\d+(\.\d+)?)', attitude_skill)
    if match19:
        positivity_enthusiasm = match19.group(1)
    match20 = re.search(r'"Resilience and Response to Challenges": (\d+(\.\d+)?)', attitude_skill)
    if match20:
        resilience_response = match20.group(1)
    match21 = re.search(r'"Motivation and Work Ethic": (\d+(\.\d+)?)', attitude_skill)
    if match21:
        motivation_work_ethic = match21.group(1)
    match22 = re.search(r'"AtitudeSummary": "([^"]+)"', attitude_skill)
    if match22:
        attitude_summary = match22.group(1)
    return attitude_score, professionalism, positivity_enthusiasm, resilience_response, motivation_work_ethic, attitude_summary

def generate_communicationskill(text):
    prompt = f"""
    CommunicationSkill Content:
    1. Make the Communication Skill Mark with one decimal by calculate the Communication Skill Mark = [(Clarity, Coherence, and Conciseness of Responses * 25%) + (Listening and Engagement in Dialogue * 25%) + (Written Communication Skills * 25%) + (Non-verbal communication * 25%)].
    2. Generate the Clarity, Coherence, and Conciseness of Responses Ranking 1 to 5 marks by Evaluate How well the candidate articulates thoughts in a clear, logical, and concise manner during interviews. 
    3. Generate the Listening and Engagement in Dialogue Ranking 1 to 5 marks by evaluates the candidate's ability to actively listen, understand questions or statements, and engage in meaningful back-and-forth dialogue. 
    4. Generate the Written Communication Skills Ranking 1 to 5 marks by evaluate proficiency in written communication, as demonstrated through email exchanges, resumes, and any take-home assignments. 
    5. Generate the Non-verbal communication Ranking 1 to 5 marks by evaluate the use of non-verbal cues, such as eye contact, gestures, and facial expressions, to complement verbal communication and enhance understanding. 
    6. Only the Communication Skill Mark with one decimal. The Clarity, Coherence, and Conciseness of Responses, Listening and Engagement in Dialogue, Written Communication Skills and Non-verbal communication are integer.
    7. Generate a fifty words assessment summary for Communication Skill of the following interview conversation: {text}. The assessment summary only can write pronoun as 'the applicant' and 'his/her'.
    8. CommunicationSkillScore, Clarity, Coherence, and Conciseness of Responses, Listening and Engagement in Dialogue, Written Communication Skills and Non-verbal communication should not be empty.
    "CommunicationSkillScore": ,
    "Clarity, Coherence, and Conciseness of Responses": ,
    "Listening and Engagement in Dialogue": ,
    "Written Communication Skills": ,
    "Non-verbal communication": ,
    "CommunicationSkillSummary": ""
    """
    summary = model.generate_content(prompt)
    # print(summary)
    communication_skill = summary.text
    communication_score = None
    response_clarity_coherence = None
    listening_engagement = None
    written_communication = None
    non_verbal_communication = None
    communication_summary = None
    match23 = re.search(r'"CommunicationSkillScore": (\d+(\.\d+)?)', communication_skill)
    if match23:
        communication_score = float(match23.group(1))
    match24 = re.search(r'"Clarity, Coherence, and Conciseness of Responses": (\d+(\.\d+)?)', communication_skill)
    if match24:
        response_clarity_coherence = match24.group(1)
    match25 = re.search(r'"Listening and Engagement in Dialogue": (\d+(\.\d+)?)', communication_skill)
    if match25:
        listening_engagement = match25.group(1)
    match26 = re.search(r'"Written Communication Skills": (\d+(\.\d+)?)', communication_skill)
    if match26:
        written_communication = match26.group(1)
    matc27 = re.search(r'"Non-verbal communication": (\d+(\.\d+)?)', communication_skill)
    if matc27:
        non_verbal_communication = matc27.group(1)
    match28 = re.search(r'"CommunicationSkillSummary": "([^"]+)"', communication_skill)
    if match28:
        communication_summary = match28.group(1)
    return communication_score, response_clarity_coherence, listening_engagement, written_communication, non_verbal_communication, communication_summary

def generate_adaptability(text):
    prompt = f"""
    AdaptabilitySkill Content:
    1. Make the AdaptabilityScore with one decimal by calculate the AdaptabilityScore = [(Successful Adaptation to Change * 25%) + (Responses to Hypothetical Scenarios * 25%) + (Learning and Applying Feedback * 25%) + (Feedback from References on Adaptability and Problem-solvin* 25%)].
    2. Generate the Successful Adaptation to Change Ranking 1 to 5 marks by evaluates specific past experiences shared by the candidate that demonstrate their ability to adapt to new situations, roles, or environments effectively. 
    3. Generate the Responses to Hypothetical Scenarios Ranking 1 to 5 marks by evaluates the candidate's creativity and problem-solving abilities when confronted with hypothetical scenarios involving change or unexpected challenges. 
    4. Generate the Learning and Applying Feedback Ranking 1 to 5 marks by evaluates the candidate's openness to feedback and their capacity to incorporate this feedback into personal growth and improvement. 
    5. Generate the Feedback from References on Adaptability and Problem-solving Ranking 1 to 5 marks by evaluate external perspectives on the candidate's adaptability and problem-solving skills in previous roles or projects, as provided by references. 
    6. Only the AdaptabilityScore with one decimal. The Successful Adaptation to Change, Responses to Hypothetical Scenarios, Learning and Applying Feedback and Feedback from References on Adaptability and Problem-solving are integer.
    7. Generate a fifty words assessment summary for Adaptability of the following interview conversation: {text}. The assessment summary only can write pronoun as 'the applicant' and 'his/her'.
    8. AdaptabilityScore, Successful Adaptation to Change, Responses to Hypothetical Scenarios, Learning and Applying Feedback and Feedback from References on Adaptability and Problem-solvin should not be empty.
    "AdaptabilityScore": ,
    "Successful Adaptation to Change": ,
    "Responses to Hypothetical Scenarios": ,
    "Learning and Applying Feedback": ,
    "Feedback from References on Adaptability and Problem-solving": ,
    "AdaptabilitySummary": "",
    """
    summary = model.generate_content(prompt)
    # print(summary)
    adaptability_skill = summary.text
    print(adaptability_skill)
    adaptability_score = None
    successful_adaptation = None
    responses_to_scenarios = None
    learning_and_applying_feedback = None
    feedback_from_references = None
    adaptability_summary = None
    match29 = re.search(r'"AdaptabilityScore": (\d+(\.\d+)?)', adaptability_skill)
    if match29:
        adaptability_score = float(match29.group(1))
    match30 = re.search(r'"Successful Adaptation to Change": (\d+(\.\d+)?)', adaptability_skill)
    if match30:
        successful_adaptation = match30.group(1)
    match31 = re.search(r'"Responses to Hypothetical Scenarios": (\d+(\.\d+)?)', adaptability_skill)
    if match31:
        responses_to_scenarios = match31.group(1)
    match32 = re.search(r'"Learning and Applying Feedback": (\d+(\.\d+)?)', adaptability_skill)
    if match32:
        learning_and_applying_feedback = match32.group(1)
    match33 = re.search(r'"Feedback from References on Adaptability and Problem-solving": (\d+(\.\d+)?)', adaptability_skill)
    if match33:
        feedback_from_references = match33.group(1)
    match34 = re.search(r'"AdaptabilitySummary": "([^"]+)"', adaptability_skill)
    if match34:
        adaptability_summary = match34.group(1)
    return adaptability_score, successful_adaptation, responses_to_scenarios, learning_and_applying_feedback, feedback_from_references, adaptability_summary

def generate_mbti(mbti_type):
    prompt = f"""
    Generate MBTISummary.
    MBTISummary Content:
    1. Generate a ninety words summary of the candidate's predicted mbti type: {mbti_type} characteristics in the workplace. Highlight their thoughtful and strategic approach, strong intuition, organizational skills, focus on positive change and sustainability, empathetic nature, and ability to foster collaboration and effective leadership.The summary only can write pronoun as 'the applicant' and 'his/her'.
    2. All Contents should not be null.
    """
    summary = model.generate_content(prompt)
    # print(summary)
    mbti_summary = summary.text
    return mbti_summary

def generate_feedback_for_candidate(text):
    prompt = f"""
    FeedbackForCandidate Content:
    1. Strengths come from many areas such as good technical skills, excellent preparation, excellent communication skills, a good attitude and the ability to adapt. 
    2. Specific, actionable feedback can also be listed on areas where candidates demonstrate gaps or opportunities for improvement.
    3. Weaknesses and areas for improvement may include recommendations for professional development, additional training, or areas to focus on in future roles. 
    4. Generate the list of the candidate's strengths in the following interview conversation: {text}. 
    5. If the candidate does not have any strengths, write the candidate did not demonstrate any significant strengths during the interview process.
    6. Generate the list of the candidate's weaknesses and areas for improvement as demonstrated in the following interview conversation: {text}. 
    7. Generate the list of the candidate's other recommended job position as demonstrated in the following interview conversation: {text}. 
    8. The Strength, Weakness and Areas For Improvement, Other Recommended Job Position should not be blank. They should more than one.
    9. All Contents should not be null.
    "Strength": {{
        "Strength 1": "",
        "Strength 2": "",
        "Strength 3": "",
    }},
    "WeaknessAndAreasForImprovement": {{
        "Weakness 1": "",
        "Weakness 2": "",
        "Weakness 3": ""
    }},
    "OtherRecommendedJobPosition": {{
        "Job Position 1": "",
        "Job Position 2": "",
        "Job Position 3": "",
    }}
    """
    summary = model.generate_content(prompt)
    # print(summary)
    feedback_for_candidate = summary.text
    # print(feedback_for_candidate)
    strength_pattern = r'"Strength (\d+)": "(.*?)"'
    weakness_pattern = r'"Weakness (\d+)": "(.*?)"'
    job_position_pattern = r'"Job Position (\d+)": "(.*?)"'
    strengths = dict(re.findall(strength_pattern, feedback_for_candidate))
    weaknesses = dict(re.findall(weakness_pattern, feedback_for_candidate))
    job_positions = dict(re.findall(job_position_pattern, feedback_for_candidate))
    return strengths, weaknesses, job_positions

def generate_overall_evaluation_N_recommendation(text):
    prompt = f"""
    OverallEvaluationAndRecommendation Content:
    1. Generate a 80 words Summary of the candidate in all aspect like the soft skill and tech skill using following interview conversation: {text}. Integrate insights from each section to highlight the candidate’s overall strengths and how they align with the role's requirements and the company's culture. Identify any potential areas for growth or concerns that emerged during the evaluation. The assessment summary only can write pronoun as 'the applicant' and 'his/her'.
    2. Based on the comprehensive assessment, generate a 40 words recommendation whether to proceed to the next round of interviews, be offered the position, consider the candidate for a different job position, or fail. Just to give suggestions that the actual HR will take the decision. 
    3. All Contents should not be null.
    "Summary":"",
    "Recommendation":""
    """
    summary = model.generate_content(prompt)
    # print(summary)
    overall_evaluation_N_recommendation = summary.text
    summary = None
    recommendation = None
    match35 = re.search(r'"Summary": "([^"]+)"', overall_evaluation_N_recommendation)
    if match35:
        summary = match35.group(1)
    match36 = re.search(r'"Recommendation": "([^"]+)"', overall_evaluation_N_recommendation)
    if match36:
        recommendation = match36.group(1)
    return summary, recommendation

def main(concatTranscript, mbti_type):
    TechnicalSkillScore, TechnicalSkillSummary = generate_technical(concatTranscript)
    preparation_score, knowledge_company_role_industry, quality_of_questions, alignment_with_job_requirements, preparation_summary = generate_preparation(concatTranscript)
    cultural_score,alignment_with_company_values,professionalism_work_ethic,teamwork_collaboration,adaptability_work_environment,problem_solving_decision_making,cultural_summary = generate_culturalfit(concatTranscript)
    attitude_score, professionalism, positivity_enthusiasm, resilience_response, motivation_work_ethic, attitude_summary = generate_attitude(concatTranscript)
    communication_score, response_clarity_coherence, listening_engagement, written_communication, non_verbal_communication, communication_summary = generate_communicationskill(concatTranscript)
    adaptability_score, successful_adaptation, responses_to_scenarios, learning_and_applying_feedback, feedback_from_references, adaptability_summary = generate_adaptability(concatTranscript)
    mbti_summary = generate_mbti(mbti_type)
    strengths, weaknesses, job_positions = generate_feedback_for_candidate(concatTranscript)
    summary, recommendation = generate_overall_evaluation_N_recommendation(concatTranscript)
    ai_report={
    "TechnicalSkill":{
        "TechnicalSkillScore": TechnicalSkillScore,
        "TechnicalSkillSummary": TechnicalSkillSummary,
    },   
    "SoftSkill":{
        "PreparationSkill":{
             "PreparationScore": preparation_score,
                "PreparationDetailScoring":{
                    "Knowledge of the Company, Role, and Industry": knowledge_company_role_industry,
                    "Quality of Questions for the Interviewer": quality_of_questions,
                    "Alignment of Skills and Experiences with Job Requirements": alignment_with_job_requirements,
                    "Formal and Appropriate Attire": 4,
                    "Grooming and Tidiness": 4,
            },
            "PreparationSummary": preparation_summary,
        },
        "CulturalFitSkill":{
            "CulturalFitScore": cultural_score,
                "CulturalFitDetailScoring":{
                    "Alignment with Core Company Values": alignment_with_company_values,
                    "Professionalism and Work Ethic": professionalism_work_ethic,
                    "Teamwork and Collaboration Style": teamwork_collaboration,
                    "Adaptability to Work Environment Preferences": adaptability_work_environment,
                    "Problem-Solving and Decision-Making Style": problem_solving_decision_making,
                },
            "CulturalFitSummary": cultural_summary,
        },
        "AttitudeSkill":{
            "AttitudeScore": attitude_score,
                "AttitudeDetailScoring": {
                    "Professionalism": professionalism,
                    "Positivity and Enthusiasm": positivity_enthusiasm,
                    "Resilience and Response to Challenges": resilience_response,
                    "Motivation and Work Ethic": motivation_work_ethic,
                },
            "AtitudeSummary": attitude_summary,
        },
        "CommunicationSkill":{
            "CommunicationSkillScore": communication_score,
                "CommunicationSkillDetailScoring":{
                    "Clarity, Coherence, and Conciseness of Responses": response_clarity_coherence,
                    "Listening and Engagement in Dialogue": listening_engagement,
                    "Written Communication Skills": written_communication,
                    "Non-verbal communication": non_verbal_communication,
                },
            "CommunicationSkillSummary": communication_summary,
        },
        "AdaptabilitySkill":{
            "AdaptabilityScore": adaptability_score,
                "AdaptabilityDetailScoring":{
                    "Successful Adaptation to Change": successful_adaptation,
                    "Responses to Hypothetical Scenarios": responses_to_scenarios,
                    "Learning and Applying Feedback": learning_and_applying_feedback,
                    "Feedback from References on Adaptability and Problem-solving": feedback_from_references,
                },
            "AdaptabilitySummary": adaptability_summary,
        },
    },
     "MBTISummary": mbti_summary,
    "FeedbackForCandidate":{
        **{"Strength {}".format(k): v for k, v in strengths.items()},
        **{"Weakness {}".format(k): v for k, v in weaknesses.items()},
        **{"Job Position {}".format(k): v for k, v in job_positions.items()}
    },
    "OverallEvaluationAndReccomendation":{
        "Summary": summary,
        "Recommendation": recommendation,
    },
    }
    # ai_report = json.dumps(ai_report, indent=4)
    return ai_report

# concatTranscript = """
# HR: Good morning! Thank you for coming in today. Let's start with some general questions about your knowledge of the company, role, and industry. Can you tell me what you know about our company's approach to sustainability?
# Candidate: Good morning! Thank you for having me. From my research, I understand that your company has implemented various sustainability initiatives, such as reducing carbon emissions in your operations and promoting renewable energy use. Additionally, you've integrated sustainability goals into your business strategies, aiming for long-term environmental and social impact.
# HR: That's correct. Now, moving on to technical aspects, could you describe your experience with data analysis tools and techniques relevant to sustainability reporting?
# Candidate: Certainly. During my internship, I gained proficiency in utilizing tools like Excel and Tableau for data visualization and analysis. I've also worked with SQL databases to extract and manipulate large datasets for sustainability performance tracking. Additionally, I'm familiar with sustainability reporting frameworks such as GRI and CDP, which involve collecting, analyzing, and disclosing environmental and social data.
# HR: Great to hear. Let's switch back to general questions. How do you envision the role of an IT Business Analyst contributing to our sustainability objectives?
# Candidate: As an IT Business Analyst focused on sustainability, I see myself playing a crucial role in leveraging technology to optimize processes and enhance data-driven decision-making. By collaborating with cross-functional teams, I aim to identify areas where IT solutions can streamline sustainability reporting, improve data accuracy, and facilitate continuous improvement in environmental performance. Ultimately, my goal would be to align IT initiatives with the company's broader sustainability goals, driving efficiency and innovation.
# HR: Excellent perspective. Now, for a technical question, could you provide an example of a sustainability-related project you've worked on where you had to analyze complex datasets to identify trends or patterns?
# Candidate: Certainly. In a recent project, I was tasked with analyzing energy consumption data across multiple facilities to identify opportunities for efficiency improvements. I utilized statistical analysis techniques to identify outliers and trends, which helped prioritize areas for intervention. By combining this data with external factors such as weather patterns and production schedules, we were able to develop targeted strategies for reducing energy waste and optimizing resource usage, resulting in significant cost savings and environmental benefits.
# HR: Impressive. Finally, let's wrap up with a general question. How do you stay updated on developments in sustainability practices and technologies within the IT industry?
# Candidate: I'm passionate about sustainability and technology, so I regularly engage in professional development activities such as attending webinars, participating in industry forums, and reading research papers and articles from reputable sources. I also actively seek out networking opportunities with professionals in both fields to exchange ideas and stay informed about emerging trends and best practices. Additionally, I'm open to pursuing relevant certifications or additional coursework to deepen my expertise in this area.
# HR: Thank you for sharing your insights. That concludes our interview for today. 
# """
# mbti_type = "intj"

# ai_report = main(concatTranscript, mbti_type)
# print(ai_report)

