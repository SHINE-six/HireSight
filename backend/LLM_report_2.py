# Vertex AI
import os
import re
import json
import time
import vertexai
from vertexai.generative_models import GenerativeModel
import vertexai.preview.generative_models as generative_models

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\annin\\OneDrive\\Desktop\\HireSight\\backend\\model\\GOOGLE_APPLICATION_CRED.json"

vertexai.init(project="civic-surge-420016", location="asia-southeast1")
 
# Set up the model
generation_config = {
    "max_output_tokens": 500,
    "temperature": 0.2,
    "top_p": 0.8,
}

model = GenerativeModel("gemini-1.0-pro",generation_config=generation_config)

def extract_data(summary, pattern):
    match = re.search(pattern, summary)
    if match:
        return match.group(1)
    else:
        return None

def extract_feedback_items(summary, pattern, name):
    items = dict(re.findall(pattern, summary))
    return {f"{name} {index + 1}": value for index, value in enumerate(items.values())}
    
def generate_technical(concatTranscript):
    prompt = f"""
    TechnicalSkill Content:
    1. Generate the Technical Skills Rating 1 to 5 marks with one decimal.
    2. Generate a fifty words assessment summary about Tehcnical Skills of the following interview conversation: {concatTranscript}. The assessment summary only can write pronoun as 'the applicant' and 'his/her'.
    3. TechnicalSkillScore and TechnicalSkillSummary should not be empty.
    4. Output should follow Json Format:
    {{
        "TechnicalSkillScore": float,  
        "TechnicalSkillSummary": "string"
    }}
    """
    summary = model.generate_content(prompt)
    technical_assessment = summary.text
    TechnicalSkillScore = float(extract_data(technical_assessment, r'"TechnicalSkillScore": (\d+(\.\d+)?)'))
    TechnicalSkillSummary = extract_data(technical_assessment, r'"TechnicalSkillSummary": "(.*)"')
    return TechnicalSkillScore, TechnicalSkillSummary

def generate_preparation(concatTranscript):
    prompt = f"""
    PreparationSkill Content:
    1. Make the PreparationScore by calculate the PreparationScore = [(Knowledge of the Company, Role, and Industry Rating * 30%) + (Quality of Questions for the Interviewer Rating * 25%) + (Alignment of Skills and Experiences with Job Requirements Rating * 25%) + (Formal and Appropriate Attire Rating * 10%) + (Grooming and Tidiness Rating * 10%)]
    2. Rate the Knowledge of the Company, Role, and Industry 1 to 5 marks by evaluate how well the candidate understands the company's mission, the specifics of the role, and industry dynamics.
    3. Rate the Quality of Questions for the Interviewer 1 to 5 marks by evaluate the depth and relevance of the questions asked by the candidate, indicating their engagement and preparation. If the candidate have not ask any question will be 0.
    4. Rate the Alignment of Skills and Experiences with Job Requirements 1 to 5 marks by evaluate the candidate's ability to articulate how their background aligns with the role's requirements. 
    5. Only the PreparationScore with one decimal. The Knowledge of the Company, Role, and Industry, Quality of Questions for the Interviewer, Alignment of Skills and Experiences with Job Requirements, Formal and Appropriate Attire and Grooming and Tidiness are integer.
    6. Generate a fifty words assessment summary for Soft Skills of the following interview conversation: {concatTranscript}. The assessment summary only can write pronoun as 'the applicant' and 'his/her'.
    7. PreparationScore, Knowledge of the Company, Role, and Industry, Quality of Questions for the Interviewer,Alignment of Skills and Experiences with Job Requirements, PreparationSummary should not be empty.
    8. Output should follow Json Format:
    {{
        "PreparationScore": float,
        "Knowledge of the Company, Role, and Industry": integer,
        "Quality of Questions for the Interviewer": integer,
        "Alignment of Skills and Experiences with Job Requirements": integer,
        "PreparationSummary": "string"
    }}
    """
    summary = model.generate_content(prompt)
    preparation_skill = summary.text
    preparation_score = float(extract_data(preparation_skill, r'"PreparationScore": (\d+(\.\d+)?)'))
    knowledge_company_role_industry = int(extract_data(preparation_skill, r'"Knowledge of the Company, Role, and Industry": (\d+(\.\d+)?)'))
    quality_of_questions = int(extract_data(preparation_skill, r'"Quality of Questions for the Interviewer": (\d+(\.\d+)?)'))
    alignment_with_job_requirements = int(extract_data(preparation_skill, r'"Alignment of Skills and Experiences with Job Requirements": (\d+(\.\d+)?)'))
    preparation_summary = extract_data(preparation_skill, r'"PreparationSummary": "([^"]+)"')
    return preparation_score, knowledge_company_role_industry, quality_of_questions, alignment_with_job_requirements, preparation_summary

def generate_culturalfit(concatTranscript):
    prompt = f"""
    CulturalFitSkill Content:
    1. Make the CulturalFitScore with one decimal by calculate the CulturalFitScore = [(Alignment with Core Company Values * 30%) + (Professionalism and Work Ethic * 20%) + (Teamwork and Collaboration Style * 20%) + (Adaptability to Work Environment Preferences * 15%) + (Problem-Solving and Decision-Making Style * 15%)].
    2. Generate the Alignment with Core Company Values Ranking 1 to 5 marks by assessing the comprehension of the company's fundamental principles in professional behavior and choices.
    3. Generate the Professionalism and Work Ethic Ranking 1 to 5 marks by evaluating dedication, reliability, and responsibility in a professional environment, including meeting commitments and deadlines.
    4. Generate the Teamwork and Collaboration Style Ranking 1 to 5 marks by assessing preference for collaborative or solitary work, communication effectiveness, and contribution to team goals.
    5. Generate the Adaptability to Work Environment Preferences Ranking 1 to 5 marks by evaluating adaptability to different work settings (remote, hybrid, or on-site) and ability to maintain productivity.
    6. Generate the Problem-Solving and Decision-Making Style Ranking 1 to 5 marks by assessing problem-solving approach, creativity, critical thinking, and conflict resolution.
    7. Only the CulturalFitScore with one decimal. The Alignment with Core Company Values, Professionalism and Work Ethic, Teamwork and Collaboration Style, Adaptability to Work Environment Preferences and Problem-Solving and Decision-Making Style are integer.
    8. Generate a fifty words assessment summary for Cultural Fit of the following interview conversation: {concatTranscript}. The assessment summary only can write pronoun as 'the applicant' and 'his/her'.
    9. CulturalFitScore, Alignment with Core Company Values, Professionalism and Work Ethic, Teamwork and Collaboration Style, Adaptability to Work Environment Preferences and Problem-Solving and Decision-Making Style should not be empty.
    10. Output should follow Json Format:
    {{
        "CulturalFitScore": ,
        "Alignment with Core Company Values": float,
        "Professionalism and Work Ethic": integer,
        "Teamwork and Collaboration Style": integer,
        "Adaptability to Work Environment Preferences": integer,
        "Problem-Solving and Decision-Making Style": integer,
        "CulturalFitSummary": "string"
    }}
    """
    summary = model.generate_content(prompt)
    culturalfit_skill = summary.text
    cultural_score = float(extract_data(culturalfit_skill, r'"CulturalFitScore": (\d+(\.\d+)?)'))
    alignment_with_company_values = int(extract_data(culturalfit_skill, r'"Alignment with Core Company Values": (\d+(\.\d+)?)'))
    professionalism_work_ethic = int(extract_data(culturalfit_skill, r'"Professionalism and Work Ethic": (\d+(\.\d+)?)'))
    teamwork_collaboration = int(extract_data(culturalfit_skill, r'"Teamwork and Collaboration Style": (\d+(\.\d+)?)'))
    adaptability_work_environment = int(extract_data(culturalfit_skill, r'"Adaptability to Work Environment Preferences": (\d+(\.\d+)?)'))
    problem_solving_decision_making = int(extract_data(culturalfit_skill, r'"Problem-Solving and Decision-Making Style": (\d+(\.\d+)?)'))
    cultural_summary = extract_data(culturalfit_skill, r'"CulturalFitSummary": "([^"]+)"')
    return cultural_score,alignment_with_company_values,professionalism_work_ethic,teamwork_collaboration,adaptability_work_environment,problem_solving_decision_making,cultural_summary

def generate_attitude(concatTranscript):
    prompt = f"""
    AtitudeSkill Content:
    1. Make the AtitudeScore with one decimal by calculate the AtitudeScore = [(Professionalism * 25%) + (Positivity and Enthusiasm * 25%) + (Resilience and Response to Challenges * 25%) + (Motivation and Work Ethic * 25%)].
    2. Generate the Professionalism Ranking 1 to 5 marks by evaluate the candidate’s conduct during the interview, including adherence to interview norms, respectful communication, and overall demeanor. 
    3. Generate the Positivity and Enthusiasm Ranking 1 to 5 marks by Evaluate he lettel of enthusiasm and positive outlook the candidate displays about the opportunity and their responses to questions. 
    4. Generate the Resilience and Response to Challenges Ranking 1 to 5 marks by evaluate the candidate's ability to discuss past challenges constructively and demonstrate learning and resilience. 
    5. Generate the Motivation and Work Ethic Ranking 1 to 5 marks by evaluate the candidate’s eagerness to contribute to the team and company, as evidenced by their energy levels, commitment to achieving goals, and feedback from references. 
    6. Only the AtitudeScore with one decimal. The Professionalism, Positivity and Enthusiasm, Resilience and Response to Challenges and Motivation and Work Ethic are integer.
    7. Generate a fifty words assessment summary for Attitude of the following interview conversation: {concatTranscript}. The assessment summary only can write pronoun as 'the applicant' and 'his/her'.
    8. AtitudeScore, Professionalism, Positivity and Enthusiasm, Resilience and Response to Challenges and Motivation and Work Ethicshould not be empty.
    9. Output should follow Json Format:
    {{
        "AtitudeScore": float,
        "Professionalism": integer,
        "Positivity and Enthusiasm": integer,
        "Resilience and Response to Challenges": integer,
        "Motivation and Work Ethic": integer,
        "AtitudeSummary": "string"
    }}
    """
    summary = model.generate_content(prompt)
    attitude_skill = summary.text
    attitude_score = float(extract_data(attitude_skill, r'"AtitudeScore": (\d+(\.\d+)?)'))
    professionalism = int(extract_data(attitude_skill, r'"Professionalism": (\d+(\.\d+)?)'))
    positivity_enthusiasm = int(extract_data(attitude_skill, r'"Positivity and Enthusiasm": (\d+(\.\d+)?)'))
    resilience_response = int(extract_data(attitude_skill, r'"Resilience and Response to Challenges": (\d+(\.\d+)?)'))
    motivation_work_ethic = int(extract_data(attitude_skill, r'"Motivation and Work Ethic": (\d+(\.\d+)?)'))
    attitude_summary = extract_data(attitude_skill, r'"AtitudeSummary": "([^"]+)"')
    return attitude_score, professionalism, positivity_enthusiasm, resilience_response, motivation_work_ethic, attitude_summary

def generate_communicationskill(concatTranscript):
    prompt = f"""
    CommunicationSkill Content:
    1. Make the Communication Skill Mark with one decimal by calculate the Communication Skill Mark = [(Clarity, Coherence, and Conciseness of Responses * 25%) + (Listening and Engagement in Dialogue * 25%) + (Written Communication Skills * 25%) + (Non-verbal communication * 25%)].
    2. Generate the Clarity, Coherence, and Conciseness of Responses Ranking 1 to 5 marks by Evaluate How well the candidate articulates thoughts in a clear, logical, and concise manner during interviews. 
    3. Generate the Listening and Engagement in Dialogue Ranking 1 to 5 marks by evaluates the candidate's ability to actively listen, understand questions or statements, and engage in meaningful back-and-forth dialogue. 
    4. Generate the Written Communication Skills Ranking 1 to 5 marks by evaluate proficiency in written communication, as demonstrated through email exchanges, resumes, and any take-home assignments. 
    5. Generate the Non-verbal communication Ranking 1 to 5 marks by evaluate the use of non-verbal cues, such as eye contact, gestures, and facial expressions, to complement verbal communication and enhance understanding. 
    6. Only the Communication Skill Mark with one decimal. The Clarity, Coherence, and Conciseness of Responses, Listening and Engagement in Dialogue, Written Communication Skills and Non-verbal communication are integer.
    7. Generate a fifty words assessment summary for Communication Skill of the following interview conversation: {concatTranscript}. The assessment summary only can write pronoun as 'the applicant' and 'his/her'.
    8. CommunicationSkillScore, Clarity, Coherence, and Conciseness of Responses, Listening and Engagement in Dialogue, Written Communication Skills and Non-verbal communication should not be empty.
    9. Output should follow Json Format:
    {{
        "CommunicationSkillScore": float,
        "Clarity, Coherence, and Conciseness of Responses": integer,
        "Listening and Engagement in Dialogue": integer,
        "Written Communication Skills": integer,
        "Non-verbal Communication": integer,
        "CommunicationSkillSummary": "string"
    }}
    """
    summary = model.generate_content(prompt)
    communication_skill = summary.text
    communication_score = float(extract_data(communication_skill, r'"CommunicationSkillScore": (\d+(\.\d+)?)'))
    response_clarity_coherence = int(extract_data(communication_skill, r'"Clarity, Coherence, and Conciseness of Responses": (\d+(\.\d+)?)'))
    listening_engagement = int(extract_data(communication_skill, r'"Listening and Engagement in Dialogue": (\d+(\.\d+)?)'))
    written_communication = int(extract_data(communication_skill, r'"Written Communication Skills": (\d+(\.\d+)?)'))
    non_verbal_communication = int(extract_data(communication_skill, r'"Non-verbal Communication": (\d+(\.\d+)?)'))
    communication_summary = extract_data(communication_skill, r'"CommunicationSkillSummary": "([^"]+)"')
    return communication_score, response_clarity_coherence, listening_engagement, written_communication, non_verbal_communication, communication_summary

def generate_adaptability(concatTranscript):
    prompt = f"""
    AdaptabilitySkill Content:
    1. Make the AdaptabilityScore with one decimal by calculate the AdaptabilityScore = [(Successful Adaptation to Change * 25%) + (Responses to Hypothetical Scenarios * 25%) + (Learning and Applying Feedback * 25%) + (Feedback from References on Adaptability and Problem-solvin* 25%)].
    2. Generate the Successful Adaptation to Change Ranking 1 to 5 marks by evaluates specific past experiences shared by the candidate that demonstrate their ability to adapt to new situations, roles, or environments effectively. 
    3. Generate the Responses to Hypothetical Scenarios Ranking 1 to 5 marks by evaluates the candidate's creativity and problem-solving abilities when confronted with hypothetical scenarios involving change or unexpected challenges. 
    4. Generate the Learning and Applying Feedback Ranking 1 to 5 marks by evaluates the candidate's openness to feedback and their capacity to incorporate this feedback into personal growth and improvement. 
    5. Generate the Feedback from References on Adaptability and Problem-solving Ranking 1 to 5 marks by evaluate external perspectives on the candidate's adaptability and problem-solving skills in previous roles or projects, as provided by references. 
    6. Only the AdaptabilityScore with one decimal. The Successful Adaptation to Change, Responses to Hypothetical Scenarios, Learning and Applying Feedback and Feedback from References on Adaptability and Problem-solving are integer.
    7. Generate a fifty words assessment summary for Adaptability of the following interview conversation: {concatTranscript}. The assessment summary only can write pronoun as 'the applicant' and 'his/her'.
    8. AdaptabilityScore, Successful Adaptation to Change, Responses to Hypothetical Scenarios, Learning and Applying Feedback and Feedback from References on Adaptability and Problem-solvin should not be empty.
    9. Output should follow Json Format:
    {{
        "AdaptabilityScore": float,
        "Successful Adaptation to Change": integer,
        "Responses to Hypothetical Scenarios": integer,
        "Learning and Applying Feedback": integer,
        "Feedback from References on Adaptability and Problem-solving": integer,
        "AdaptabilitySummary": "string",
    }}
    """
    summary = model.generate_content(prompt)
    adaptability_skill = summary.text
    adaptability_score = float(extract_data(adaptability_skill, r'"AdaptabilityScore": (\d+(\.\d+)?)'))
    successful_adaptation = int(extract_data(adaptability_skill, r'"Successful Adaptation to Change": (\d+(\.\d+)?)'))
    responses_to_scenarios = int(extract_data(adaptability_skill, r'"Responses to Hypothetical Scenarios": (\d+(\.\d+)?)'))
    learning_and_applying_feedback = int(extract_data(adaptability_skill, r'"Learning and Applying Feedback": (\d+(\.\d+)?)'))
    feedback_from_references = int(extract_data(adaptability_skill, r'"Feedback from References on Adaptability and Problem-solving": (\d+(\.\d+)?)'))
    adaptability_summary = extract_data(adaptability_skill, r'"AdaptabilitySummary": "([^"]+)"')
    return adaptability_score, successful_adaptation, responses_to_scenarios, learning_and_applying_feedback, feedback_from_references, adaptability_summary

def generate_mbti(mbti_type):
    prompt = f"""
    Generate MBTISummary.
    MBTISummary Content:
    1. Generate a ninety words summary of the candidate's predicted mbti type: {mbti_type} characteristics in the workplace. Highlight their thoughtful and strategic approach, strong intuition, organizational skills, focus on positive change and sustainability, empathetic nature, and ability to foster collaboration and effective leadership.The summary only can write pronoun as 'the applicant' and 'his/her'.
    2. Content should not be null.
    Output should follow Json Format:
    {{
        "MBTISummary": "string",
    }}
    """
    summary = model.generate_content(prompt)
    mbti_summary = summary.text
    mbti_summary = extract_data(mbti_summary, r'"MBTISummary": "([^"]+)"')
    return mbti_summary

def generate_feedback_for_candidate(concatTranscript):
    prompt = f"""
    FeedbackForCandidate Content:
    1. Strengths come from many areas such as good technical skills, excellent preparation, excellent communication skills, a good attitude and the ability to adapt. 
    2. Specific, actionable feedback can also be listed on areas where candidates demonstrate gaps or opportunities for improvement.
    3. Weaknesses and areas for improvement may include recommendations for professional development, additional training, or areas to focus on in future roles. 
    4. Generate the list of the candidate's 3 strengths in the following interview conversation: {concatTranscript}. 
    5. If the candidate does not have any strength, write the candidate did not demonstrate any significant strengths during the interview process.
    6. Generate the list of the candidate's 3 weaknesses and areas for improvement as demonstrated in the following interview conversation: {concatTranscript}. 
    7. Generate the list of the candidate's other 3 recommended job position as demonstrated in the following interview conversation: {concatTranscript}. 
    8. The Strengths, Weakness and Areas For Improvement, Other Recommended Job Position should not be empty. They should more than one.
    9. Output should follow Json Format:
    {{
        "Strengths": {{
            "Strength 1": "string",
            "Strength 2": "string",
            "Strength 3": "string",
        }},
        "WeaknessAndAreasForImprovement": {{
            "Weakness 1": "string",
            "Weakness 2": "string",
            "Weakness 3": "string"
        }},
        "OtherRecommendedJobPosition": {{
            "Job Position 1": "string",
            "Job Position 2": "string",
            "Job Position 3": "string",
        }}
    }}
    """
    summary = model.generate_content(prompt)
    feedback_for_candidate = summary.text
    strengths = extract_feedback_items(feedback_for_candidate, r'"Strength (\d+)": "(.*?)"', "Strength")
    weaknesses = extract_feedback_items(feedback_for_candidate, r'"Weakness (\d+)": "(.*?)"', "Weakness")
    job_positions = extract_feedback_items(feedback_for_candidate, r'"Job Position (\d+)": "(.*?)"', "Job Position")
    return strengths, weaknesses, job_positions

def generate_overall_evaluation_N_recommendation(concatTranscript):
    prompt = f"""
    OverallEvaluationAndRecommendation Content:
    1. Generate a 80 words Summary of the candidate in all aspect like the soft skill and tech skill using following interview conversation: {concatTranscript}. Integrate insights from each section to highlight the candidate’s overall strengths and how they align with the role's requirements and the company's culture. Identify any potential areas for growth or concerns that emerged during the evaluation. The assessment summary only can write pronoun as 'the applicant' and 'his/her'.
    2. Based on the comprehensive assessment, generate a 40 words recommendation whether to proceed to the next round of interviews, be offered the position, consider the candidate for a different job position, or fail. Just to give suggestions that the actual HR will take the decision. 
    3. All Contents should not be null.
    4. Output should follow Json Format:
    {{
        "Summary":"string",
        "Recommendation":"string"
    }}
    """
    summary = model.generate_content(prompt)
    overall_evaluation_N_recommendation = summary.text
    summary = extract_data(overall_evaluation_N_recommendation, r'"Summary": "([^"]+)"')
    recommendation = extract_data(overall_evaluation_N_recommendation, r'"Recommendation": "([^"]+)"')
    return summary, recommendation

def main(concatTranscript, mbti_type):
    TechnicalSkillScore, TechnicalSkillSummary = generate_technical(concatTranscript)
    preparation_score, knowledge_company_role_industry, quality_of_questions, alignment_with_job_requirements, preparation_summary = generate_preparation(concatTranscript)
    time.sleep(60)
    cultural_score,alignment_with_company_values,professionalism_work_ethic,teamwork_collaboration,adaptability_work_environment,problem_solving_decision_making,cultural_summary = generate_culturalfit(concatTranscript)
    attitude_score, professionalism, positivity_enthusiasm, resilience_response, motivation_work_ethic, attitude_summary = generate_attitude(concatTranscript)
    time.sleep(60)
    communication_score, response_clarity_coherence, listening_engagement, written_communication, non_verbal_communication, communication_summary = generate_communicationskill(concatTranscript)
    adaptability_score, successful_adaptation, responses_to_scenarios, learning_and_applying_feedback, feedback_from_references, adaptability_summary = generate_adaptability(concatTranscript)
    time.sleep(60)
    mbti_summary = generate_mbti(mbti_type)
    strengths, weaknesses, job_positions = generate_feedback_for_candidate(concatTranscript)
    time.sleep(60)
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
        "Strength": strengths,
        "WeaknessAndAreasForImprovement": weaknesses,
        "OtherRecommendedJobPosition": job_positions
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

