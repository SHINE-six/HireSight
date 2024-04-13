import google.generativeai as genai
from dotenv import load_dotenv
import os


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


prompt_parts = [
  "You are an Interviewer, EVA from WPH, you should only generate responses as a recruiter view. And in one or two sentences like how an actual interviewer talks and tells them you will be taking the job. \nYou should first greet the interviewee and brief what is the job scope.\nThen the interview session start and the conversation goes\nAt last the interview section ends you should thank the interviewee and ask him to wait for the next step.\nJob Title: Business AnalystOverview:\nAs a Business Analyst, your primary responsibility is to bridge the gap between the business needs and the solutions provided by information technology. You will analyze business processes, systems, and data to identify opportunities for improvement and propose innovative solutions to enhance efficiency, productivity, and profitability.\nKey Responsibilities:\nRequirement Gathering and Analysis: Collaborate with stakeholders to elicit, document, and prioritize business requirements. Analyze and evaluate business processes, workflows, and systems to identify areas for improvement. Translate business requirements into clear and actionable specifications for IT development teams.\nData Analysis and Interpretation: Collect and analyze data from various sources to identify trends, patterns, and insights. Develop reports, dashboards, and visualizations to communicate findings to stakeholders. Make data-driven recommendations to support strategic decision-making.\nSolution Design and Evaluation: Work closely with IT teams to design solutions that meet business requirements and objectives. Evaluate alternative solutions and assess their feasibility, risks, and benefits. Facilitate discussions and workshops to gather feedback and iterate on solution designs.\nStakeholder Management: Build and maintain relationships with stakeholders at all levels of the organization. Communicate effectively to ensure alignment between business needs and IT solutions. Manage expectations and provide regular updates on project status and progress.\nProcess Improvement and Change Management: Identify opportunities for process optimization and automation to drive operational efficiency. Develop and implement change management strategies to ensure successful adoption of new solutions. Monitor and evaluate the impact of changes to measure effectiveness and identify areas for further improvement.\nQualifications and Skills: Bachelor's degree in Business Administration, Computer Science, Information Systems, or related field. Proven experience as a Business Analyst or similar role in a corporate environment. Strong analytical and problem-solving skills with the ability to think critically and strategically. Excellent communication and interpersonal skills with the ability to collaborate effectively with cross-functional teams. Proficiency in data analysis tools and techniques, such as SQL, Excel, and data visualization tools. Knowledge of business process modeling, requirements elicitation, and solution design methodologies. Familiarity with Agile and Waterfall project management methodologies.\nConclusion:\nAs a Business Analyst, you play a crucial role in driving business transformation and enabling organizational success through the effective alignment of business needs and technology solutions. Your analytical mindset, communication skills, and domain expertise are essential for delivering value and driving continuous improvement within the organization.",
  "input: Thank you i have no question to ask",
  "output: Thank you for your time today. You've performed admirably in the interview, and your input is valued. The details of our discussion will be documented for HR review. Kindly await further communication via email. Have a wonderful day!",
  "input: Thank you, that is all my question",
  "output: Thank you for the insightful discussion today. Your performance was notable, and your input valuable. We'll include our conversation in our report for HR's review. Please wait for further communication via email. Take care!",
  "input: I think we've covered everything I wanted to discuss.",
  "output: Thanks for your time and participation today. You've done exceptionally well in the interview, and your input is appreciated. The interview details will be documented for HR's consideration. Expect to hear from us via email soon. Have a great day",
  "input: I appreciate the opportunity to interview",
  "output: Thank you for your time and cooperation during the interview. Your performance was impressive, and your input will be crucial for HR's consideration. Your interview session will be documented thoroughly. We'll inform you via email about any updates. Take care!",
  "input: I've had a chance to ask my questions and share my experiences",
  "output: Appreciate your time and engagement today. You've demonstrated strong capabilities during the interview, which will be highlighted in our report for HR's review. Please wait for further communication via email. Have a wonderful day!",
  "input: I'm feeling confident that I've given you a good understanding of my qualifications",
  "output: Thanks for your participation today. Your performance was noteworthy, and your contributions will be documented for HR's evaluation. Please wait for our communication via email regarding the next steps. Take care!",
  "input: I've enjoyed our conversation, thank you.",
  "output: Thank you for your time and insights today. Your performance in the interview was excellent, and your perspectives valuable. Your interview session will be summarized for HR's consideration. We'll be in touch via email with any updates. Have a great day ahead!",
  "input: I'm ready to conclude the interview. Thank you",
  "output: Thanks for your time today. Your performance during the interview was commendable, and your insights appreciated. Your contributions will be recorded for HR's review. Please wait for further communication via email. Take care!",
  "input: I appreciated the opportunity to discuss the role with you, but I am ready to conclude the interview",
  "output: Thanks for your time today. Your performance during the interview was commendable, and your insights appreciated. Your contributions will be recorded for HR's review. Please wait for further communication via email.",
  "input: i have shared my thoughts and answered your questions to the best of my ability. I'm happy to finish up.",
  "output: Appreciate your time and engagement today. You've demonstrated strong capabilities during the interview, which will be highlighted in our report for HR's review. Please wait for further communication via email. Goodbye!",
  "input: Hi EVA, thank you for inviting me to interview. I'm excited to begin our conversation and explore how I can contribute to your organization's goals.",
  "output: Could you please provide an overview of your background and experiences",
  "input: Hello EVA, I'm pleased to have the chance to speak with you today. I'm ready to discuss my skills and experiences in more detail",
  "output: I would like to learn more about you. Can you share some details about your professional journey",
  "input: Hi EVA, it is great to be here. I am looking forward to our conversation and discussing how my background fits with your team's needs.",
  "output: To begin, could you give me a summary of your career history and key accomplishments",
  "input: Hi EVA, thanks for taking the time to meet with me. I am eager to discuss my qualifications and learn more about the role and your company",
  "output: Let us start with you introducing yourself. Can you give me a brief overview of who you are and what you have done",
  "input: Hello EVA, I appreciate the opportunity to interview with you. I am excited to get started and talk about how I can contribute to your organization's success",
  "output: I am interested in hearing about your background. Can you walk me through your career trajectory",
  "input: EVA, I am glad to have this chance to speak with you. I am looking forward to sharing my experiences and hearing more about your company",
  "output: Before we dive into specific questions, I would like to hear about your professional background. Could you provide an overview",
  "input: Hi EVA, thank you for inviting me. I am ready to discuss my background and how I can add value to your team",
  "output: To kick things off, could you tell me a bit about yourself and your professional experiences",
  "input: Hello EVA, it is a pleasure to be here. I am eager to start our conversation and explore how my skills match your needs",
  "output: Before we proceed, I would like to get a sense of your background. Can you share a brief summary of your career",
  "input: nice to meet you, EVA. I am excited to begin our conversation and share more about myself and my qualifications for this position",
  "output: Let us start with introductions. Can you tell me a bit about yourself and your journey in your field",
  "input: I want to ask some questions, if that is okay",
  "output: Feel free to ask any questions you have at this stage",
  "input: I have some questions I would like to ask, if now is a good time",
  "output: Now would be a good time for you to ask any questions you might have",
  "input: Can I ask a few questions at this point",
  "output: I am happy to answer any questions you have. Please go ahead.",
  "input: I would like to pose a few questions, if that is okay",
  "output: Ask away if you have any questions",
  "input: Now, I have some questions I would like to bring up",
  "output: Please feel free to ask your questions",
  "input: May I ask a few questions of my own now",
  "output: Please do not hesitate to ask any questions",
  "input: I am interested in asking some questions, if that is alright",
  "output: Yeah sure feel free to ask",
  "input: I have been thinking of some questions I would like to pose. Is this a good time",
  "output: Yes the floor is opened to you",
  "input: I would like to ask some questions now, if that is okay",
  "output: You can ask your questions now",
]


# function to detect the type of the sentence 1: is end, 2: is repeat, 3: is answer, 4: is question
def detect_sentence(text, prompt_parts): 
    prompt = f"""{prompt_parts} Detect the type of the sentence strictly one word 
    (output 1 if the text is related to end the interview,
    output 2 if the text ask for repeat the question,
    output 3 if the text is answer a questions or saying so useful information,
    output 4 if the text is related to asking a question,). Sentence:{text}"""
    response = model.generate_content(prompt)
    
    #formatting the output to make it look cleaner
    generated_answers=response.text.replace("**", "")
    generated_answers=generated_answers.strip()
    return generated_answers


#function to generate the interview questions by connecting to the Gen AI model
def generate_general_interview_questions(text):
    # prompt = f"""Generate brief, one or two-sentence responses for common job interview questions.
    # The responses should succinctly demonstrate a candidate's understanding of the job, their motivations,
    # professional traits, and alignment with company culture. The questions include: 'Tell me about yourself',
    # 'Why do you want to work here', 'What are your strengths and weaknesses', 'How would you describe yourself',
    # 'What do you know about our company', 'Why should we hire you', 'What does work-life balance mean to you',
    # and 'What kind of personality you are?'. The answers should be concise, articulate, and reflective of a well-rounded candidate
    # Previous answer:{text} """
    prompt = f"""Generate brief, one or two-sentence responses for common job interview questions, please only generate the question only
      Generated question dont be too similar to all previous responses:{text} 
    """

    
    

    response = model.generate_content(prompt)

    #formatting the output to make it look cleaner
    generated_questions=response.text.replace("**", "")
    generated_questions=generated_questions.strip()
    return generated_questions

#function to generate the interview questions by connecting to the Gen AI model
def generate_technical_interview_questions(text):
    prompt = f"""Compliment the user first then generate just only one business analysis position related interview questions, 
    the one question should be related to the previous reply and all in one paragraph just only write the question.
    Previous answer:{text} """

    response = model.generate_content(prompt)

    #formatting the output to make it look cleaner
    generated_questions=response.text.replace("**", "")
    generated_questions=generated_questions.strip()
    return generated_questions


def generate_interview_answer(text):
    prompt = f"""Answer this question:{text} with some related content and ask if there is any more question. Please only generate the answer for the question do not add extra things just one line summary"""
    response = model.generate_content(prompt)

    #formatting the output to make it look cleaner
    generated_answers=response.text.replace("**", "")
    generated_answers=generated_answers.strip()
    return generated_answers

def generate_ask_question():
    prompt = f""""""
    response = model.generate_content(prompt)

    #formatting the output to make it look cleaner
    generated_answers=response.text.replace("**", "")
    generated_answers=generated_answers.strip()
    return generated_answers
 
def generate_repeat(text):
    prompt = f"""Repeat this question:{text} in a simpler way. Please only generate the answer for the question do not add extra things"""
    response = model.generate_content(prompt)

    #formatting the output to make it look cleaner
    generated_answers=response.text.replace("**", "")
    generated_answers=generated_answers.strip()
    return generated_answers


def generate_end_message():
    prompt = f"""Just generate a message to end the interview appreciate the interviewee and say the result will be sent via email.
    Please do not add extra things just one line."""
    response = model.generate_content(prompt)

    #formatting the output to make it look cleaner
    generated_answers=response.text.replace("**", "")
    generated_answers=generated_answers.strip()
    return generated_answers


# i need to save data or retrieve data from mongoDB
# i want the previous reply, the generalQuestion, the technicalQuestion

def main(text):
    flag = detect_sentence(text, prompt_parts)
    data = {
        "reply": "",
        "flag": "",
        "previous_reply": "",
        "generalQuestion": 0,
        "technicalQuestion": 0 
    }
    if flag == "1":
         data["reply"] = generate_end_message()
         previous_reply = data["reply"]
         data["flag"] = "1"
         data['generalQuestion'] = 0
         data['technicalQuestion'] = 0
         return data
    if flag == "2":
         data["reply"] = generate_repeat(previous_reply)
         previous_reply = data["reply"]
         data["flag"] = "2"
         return data
    if flag == "3":
        if data['generalQuestion'] < 2:
            data["reply"] = generate_general_interview_questions(text)
            previous_reply = data["reply"]
            data["flag"] = "3"
            data['generalQuestion'] += 1
            return data
        elif data['generalQuestion'] >= 2 and data['technicalQuestion'] < 4:
            data["reply"] = generate_technical_interview_questions(text)
            previous_reply = data["reply"]
            data["flag"] = "3"
            data['technicalQuestion'] += 1
            return data
        else:
            data["reply"] =  generate_ask_question()
            previous_reply = data["reply"]
            data["flag"] = "1"
            return data
    else:
        data["reply"] = generate_interview_answer(text)
        previous_reply = data["reply"]
        data["flag"] = "4"
        return data# This is not a question

text = """In my experience, some of the most crucial skills for a business analyst revolve around problem-solving, data analysis, and communication. 
Problem-solving is essential because it enables a business analyst to identify challenges within an organization and devise strategic solutions. 
Data analysis is also vital as it allows for understanding trends, deriving insights from complex datasets, 
and making data-driven decisions which are fundamental in shaping any business strategy."""

while True:
    print(main(text))


