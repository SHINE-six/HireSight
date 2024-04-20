import Link from 'next/link';
import * as React from 'react';


const App = () => {
	return (
		<div className='mx-[2rem]'>
			<div className='flex justify-between mx-[3rem] mt-[5rem] text-center text-2xl'>
				<div className='w-[20rem] bg-gray-200 flex flex-col relative p-[2rem] items-center rounded-lg'>
					<div className='w-[5rem] h-[5rem] rounded-full bg-white shadow-sm shadow-black absolute top-[-3rem] flex justify-center'>
						<img src="resume.svg" alt="resume" className='w-[3.5rem]'/>
					</div>
					<div className='font-bold my-[1rem] px-[2rem]'>Resume AI Detection</div>
					<div className='w-[14rem] bg-gray-400 h-[0.1rem]'></div>
					<div className='w-[14rem] bg-white rounded-md mt-[3rem] text-xl justify-between flex flex-row py-[0.5rem] px-[1rem] font-semibold shadow-sm shadow-black'>
						<div>Applicant:</div> 
						<div className='text-red-700'>96</div>
					</div>
					<Link href='/applicant-detail'><div className='mt-[3rem] w-[14rem] bg-red-700 text-xl px-[1rem] py-[0.25rem] rounded-lg text-white font-semibold'>View Applicant Detail</div></Link>
				</div>

				<div className='w-[20rem] bg-gray-200 flex flex-col relative p-[2rem] items-center rounded-lg'>
					<div className='w-[5rem] h-[5rem] rounded-full bg-white shadow-sm shadow-black absolute top-[-3rem] flex justify-center'>
						<img src="suitability.svg" alt="suitability" className='w-[3.5rem]'/>
					</div>
					<div className='font-bold my-[1rem] px-[2rem]'>Resume Suitability</div>
					<div className='w-[14rem] bg-gray-400 h-[0.1rem]'></div>
					<div className='w-[14rem] bg-white rounded-md mt-[3rem] text-xl justify-between flex flex-row py-[0.5rem] px-[1rem] font-semibold shadow-sm shadow-black'>
						<div>Applicant:</div> 
						<div className='text-red-700'>33</div>
					</div>
					<Link href='/suitability-ranking'><div className='mt-[3rem] w-[14rem] bg-red-700 text-xl px-[1rem] py-[0.25rem] rounded-lg text-white font-semibold'>View Suitability Ranking</div></Link>
				</div>

				<div className='w-[20rem] bg-gray-200 flex flex-col relative p-[2rem] items-center rounded-lg'>
					<div className='w-[5rem] h-[5rem] rounded-full bg-white shadow-sm shadow-black absolute top-[-3rem] flex justify-center'>
						<img src="interview.svg" alt="interview" className='w-[3.5rem]'/>
					</div>
					<div className='font-bold my-[1rem] px-[3rem]'>AI Interviewing</div>
					<div className='w-[14rem] bg-gray-400 h-[0.1rem]'></div>
					<div className='w-[14rem] bg-white rounded-md mt-[3rem] text-xl justify-between flex flex-row py-[0.5rem] px-[1rem] font-semibold shadow-sm shadow-black'>
						<div>Applicant:</div> 
						<div className='text-red-700'>10</div>
					</div>
					<Link href='/interview-result'><div className='mt-[3rem] w-[14rem] bg-red-700 text-xl px-[1rem] py-[0.25rem] rounded-lg text-white font-semibold'>View Interview Ranking & Result</div></Link>
				</div>
			</div>
		</div>
	);

};

export default App;