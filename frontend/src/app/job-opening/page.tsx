'use client';

import React from 'react';
import IndiJobCategory, { JobCatType} from './indiJobCategory';


async function getData() {
  // sample data
  const res = await fetch('http://localhost:8000/jobopenings', { cache: "no-store" });
  const data = await res.json();
  console.log("request data done");
  return data;
}


export default async function jobOpeningPage() {
  const data = await getData();
    
  return (
    <div className='flex justify-center w-full'>
      <div className='flex flex-col w-full'>
        <div className='text-[2.9rem] font-semibold my-[2rem] leading-tight mx-[4rem]'>
        HireSight job offerings
        </div>
        <div className='text-[1.2rem] font-semibold leading-tight mx-[4rem]'>
        HireSight has a variety of job openings in different categories. Click on the job category to view the available job openings.
        </div>
        <div className='mt-[4rem] bg-gray-100 w-screen'>
          <div className='flex justify-center '>
            <div className='text-2xl font-semibold mt-[1rem]'>Job Offering</div>
          </div>
          <br />
          <div className='flex justify-center w-full'>
            <div className='grid grid-cols-2 gap-4 w-fit'>
              {Array.isArray(data) && data.map((jobCategory: JobCatType) => (
                <IndiJobCategory key={jobCategory.id} jobCat={jobCategory} />
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}