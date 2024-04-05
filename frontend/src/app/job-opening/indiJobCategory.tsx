import React, { Key } from 'react';
import Link from 'next/link';

const IndiJobCategory = ({ jobCat }: { jobCat: JobCatType}) => {
    console.log("jobCat", jobCat);
    return (
        <div className='flex flex-col bg-white w-[30rem] h-[18rem] px-[2rem] py-[1.2rem] place-content-between justify-self-center rounded-md shadow-lg'>
            <div>
                <div className='text-xl font-semibold text-red-700 uppercase'>{jobCat.jobCategory}</div>
                <br/>
                <div className='text-base font-semibold text-black'>{jobCat.jobCategoryDescription}</div>
            </div>
            <div className='flex flex-row space-x-3'>
                {jobCat && jobCat.availableJobs.map((job, index) => (
                    <div key={index} className='bg-gray-500 px-[0.6rem] text-[0.9rem] py-1 rounded-md text-white tracking-[-0.06rem]'>
                            <Link href={`/job-opening/${job.jobId}`}>{job.jobTitle}</Link>
                    </div>
                ))}
            </div>
        </div>
    )
}
export default IndiJobCategory;

export interface JobCatType {
    id: Key | null | undefined;
    jobCategory: string,
    jobCategoryDescription: string,
    availableJobs: Job[]
}

export interface Job {
    jobId: Key | null | undefined;
    jobTitle: string,
    jobDescription: string,
    jobSkills: string[] 
}