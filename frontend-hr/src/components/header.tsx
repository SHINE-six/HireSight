'use client';

import React, { useEffect, useRef, useState } from 'react';



const Header = () => {
    const runOnce = useRef(false);
    const [jobCategory, setJobCategory] = useState<any[]>([]);
    const [subCategories, setSubCategories] = useState<any[]>([]);
    const [availableJobs, setAvailableJobs] = useState<any[]>([]);
    const [selectedCategory, setSelectedCategory] = useState<string>('');
    const [selectedSubCategory, setSelectedSubCategory] = useState<string>('');
    
    const handleGetData = async () => {
        try {
            const res = await fetch('http://localhost:8000/jobopenings', { cache: "no-store" });
            const data = await res.json();
            console.log("request data done");
            console.log(data);
            setJobCategory(data);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    const handleCategoryChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
        const category = e.target.value;
        setSelectedCategory(category);
        console.log(category);
        const selectedCategoryData = jobCategory.find(jobCat => jobCat['jobCategory'] === category);
        if (selectedCategoryData) {
            setSubCategories(selectedCategoryData['subCategories']);
            setSelectedSubCategory(selectedCategoryData['subCategories'][0]['subCategoryId']);
            setAvailableJobs(selectedCategoryData['subCategories'][0]['availableJobs']);
        }
    };

    const handleSubCategoryChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
        const subCategory = e.target.value;
        setSelectedSubCategory(subCategory);
        console.log(subCategory);
        const selectedSubCategoryData = subCategories.find(subCat => subCat['subCategoryId'] === subCategory);
        if (selectedSubCategoryData) {
            setAvailableJobs(selectedSubCategoryData['availableJobs']);
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
            setSelectedSubCategory(initialSubCategories[0]['subCategoryId']);
        }
    }, [jobCategory]);

    return (
        <div className="px-[2rem]">
            <div className='text-3xl font-bold my-[1rem]'>
                <select value={selectedCategory} onChange={handleCategoryChange}>
                    {jobCategory.map((jobCat) => (
                        <option key={jobCat['jobCategory']} value={jobCat['jobCategory']}>{jobCat['jobCategory']}</option>
                    ))}
                </select>
            </div>

            {subCategories.length > 0 && (
                <div className='bg-gray-400 w-fit p-[0.5rem] rounded-md mb-4'>
                    <select className='bg-transparent font-semibold' value={selectedSubCategory} onChange={handleSubCategoryChange}>
                        {subCategories.map((subCat) => (
                            <option key={subCat['subCategoryId']} value={subCat['subCategoryId']}>{subCat['subCategoryName']}</option>
                        ))}
                    </select>
                </div>
            )}
            {availableJobs.length > 0 && (
                <div className='bg-gray-400 w-fit p-[0.5rem] rounded-md'>
                    <select className='bg-transparent font-semibold'>
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