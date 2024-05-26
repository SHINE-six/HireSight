import shutil
import time
from fastapi import FastAPI, File, Form, Request, UploadFile, BackgroundTasks, WebSocket
from fastapi.responses import FileResponse
import uvicorn
# import resume_parser
import resumeRanker
import speech_to_text
import facial_prediction
import eye_tracking
# import LLM
# import tts
# import LLM
# import tts
import LLM_copy
import googleTTS
import wavspeech_to_json
import mongoDB
import disfluency
import plagiarism
import aiDetection
import mbti_last
import reportGeneration
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict
import datetime
import json
from pydantic import BaseModel


app = FastAPI()


origins = [
    "http://localhost:3000",  # Assuming your frontend app runs on localhost:3000
    "http://localhost:3001"
    # "https://ddncl8rd-8000.asse.devtunnels.ms/",  # Add your production origin as needed
]

# Add CORSMiddleware to the application
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specified origins
    allow_credentials=True,  # Allows cookies to be included in cross-origin HTTP requests
    allow_methods=["*"],  # Allows all methods (e.g., GET, POST, PUT, DELETE)
    allow_headers=["*"],  # Allows all headers
)

taskStatus: Dict[str, bool] = {"transcript": False, "faceEmotion": False, "eye": False, "text_LLM_tts_wavToJson": False}

# sample data
data = [
{
    "categoryId": 1,
    "jobCategory": "IT, Software & Digital",
    "jobCategoryDescription": "This division is responsible for spearheading innovative and complex technical projects, with a focus on information technology and digital transformation within the organization.",
    "subCategories": [
        {
            "subCategoryId": "1A",
            "subCategoryName": "IT Business Analyst",
            "subCategoryDescription": "Focused on leveraging business analytics tools and methodologies to improve decision-making and business practices within IT, Software & Digital projects.",
            "availableJobs": [
                {
                    "jobId": "1A_a",
                    "jobTitle": "IT BUSINESS ANALYST (SUSTAINABILITY)- Fresh Graduates",
                    "jobDescription": "As an IT Business Analyst, you will collaborate with the IT Product Owner and work with Global Sustainability Business Teams on key areas like Innovation, Compliance, Operation Excellence, Digitalization, and Automation. Your primary focus will be on the ERP systems SAP S/4HANA and SAP Business ByDesign, including implementing modules like the Sustainability Control Tower to meet compliance and enhance reporting. You'll be tasked with learning business processes, supporting the design and implementation of solutions, and interacting with third-party applications. Additionally, you will define processes, develop system requirements, and assist in designing and testing custom solutions. You will also handle daily operational issues through the ServiceNow ticketing platform, working alongside the Corporate Functions IT team to deliver effective business solutions.",
                    "jobSkills": ["Possess a Bachelor’s or Master’s degree in IT, Computer Science, or a related field with a CGPA of 3.5 or higherFluent in English with a willingness to work in a multicultural environment","Keen interest in ERP solutions, especially SAP S/4HANA, and system functionalities",
                                  "Eager to work on defining and coding business processes in sustainability domains","High willingness to learn and self-develop within the domain","Excellent communication skills, proactive approach, and a strong commitment to success."]
                },
                {
                    "jobId": "1A_b",
                    "jobTitle": "IT Business Analyst Salesforce",
                    "jobDescription": "As a Business Analyst in Hilti's Systematic Account Development program, you'll focus on enhancing Customer Relationship Management through Salesforce Sales Cloud. This role involves understanding business requirements, designing solution proposals, and supporting their implementation within Salesforce to optimize sales processes. You'll work within an international scrum team, using agile methodologies to deliver significant customer impact. While Salesforce Sales Cloud is your primary technology focus, you'll also engage with SAP S4 HANA, Salesforce Service Cloud, and AWS Microservices among others. This position plays a crucial role in providing transparency on sales opportunities and enabling effective use of Hilti products on job sites.",
                    "jobSkills": ["Bachelor’s degree in computer science, software engineering, information technology, or related fields","Over 5 years of experience with cloud software (preferably Salesforce), business process management, and agile methodologies","Excellent communication and interpersonal skills, fluent in English for effective stakeholder management in a global matrix environment",
                                  "Passion for marketing, sales, and service business process design with a keen interest in CRM software","Strong willingness and capacity to learn."]
                },
                {
                    "jobId": "1A_c",
                    "jobTitle": "Business Intelligence Analyst",
                    "jobDescription": "As a Business Intelligence Analyst in the Global SAP Business Warehouse Team, you will enhance analytics and reporting within the Hilti organization. Your role involves collaborating with key business stakeholders to gather requirements and develop SAP BW data models to support decision-making processes. You will also advocate for the adoption of analytics, identify improvement opportunities in existing processes, and work with partners to implement new data models. Additionally, you will support and maintain these data models, driving change and leveraging data to inform strategic and tactical business decisions.",
                    "jobSkills": ["Bachelor's degree in Computer Science, IT, or Engineering required; Master's degree preferred","Minimum 2 years of experience with SAP Business Warehouse","Proficient in Business Intelligence, Data Warehousing, Data Modeling, SAP BW/4HANA, SAP BW on HANA, and ABAP",
                                  "Entrepreneurial, team-oriented, with strong problem-solving skills and an interest in technical leadership","Fluent in English with excellent communication skills."]
                },
                {
                    "jobId": "1A_d",
                    "jobTitle": "Internship - IT Business Analyst",
                    "jobDescription": "Join our IT team as an Intern and work as an IT Business Analyst on global IT projects. In this role, you will bridge the gap between business and IT, providing advice on incidents, and turning business requirements into practical solutions. You will help build and operate digital solutions that include mobile apps, cloud-based services, and backend systems based on our ERP solutions. This internship, lasting 4-6 months and starting flexibly based on your availability, offers hands-on experience in solution management and the opportunity to develop new product features in collaboration with product managers and technical staff.",
                    "jobSkills": ["Enrolled in Bachelor's/Master's in IT, Software Engineering, Data Science, or related fields","Strategic thinker with excellent problem-solving skills","Proactive and hands-on mentality","Strong communication and interpersonal abilities","Fluent in written and spoken English","Eager to learn and embrace challenges."]
                }
            ]
        }
    ],
    "availableJobs": [
        {
            "jobId": "1_a",
            "jobTitle": "Cloud QA Automation Engineer",
            "jobDescription": "As a Cloud QA Automation Engineer at Hilti, you will focus on defining and executing test cases, approaches, automation, and documentation within the Sales Core IT area. Your main goal is to ensure business requirements are accurately met through meticulous testing methods for complex software applications. Daily responsibilities include integrating with product or project teams to deliver high-quality software, thoroughly testing changes before production, and utilizing automation test suites. Additionally, you will continually seek to implement cutting-edge technologies to enhance IT QA processes at Hilti.",
            "jobSkills": ["Bachelor's or Master's in Information Systems, Computer Science, or related fields with a CGPA > 3.0","4+ years QA Engineer experience in the IT sector","Expertise in test automation tools like Cucumber, BDD, Gherkin, JMeter, and Postman","Familiarity with AWS products and navigating the AWS console",
                          "Skilled in analyzing test results and reporting with defined KPIs","Experience in agile environments and understanding of CI/CD processes; fluent in English."]
        },
        {
            "jobId": "1_b",
            "jobTitle": "Process Expert - Procurement IT",
            "jobDescription": "As a Procurement Support Specialist at Hilti, you will assist and guide Procurement Managers through the sourcing process to ensure compliance and high quality. You'll gain expertise in drafting Requests for Proposal, setting up auctions, and forming contracts, while also managing supplier data and leading system improvement projects. This role offers a comprehensive introduction to Hilti's business operations and involvement in a global team.",
            "jobSkills": ["Bachelor’s degree in Information Technology or Business Administration; Master’s degree preferred","Relevant professional experience, especially with ERP and procurement systems","Strong interdisciplinary teamwork and project management skills","Comprehensive approach to tasks, from planning to continuous improvement and documentation",
                          "Good analytical abilities with a strong affinity for IT systems","Excellent communication and presentation skills in English; additional languages beneficial."]
        },
    ]
},
{
    "categoryId": 2,
    "jobCategory": "Engineering",
    "jobCategoryDescription": "A core unit that drives the development of new products and services, ensuring the company stays at the forefront of engineering innovation and advancement.",
    "availableJobs": [
        {
            "jobId": "2_a",
            "jobTitle": "Application Engineer",
            "jobDescription": "This is an Application Engineer role providing structural analysis and design for Hilti's modular support systems. You'll support sales and business development teams during project acquisition and client interaction. You'll also lead engineering solution development and ensure adherence to project standards.",
            "jobSkills": ["Master's degree in Structural/Civil Engineering (PE preferred)","Extensive experience in steel structure design/civil engineering (Energy & Industry, large data centers, or complex modular buildings)",
                          "Experience with structural analysis software (e.g., RStab by Dlubal)","Familiarity with BIM Modeling software","Project management and tendering/estimating experience"]
        },
        {
            "jobId": "2_b",
            "jobTitle": "BIM Modeler",
            "jobDescription": " As a BIM Modeler I, you'll be the go-to person for Hilti's South Asia Pacific sales and projects in Energy, Industry, and Construction.  Using BIM software (Revit, AutoCAD), you'll create models, drawings, and documentation to support various teams.  Your expertise in structural modeling, MEP/FP, and construction standards will ensure high-quality deliverables for clients.  This role involves collaboration across departments and potential travel for meetings and training.",
            "jobSkills": ["Proficient in REVIT, AUTOCAD, and INVENTOR","Expertise in modular support systems, direct fastening, and firestop solutions","Skilled in producing technical documentation: models, drawings, and bills of materials",
                          "Effective communicator for project requirements and RFIs/RFPs/RFQs","Maintains detailed project and client records","Willing to travel for project-related activities."]
        }
    ]
},
{
    "categoryId": 3,
    "jobCategory": "Sales",
    "jobCategoryDescription": "A dynamic sector tasked with driving growth and revenue through strategic sales initiatives, combining deep technical knowledge with market acumen.",
    "availableJobs": [
        {
            "jobId": "3_a",
            "jobTitle": "Outperformer - Global Management Development Program - Business Track",
            "jobDescription": "The Hilti Outperformer is a two-year global management development program aimed at grooming post-graduate talent through real-world responsibilities. Participants rotate through key roles, starting with 12 months as an account manager or field engineer, followed by projects in logistics, HR, finance, marketing, or engineering at the national and regional headquarters, including a final strategic project in a contrasting market. The program, supported by senior management mentoring, offers rapid exposure and career advancement in various business areas.",
            "jobSkills": ["Studying for or recently graduated with a Master's or PhD, especially in business, engineering, or related fields","At least three months to two years of professional experience in internships, apprenticeships, or similar.","Fluent in English and at least one additional language; more languages preferred",
                          "Experience with international work or study","Assertive, curious, and committed with excellent communication and teamwork skills","Open to intercultural experiences and willing to work abroad; Malaysian citizenship or permanent residency required."]
        },
        {
            "jobId": "3_b",
            "jobTitle": "Account Manager (Sales role)",
            "jobDescription": "We are seeking a high-potential Account Manager with strong business acumen to join Hilti's high performing and supportive culture. This role involves achieving sales targets in an assigned territory by identifying business opportunities, promoting Hilti’s product line, and providing solutions through product demonstrations and user training. The candidate will expand sales by acquiring new clients and maintaining relationships with existing ones, ensure disciplined sales execution, handle customer inquiries and complaints, and engage in sales forecasting. Additionally, the role requires introducing new products to the market, collaborating with various departments, and handling ad-hoc tasks as needed.",
            "jobSkills": ["Minimum of a Diploma in any discipline","Open to fresh graduates with an interest in Sales and the Construction industry","Independent and effective in a team setting","Persuasive, persistent, sales-driven, and customer-focused",
                          "Strong communication and interpersonal skills","Previous sales experience with a successful track record is beneficial."]
        }
    ]
},
{
    "categoryId": 4,
    "jobCategory": "Human Resources",
    "jobCategoryDescription": "This team focuses on optimizing talent acquisition and management, particularly for roles that support the company's digital and technological initiatives.",
    "availableJobs": [
        {
            "jobId": "4_a",
            "jobTitle": "Talent Engagement Specialist - Digital",
            "jobDescription": "As a Talent Engagement Specialist at Hilti's Kuala Lumpur-based Digital Strategic Sourcing Hub, you'll focus on building a pipeline of IT, digital, and software talent for future roles across Asia-Pacific. Your responsibilities include proactive headhunting, managing talent pools using Beamery, and collaborating with Talent Acquisition Partners to meet Hilti's Lead 2030 hiring goals. You'll also enhance candidate experiences, promote Hilti’s digital presence, and maintain a strong network within the sourcing community to ensure a diverse and high-quality candidate pool.",
            "jobSkills": ["Bachelor’s degree in a related field with a minimum CGPA of 3.0","Expert in advanced search techniques and data mining for IT and digital sectors","6-10 years of sourcing experience with a focus on excellence","Skilled in delivering exceptional candidate experiences, preferably in the Asia Pacific region",
                          "Proficient with Applicant Tracking Systems and Talent Relationship Management, like Haufe and Beamery","Resilient in managing changing priorities and multiple stakeholder needs."]
        }
    ]
}
]

@app.get("/")
async def readRoot():
    print("Welcome to the Job Portal!")
    return {"message": "Welcome to the Job Portal!"}

@app.get("/jobopenings")
async def readRoot():
    return data

@app.get("/jobopenings/{category_id}")
async def readCategory(category_id: int):
    for category in data:
        if category["categoryId"] == category_id:
            return category
    return {"message": "Category not found"}

@app.get("/jobopenings/job/{job_id}")
async def readJob(job_id: str):
    for category in data:
        if 'subCategories' in category:
            for subCategory in category["subCategories"]:
                for job in subCategory["availableJobs"]:
                    if job["jobId"] == job_id:
                        return job
        if 'availableJobs' in category:
            for job in category["availableJobs"]:
                if job["jobId"] == job_id:
                    return job
    return {"message": "Job not found"}

def formatResumeIntoJson(resumeFile):
    if resumeFile.filename.endswith(".pdf"):  # Check if the uploaded file is a PDF
        # Read the uploaded PDF file as binary data
        pdfData = resumeFile.file.read()
        
        # Construct data object to post to the collection
        resume_data = {
            "filename": resumeFile.filename,
            "pdfData": pdfData
        }
        
        return resume_data

class jobDetail(BaseModel):
    jobId: str
    jobTitle: str
    jobDescription: str
    jobSkills: list

@app.post("/resume")
async def uploadResume(jobDetails: str = Form(...), email:str = Form(...), uniqueResumeID: str = Form(...), resume: UploadFile = File(...)):
    print("Received and processing resume...")
    
    jobDetails_dict = json.loads(jobDetails)
    jobDetails_dict = jobDetail(**jobDetails_dict)

    # mongoDB.postData("resumeDatabase", resumeRanker.postDataTOCollection(resume))
    toStoreJson = {
        "filename": None,
        "email": email,
        "uniqueResumeId": uniqueResumeID,
        "jobPostitionApply": jobDetails_dict.jobTitle,
        "AiDetection": None,
        "plagiarism": None,
        "suitability": None,
        "stage": "Ai detection",
        "pdfData": {}
    }
    parsedBinaryResume = formatResumeIntoJson(resume)
    toStoreJson['filename'] = parsedBinaryResume['filename']
    toStoreJson['pdfData'] = parsedBinaryResume['pdfData']

    parsedPdfToText:str = resumeRanker.main_PdfToText(parsedBinaryResume['pdfData'])

    toStoreJson['suitability'] = resumeRanker.main_ResumeSuitability(parsedBinaryResume['pdfData'], jobDetails_dict)
    toStoreJson['AiDetection'] = (aiDetection.main(parsedPdfToText))['probability_ai']
    toStoreJson['plagiarism'] = (plagiarism.main(parsedPdfToText))['Score']

    print(mongoDB.postData("resumeDatabase", toStoreJson))


    return {"status": 200, "message": "Resume uploaded successfully"}


@app.post("/resumeRanking")
async def getResumeRanking( jobTitle: str = Form(...), onlyApplicantCount: bool = Form(False)):
    # Get resume from MongoDB
    if onlyApplicantCount:
        return mongoDB.getResumeCount(jobTitle)
    else:
        return mongoDB.getResumeDetailsNoPdf(jobTitle, "Ai detection")
    # Get job title to pull relative job description
    # resumeRanker.oneJobDescriptionToAllResume(jobDescription, filePath)

# @app.get("/resume-ranking")
# async def getResumeRanking():  #* to change; pull all 'ba' job from mongodb, combine to json, and serve to hr frontend suitability
#     # fileter
#     return FileResponse(filePath, media_type="application/json", filename="resume_ranking.json")

# @app.get("/resume-ranking")
# async def getResumeRanking():  #* to change; pull all 'ba' job from mongodb, combine to json, and serve to hr frontend ai interview
#     filePath = "resume/resume_ranking.json"
#     return FileResponse(filePath, media_type="application/json", filename="resume_ranking.json")

@app.post("/login")
async def login(email: str = Form(...), password: str = Form(...)):
    foundUser = mongoDB.getOneDataFromCollection("Users", {"email": email})
    if foundUser:
        if foundUser['password'] == password:
            return {"status": 200, "message": "Login successful", "aiStage": foundUser['aiStage']}
        else:
            return {"status": 401, "message": "Incorrect password"}
        
    elif (not foundUser):
        mongoDB.postData("Users", {"email": email, "password": password, "aiStage": False})
        return {"status": 200, "message": "Sign up successful", "aiStage": False}

# -------------------- Initialize the session --------------------
global uniqueSessionID
uniqueSessionID = ""

@app.post("/ai-interview/session/start")
async def create_session(sessionJson: Request):
    sessionJson = await sessionJson.json()
    global uniqueSessionID
    uniqueSessionID = sessionJson['uniqueSessionID']
    print(mongoDB.postData("combinedData", sessionJson))
    print(mongoDB.postData("conversationLog", sessionJson))
    return {"status": 200, "message": "Session created successfully"}

# ----------------------- Audio thingy -----------------------
def text_LLM_tts_wavToJson(userTranscript: str):
    outputText = LLM_copy.main(userTranscript)
    print(mongoDB.appendDataToDocument("conversationLog", {"user": "Ai - EVA", "text": outputText['reply']}, uniqueSessionID))
    googleTTS.main(outputText['reply'])
    wavspeech_to_json.main()
    print("Text, TTS, and WAV to JSON conversion completed")
    taskStatus["text_LLM_tts_wavToJson"] = True

def run_speech_to_text(background_tasks):
    userTranscript = speech_to_text.main()
    userTranscript = userTranscript['text']
    print(mongoDB.appendDataToDocument("conversationLog", {"user": "applicant", "text": userTranscript}, uniqueSessionID))
    background_tasks.add_task(text_LLM_tts_wavToJson, userTranscript)
    taskStatus["transcript"] = True
    checkProcessFiles()

@app.post("/audio")
async def upload_audio(background_tasks: BackgroundTasks, audio: UploadFile = File(...)):
    print(audio)
    background_tasks.add_task(run_speech_to_text, background_tasks)
    with open(f"uploads/audio/{audio.filename}", "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)
        print(buffer)
        buffer.close()

    return {"message": "Audio converted and saved successfully"}

@app.get("/get-fromAI-wav")
async def get_fromAI_wav():
    filePath = "uploads/audio/fromAI.wav"
    return FileResponse(filePath, media_type="audio/wav", filename="fromAI.wav")

@app.get("/get-fromAI-json")
async def get_fromAI_json():
    filePath = "uploads/audio/fromAI.json"
    taskStatus["text_LLM_tts_wavToJson"] = False
    return FileResponse(filePath, media_type="application/json", filename="fromAI.json")

@app.get("/task-status")
async def get_task_status():
    print("I was called by frontend:", taskStatus)
    return {"status": taskStatus["text_LLM_tts_wavToJson"]}

# ----------------------- Video thingy -----------------------
def runFacialPrediction():
    facial_prediction.main()
    taskStatus["faceEmotion"] = True
    checkProcessFiles()

def run_eye_track():
    eye_tracking.main()
    taskStatus["eye"] = True
    checkProcessFiles()

@app.post("/video")
async def upload_video(background_tasks: BackgroundTasks, video: UploadFile = File(...)):
    print(video)
    with open(f"uploads/video/{video.filename}", "wb") as buffer:
        shutil.copyfileobj(video.file, buffer)
        buffer.close()
    background_tasks.add_task(runFacialPrediction)
    run_eye_track()

    return {"message": "Video converted and saved successfully"}


# ----------------------- Combine transcript, emotion, eye -----------------------
def combineTranscriptEmotionEye():
    taskStatus["transcript"] = False
    taskStatus["faceEmotion"] = False
    taskStatus["eye"] = False

    currentTime = datetime.datetime.now()
    transcriptFile = open("uploads/audio/transcript_detected.json", "r")
    emotionFile = open("uploads/video/emotion_detected.json", "r")
    eyeFile = open("uploads/video/blink_detected.json", "r")

    transcriptData = json.load(transcriptFile)
    emotionData = json.load(emotionFile)
    eyeData = json.load(eyeFile)

    transcriptFile.close()
    emotionFile.close()
    eyeFile.close()

    combinedJsonData = {
        "timestamp": currentTime.strftime("%H:%M:%S"),
        "transcript": transcriptData['text'],
        "emotion": emotionData,
        "eye": eyeData,
        "disfluencies": None,
        "behavioralAnalysis": None,
        "plagiarism": None,
    }

    combinedJsonData['disfluencies'] = disfluency.main(transcriptData['text'])
    combinedJsonData['plagiarism'] = plagiarism.main(transcriptData['text'])
    # combinedJsonData[behavioralAnalysis] = behavioralAnalysis.main(combinedJsonData)  # await cleanup, deadline 12/4
    #* to process, behavioral analysis at here

    print(mongoDB.appendDataToDocument("combinedData", combinedJsonData, uniqueSessionID))

    print ("Transcript and emotion combined successfully")

def checkProcessFiles():
    if taskStatus["transcript"] and taskStatus["faceEmotion"] and taskStatus["eye"]:
        combineTranscriptEmotionEye()

        return True
    else:
        print("Not all files are processed yet")
        return False

# ----------------------- Interview Session Finish -----------------------
@app.post("/ai-interview/session/end")
async def finish_interview(BackgroundTasks: BackgroundTasks):
    time.sleep(5)   # Wait for the last process to finish

    BackgroundTasks.add_task(generateReportFormat)

    return {"status": 200, "message": "Interview session finished successfully"}

def concat_user_transcript():
    conversationLog = mongoDB.getDataWithUniqueSessionID("conversationLog", uniqueSessionID)
    log_full:str = ""
    for log in conversationLog['log']:
        if log['user'] == "applicant":
            log_full += log['text'] + ". "
        
    return log_full

def concat_user_eva_transcript():
    conversationLog = mongoDB.getDataWithUniqueSessionID("conversationLog", uniqueSessionID)
    log_full:str = ""
    for log in conversationLog['log']:
        if log['user'] == "applicant":
            log_format = "Candidate: " + log['text'] + ". "
            log_full += log_format
        elif log['user'] == "Ai - EVA":
            log_format = "HR: " + log['text']
            log_full += log_format
    return log_full 

# def concat_user_answering(flag):

#Get UniqueResumeID and JobPositionApply from combinedData collecetion to be put into reportData collection
def getJobPositionApply():
    data = mongoDB.getDataWithUniqueSessionID("combinedData", uniqueSessionID)
    return data['jobPostitionApply'], data['uniqueResumeID'], data['email']

def generateReportFormat():
    toStoreJson = {
        # "name": None, #reportPurpose
        # "id": None,  #reportPurpose
        # "overallSuitability": None, #reportPurpose
        # "interviewDate": None, #reportPurpose
        # "radarChartBinaryArray" : None, #reportPurpose
        # "radarChartSummary": None, #reportPurpose
        "email": None,
        "interviewPosition": None,
        "uniqueResumeID": None,
        "concatAllResult": None,
        "uniqueSessionID": uniqueSessionID,
        "disfluencies": None,
        "plagiarism": None,
        "aiDetector": None,  # Dict 
        "mbti": None,
        "tone": None,  # Dict
        "companySpecificSuitability": None,   # Dict
        # "personalityAnalysis": None,   # Dict
        "hiringIndex": None
    }

    concatAllResult = concat_user_eva_transcript()
    concatApplicantResult = concat_user_transcript()
    toStoreJson["interviewPosition"] = getJobPositionApply()[0]
    toStoreJson["uniqueResumeID"] = getJobPositionApply()[1]
    toStoreJson["email"] = getJobPositionApply()[2]
    toStoreJson['concatAllResult'] = concatAllResult
    toStoreJson['concatResult'] = concatApplicantResult
    toStoreJson['disfluencies'] = disfluency.main(concatApplicantResult)
    toStoreJson['plagiarism'] = plagiarism.main(concatApplicantResult)
    toStoreJson['aiDetector'] = aiDetection.main(concatApplicantResult)
    toStoreJson['mbti'] = mbti_last.main(concatApplicantResult)
    # toStoreJson['hiringIndex'] = hiringIndex.main(toStoreJson)
    #* to process MBTI, tone, companySpecificSuitability  at here

    print(mongoDB.postData("reportData", toStoreJson))
    generateReport()

    return {"status": 200, "message": "Report generated successfully"}

def generateReport():
    reportData = mongoDB.getOneDataFromCollection("reportData", {"uniqueSessionID": uniqueSessionID})
    toReportJson = reportGeneration.main(reportData, uniqueSessionID)
    #Overwrite whole reportdata with same uniqueSessionID

# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#         await websocket.accept()
#         while True:
#             # await audio data
#             data = await websocket.receive_bytes()
            
#             print("Received audio data")
            
#             # Check if it is a proper webm file
#             if data[:4] == b'\x1a\x45\xdf\xa3':
#                 # save_audio(data)
#                 print("Audio data saved successfully")
#             else:
#                 print("Invalid audio format")
#                 save_audio(data)
            

# def save_audio(data):
    # # save the webm audio 
    # with open("uploads/audio/mic-audio_live_bad.webm", "wb") as audio:
    #     audio.write(data)
    #     audio.close()
    #  return speech_to_text.main_for_live()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, workers=4)
