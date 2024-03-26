import React, { Key } from 'react';
import Link from 'next/link';

const IndiJobCategory = ({ jobCat }: { jobCat: JobCatType}) => {
    console.log("jobCat", jobCat);
    return (
        <div className='flex flex-col bg-gray-300 w-[30rem] h-[18rem] p-4 place-content-between'>
            <div>
                <div className='text-xl font-medium text-red-700'>{jobCat.jobCategory}</div>
                <br/>
                <div className='text-base text-black'>{jobCat.jobCategoryDescription}</div>
            </div>
            <div className='flex flex-row space-x-2'>
                {jobCat && jobCat.availableJobs.map((job, index) => (
                    <div key={index} className='bg-gray-700 p-1 rounded-md'>
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