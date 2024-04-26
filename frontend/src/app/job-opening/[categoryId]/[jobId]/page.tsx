'use client';

import { Job } from "../../indiJobCategory";

async function getJobDetail(JobId: string) {
    console.log(JobId)
    const res = await fetch(`http://localhost:8000/jobopenings/job/${JobId}`)
    const data = await res.json()


    return data
}



export default async function jobOpeningPage({ params }: any) {
    let thisJob: Job;
    thisJob = await getJobDetail(params.jobId);

    const postResume = async (e: any) => {
        e.preventDefault();
        console.log("postResume");
        
        const fileInput = document.querySelector('input[type="file"]') as HTMLInputElement;
        const formData = new FormData();
        
        // 6 characters random string
        const uniqueResumeID = Math.random().toString(36).substring(2, 8);
        
        if (fileInput && fileInput.files && fileInput.files.length > 0) {
            formData.append('resume', fileInput.files[0]);
            formData.append('jobDetails', JSON.stringify(thisJob));
            formData.append('email', 'user@example.com');
            formData.append('uniqueResumeID', uniqueResumeID);

            const res = await fetch('http://localhost:8000/resume', {
                method: 'POST',
                body: formData
            });
            const data = await res.json();
            console.log(data);
        }
    }


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
            <form onSubmit={postResume} className="space-y-5">
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