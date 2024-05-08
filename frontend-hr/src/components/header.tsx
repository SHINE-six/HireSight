'use client';

import React, { useEffect, useRef, useState } from 'react';

import { usePageConfigStore } from '@/stores/PageConfigStore';

const Header = () => {
    const runOnce = useRef(false);
    const [jobCategory, setJobCategory] = useState<any[]>([]);
    const [subCategories, setSubCategories] = useState<any[]>([]);
    const [availableJobs, setAvailableJobs] = useState<any[]>([]);
    const [selectedCategory, setSelectedCategory] = useState<string>('');
    const [selectedSubCategory, setSelectedSubCategory] = useState<string>('');
    const { setCurrentAvailableJob } = usePageConfigStore();
    
    const handleGetData = async () => {
        try {
            const res = await fetch('http://localhost:8000/jobopenings', { cache: "no-store" });
            const data = await res.json();
            console.log("request data done");
            console.log(data);
            for (let jobCat of data) {
                if(jobCat['subCategories']) {
                    jobCat['subCategories'].push({"subCategoryId":-1})
                }
            }
            setJobCategory(data);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    const handleCategoryChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
        const category = e.target.value;
        setSelectedCategory(category);
        const selectedCategoryData = jobCategory.find(jobCat => jobCat['jobCategory'] === category);
        if (selectedCategoryData) {
            if (selectedCategoryData['subCategories']) {
                setSubCategories(selectedCategoryData['subCategories']);
                setSelectedSubCategory(selectedCategoryData['subCategories'][0]['subCategoryId']);
                setAvailableJobs(selectedCategoryData['subCategories'][0]['availableJobs']);
                setCurrentAvailableJob(selectedCategoryData['subCategories'][0]['availableJobs'][0]['jobTitle']);
            }
            else {
                setSubCategories([]);
                setAvailableJobs(selectedCategoryData['availableJobs']);
                setCurrentAvailableJob(selectedCategoryData['availableJobs'][0]['jobTitle']);
            }
        }
    };

    const handleSubCategoryChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
        const subCategory = e.target.value;
        setSelectedSubCategory(subCategory);
        const selectedSubCategoryData = subCategories.find(subCat => subCat['subCategoryId'] === subCategory);
        if (selectedSubCategoryData) {
            setAvailableJobs(selectedSubCategoryData['availableJobs']);
            setCurrentAvailableJob(selectedSubCategoryData['availableJobs'][0]['jobTitle']);
        } else {
            const availableJobs = jobCategory.find(jobCat => jobCat['jobCategory'] === selectedCategory)['availableJobs'];
            setAvailableJobs(availableJobs);
            setCurrentAvailableJob(availableJobs[0]['jobTitle']);
        }
    };


    useEffect(() => {
        if (!runOnce.current) {
            handleGetData()
            runOnce.current = true
        }
    }, [])


    useEffect(() => {
        if (jobCategory.length > 0) {
            const initialCategory = jobCategory[0]['jobCategory'];
            setSelectedCategory(initialCategory);
            const initialSubCategories = jobCategory[0]['subCategories'];
            setSubCategories(initialSubCategories);
            const initialAvailableJobs = initialSubCategories[0]['availableJobs'];
            setAvailableJobs(initialAvailableJobs);
            setCurrentAvailableJob(initialAvailableJobs[0]['jobTitle']);
            setSelectedSubCategory(initialSubCategories[0]['subCategoryId']);
        }
    }, [jobCategory]);

    return (
        <div className="px-[2rem]">
            <div className='text-3xl font-bold my-[1rem]'>
                <select value={selectedCategory} onChange={handleCategoryChange}>
                    {jobCategory.map((jobCat) => (
                        <option key={jobCat['jobCategory']} value={jobCat['jobCategory']} className='text-lg'>{jobCat['jobCategory']}</option>
                    ))}
                </select>
            </div>

            {subCategories && (subCategories.length > 0) && (
                <div className='bg-gray-400 w-fit p-[0.5rem] rounded-md mb-4'>
                    <select className='bg-transparent font-semibold' value={selectedSubCategory} onChange={handleSubCategoryChange}>
                        {subCategories.map((subCat) => (
                            <option key={subCat['subCategoryId']} value={subCat['subCategoryId']}>{subCat['subCategoryName']}</option>
                        ))}
                    </select>
                </div>
            )}
            {availableJobs && (
                <div className='bg-gray-400 w-fit p-[0.5rem] rounded-md'>
                    <select className='bg-transparent font-semibold' onChange={(e) => setCurrentAvailableJob((availableJobs.find(job => job['jobId'] === e.target.value)['jobTitle']))}>
                        {availableJobs.map((job) => (
                            <option key={job['jobId']} value={job['jobId']}>{job['jobTitle']}</option>
                        ))}
                    </select>
                </div>
            )}
            <div className='ml-[1rem] mt-[1rem] w-[10rem] h-[0.55rem] bg-red-700'></div>
        </div>
    );
};

export default Header;