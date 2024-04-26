import google.generativeai as genai
from dotenv import load_dotenv
import os

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
    Rate the Technical Skills Rating 1 to 5 marks with one decimal.
    Generate a fifty words assessment summary about Tehcnical Skills of the following interview conversation: {text}. The assessment summary only can write pronoun as 'the applicant' and 'his/her'.
    """

    summary = model.generate_content(prompt)

    #formatting the output to make it look cleaner
    technical_assessment = summary.text.replace("**", "").replace("\n\n", "\n")
    return technical_assessment 

def generate_preparation(text):

    prompt = f"""
    Make the Preparation Marks by calculate the Preparation Marks = [(Knowledge of the Company, Role, and Industry Rating * 30%) + (Quality of Questions for the Interviewer Rating * 25%) + (Alignment of Skills and Experiences with Job Requirements Rating * 25%) + (Formal and Appropriate Attire Rating * 10%) + (Grooming and Tidiness Rating * 10%)]
    Rate the Knowledge of the Company, Role, and Industry 1 to 5 marks by evaluate how well the candidate understands the company's mission, the specifics of the role, and industry dynamics.
    Rate the Quality of Questions for the Interviewer 1 to 5 marks by evaluate the depth and relevance of the questions asked by the candidate, indicating their engagement and preparation. If the candidate have not ask any question will be 0.
    Rate the Alignment of Skills and Experiences with Job Requirements 1 to 5 marks by evaluate the candidate's ability to articulate how their background aligns with the role's requirements. 
    Rate the Formal and Appropriate Attire 1 to 5 marks by evaluate the candidate's effort to dress formally and appropriately for the interview context. 
    Rate the Grooming and Tidiness 1 to 5 marks by evaluate the candidate's attention to personal grooming and tidiness, reflects their professionalism. 
    Only the Preparation Marks with one decimal. The Knowledge of the Company, Role, and Industry, Quality of Questions for the Interviewer, Alignment of Skills and Experiences with Job Requirements, Formal and Appropriate Attire and Grooming and Tidiness are integer.
    Generate a fifty words assessment summary for Soft Skills of the following interview conversation: {text}. The assessment summary only can write pronoun as 'the applicant' and 'his/her'.
    """

    summary = model.generate_content(prompt)
    # print(summary)

    # formatting the output to make it look cleaner
    # preparation = summary.text.replace("**", "")
    preparation = summary.text.replace("\n\n", "\n").replace("**", "")
    return preparation 

def generate_culturalfit(text):

    prompt = f"""
    Make the Cultural Fit Mark with one decimal by calculate the Cultural Fit Mark = [(Alignment with Core Company Values * 30%) + (Professionalism and Work Ethic * 20%) + (Teamwork and Collaboration Style * 20%) + (Adaptability to Work Environment Preferences * 15%) + (Problem-Solving and Decision-Making Style * 15%)].
    Generate the Alignment with Core Company Values Ranking 1 to 5 marks by assessing the comprehension of the company's fundamental principles in professional behavior and choices.
    Generate the Professionalism and Work Ethic Ranking 1 to 5 marks by evaluating dedication, reliability, and responsibility in a professional environment, including meeting commitments and deadlines.
    Generate the Teamwork and Collaboration Style Ranking 1 to 5 marks by assessing preference for collaborative or solitary work, communication effectiveness, and contribution to team goals.
    Generate the Adaptability to Work Environment Preferences Ranking 1 to 5 marks by evaluating adaptability to different work settings (remote, hybrid, or on-site) and ability to maintain productivity.
    Generate the Problem-Solving and Decision-Making Style Ranking 1 to 5 marks by assessing problem-solving approach, creativity, critical thinking, and conflict resolution.
    Only the Cultural Fit Mark with one decimal. The Alignment with Core Company Values, Professionalism and Work Ethic, Teamwork and Collaboration Style, Adaptability to Work Environment Preferences and Problem-Solving and Decision-Making Style are integer.
    Generate a fifty words assessment summary for Cultural Fit of the following interview conversation: {text}. The assessment summary only can write pronoun as 'the applicant' and 'his/her'.
    """

    summary = model.generate_content(prompt)
    # print(summary)

    # formatting the output to make it look cleaner
    culturalfit = summary.text.replace("**", "").replace("\n\n", "\n")
    return culturalfit

def generate_attitude(text):

    prompt = f"""
    Make the Attitude Mark with one decimal by calculate the Attitude Mark = [(Professionalism * 25%) + (Positivity and Enthusiasm * 25%) + (Resilience and Response to Challenges * 25%) + (Motivation and Work Ethic * 25%)].
    Generate the Professionalism Ranking 1 to 5 marks by evaluate the candidate’s conduct during the interview, including adherence to interview norms, respectful communication, and overall demeanor. 
    Generate the Positivity and Enthusiasm Ranking 1 to 5 marks by Evaluate he lettel of enthusiasm and positive outlook the candidate displays about the opportunity and their responses to questions. 
    Generate the Resilience and Response to Challenges Ranking 1 to 5 marks by evaluate the candidate's ability to discuss past challenges constructively and demonstrate learning and resilience. 
    Generate the Motivation and Work Ethic Ranking 1 to 5 marks by evaluate the candidate’s eagerness to contribute to the team and company, as evidenced by their energy levels, commitment to achieving goals, and feedback from references. 
    Only the Attitude Mark with one decimal. The Professionalism, Positivity and Enthusiasm, Resilience and Response to Challenges and Motivation and Work Ethic are integer.
    Generate a fifty words assessment summary for Attitude of the following interview conversation: {text}. The assessment summary only can write pronoun as 'the applicant' and 'his/her'.
    """

    summary = model.generate_content(prompt)
    # print(summary)

    # formatting the output to make it look cleaner
    attitude = summary.text.replace("**", "").replace("\n\n", "\n")
    return attitude

def generate_communicationskill(text):

    prompt = f"""
    Make the Communication Skill Mark with one decimal by calculate the Communication Skill Mark = [(Clarity, Coherence, and Conciseness of Responses * 25%) + (Listening and Engagement in Dialogue * 25%) + (Written Communication Skills * 25%) + (Non-verbal communication * 25%)].
    Generate the Clarity, Coherence, and Conciseness of Responses Ranking 1 to 5 marks by Evaluate How well the candidate articulates thoughts in a clear, logical, and concise manner during interviews. 
    Generate the Listening and Engagement in Dialogue Ranking 1 to 5 marks by evaluates the candidate's ability to actively listen, understand questions or statements, and engage in meaningful back-and-forth dialogue. 
    Generate the Written Communication Skills Ranking 1 to 5 marks by evaluate proficiency in written communication, as demonstrated through email exchanges, resumes, and any take-home assignments. 
    Generate the Non-verbal communication Ranking 1 to 5 marks by evaluate the use of non-verbal cues, such as eye contact, gestures, and facial expressions, to complement verbal communication and enhance understanding. 
    Only the Communication Skill Mark with one decimal. The Clarity, Coherence, and Conciseness of Responses, Listening and Engagement in Dialogue, Written Communication Skills and Non-verbal communication are integer.
    Generate a fifty words assessment summary for Communication Skill of the following interview conversation: {text}. The assessment summary only can write pronoun as 'the applicant' and 'his/her'.
    """

    summary = model.generate_content(prompt)
    # print(summary)

    # formatting the output to make it look cleaner
    communicationskill = summary.text.replace("**", "").replace("\n\n", "\n")
    return communicationskill

def generate_adaptability(text):

    prompt = f"""
    Make the Adaptability Mark with one decimal by calculate the Adaptability Mark = [(Successful Adaptation to Change * 25%) + (Responses to Hypothetical Scenarios * 25%) + (Learning and Applying Feedback * 25%) + (Feedback from References on Adaptability and Problem-solvin* 25%)].
    Generate the Successful Adaptation to Change Ranking 1 to 5 marks by evaluates specific past experiences shared by the candidate that demonstrate their ability to adapt to new situations, roles, or environments effectively. 
    Generate the Responses to Hypothetical Scenarios Ranking 1 to 5 marks by evaluates the candidate's creativity and problem-solving abilities when confronted with hypothetical scenarios involving change or unexpected challenges. 
    Generate the Learning and Applying Feedback Ranking 1 to 5 marks by evaluates the candidate's openness to feedback and their capacity to incorporate this feedback into personal growth and improvement. 
    Generate the Feedback from References on Adaptability and Problem-solving Ranking 1 to 5 marks by evaluate external perspectives on the candidate's adaptability and problem-solving skills in previous roles or projects, as provided by references. 
    Only the Adaptability Mark with one decimal. The Successful Adaptation to Change, Responses to Hypothetical Scenarios, Learning and Applying Feedback and Feedback from References on Adaptability and Problem-solvin are integer.
    Generate a fifty words assessment summary for Adaptability of the following interview conversation: {text}. The assessment summary only can write pronoun as 'the applicant' and 'his/her'.
    """

    summary = model.generate_content(prompt)
    # print(summary)

    # formatting the output to make it look cleaner
    adaptability = summary.text.replace("**", "").replace("\n\n", "\n")
    return adaptability

def generate_mbti(mbti_type):

    prompt = f"""
    Generate a ninety words summary of the candidate's predicted mbti type: {mbti_type} characteristics in the workplace. Highlight their thoughtful and strategic approach, strong intuition, organizational skills, focus on positive change and sustainability, empathetic nature, and ability to foster collaboration and effective leadership.The summary only can write pronoun as 'the applicant' and 'his/her'.
    """

    summary = model.generate_content(prompt)
    # print(summary)

    # formatting the output to make it look cleaner
    mbti = summary.text.replace("**", "").replace("\n\n", "\n")
    return mbti

def generate_summary_recommendation_interviewee(text):

    prompt = f"""
    Strengths come from many areas such as good technical skills, excellent preparation, excellent communication skills, a good attitude and the ability to adapt. 
    Specific, actionable feedback can also be listed on areas where candidates demonstrate gaps or opportunities for improvement.
    Weaknesses and areas for improvement may include recommendations for professional development, additional training, or areas to focus on in future roles. 
    Generate the list of the candidate's strengths in the following interview conversation: {text}. 
    If the candidate does not have any strengths, write the candidate did not demonstrate any significant strengths during the interview process.
    Generate the list of the candidate's weaknesses and areas for improvement as demonstrated in the following interview conversation: {text}. 
    """
    summary = model.generate_content(prompt)
    # print(summary)

    # formatting the output to make it look cleaner
    summary_recommendation_interviewee = summary.text.replace("**", "").replace("\n\n", "\n").replace("*",".")
    return summary_recommendation_interviewee

def generate_summary_recommendation_hr(text):

    prompt = f"""
    Generate a 80 words Summary of the candidate in all aspect like the soft skill and tech skill using following interview conversation: {text}. Integrate insights from each section to highlight the candidate’s overall strengths and how they align with the role's requirements and the company's culture. Identify any potential areas for growth or concerns that emerged during the evaluation. The assessment summary only can write pronoun as 'the applicant' and 'his/her'.
    Based on the comprehensive assessment, generate a 40 words recommendation whether to proceed to the next round of interviews, be offered the position, consider the candidate for a different job position, or fail. Just to give suggestions that the actual HR will take the decision. 
    """

    summary = model.generate_content(prompt)
    # print(summary)

    # formatting the output to make it look cleaner
    summary_recommendation_hr = summary.text.replace("**", "").replace("\n\n", "\n")
    return summary_recommendation_hr

def main(text, mbti_type):
    technical = generate_technical(text)
    preparation = generate_preparation(text)
    culturalfit = generate_culturalfit(text)
    attitude = generate_attitude(text)
    communicationskill = generate_communicationskill(text)
    adaptability = generate_adaptability(text)
    mbti = generate_mbti(mbti_type)
    summary_recommendation_interviewee = generate_summary_recommendation_interviewee(text)
    summary_recommendation_hr = generate_summary_recommendation_hr(text)
    return technical, preparation, culturalfit, attitude, communicationskill, adaptability, mbti, summary_recommendation_interviewee, summary_recommendation_hr

text = """
HR: Good morning! Thank you for coming in today. Let's start with some general questions about your knowledge of the company, role, and industry. Can you tell me what you know about our company's approach to sustainability?
Candidate: Um, well, I know your company is big on being green and stuff. Like, you recycle and use solar panels, right?
HR: Actually, while those are components of our sustainability efforts, our approach is much broader. We focus on reducing our carbon footprint across all operations and integrating sustainability into our business strategies for long-term impact. Let's move on to the next question.
HR: Now, moving on to technical aspects, could you describe your experience with data analysis tools and techniques relevant to sustainability reporting?
Candidate: Uh, I've used Excel a bit, I guess. And I know what Tableau is, but I haven't really used it. I'm not sure what you mean by sustainability reporting, though.
HR: I see. Sustainability reporting involves collecting and analyzing data related to environmental and social performance to assess our impact and progress towards sustainability goals. It's essential for companies like ours to track and report on metrics such as energy consumption, emissions, and waste management. Let's move on to the next question.
HR: Great to hear. Let's switch back to general questions. How do you envision the role of an IT Business Analyst contributing to our sustainability objectives?
Candidate: Um, I guess an IT Business Analyst could help, like, make sure computers are turned off when they're not being used? And maybe, like, track how much paper we use?
HR: While those are valid points, the role of an IT Business Analyst in sustainability goes beyond those tasks. It involves leveraging technology to optimize processes, analyse data, and support strategic decision-making aligned with our sustainability goals. Let's move on to the next question.
HR: Now, for a technical question, could you provide an example of a sustainability-related project you've worked on where you had to analyse complex datasets to identify trends or patterns?
Candidate: Um, I haven't really worked on anything like that before. I mean, I did a project in school once where we had to, like, analyse some data about recycling rates, but it wasn't that complicated.
HR: I see. It's important for this role to have experience in analysing complex datasets to drive informed decision-making regarding sustainability initiatives. Let's move on to the next question.
HR: Finally, how do you stay updated on developments in sustainability practices and technologies within the IT industry?
Candidate: Uh, I don't really keep up with that stuff. I mean, I guess I could Google it if I needed to.
HR: It's crucial for professionals in this field to stay informed about emerging trends and best practices. Let's conclude our interview for today.
"""
mbti_type = "intj"

technical, preparation, culturalfit, attitude, communicationskill, adaptability, mbti, summary_recommendation_interviewee, summary_recommendation_hr = main(text, mbti_type)

print("Technical Assessment")
print("Technical Tool Proficiency")
print(technical)
print("\nSoft Skills Assessment")
print(preparation)
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print(culturalfit)
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print(attitude)
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print(communicationskill)
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print(adaptability)
print("\nMBTI Personality Assessment in Workplace")
print("--picture--")
print(mbti)
print("\nOverall Evaluation and Recommendation for Interviewee")
print("Feedback for Candidate")
print(summary_recommendation_interviewee)
print("\nOverall Evaluation and Recommendation for HR")
print(summary_recommendation_hr)


#Good
# text = """
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

#Average
# text = """
# HR: Good morning! Thank you for coming in today. Let's start with some general questions about your knowledge of the company, role, and industry. Can you tell me what you know about our company's approach to sustainability?
# Candidate: Good morning. From my research, I understand that your company has implemented various sustainability initiatives, such as investing in renewable energy sources and reducing waste in your supply chain. You've also been involved in community outreach programs promoting environmental awareness. 
# HR: That's a good overview. Now, moving on to technical aspects, could you describe your experience with data analysis tools and techniques relevant to sustainability reporting?
# Candidate: Sure. I have experience using Excel for data manipulation and analysis during my internship. I've also used some visualization tools like Power BI to create reports. While I haven't specifically worked on sustainability reporting, I believe my skills in data analysis can be applied to analyse environmental data and track performance metrics.
# HR: Thank you for sharing. Let's switch back to general questions. How do you envision the role of an IT Business Analyst contributing to our sustainability objectives?
# Candidate: I believe an IT Business Analyst can play a key role in identifying opportunities for integrating sustainability considerations into IT systems and processes. This could involve developing tools to track energy consumption or analysing data to identify areas for efficiency improvements. Additionally, collaborating with cross-functional teams to ensure IT projects align with sustainability goals would be essential.
# HR: That's a thoughtful response. Now, for a technical question, could you provide an example of a sustainability-related project you've worked on where you had to analyse complex datasets to identify trends or patterns?
# Candidate: In a previous project, I was involved in analysing customer data to identify opportunities for waste reduction in product packaging. By examining purchasing patterns and feedback data, we were able to propose changes to packaging materials and design, resulting in reduced environmental impact and cost savings for the company.
# HR: Interesting. Finally, how do you stay updated on developments in sustainability practices and technologies within the IT industry?
# Candidate: I make an effort to stay informed by following industry blogs and attending webinars on sustainability trends. Additionally, I try to incorporate sustainability considerations into my personal projects and research to stay engaged with current practices and technologies.
# HR: Thank you for sharing your approach. That concludes our interview for today.
# """

#Bad
# text = """
# HR: Good morning! Thank you for coming in today. Let's start with some general questions about your knowledge of the company, role, and industry. Can you tell me what you know about our company's approach to sustainability?
# Candidate: Um, well, I know your company is big on being green and stuff. Like, you recycle and use solar panels, right?
# HR: Actually, while those are components of our sustainability efforts, our approach is much broader. We focus on reducing our carbon footprint across all operations and integrating sustainability into our business strategies for long-term impact. Let's move on to the next question.
# HR: Now, moving on to technical aspects, could you describe your experience with data analysis tools and techniques relevant to sustainability reporting?
# Candidate: Uh, I've used Excel a bit, I guess. And I know what Tableau is, but I have not really used it. I'm not sure what you mean by sustainability reporting, though.
# HR: I see. Sustainability reporting involves collecting and analyzing data related to environmental and social performance to assess our impact and progress towards sustainability goals. It's essential for companies like ours to track and report on metrics such as energy consumption, emissions, and waste management. Let's move on to the next question.
# HR: Great to hear. Let's switch back to general questions. How do you envision the role of an IT Business Analyst contributing to our sustainability objectives?
# Candidate: Um, I guess an IT Business Analyst could help, like, make sure computers are turned off when they're not being used? And maybe, like, track how much paper we use?
# HR: While those are valid points, the role of an IT Business Analyst in sustainability goes beyond those tasks. It involves leveraging technology to optimize processes, analyse data, and support strategic decision-making aligned with our sustainability goals. Let's move on to the next question.
# HR: Now, for a technical question, could you provide an example of a sustainability-related project you've worked on where you had to analyse complex datasets to identify trends or patterns?
# Candidate: Um, I have not really worked on anything like that before. I mean, I did a project in school once where we had to, like, analyse some data about recycling rates, but it was not that complicated.
# HR: I see. It's important for this role to have experience in analysing complex datasets to drive informed decision-making regarding sustainability initiatives. Let's move on to the next question.
# HR: Finally, how do you stay updated on developments in sustainability practices and technologies within the IT industry?
# Candidate: Uh, I do not really keep up with that stuff. I mean, I guess I could Google it if I needed to.
# HR: It's crucial for professionals in this field to stay informed about emerging trends and best practices. Let's conclude our interview for today.
# """

