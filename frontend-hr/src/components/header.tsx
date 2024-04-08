'use client';

import { useEffect, useRef, useState } from 'react';



const Header = () => {
    const runOnce = useRef(false)
    const [jobCategory, setJobCategory] = useState<any[]>([])
    const [availableJobs, setAvailableJobs] = useState<any[]>([])
    const [value, setValue] = useState<string>('')
    
    const handleGetData = () => {
        const getData = async () => {
            const res = await fetch('http://localhost:8000/jobopenings', { cache: "no-store" });
            const data = await res.json();
            console.log("request data done");
            console.log(data)
            setJobCategory(data)
            return data;
        }
        getData()
    }

    const handleChange = (e: { target: { value: React.SetStateAction<string>; }; }) => {
        setValue(e.target.value)
        console.log(e.target.value)
        const toSet = jobCategory.filter((jobCat) => jobCat['jobCategory'] === e.target.value)
        setAvailableJobs(toSet[0]['availableJobs'])
    }


    useEffect(() => {
        if (!runOnce.current) {
            handleGetData()
        }
        runOnce.current = true
    }, [])

  return (
    <div className="px-[2rem]">
        <div className='text-3xl font-bold my-[1rem]'>
            <select value={value} onChange={handleChange}>
                {jobCategory.map((jobCat) => {
                    return <option className='text-sm' key={jobCat['jobCategory']} value={jobCat['jobCategory']}>{jobCat['jobCategory']}</option>
                })}
            </select>
        </div>
        <div className='bg-gray-400 w-fit p-[0.5rem] rounded-md'>
            <select className='bg-transparent font-semibold'>
                {availableJobs.map((job) => {
                    return <option key={job['jobId']} value={job['jobId']}>{job['jobTitle']}</option>
                })}
            </select>
        </div>
        <div className='ml-[1rem] mt-[1rem] w-[8rem] h-[0.75rem] bg-red-700'>
        </div>        
    </div>
  );
}

export default Header;