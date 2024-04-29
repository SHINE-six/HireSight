import os
import vertexai
from vertexai.generative_models import GenerativeModel
import vertexai.preview.generative_models as generative_models

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ".\GOOGLE_APPLICATION_CRED.json"

vertexai.init(project="civic-surge-420016", location="asia-southeast1")


 

# Set up the model
generation_config = {
    "max_output_tokens": 100,
    "temperature": 0.2,
    "top_p": 0.8,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}


model = GenerativeModel("gemini-1.0-pro",generation_config=generation_config, safety_settings=safety_settings)

prompt_parts = [
  "Role: You are an Interviewer, EVA from HILTI, you should only generate responses as a recruiter view in one or two sentences like how an actual interviewer talks. Just generate the reply do not add extra things like label or newline.",
  "jobTitle: IT BUSINESS ANALYST (SUSTAINABILITY)- Fresh Graduates",
  "jobDescription: As an IT Business Analyst in (SUSTAINABILITY), the employee  will collaborate with the IT Product Owner and work with Global Sustainability Business Teams on key areas like Innovation, Compliance, Operation Excellence, Digitalization, and Automation. The job primary focus will be on the ERP systems SAP S/4HANA and SAP Business ByDesign, including implementing modules like the Sustainability Control Tower to meet compliance and enhance reporting. The employee will be tasked with learning business processes, supporting the design and implementation of solutions, and interacting with third-party applications. Additionally, the employee will define processes, develop system requirements, and assist in designing and testing custom solutions. The job need to handle daily operational issues through the ServiceNow ticketing platform, working alongside the Corporate Functions IT team to deliver effective business solutions.",
  "jobSkills: Possess a Bachelor's or Master's degree in IT, Computer Science, or a related field with a CGPA of 3.5 or higher. Fluent in English with a willingness to work in a multicultural environment. Keen interest in ERP solutions, especially SAP S/4HANA, and system functionalities. Eager to work on defining and coding business processes in sustainability domains. High willingness to learn and self-develop within the domain. Excellent communication skills, proactive approach, and a strong commitment to success.",
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
    output 3 if the text is answering a questions or saying so useful information or not asking a question,
    output 4 if the text is related to asking a question,). Sentence:{text}"""
    response = model.generate_content(prompt)
    
    #formatting the output to make it look cleaner
    generated_answers=response.text.replace("**", "")
    generated_answers=response.text.replace("##", "")
    generated_answers=generated_answers.strip()
    return generated_answers


#function to generate the interview questions by connecting to the Gen AI model
def generate_general_interview_questions(text,previous_reply):

    prompt = f"""Generate one or two-sentence responses for only one general interview question just like a HR recruiter view., 
    please only generate the question only, do not add extra things like label or newline.
      New generated question must not similar to current reply:{text} and previous_question:{previous_reply}
    """

    response = model.generate_content(prompt)

    #formatting the output to make it look cleaner
    generated_questions=response.text.replace("**", "")
    generated_questions=response.text.replace("##", "")
    generated_questions=generated_questions.strip()
    return generated_questions


#function to generate the interview questions by connecting to the Gen AI model
def generate_technical_interview_questions(text,previous_reply):
    prompt = f"""praise the user then generate strictly one business analysis position related interview question especially ERP solutions (SAP S/4HANA) or sustainablilty business, please only make in a sentence do not add extra things like label or newline.
    the one question should not be similar to previous question:{text}. and previous question:{previous_reply}
    """

    response = model.generate_content(prompt)

    #formatting the output to make it look cleaner
    generated_questions=response.text.replace("**", "")
    generated_questions=response.text.replace("##", "")
    generated_questions=generated_questions.strip()
    return generated_questions


def generate_interview_answer(text):
    prompt = f"""Answer this question:{text} with some related content and ask if there is any more question. Please only generate the answer for the question do not add extra things just one line summary"""
    response = model.generate_content(prompt)

    #formatting the output to make it look cleaner
    generated_answers=response.text.replace("**", "")
    generated_answers=response.text.replace("##", "")
    generated_answers=generated_answers.strip()
    return generated_answers


def generate_ask_question():
    prompt = f"""Generate a reponse to ask the interviewee if they have any questions. Please only generate the question do not add extra things."""
    response = model.generate_content(prompt)

    #formatting the output to make it look cleaner
    generated_answers=response.text.replace("**", "")
    generated_answers=response.text.replace("##", "")
    generated_answers=generated_answers.strip()
    return generated_answers
 

def generate_repeat(text):
    prompt = f"""Repeat this question:{text} in a simpler way. Please only generate the question do not add extra things"""
    response = model.generate_content(prompt)

    #formatting the output to make it look cleaner
    generated_answers=response.text.replace("**", "")
    generated_answers=response.text.replace("##", "")
    generated_answers=generated_answers.strip()
    return generated_answers


def generate_end_message():
    prompt = f"""Just generate a message to end the interview appreciate the interviewee and say the result will be sent via email.
    Please do not add extra things just one line."""
    response = model.generate_content(prompt)

    #formatting the output to make it look cleaner
    generated_answers=response.text.replace("**", "")
    generated_answers=response.text.replace("##", "")
    generated_answers=generated_answers.strip()
    return generated_answers


# i need to save data or retrieve data from mongoDB
# i want the previous reply, the generalQuestion, the technicalQuestion
previous_reply = ""
generalQuestion = 0
technicalQuestion = 0

def llm_process(text):
    global previous_reply
    global generalQuestion
    global technicalQuestion
    flag = detect_sentence(text, prompt_parts)
    data = {
        "reply": "",
        "flag": "",
    }
    if flag == "1":
         data["reply"] = generate_end_message()
         previous_reply = data["reply"]
         data["flag"] = "1"
         generalQuestion = 0
         technicalQuestion = 0
         return data
    if flag == "2":
         data["reply"] = generate_repeat(previous_reply)
         previous_reply = data["reply"]
         data["flag"] = "2"
         return data
    if flag == "3":
        if generalQuestion < 1:
            data["reply"] = generate_general_interview_questions(text,previous_reply)
            previous_reply = data["reply"]
            data["flag"] = "3"
            generalQuestion += 1
            return data
        elif generalQuestion >= 1 and technicalQuestion < 3:
            data["reply"] = generate_technical_interview_questions(text,previous_reply)
            previous_reply = data["reply"]
            data["flag"] = "3"
            technicalQuestion += 1
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
        return data

    
def main(text):
    data = llm_process(text)
    return data