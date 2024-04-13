import resumeRanker as rr

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
            "jobDescription": "This is an IT Business Analyst role focused on the Treasury area. Youll collaborate with business teams on various topics (innovation, compliance) using SAP S/4HANA and Business ByDesign. Youll design, develop, test, and implement solutions for finance processes, working with both internal ERP systems and 3rd party Treasury/Banking systems. Additionally, youll support daily operations through a ticketing platform.",
            "jobSkills": ["Bachelors/Masters in IT, CS, or similar + 4+ years experience in Treasury modules of SAP ECC 6.0/S/4HANA", "Understanding of SAP modules (GL, AR, AP, Currency Exchange, Banking & Treasury)", 
                          "Strong conceptual, analytical skills, and business process understanding in finance integration", "Excellent communication and adaptation skills in a multicultural environment",
                          "Experience implementing SAP or 3rd party solutions","Familiarity with Atlassian (JIRA/Confluence), ServiceNow, and collaboration tools"]
        },
        {
            "jobId": "WD-0025438",
            "jobTitle": "IT BA - SAP Controlling",
            "jobDescription": "As an IT Business Analyst in Finance & Controlling, you will lead the planning, development, and management of our SAP S/4HANA solutions. Partnering with business units, youll develop strategic roadmaps, enhance the SAP system landscape, and uphold our commitment to operational excellence. Youll own the outcomes, decisions, and activities within your scope, aligning them with the Hilti Business Model and IT guidelines. By managing stakeholder relations and using an agile delivery approach, youll achieve rapid results and maintain high solution quality. This role requires technical expertise, strategic thinking, and a thorough understanding of financial and controlling processes to support and drive business objectives.",
            "jobSkills": ["Degree in IT, Computer Science, or similar, with at least 5 years of experience in SAP ERP 6.0 or S/4HANA, focusing on Controlling and Finance","Adept at creating strategic IT roadmaps and collaborating with various business units","Capable of crafting user stories, delivering demonstrations, and leading training sessions","Strong analytical abilities and proficiency in solving complex problems",
                          "Experienced in planning and executing projects with strong control over project management processes","Excellent communicator with a background in international team environments and a mastery of Agile methodologies for project delivery."]
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
            "jobDescription": "This is an Application Engineer role providing structural analysis and design for Hiltis modular support systems. Youll support sales and business development teams during project acquisition and client interaction. Youll also lead engineering solution development and ensure adherence to project standards.",
            "jobSkills": ["Masters degree in Structural/Civil Engineering (PE preferred)","Extensive experience in steel structure design/civil engineering (Energy & Industry, large data centers, or complex modular buildings)",
                          "Experience with structural analysis software (e.g., RStab by Dlubal)","Familiarity with BIM Modeling software","Project management and tendering/estimating experience"]
        },
        {
            "jobId": "WD-0013288",
            "jobTitle": "BIM Modeler",
            "jobDescription": " As a BIM Modeler I, youll be the go-to person for Hiltis South Asia Pacific sales and projects in Energy, Industry, and Construction.  Using BIM software (Revit, AutoCAD), youll create models, drawings, and documentation to support various teams.  Your expertise in structural modeling, MEP/FP, and construction standards will ensure high-quality deliverables for clients.  This role involves collaboration across departments and potential travel for meetings and training.",
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
            "jobSkills": ["Studying for or recently graduated with a Masters or PhD, especially in business, engineering, or related fields","At least three months to two years of professional experience in internships, apprenticeships, or similar.","Fluent in English and at least one additional language; more languages preferred",
                          "Experience with international work or study","Assertive, curious, and committed with excellent communication and teamwork skills","Open to intercultural experiences and willing to work abroad; Malaysian citizenship or permanent residency required."]
        },
        {
            "jobId": "35316",
            "jobTitle": "Account Manager (Sales role)",
            "jobDescription": "We are seeking a high-potential Account Manager with strong business acumen to join Hiltis high performing and supportive culture. This role involves achieving sales targets in an assigned territory by identifying business opportunities, promoting Hilti’s product line, and providing solutions through product demonstrations and user training. The candidate will expand sales by acquiring new clients and maintaining relationships with existing ones, ensure disciplined sales execution, handle customer inquiries and complaints, and engage in sales forecasting. Additionally, the role requires introducing new products to the market, collaborating with various departments, and handling ad-hoc tasks as needed.",
            "jobSkills": ["Minimum of a Diploma in any discipline","Open to fresh graduates with an interest in Sales and the Construction industry","Independent and effective in a team setting","Persuasive, persistent, sales-driven, and customer-focused",
                          "Strong communication and interpersonal skills","Previous sales experience with a successful track record is beneficial."]
        }
    ]
},
{
    "id": 4,
    "jobCategory": "Human Resources",
    "jobCategoryDescription": "This team focuses on optimizing talent acquisition and management, particularly for roles that support the companys digital and technological initiatives.",
    "availableJobs": [
        {
            "jobId": "WD-0026253",
            "jobTitle": "Talent Engagement Specialist - Digital",
            "jobDescription": "As a Talent Engagement Specialist at Hiltis Kuala Lumpur-based Digital Strategic Sourcing Hub, youll focus on building a pipeline of IT, digital, and software talent for future roles across Asia-Pacific. Your responsibilities include proactive headhunting, managing talent pools using Beamery, and collaborating with Talent Acquisition Partners to meet Hiltis Lead 2030 hiring goals. Youll also enhance candidate experiences, promote Hilti’s digital presence, and maintain a strong network within the sourcing community to ensure a diverse and high-quality candidate pool.",
            "jobSkills": ["Bachelors degree in a related field with a minimum CGPA of 3.0","Expert in advanced search techniques and data mining for IT and digital sectors","6-10 years of sourcing experience with a focus on excellence","Skilled in delivering exceptional candidate experiences, preferably in the Asia Pacific region",
                          "Proficient with Applicant Tracking Systems and Talent Relationship Management, like Haufe and Beamery","Resilient in managing changing priorities and multiple stakeholder needs."]
        }
    ]
}
]

jobDesctiptionArray = []
jobTitleArray = []

for category in data:
    for job in category["availableJobs"]:
        jobTitleArray.append(job["jobTitle"])
        concatenated_text = job["jobDescription"] + "\n" + "\n".join(job["jobSkills"])
        jobDesctiptionArray.append(concatenated_text)

#Await for testing
resumePath = "C:\\Users\\YC PUAH\\OneDrive - Asia Pacific University\\Puah Yi Kai\\Resume Ranking\\resume-ranker\\Resume_Sample\\Abiral_Pandey_Fullstack_Java.pdf"
result = rr.allJobDescriptionsToOneResume(resumePath, jobTitleArray, jobDesctiptionArray)

print(result)


