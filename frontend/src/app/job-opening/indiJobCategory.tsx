import React, { Key } from 'react';
import Link from 'next/link';

const IndiJobCategory = ({ jobCat }: { jobCat: JobCatType}) => {
    return (
        <Link href={`/job-opening/${jobCat.categoryId}`}>
            <div className='flex flex-col bg-white w-[35rem] h-[15rem] px-[2rem] py-[1.2rem] place-content-between justify-self-center rounded-md shadow-lg'>
                <div>
                    <div className='text-xl font-semibold text-red-700 uppercase underline-offset-8 underline decoration-gray-300'>{jobCat.jobCategory}</div>
                    <br/>
                    <div className='text-[1.075rem] text-justify font-medium text-black'>{jobCat.jobCategoryDescription}</div>
                </div>
            </div>
        </Link>
    )
}
export default IndiJobCategory;

export interface JobCatType {
    categoryId: Key | null | undefined,
    jobCategory: string,
    jobCategoryDescription: string,
    subCategories: SubCategory[] | null | undefined,
    availableJobs: Job[]
}

export interface SubCategory {
    subCategoryId: Key | null | undefined,
    subCategoryName: string,
    subCategoryDescription: string,
    availableJobs: Job[]
}

export interface Job {
    jobId: Key | null | undefined,
    jobTitle: string,
    jobDescription: string,
    jobSkills: string[] 
}