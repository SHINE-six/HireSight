import shutil
from fastapi import FastAPI, File, Request, UploadFile, BackgroundTasks, WebSocket
from fastapi.responses import FileResponse
import uvicorn
import resume_parser
import speech_to_text
import facial_prediction
import eye_tracking
import LLM
import tts
import wavspeech_to_json
import mongoDB
import disfluency
import plagiarism
# import mbti
# import ai_detection
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict
import datetime
import json


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

taskStatus: Dict[str, bool] = {"transcript": False, "face_emotion": False, "eye": False, "text_LLM_tts_wavToJson": False}
# {
#     "id": 1,
#     "jobCategory": "Project Managements",
#     "jobCategoryDescription": "Delivering exciting, innovative, complex, and technical projects.",
#     "availableJobs": [
#         {
#             "jobId": "1a",
#             "jobTitle": "Scrum Master",
#             "jobDescription": "Scrum Master is responsible for ensuring that the team follows the rules of Scrum, and helps the team to continuously improve their process.",
#             "jobSkills": ["Scrum", "Agile", "Kanban", "Jira"]
#         },
#         {
#             "jobId": "1b",
#             "jobTitle": "Project Manager",
#             "jobDescription": "Project Manager is responsible for planning, executing, and closing projects.",
#             "jobSkills": ["Project Management", "Agile", "Jira", "Risk Management"]
#         },
#         {
#             "jobId": "1c",
#             "jobTitle": "Business Analyst",
#             "jobDescription": "Business Analyst is responsible for analyzing the business needs of clients to help identify business problems and propose solutions.",
#             "jobSkills": ["Business Analysis", "Requirement Gathering", "Jira", "SQL"]
#         }
#     ]
# },
# sample data
data = [
{
    "id": 1,
    "jobCategory": "IT, Software & Digital",
    "jobCategoryDescription": "This division is responsible for spearheading innovative and complex technical projects, with a focus on information technology and digital transformation within the organization.",
    "availableJobs": [
        {
            "jobId": "WD-0012443",
            "jobTitle": "IT BA – SAP FICO",
            "jobDescription": "This is an IT Business Analyst role focused on the financial aspects of software sales, including subscriptions, rentals, leasing, and usage concepts for Hilti tools. You will bridge the gap between business needs and SAP FICO implementations, working on global projects, daily support, and compliance initiatives.",
            "jobSkills": ["SAP FICO consultant background (3+ years experience)", "Experience with SAP ERP 6.0 / S/4HANA in finance (General Ledger, AR, AA)", 
                          "Understanding of business processes in finance, controlling, sales & distribution", "Ability to handle complex projects and implement IFRS standards","Strong communication, problem-solving, and teamwork skills","Experience in international/virtual teams"]
        },
        {
            "jobId": "WD-0024970",
            "jobTitle": "IT BA – SAP Treasury",
            "jobDescription": "This is an IT Business Analyst role focused on the Treasury area. You'll collaborate with business teams on various topics (innovation, compliance) using SAP S/4HANA and Business ByDesign. You'll design, develop, test, and implement solutions for finance processes, working with both internal ERP systems and 3rd party Treasury/Banking systems. Additionally, you'll support daily operations through a ticketing platform.",
            "jobSkills": ["Bachelor's/Master's in IT, CS, or similar + 4+ years' experience in Treasury modules of SAP ECC 6.0/S/4HANA", "Understanding of SAP modules (GL, AR, AP, Currency Exchange, Banking & Treasury)", 
                          "Strong conceptual, analytical skills, and business process understanding in finance integration", "Excellent communication and adaptation skills in a multicultural environment",
                          "Experience implementing SAP or 3rd party solutions","Familiarity with Atlassian (JIRA/Confluence), ServiceNow, and collaboration tools"]
        },
        {
            "jobId": "WD-0025438",
            "jobTitle": "IT BA - SAP Controlling",
            "jobDescription": "As an IT Business Analyst in Finance & Controlling, you will lead the planning, development, and management of our SAP S/4HANA solutions. Partnering with business units, you'll develop strategic roadmaps, enhance the SAP system landscape, and uphold our commitment to operational excellence. You'll own the outcomes, decisions, and activities within your scope, aligning them with the Hilti Business Model and IT guidelines. By managing stakeholder relations and using an agile delivery approach, you'll achieve rapid results and maintain high solution quality. This role requires technical expertise, strategic thinking, and a thorough understanding of financial and controlling processes to support and drive business objectives.",
            "jobSkills": ["Degree in IT, Computer Science, or similar, with at least 5 years of experience in SAP ERP 6.0 or S/4HANA, focusing on Controlling and Finance","Adept at creating strategic IT roadmaps and collaborating with various business units","Capable of crafting user stories, delivering demonstrations, and leading training sessions","Strong analytical abilities and proficiency in solving complex problems",
                          "Experienced in planning and executing projects with strong control over project management processesExcellent communicator with a background in international team environments and a mastery of Agile methodologies for project delivery."]
        }
    ]
},
{
    "id": 2,
    "jobCategory": "Engineering",
    "jobCategoryDescription": "A core unit that drives the development of new products and services, ensuring the company stays at the forefront of engineering innovation and advancement.",
    "availableJobs": [
        {
            "jobId": "4796",
            "jobTitle": "Application Engineer",
            "jobDescription": "This is an Application Engineer role providing structural analysis and design for Hilti's modular support systems. You'll support sales and business development teams during project acquisition and client interaction. You'll also lead engineering solution development and ensure adherence to project standards.",
            "jobSkills": ["Master's degree in Structural/Civil Engineering (PE preferred)","Extensive experience in steel structure design/civil engineering (Energy & Industry, large data centers, or complex modular buildings)",
                          "Experience with structural analysis software (e.g., RStab by Dlubal)","Familiarity with BIM Modeling software","Project management and tendering/estimating experience"]
        },
        {
            "jobId": "WD-0013288",
            "jobTitle": "BIM Modeler",
            "jobDescription": " As a BIM Modeler I, you'll be the go-to person for Hilti's South Asia Pacific sales and projects in Energy, Industry, and Construction.  Using BIM software (Revit, AutoCAD), you'll create models, drawings, and documentation to support various teams.  Your expertise in structural modeling, MEP/FP, and construction standards will ensure high-quality deliverables for clients.  This role involves collaboration across departments and potential travel for meetings and training.",
            "jobSkills": ["Proficient in REVIT, AUTOCAD, and INVENTOR","Expertise in modular support systems, direct fastening, and firestop solutions","Skilled in producing technical documentation: models, drawings, and bills of materials",
                          "Effective communicator for project requirements and RFIs/RFPs/RFQs","Maintains detailed project and client records","Willing to travel for project-related activities."]
        }
    ]
},
{
    "id": 3,
    "jobCategory": "Sales",
    "jobCategoryDescription": "A dynamic sector tasked with driving growth and revenue through strategic sales initiatives, combining deep technical knowledge with market acumen.",
    "availableJobs": [
        {
            "jobId": "41262",
            "jobTitle": "Outperformer - Global Management Development Program - Business Track",
            "jobDescription": "The Hilti Outperformer is a two-year global management development program aimed at grooming post-graduate talent through real-world responsibilities. Participants rotate through key roles, starting with 12 months as an account manager or field engineer, followed by projects in logistics, HR, finance, marketing, or engineering at the national and regional headquarters, including a final strategic project in a contrasting market. The program, supported by senior management mentoring, offers rapid exposure and career advancement in various business areas.",
            "jobSkills": ["Studying for or recently graduated with a Master's or PhD, especially in business, engineering, or related fields","At least three months to two years of professional experience in internships, apprenticeships, or similar.","Fluent in English and at least one additional language; more languages preferred",
                          "Experience with international work or study","Assertive, curious, and committed with excellent communication and teamwork skills","Open to intercultural experiences and willing to work abroad; Malaysian citizenship or permanent residency required."]
        },
        {
            "jobId": "35316",
            "jobTitle": "Account Manager (Sales role)",
            "jobDescription": "We are seeking a high-potential Account Manager with strong business acumen to join Hilti's high performing and supportive culture. This role involves achieving sales targets in an assigned territory by identifying business opportunities, promoting Hilti’s product line, and providing solutions through product demonstrations and user training. The candidate will expand sales by acquiring new clients and maintaining relationships with existing ones, ensure disciplined sales execution, handle customer inquiries and complaints, and engage in sales forecasting. Additionally, the role requires introducing new products to the market, collaborating with various departments, and handling ad-hoc tasks as needed.",
            "jobSkills": ["Minimum of a Diploma in any discipline","Open to fresh graduates with an interest in Sales and the Construction industry","Independent and effective in a team setting","Persuasive, persistent, sales-driven, and customer-focused",
                          "Strong communication and interpersonal skills","Previous sales experience with a successful track record is beneficial."]
        }
    ]
},
{
    "id": 4,
    "jobCategory": "Human Resources",
    "jobCategoryDescription": "This team focuses on optimizing talent acquisition and management, particularly for roles that support the company's digital and technological initiatives.",
    "availableJobs": [
        {
            "jobId": "WD-0026253",
            "jobTitle": "Talent Engagement Specialist - Digital",
            "jobDescription": "As a Talent Engagement Specialist at Hilti's Kuala Lumpur-based Digital Strategic Sourcing Hub, you'll focus on building a pipeline of IT, digital, and software talent for future roles across Asia-Pacific. Your responsibilities include proactive headhunting, managing talent pools using Beamery, and collaborating with Talent Acquisition Partners to meet Hilti's Lead 2030 hiring goals. You'll also enhance candidate experiences, promote Hilti’s digital presence, and maintain a strong network within the sourcing community to ensure a diverse and high-quality candidate pool.",
            "jobSkills": ["Bachelor’s degree in a related field with a minimum CGPA of 3.0","Expert in advanced search techniques and data mining for IT and digital sectors","6-10 years of sourcing experience with a focus on excellence","Skilled in delivering exceptional candidate experiences, preferably in the Asia Pacific region",
                          "Proficient with Applicant Tracking Systems and Talent Relationship Management, like Haufe and Beamery","Resilient in managing changing priorities and multiple stakeholder needs."]
        }
    ]
}
]

@app.post("/")
async def readRoot():
    print("Welcome to the Job Portal!")
    return {"message": "Welcome to the Job Portal!"}

@app.get("/jobopenings")
async def readRoot():
    return data

@app.get("/jobopenings/{job_id}")
async def readJob(job_id: str):
    for category in data:
        for job in category["availableJobs"]:
            if job["jobId"] == job_id:
                return job
    return {"message": "Job not found"}

@app.post("/resume")
async def uploadResume(resume: UploadFile = File(...)):
    with open(f"resume/resume_in/{resume.filename}", "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)
        resumeData = resume_parser.main(resume.filename)
        
        
    

    return {"status": 200, "message": "Resume uploaded successfully"}

@app.get("/resume-ranking")
async def getResumeRanking():
    filePath = "resume/resume_ranking.json"
    return FileResponse(filePath, media_type="application/json", filename="resume_ranking.json")

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
    outputText = LLM.main(userTranscript)
    print(mongoDB.appendDataToDocument("conversationLog", {"user": "Ai - EVA", "text": outputText}, uniqueSessionID))
    tts.main(outputText)
    wavspeech_to_json.main()
    print("Text, TTS, and WAV to JSON conversion completed")
    taskStatus["text_LLM_tts_wavToJson"] = True

def run_speech_to_text(background_tasks):
    userTranscript = speech_to_text.main()
    userTranscript = userTranscript['text']
    print(mongoDB.appendDataToDocument("conversationLog", {"user": "applicant", "text": userTranscript}, uniqueSessionID))
    background_tasks.add_task(text_LLM_tts_wavToJson, userTranscript)
    taskStatus["transcript"] = True
    check_process_files()

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
def run_facial_prediction():
    facial_prediction.main()
    taskStatus["face_emotion"] = True
    check_process_files()

def run_eye_track():
    eye_tracking.main()
    taskStatus["eye"] = True
    check_process_files()

@app.post("/video")
async def upload_video(background_tasks: BackgroundTasks, video: UploadFile = File(...)):
    print(video)
    with open(f"uploads/video/{video.filename}", "wb") as buffer:
        shutil.copyfileobj(video.file, buffer)
        buffer.close()
    background_tasks.add_task(run_facial_prediction)
    run_eye_track()

    return {"message": "Video converted and saved successfully"}


# ----------------------- Combine transcript, emotion, eye -----------------------
def combine_transcript_emotion_eye():
    taskStatus["transcript"] = False
    taskStatus["face_emotion"] = False
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

    combinedJsonData = disfluency.main(combinedJsonData)
    # combinedJsonData = behavioralAnalysis.main(combinedJsonData)  # await cleanup, deadline 12/4
    # combinedJsonData = plagiarism.main(combinedJsonData)   # await cleanup, deadline 14/4
    #* to process plagiarism, disfluency, behavioral analysis at here

    print(mongoDB.append_data_to_document("combinedData", combinedJsonData, uniqueSessionID))

    print ("Transcript and emotion combined successfully")

def check_process_files():
    if taskStatus["transcript"] and taskStatus["face_emotion"] and taskStatus["eye"]:
        combine_transcript_emotion_eye()

        return True
    else:
        return False

# ----------------------- Interview Session Finish -----------------------
@app.post("/ai-interview/session/end")
async def finish_interview(BackgroundTasks: BackgroundTasks):
    while True:
        if check_process_files():
            break
        else:
            continue

    concat_result = concat_user_transcript()
    BackgroundTasks.add_task(generate_report, concat_result)

    return {"status": 200, "message": "Interview session finished successfully"}

def concat_user_transcript():
    conversationLog = mongoDB.get_data_with_uniqueSessionID("conversationLog", uniqueSessionID)
    log_full:str = ""
    for log in conversationLog['log']:
        if log['user'] == "applicant":
            log_full += log['text'] + ". "
        
    return log_full

def generate_report(concat_result: str):
    to_store_json = {
        "email": str,
        "concat_result": concat_result,
        "uniqueSessionID": uniqueSessionID,
        "disfluencies": None,
        "plagiarism": None,
        "aiDetection": None,  # Dict
        "mbti": None,
        "tone": None,  # Dict
        "companySpecificSuitability": None,   # Dict
        # "personalityAnalysis": None,   # Dict
        "HiringIndex": None
    }
    # @ An Ning, @ Chen Ming
    to_store_json['aiDetection'] = plagiarism.main(to_store_json)
    #* to process MBTI, disfluency, behavioral analysis at here

    return {"status": 200, "message": "Report generated successfully"}

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
