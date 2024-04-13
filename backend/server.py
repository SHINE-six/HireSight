import shutil
import time
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
import aiDetection
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

taskStatus: Dict[str, bool] = {"transcript": False, "faceEmotion": False, "eye": False, "text_LLM_tts_wavToJson": False}

# sample data
data = [
{
    "id": 1,
    "jobCategory": "Project Management",
    "jobCategoryDescription": "Delivering exciting, innovative, complex, and technical projects.",
    "availableJobs": [
        {
            "jobId": "1a",
            "jobTitle": "Scrum Master",
            "jobDescription": "Scrum Master is responsible for ensuring that the team follows the rules of Scrum, and helps the team to continuously improve their process.",
            "jobSkills": ["Scrum", "Agile", "Kanban", "Jira"]
        },
        {
            "jobId": "1b",
            "jobTitle": "Project Manager",
            "jobDescription": "Project Manager is responsible for planning, executing, and closing projects.",
            "jobSkills": ["Project Management", "Agile", "Jira", "Risk Management"]
        },
        {
            "jobId": "1c",
            "jobTitle": "Business Analyst",
            "jobDescription": "Business Analyst is responsible for analyzing the business needs of clients to help identify business problems and propose solutions.",
            "jobSkills": ["Business Analysis", "Requirement Gathering", "Jira", "SQL"]
        }
    ]
},
{
    "id": 2,
    "jobCategory": "Research & Development",
    "jobCategoryDescription": "Research & Development is responsible for developing new products and services.",
    "availableJobs": [
        {
            "jobId": "2a",
            "jobTitle": "Full Stack Developer",
            "jobDescription": "Scrum Master is responsible for ensuring that the team follows the rules of Scrum, and helps the team to continuously improve their process.",
            "jobSkills": ["Scrum", "Agile", "Kanban", "Jira"]
        },
        {
            "jobId": "2b",
            "jobTitle": "Test Engineer",
            "jobDescription": "We're looking for a dedicated Product Manager to spearhead the lifecycle of our products. In this role, you'll be at the helm of product development from inception through to launch. Collaboration will be key as you work closely with teams across the board, from engineering and design to marketing and sales, ensuring our products not only meet market demands but also drive our business objectives forward. Your responsibilities will include conducting thorough market research, strategizing product development, prioritizing features, and orchestrating effective go-to-market plans. With your keen eye for detail and knack for problem-solving, you'll track and analyze performance metrics to continually refine and improve our offerings. As the go-to expert for our products, you'll provide invaluable support to both internal teams and external stakeholders, guiding them through the intricacies of our product line. If you're ready to make your mark in a fast-paced and collaborative environment, join us on this exciting journey of innovation and growth.",
            "jobSkills": ["Project Management", "Agile", "Jira", "Risk Management"]
        }
    ]
},
{
    "id": 3,
    "jobCategory": "Visual Design",
    "jobCategoryDescription": "Delivering exciting, innovative, complex, and technical projects",
    "availableJobs": [
        {
            "jobId": "3a",
            "jobTitle": "UI/UX Designer",
            "jobDescription": "Scrum Master is responsible for ensuring that the team follows the rules of Scrum, and helps the team to continuously improve their process.",
            "jobSkills": ["Scrum", "Agile", "Kanban", "Jira"]
        },
        {
            "jobId": "3b",
            "jobTitle": "Marketing Designer",
            "jobDescription": "Scrum Master is responsible for ensuring that the team follows the rules of Scrum, and helps the team to continuously improve their process.",
            "jobSkills": ["Scrum", "Agile", "Kanban", "Jira"]
        }
    ]
},
{
    "id": 4,
    "jobCategory": "Human Resources",
    "jobCategoryDescription": "Delivering exciting, innovative, complex, and technical projects",
    "availableJobs": [
        {
            "jobId": "4a",
            "jobTitle": "Business Analyst",
            "jobDescription": "Scrum Master is responsible for ensuring that the team follows the rules of Scrum, and helps the team to continuously improve their process.",
            "jobSkills": ["Scrum", "Agile", "Kanban", "Jira"]
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
    # combinedJsonData = behavioralAnalysis.main(combinedJsonData)  # await cleanup, deadline 12/4
    # combinedJsonData = plagiarism.main(combinedJsonData)   # await cleanup, deadline 14/4
    #* to process plagiarism, disfluency, behavioral analysis at here

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

    concatResult = concat_user_transcript()
    BackgroundTasks.add_task(generateReport, concatResult)

    return {"status": 200, "message": "Interview session finished successfully"}

def concat_user_transcript():
    conversationLog = mongoDB.getDataWithUniqueSessionID("conversationLog", uniqueSessionID)
    log_full:str = ""
    for log in conversationLog['log']:
        if log['user'] == "applicant":
            log_full += log['text'] + ". "
        
    return log_full

def generateReport(concatResult: str):
    toStoreJson = {
        "email": None,
        "concatResult": concatResult,
        "uniqueSessionID": uniqueSessionID,
        "disfluencies": None,
        "plagiarism": None,
        "aiDetector": None,  # Dict
        "mbti": None,
        "tone": None,  # Dict
        "companySpecificSuitability": None,   # Dict
        # "personalityAnalysis": None,   # Dict
        "HiringIndex": None
    }
    # @ An Ning, @ Chen Ming
    toStoreJson['disfluencies'] = disfluency.main(concatResult)
    toStoreJson['plagiarism'] = plagiarism.main(concatResult)
    toStoreJson['aiDetector'] = aiDetection.main(concatResult)
    #* to process MBTI, disfluency, behavioral analysis at here

    print(mongoDB.postData("reportData", toStoreJson))

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
