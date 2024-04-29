'use client';

import React from 'react';
import IndiJobCategory, { JobCatType } from './indiJobCategory';


async function getData() {
  const res = await fetch('http://localhost:8000/jobopenings', { cache: "no-store" });
  const data = await res.json();
  console.log("request data done", data);
  
  return data;
}


export default async function jobOpeningPage() {
  const data = await getData();
    
  return (
    <div className='flex justify-center w-full'>
      <div className='flex flex-col w-full'>
        <div className='text-[1.4rem] font-medium leading-tight mx-[4rem] my-[2rem]'>
        HireSight has a variety of job openings in different categories. Click on the job category to view the available job openings.
        </div>
          <div className='flex justify-center '>
            <div className='text-2xl font-semibold mt-[4rem]'>Job Offering</div>
          </div>
        <div className='mt-[1rem] bg-gray-100 w-screen'>
          <br />
          <div className='flex justify-center w-full'>
            <div className='grid grid-cols-2 gap-[2rem] w-fit'>
              {Array.isArray(data) && data.map((jobCategory: JobCatType) => (
                <IndiJobCategory key={jobCategory.categoryId} jobCat={jobCategory}/>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}