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
            "jobDescription": "Full Stack Developer is responsible for developing and maintaining both the front-end and back-end of web applications.",
            "jobSkills": ["Scrum", "Agile", "Kanban", "Jira"]
        },
        {
            "jobId": "2b",
            "jobTitle": "Test Engineer",
            "jobDescription": "Test Engineer is responsible for designing and implementing tests, debugging and defining corrective actions.",
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
            "jobDescription": "UI/UX Designer is responsible for designing user interfaces and user experiences for web and mobile applications.",
            "jobSkills": ["Scrum", "Agile", "Kanban", "Jira"]
        },
        {
            "jobId": "3b",
            "jobTitle": "Marketing Designer",
            "jobDescription": "Marketing Designer is responsible for creating visual content for marketing campaigns.",
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
            "jobDescription": "Business Analyst is responsible for analyzing the business needs of clients to help identify business problems and propose solutions.",
            "jobSkills": ["Scrum", "Agile", "Kanban", "Jira"]
        }
    ]
}
]


jobDesctiptionArray = []
jobTitleArray = []

for category in data:
    for job in category["availableJobs"]:
        jobTitleArray.append(job["jobTitle"])
        jobDesctiptionArray.append(job["jobDescription"])

#Await for testing


