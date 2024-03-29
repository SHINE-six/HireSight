import shutil
from fastapi import FastAPI, File, UploadFile, BackgroundTasks
import uvicorn
import resume_parser
import speech_to_text
import facial_prediction
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict


app = FastAPI()


origins = [
    "https://ddncl8rd-3000.asse.devtunnels.ms/",  # Assuming your React app runs on localhost:3000
    "https://ddncl8rd-8000.asse.devtunnels.ms/",  # Add your production origin as needed
]

# Add CORSMiddleware to the application
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specified origins
    allow_credentials=True,  # Allows cookies to be included in cross-origin HTTP requests
    allow_methods=["*"],  # Allows all methods (e.g., GET, POST, PUT, DELETE)
    allow_headers=["*"],  # Allows all headers
)



# sample data
data = [
{
    "id": 1,
    "jobCategory": "Project Management",
    "jobCategoryDescription": "Delivering exciting, innovative, complex, and technical projects",
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
    "jobCategory": "Project Management",
    "jobCategoryDescription": "Delivering exciting, innovative, complex, and technical projects",
    "availableJobs": [
        {
            "jobId": "2a",
            "jobTitle": "Scrum Master",
            "jobDescription": "Scrum Master is responsible for ensuring that the team follows the rules of Scrum, and helps the team to continuously improve their process.",
            "jobSkills": ["Scrum", "Agile", "Kanban", "Jira"]
        },
        {
            "jobId": "2b",
            "jobTitle": "Project Manager",
            "jobDescription": "We're looking for a dedicated Product Manager to spearhead the lifecycle of our products. In this role, you'll be at the helm of product development from inception through to launch. Collaboration will be key as you work closely with teams across the board, from engineering and design to marketing and sales, ensuring our products not only meet market demands but also drive our business objectives forward. Your responsibilities will include conducting thorough market research, strategizing product development, prioritizing features, and orchestrating effective go-to-market plans. With your keen eye for detail and knack for problem-solving, you'll track and analyze performance metrics to continually refine and improve our offerings. As the go-to expert for our products, you'll provide invaluable support to both internal teams and external stakeholders, guiding them through the intricacies of our product line. If you're ready to make your mark in a fast-paced and collaborative environment, join us on this exciting journey of innovation and growth.",
            "jobSkills": ["Project Management", "Agile", "Jira", "Risk Management"]
        },
        {
            "jobId": "2c",
            "jobTitle": "Business Analyst",
            "jobDescription": "Business Analyst is responsible for analyzing the business needs of clients to help identify business problems and propose solutions.",
            "jobSkills": ["Business Analysis", "Requirement Gathering", "Jira", "SQL"]
        }
    ]
},
{
    "id": 3,
    "jobCategory": "Game Management",
    "jobCategoryDescription": "Delivering exciting, innovative, complex, and technical projects",
    "availableJobs": [
        {
            "jobId": "3a",
            "jobTitle": "Scrum Master",
            "jobDescription": "Scrum Master is responsible for ensuring that the team follows the rules of Scrum, and helps the team to continuously improve their process.",
            "jobSkills": ["Scrum", "Agile", "Kanban", "Jira"]
        },
        {
            "jobId": "3b",
            "jobTitle": "Project Manager",
            "jobDescription": "Project Manager is responsible for planning, executing, and closing projects.",
            "jobSkills": ["Project Management", "Agile", "Jira", "Risk Management"]
        },
        {
            "jobId": "3c",
            "jobTitle": "Business Analyst",
            "jobDescription": "Business Analyst is responsible for analyzing the business needs of clients to help identify business problems and propose solutions.",
            "jobSkills": ["Business Analysis", "Requirement Gathering", "Jira", "SQL"]
        }
    ]
},
{
    "id": 4,
    "jobCategory": "Project Management",
    "jobCategoryDescription": "Delivering exciting, innovative, complex, and technical projects",
    "availableJobs": [
        {
            "jobId": "4a",
            "jobTitle": "Scrum Master",
            "jobDescription": "Scrum Master is responsible for ensuring that the team follows the rules of Scrum, and helps the team to continuously improve their process.",
            "jobSkills": ["Scrum", "Agile", "Kanban", "Jira"]
        },
        {
            "jobId": "4b",
            "jobTitle": "Project Manager",
            "jobDescription": "Project Manager is responsible for planning, executing, and closing projects.",
            "jobSkills": ["Project Management", "Agile", "Jira", "Risk Management"]
        },
        {
            "jobId": "4c",
            "jobTitle": "Business Analyst",
            "jobDescription": "Business Analyst is responsible for analyzing the business needs of clients to help identify business problems and propose solutions.",
            "jobSkills": ["Business Analysis", "Requirement Gathering", "Jira", "SQL"]
        }
    ]
}
]

@app.post("/")
async def read_root():
    print("Welcome to the Job Portal!")
    return {"message": "Welcome to the Job Portal!"}

@app.get("/jobopenings")
async def read_root():
    return data

@app.get("/jobopenings/{job_id}")
async def read_job(job_id: str):
    for category in data:
        for job in category["availableJobs"]:
            if job["jobId"] == job_id:
                return job
    return {"message": "Job not found"}

@app.post("/resume")
async def upload_resume(resume: UploadFile = File(...)):
    with open(f"resume/resume_in/{resume.filename}", "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)
        resume_data = resume_parser.parse_resume(resume.filename)

    return resume_data

task_status: Dict[str, bool] = {"audio": False, "video": False}

def run_speech_to_text():
    speech_to_text.main()
    task_status["audio"] = True
    check_process_files()

@app.post("/audio")
async def upload_audio(background_tasks: BackgroundTasks, audio: UploadFile = File(...)):
    print(audio)
    with open(f"uploads/audio/{audio.filename}", "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)
        print(buffer)
        buffer.close()
    background_tasks.add_task(run_speech_to_text)

    return {"message": "Audio converted and saved successfully"}

def run_facial_prediction():
    facial_prediction.main()
    task_status["video"] = True
    check_process_files()

@app.post("/video")
async def upload_video(background_tasks: BackgroundTasks, video: UploadFile = File(...)):
    print(video)
    with open(f"uploads/video/{video.filename}", "wb") as buffer:
        shutil.copyfileobj(video.file, buffer)
        buffer.close()
    background_tasks.add_task(run_facial_prediction)

    return {"message": "Video converted and saved successfully"}

def combine_transcript_and_emotion():
    task_status["audio"] = False
    task_status["video"] = False
    return {"message": "Transcript and emotion combined successfully"}

def check_process_files():
    if task_status["audio"] and task_status["video"]:
        combine_transcript_and_emotion()

        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    else:
        print("nope, havent finish BBBBBBBBBBBBBBBB")

# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     image_chunk_counter = 0
#     list_to_write = []
#     while True:
#         data = await websocket.receive_bytes()
#         list_to_write.append(data)
#         print(len(list_to_write), len(data))
#         if len(list_to_write) >= 10:
#             save_images(image_chunk_counter, list_to_write)
#             image_chunk_counter += 1
#             list_to_write = []

# def save_images(image_chunk_counter: int, list_to_write: list):
#     print(f"Saving image chunk")
#     image_counter = 0
#     for item in list_to_write:
#         with open(f"uploads/image_{image_chunk_counter}_{image_counter}.jpg", "wb") as f:
#             f.write(item)
#             print(f"Image saved {image_counter}")
#             image_counter += 1


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, workers=4)