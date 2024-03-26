import React from 'react';
import IndiJobCategory, { JobCatType} from './indiJobCategory';


async function getData() {
  // sample data
  const res = await fetch('https://ddncl8rd-8000.asse.devtunnels.ms/jobopenings', { cache: "no-store" });
  const data = await res.json();
  console.log("request data done");
  return data;
}


export default async function jobOpeningPage() {
  const data = await getData();
  return (
    <div className='flex justify-center  w-full'>
      <div className='flex flex-col '>
        <div className='flex justify-center'>
          <div className='text-2xl font-semibold'>Career Openings</div>
        </div>
        <br />
        <div className='grid grid-cols-2 gap-4'>
          {data && data.map((jobCategory: JobCatType) => (
            <IndiJobCategory key={jobCategory.id} jobCat={jobCategory} />
          ))}
        </div>
      </div>
    </div>
  );
}