'use client';

import Link from "next/link";
import { JobCatType } from "../indiJobCategory";
import { useEffect, useRef, useState } from "react";


async function getSubcategoryDetail(CategoryId: any) {
    const res = await fetch(`http://localhost:8000/jobopenings/${CategoryId}`);
    const data = await res.json();

    return data;
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