'use client';

import Link from 'next/link';
import React, { useEffect } from 'react';

import { usePageConfigStore } from '@/stores/PageConfigStore';


const getResumeData = async (currentAvailableJob: string) => {
	try {
		const formData = new FormData();
		formData.append('jobTitle', currentAvailableJob);
		formData.append('onlyApplicantCount', 'true');
		const res = await fetch('http://localhost:8000/resumeRanking',
			{ 
				method: 'POST',
				body: formData
			});
		const data = await res.json();
		console.log("request data done");
		console.log(data);
		return data;
	} catch (error) {
		console.error('Error fetching data:', error);
	}
}


const App = () => {
	const { currentAvailableJob, resumeCount, setResumeCount_Ai_detection, setResumeCount_Interview, setResumeCount_Resume_suitability } = usePageConfigStore();

	useEffect(() => {
		getResumeData(currentAvailableJob)?.then((data) => {
			setResumeCount_Ai_detection(data['Ai_detection']);
			setResumeCount_Resume_suitability(data['Resume_suitability']);
			setResumeCount_Interview(data['Interview']);
		});
	}, [currentAvailableJob]);

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
						<div className='text-red-700'>{resumeCount['Ai_detection']}</div>
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
						<div className='text-red-700'>{resumeCount['Resume_suitability']}</div>
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
						<div className='text-red-700'>{resumeCount['Interview']}</div>
					</div>
					<Link href='/interview-result'><div className='mt-[3rem] w-[14rem] bg-red-700 text-xl px-[1rem] py-[0.25rem] rounded-lg text-white font-semibold'>View Interview Ranking & Result</div></Link>
				</div>
			</div>
		</div>
	);

};

export default App;