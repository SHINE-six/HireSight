import resumeRanker as rr
import os
#import mongoDB as mdb
from bson import Binary

data = [
{
    "id": 1,
    "jobCategory": "IT, Software & Digital",
    "jobCategoryDescription": "Delivering exciting, innovative, complex, and technical projects.",
    "subCategories": [
        {
            "subCategoryId": "1A",
            "subCategoryName": "IT Business Analyst",
            "subCategoryDescription": "Focused on leveraging business analytics tools and methodologies to improve decision-making and business practices within IT, Software & Digital projects.",
            "availableJobs": [
                {
                    "jobId": "1A_a",
                    "jobTitle": "IT Business Analyst – SAP FICO",
                    "jobDescription": "This is an IT Business Analyst role focused on the financial aspects of software sales, including subscriptions, rentals, leasing, and usage concepts for Hilti tools. You will bridge the gap between business needs and SAP FICO implementations, working on global projects, daily support, and compliance initiatives.",
                    "jobSkills": ["SAP FICO consultant background (3+ years experience)", "Experience with SAP ERP 6.0 / S/4HANA in finance (General Ledger, AR, AA)", 
                                    "Understanding of business processes in finance, controlling, sales & distribution", "Ability to handle complex projects and implement IFRS standards","Strong communication, problem-solving, and teamwork skills","Experience in international/virtual teams"]
                },
                {
                    "jobId": "1A_b",
                    "jobTitle": "IT Business Analyst – SAP Treasury",
                    "jobDescription": "This is an IT Business Analyst role focused on the Treasury area. You'll collaborate with business teams on various topics (innovation, compliance) using SAP S/4HANA and Business ByDesign. You'll design, develop, test, and implement solutions for finance processes, working with both internal ERP systems and 3rd party Treasury/Banking systems. Additionally, you'll support daily operations through a ticketing platform.",
                    "jobSkills": ["Bachelor's/Master's in IT, CS, or similar + 4+ years' experience in Treasury modules of SAP ECC 6.0/S/4HANA", "Understanding of SAP modules (GL, AR, AP, Currency Exchange, Banking & Treasury)", 
                                    "Strong conceptual, analytical skills, and business process understanding in finance integration", "Excellent communication and adaptation skills in a multicultural environment",
                                    "Experience implementing SAP or 3rd party solutions","Familiarity with Atlassian (JIRA/Confluence), ServiceNow, and collaboration tools"]
                },
                {
                    "jobId": "1A_c",
                    "jobTitle": "IT Business Analyst - SAP Controlling",
                    "jobDescription": "As an IT Business Analyst specializing in Finance & Controlling, you are entrusted with leading the planning, development, and operational management of our SAP S/4HANA solutions. In this vital role, you will partner with business units to develop strategic roadmaps, enhance our SAP system landscape in alignment with our overarching IT strategy, and support our commitment to operational excellence. Your responsibilities include the full ownership of outcomes, decisions, and activities within the defined scope of your solutions, ensuring they are aligned with the Hilti Business Model and IT guidelines. By managing stakeholder relations and employing an agile approach to project delivery, you will drive rapid results while maintaining high standards in solution quality and business impact. This role demands a blend of technical expertise, strategic thinking, and a deep understanding of financial and controlling processes to effectively support and advance business goals.",
                    "jobSkills": ["Bachelor’s, Master’s, or PhD in Information Technology, Computer Science, or related field",
                                    "At least 5 years of experience in SAP ERP 6.0 or S/4HANA, particularly in Controlling (COPA, CO-PC, Material Ledger) and Finance (General Ledger, Fixed Assets)",
                                    "Proficient in defining IT roadmaps and working towards strategic goals in collaboration with business teams",
                                    "Experience in creating user stories for functional and non-functional requirements, conducting demos, and providing training",
                                    "Strong analytical skills for effective problem-solving and decision-making",
                                    "Excellent planning, realization, and controlling abilities",
                                    "Effective communication skills and the ability to work in an international, geographically dispersed team",
                                    "Agile methodology proficiency for quick and efficient project delivery",
                                    "Commitment to continuous learning and development, both for self and team"]
                },
                {
                    "jobId": "1A_d",
                    "jobTitle": "IT Business Analyst Salesforce",
                    "jobDescription": "As a Business Analyst in Hilti's Systematic Account Development program, you'll focus on enhancing Customer Relationship Management through Salesforce Sales Cloud. This role involves understanding business requirements, designing solution proposals, and supporting their implementation within Salesforce to optimize sales processes. You'll work within an international scrum team, using agile methodologies to deliver significant customer impact. While Salesforce Sales Cloud is your primary technology focus, you'll also engage with SAP S4 HANA, Salesforce Service Cloud, and AWS Microservices among others. This position plays a crucial role in providing transparency on sales opportunities and enabling effective use of Hilti products on job sites.",
                    "jobSkills": ["Bachelor’s degree in computer science, software engineering, information technology, or related fields","Over 5 years of experience with cloud software (preferably Salesforce), business process management, and agile methodologies","Excellent communication and interpersonal skills, fluent in English for effective stakeholder management in a global matrix environment",
                                  "Passion for marketing, sales, and service business process design with a keen interest in CRM software","Strong willingness and capacity to learn."]
                }
            ]
        },
        {
            "subCategoryId": "1B",
            "subCategoryName": "Internship",
            "subCategoryDescription": "Focused on leveraging business analytics tools and methodologies to improve decision-making and business practices within IT, Software & Digital projects.",
            "availableJobs": [
                {
                    "jobId": "1B_a",
                    "jobTitle": "Internship - DevOps Engineer",
                    "jobDescription": "Join our IT team as a DevOps Engineer Intern and engage in exciting projects, gaining practical expertise and solving real-world challenges in a global setting. You will partner with stakeholders to translate requirements into technical designs, improve CI/CD toolchains, drive lifecycle activities, and enhance IT systems with new technologies. You'll also provide advanced support to both business and IT teams. This internship offers flexible start dates and lasts 4-6 months, providing a comprehensive experience in cloud product management and operations.",
                    "jobSkills": ["Enrolled in Bachelor's/Master's in IT, Software Engineering, Data Science, or related fields","Strategic thinker with excellent problem-solving skills","Proactive and hands-on mentality","Strong communication and interpersonal abilities","Fluent in written and spoken English","Eager to learn and embrace challenges."]
                },
                {
                    "jobId": "1B_b",
                    "jobTitle": "Internship - IT Quality Assurance Analyst",
                    "jobDescription": "Join our IT team as an IT Quality Assurance Analyst Intern on a variety of exciting projects. This internship offers a flexible start and lasts 4-6 months, where you'll enhance your skills in global IT project management and solution delivery. You will be involved in refining QA processes, designing and reviewing test cases, and working within the software development lifecycle to ensure functionality, performance, security, and user experience standards are met. Additionally, you will monitor software development stages to manage malfunctions and continuously improve quality standards.",
                    "jobSkills": ["Enrolled in Bachelor's/Master's in IT, Software Engineering, Data Science, or related fields","Strategic thinker with excellent problem-solving skills","Proactive and hands-on mentality","Strong communication and interpersonal abilities","Fluent in written and spoken English","Eager to learn and embrace challenges."]
                },
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
    "id": 2,
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
    "id": 3,
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
    "id": 4,
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

# jobDesctiptionArray = []
# jobTitleArray = []

# for category in data:
#     if "availableJobs" in category:
#         for job in category["availableJobs"]:
#             jobTitleArray.append(job["jobTitle"])
#             concatenated_text = job["jobDescription"] + "\n" + "\n".join(job["jobSkills"])
#             jobDesctiptionArray.append(concatenated_text)
    
#     if "subCategories" in category:
#         for sub_category in category["subCategories"]:
#             if "availableJobs" in sub_category:
#                 for job in sub_category["availableJobs"]:
#                     jobTitleArray.append(job["jobTitle"])
#                     concatenated_text = job["jobDescription"] + "\n" + "\n".join(job["jobSkills"])
#                     jobDesctiptionArray.append(concatenated_text)

# print('\n'.join(jobTitleArray))
# print('\n'.join(jobDesctiptionArray))

# #Await for testing
# resumePath = "C:\\Users\\YC PUAH\\OneDrive - Asia Pacific University\\Puah Yi Kai\\Resume Ranking\\resume-ranker\\Resume_Sample\\Abiral_Pandey_Fullstack_Java.pdf"
# result = rr.allJobDescriptionsToOneResume(resumePath, jobTitleArray, jobDesctiptionArray)

# print(result)

#________________________________________________________________________________________________________________________________________________________________
# folder_path = "C:\\Users\\YC PUAH\\OneDrive - Asia Pacific University\\Puah Yi Kai\\Resume_Sample_Five_Test"

# for filename in os.listdir(folder_path):
#     if filename.endswith(".pdf"):  # Assuming all files are PDFs
#         # Construct the full path to the PDF file
#         file_path = os.path.join(folder_path, filename)
        
#         # Read the PDF file as binary data
#         with open(file_path, "rb") as file:
#             pdf_data = file.read()
        
#         # Construct data object to post to the collection
#         resume_data = {
#             "filename": filename,
#             "pdf_data": pdf_data
#         }
        
#         # Post the resume data to the collection
#         response = mdb.postData("resumeDatabase", resume_data)
#________________________________________________________________________________________________________________________________________________________________

# # #Mongo DB Test all pdf
# for category in data:
#     for job in category["availableJobs"]:
#         concatenated_text = job["jobDescription"] + "\n" + "\n".join(job["jobSkills"])
#         break
#     break

# rr.oneJobDescriptionToAllResume(concatenated_text)

jd = "This is an IT Business Analyst role focused on the financial aspects of software sales, including subscriptions, rentals, leasing, and usage concepts for Hilti tools. You will bridge the gap between business needs and SAP FICO implementations, working on global projects, daily support, and compliance initiatives.\nSAP FICO consultant background (3+ years experience)\nExperience with SAP ERP 6.0 / S/4HANA in finance (General Ledger, AR, AA)\nUnderstanding of business processes in finance, controlling, sales & distribution\nAbility to handle complex projects and implement IFRS standards\nStrong communication, problem-solving, and teamwork skills\nExperience in international/virtual teams"
resumePath = "C:\\Users\\YC PUAH\\OneDrive - Asia Pacific University\\Puah Yi Kai\\Resume Ranking\\resume-ranker\\Resume_Sample\\Abiral_Pandey_Fullstack_Java.pdf"

result = rr.extractTextFromPDF(resumePath)
print(result)