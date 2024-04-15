import { Job } from "../indiJobCategory";


async function getJobDetail(JobId: any) {
    const res = await fetch(`http://localhost:8000/jobopenings/${JobId}`, 
        {
            next: { revalidate: 10 },
        }
    );
    const data = await res.json();
    return data;
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
