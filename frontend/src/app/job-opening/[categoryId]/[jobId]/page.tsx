'use client';

import { Job } from "../../indiJobCategory";

async function getJobDetail(JobId: string) {
    console.log(JobId)
    const res = await fetch(`http://localhost:8000/jobopenings/job/${JobId}`)
    const data = await res.json()
    // const data = {
    //     "jobId": "1A_a",
    //     "jobTitle": "IT Business Analyst – SAP FICO",
    //     "jobDescription": "This is an IT Business Analyst role focused on the financial aspects of software sales, including subscriptions, rentals, leasing, and usage concepts for Hilti tools. You will bridge the gap between business needs and SAP FICO implementations, working on global projects, daily support, and compliance initiatives.",
    //     "jobSkills": ["SAP FICO consultant background (3+ years experience)", "Experience with SAP ERP 6.0 / S/4HANA in finance (General Ledger, AR, AA)", 
    //                     "Understanding of business processes in finance, controlling, sales & distribution", "Ability to handle complex projects and implement IFRS standards","Strong communication, problem-solving, and teamwork skills","Experience in international/virtual teams"]
    // }

    return data

}
export default async function jobOpeningPage({ params }: any) {
    let thisJob: Job;
    thisJob = await getJobDetail(params.jobId);

    return (
        <div className="m-20 mb-0">
            <div className="text-4xl font-bold">{thisJob.jobTitle}</div>
            <br /> <hr /> <br />
            <div className="text-balance leading-relaxed">{thisJob.jobDescription}</div>
            <br />
            <div className="text-2xl font-bold">Skill we are looking for this role</div>
            <ul>
                {thisJob.jobSkills && thisJob.jobSkills.map((skill, index) => (
                    <li key={index} className="text-lg">
                        <span className="mr-2">&#8226;</span>
                        {skill}
                    </li>
                ))}
            </ul>
            <br /> <hr /> <br />
            <div className="text-2xl font-bold">Apply for this job</div>
            <br />
            <form action="http://localhost:8000/resume" method="post" encType="multipart/form-data" target="form_target" className="space-y-5">
                <div className="flex flex-row justify-start">
                    <div className="w-[20rem] flex items-center justify-center h-12 border border-transparent rounded-md shadow-sm text-base font-medium text-white bg-indigo-600 hover:bg-indigo-700">
                        <div>Upload a file</div>
                        <input type="file" accept=".pdf" name="resume" className="border-2 absolute h-12 w-[20rem] opacity-0"/>
                    </div>
                    <button type="submit" className="ml-8 flex items-center justify-center w-[6rem] py-3 border border-transparent text-base font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700">
                        Submit
                    </button>
                </div>
            </form>
            <iframe name="form_target" style={{display: 'none'}}></iframe>
        </div>
    );
}