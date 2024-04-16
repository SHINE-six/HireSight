'use client';

import Link from "next/link";
import { JobCatType } from "../indiJobCategory";
import { useEffect, useRef, useState } from "react";


async function getSubcategoryDetail(CategoryId: any) {
    const res = await fetch(`http://localhost:8000/jobopenings/${CategoryId}`);
    const data = await res.json();

    return data;
    // const data = 
    //     {
    //         "categoryId": 1,
    //         "jobCategory": "IT, Software & Digital",
    //         "jobCategoryDescription": "This division is responsible for spearheading innovative and complex technical projects, with a focus on information technology and digital transformation within the organization.",
    //         "subCategories": [
    //             {
    //                 "subCategoryId": "1A",
    //                 "subCategoryName": "IT Business Analyst",
    //                 "subCategoryDescription": "Focused on leveraging business analytics tools and methodologies to improve decision-making and business practices within IT, Software & Digital projects.",
    //                 "availableJobs": [
    //                     {
    //                         "jobId": "1A_a",
    //                         "jobTitle": "IT Business Analyst – SAP FICO",
    //                         "jobDescription": "This is an IT Business Analyst role focused on the financial aspects of software sales, including subscriptions, rentals, leasing, and usage concepts for Hilti tools. You will bridge the gap between business needs and SAP FICO implementations, working on global projects, daily support, and compliance initiatives.",
    //                         "jobSkills": ["SAP FICO consultant background (3+ years experience)", "Experience with SAP ERP 6.0 / S/4HANA in finance (General Ledger, AR, AA)", 
    //                                         "Understanding of business processes in finance, controlling, sales & distribution", "Ability to handle complex projects and implement IFRS standards","Strong communication, problem-solving, and teamwork skills","Experience in international/virtual teams"]
    //                     },
    //                     {
    //                         "jobId": "1A_b",
    //                         "jobTitle": "IT Business Analyst – SAP Treasury",
    //                         "jobDescription": "This is an IT Business Analyst role focused on the Treasury area. You'll collaborate with business teams on various topics (innovation, compliance) using SAP S/4HANA and Business ByDesign. You'll design, develop, test, and implement solutions for finance processes, working with both internal ERP systems and 3rd party Treasury/Banking systems. Additionally, you'll support daily operations through a ticketing platform.",
    //                         "jobSkills": ["Bachelor's/Master's in IT, CS, or similar + 4+ years' experience in Treasury modules of SAP ECC 6.0/S/4HANA", "Understanding of SAP modules (GL, AR, AP, Currency Exchange, Banking & Treasury)", 
    //                                         "Strong conceptual, analytical skills, and business process understanding in finance integration", "Excellent communication and adaptation skills in a multicultural environment",
    //                                         "Experience implementing SAP or 3rd party solutions","Familiarity with Atlassian (JIRA/Confluence), ServiceNow, and collaboration tools"]
    //                     },
    //                     {
    //                         "jobId": "1A_c",
    //                         "jobTitle": "IT Business Analyst - SAP Controlling",
    //                         "jobDescription": "As an IT Business Analyst specializing in Finance & Controlling, you are entrusted with leading the planning, development, and operational management of our SAP S/4HANA solutions. In this vital role, you will partner with business units to develop strategic roadmaps, enhance our SAP system landscape in alignment with our overarching IT strategy, and support our commitment to operational excellence. Your responsibilities include the full ownership of outcomes, decisions, and activities within the defined scope of your solutions, ensuring they are aligned with the Hilti Business Model and IT guidelines. By managing stakeholder relations and employing an agile approach to project delivery, you will drive rapid results while maintaining high standards in solution quality and business impact. This role demands a blend of technical expertise, strategic thinking, and a deep understanding of financial and controlling processes to effectively support and advance business goals.",
    //                         "jobSkills": ["Bachelor’s, Master’s, or PhD in Information Technology, Computer Science, or related field",
    //                                         "At least 5 years of experience in SAP ERP 6.0 or S/4HANA, particularly in Controlling (COPA, CO-PC, Material Ledger) and Finance (General Ledger, Fixed Assets)",
    //                                         "Proficient in defining IT roadmaps and working towards strategic goals in collaboration with business teams",
    //                                         "Experience in creating user stories for functional and non-functional requirements, conducting demos, and providing training",
    //                                         "Strong analytical skills for effective problem-solving and decision-making",
    //                                         "Excellent planning, realization, and controlling abilities",
    //                                         "Effective communication skills and the ability to work in an international, geographically dispersed team",
    //                                         "Agile methodology proficiency for quick and efficient project delivery",
    //                                         "Commitment to continuous learning and development, both for self and team"]
    //                     },
    //                     {
    //                         "jobId": "1A_d",
    //                         "jobTitle": "IT Business Analyst Salesforce",
    //                         "jobDescription": "As a Business Analyst in Hilti's Systematic Account Development program, you'll focus on enhancing Customer Relationship Management through Salesforce Sales Cloud. This role involves understanding business requirements, designing solution proposals, and supporting their implementation within Salesforce to optimize sales processes. You'll work within an international scrum team, using agile methodologies to deliver significant customer impact. While Salesforce Sales Cloud is your primary technology focus, you'll also engage with SAP S4 HANA, Salesforce Service Cloud, and AWS Microservices among others. This position plays a crucial role in providing transparency on sales opportunities and enabling effective use of Hilti products on job sites.",
    //                         "jobSkills": ["Bachelor’s degree in computer science, software engineering, information technology, or related fields","Over 5 years of experience with cloud software (preferably Salesforce), business process management, and agile methodologies","Excellent communication and interpersonal skills, fluent in English for effective stakeholder management in a global matrix environment",
    //                                       "Passion for marketing, sales, and service business process design with a keen interest in CRM software","Strong willingness and capacity to learn."]
    //                     }
    //                 ]
    //             },
    //             {
    //                 "subCategoryId": "1B",
    //                 "subCategoryName": "Internship",
    //                 "subCategoryDescription": "Focused on leveraging business analytics tools and methodologies to improve decision-making and business practices within IT, Software & Digital projects.",
    //                 "availableJobs": [
    //                     {
    //                         "jobId": "1B_a",
    //                         "jobTitle": "Internship - DevOps Engineer",
    //                         "jobDescription": "Join our IT team as a DevOps Engineer Intern and engage in exciting projects, gaining practical expertise and solving real-world challenges in a global setting. You will partner with stakeholders to translate requirements into technical designs, improve CI/CD toolchains, drive lifecycle activities, and enhance IT systems with new technologies. You'll also provide advanced support to both business and IT teams. This internship offers flexible start dates and lasts 4-6 months, providing a comprehensive experience in cloud product management and operations.",
    //                         "jobSkills": ["Enrolled in Bachelor's/Master's in IT, Software Engineering, Data Science, or related fields","Strategic thinker with excellent problem-solving skills","Proactive and hands-on mentality","Strong communication and interpersonal abilities","Fluent in written and spoken English","Eager to learn and embrace challenges."]
    //                     },
    //                     {
    //                         "jobId": "1B_b",
    //                         "jobTitle": "Internship - IT Quality Assurance Analyst",
    //                         "jobDescription": "Join our IT team as an IT Quality Assurance Analyst Intern on a variety of exciting projects. This internship offers a flexible start and lasts 4-6 months, where you'll enhance your skills in global IT project management and solution delivery. You will be involved in refining QA processes, designing and reviewing test cases, and working within the software development lifecycle to ensure functionality, performance, security, and user experience standards are met. Additionally, you will monitor software development stages to manage malfunctions and continuously improve quality standards.",
    //                         "jobSkills": ["Enrolled in Bachelor's/Master's in IT, Software Engineering, Data Science, or related fields","Strategic thinker with excellent problem-solving skills","Proactive and hands-on mentality","Strong communication and interpersonal abilities","Fluent in written and spoken English","Eager to learn and embrace challenges."]
    //                     },
    //                 ]
    //             } 
    //         ],
    //         "availableJobs": [
    //             {
    //                 "jobId": "1_a",
    //                 "jobTitle": "Cloud QA Automation Engineer",
    //                 "jobDescription": "As a Cloud QA Automation Engineer at Hilti, you will focus on defining and executing test cases, approaches, automation, and documentation within the Sales Core IT area. Your main goal is to ensure business requirements are accurately met through meticulous testing methods for complex software applications. Daily responsibilities include integrating with product or project teams to deliver high-quality software, thoroughly testing changes before production, and utilizing automation test suites. Additionally, you will continually seek to implement cutting-edge technologies to enhance IT QA processes at Hilti.",
    //                 "jobSkills": ["Bachelor's or Master's in Information Systems, Computer Science, or related fields with a CGPA > 3.0","4+ years QA Engineer experience in the IT sector","Expertise in test automation tools like Cucumber, BDD, Gherkin, JMeter, and Postman","Familiarity with AWS products and navigating the AWS console",
    //                               "Skilled in analyzing test results and reporting with defined KPIs","Experience in agile environments and understanding of CI/CD processes; fluent in English."]
    //             },
    //             {
    //                 "jobId": "1_b",
    //                 "jobTitle": "Procerocurement IT",
    //                 "jobDescription": "As a Procurement Support Specialist at Hilti, you will assist and guide Procurement Managers through the sourcing process to ensure compliance and high quality. You'll gain expertise in drafting Requests for Proposal, setting up auctions, and forming contracts, while also managing supplier data and leading system improvement projects. This role offers a comprehensive introduction to Hilti's business operations and involvement in a global team.",
    //                 "jobSkills": ["Bachelor’s degree in Information Technology or Business Administration; Master’s degree preferred","Relevant professional experience, especially with ERP and procurement systems","Strong interdisciplinary teamwork and project management skills","Comprehensive approach to tasks, from planning to continuous improvement and documentation",
    //                               "Good analytical abilities with a strong affinity for IT systems","Excellent communication and presentation skills in English; additional languages beneficial."]
    //             },
    //         ]
    //     }
}




export default function CatOpeningPage({ params }: any) {
    const [clickedIndex, setClickedIndex] = useState<number | null>(null);
    const [thisCategory, setThisCategory] = useState<JobCatType | null>(null);
    const firstTimeRef = useRef(true);

    const handleClick = (index: number) => {
        if (clickedIndex === index) {
            setClickedIndex(null);
        } else {
            setClickedIndex(index);
        }
    }

    useEffect(() => {
        const initializeData = async (CategoryId: any) => {
            const data = await getSubcategoryDetail(params.categoryId);
            setThisCategory(data);
        }
        if (firstTimeRef.current) {
            console.log(params.categoryId)
            initializeData(params.categoryId);
            firstTimeRef.current = false;
        }
    },[])

    return (
        <div className="mx-[5rem] mt-[3rem]">
            {thisCategory && <div className="text-4xl text-red-700 font-extrabold italic uppercase">{thisCategory.jobCategory}</div>}
            <div className="mt-[1rem] text-lg font-semibold">Jobs Available</div>
            {thisCategory && thisCategory.subCategories && thisCategory.subCategories.map((subCat, index) => (   
                <div key={index} className={`animate-expand ${(clickedIndex === index) ? 'active' : ''} mt-[1rem] bg-gray-100 px-[1rem] py-[1rem] rounded-lg shadow-md shadow-gray-500`}>
                    {(clickedIndex === index) ? (
                        <div onClick={() => handleClick(-1)}>
                            <div className="text-2xl font-bold text-red-700 uppercase tracking-tight underline underline-offset-8 decoration-gray-300">{subCat.subCategoryName}</div>
                            <div className="p-[0.5rem] font-medium">{subCat.subCategoryDescription}</div>
                            <div className="grid grid-cols-2 gap-x-[1.5rem]">
                                {subCat.availableJobs && subCat.availableJobs.map((job, index) => (
                                    <div key={index} className="bg-gray-100 px-[1rem] py-[1rem] rounded-lg shadow-md shadow-gray-500 mt-[1rem]">
                                        <Link href={`/job-opening/${params.categoryId}/${job.jobId}`} ><div className="text-xl font-semibold text-black tracking-tighter">{job.jobTitle}</div></Link>
                                    </div>
                                ))}
                            </div>
                        </div>
                    ) : (
                        <div onClick={() => handleClick(index)} className="text-2xl font-bold text-red-700 uppercase tracking-tight">{subCat.subCategoryName}</div>
                    )}
                </div>
                ))}
            <div className="grid grid-cols-2 p-[2rem] gap-[4rem] bg-gray-100 rounded-lg shadow-md shadow-gray-500 mt-[1rem]">
                {thisCategory && thisCategory.availableJobs && thisCategory.availableJobs.map((job, index) => (
                    <div key={index} className="bg-gray-100 px-[1rem] py-[1rem] rounded-lg shadow-md shadow-gray-500">
                        <Link href={`/job-opening/${params.categoryId}/${job.jobId}`}><div className="text-2xl font-bold text-black tracking-tight">{job.jobTitle}</div></Link>
                    </div>
                ))}
            </div>
        </div>
    );
}
