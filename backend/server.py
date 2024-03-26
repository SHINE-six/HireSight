import shutil
from fastapi import FastAPI, File, UploadFile
import uvicorn
import resume_parser

app = FastAPI()

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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)