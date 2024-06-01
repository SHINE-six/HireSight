'use client';


import { useEffect, useState } from 'react';

import { usePageConfigStore } from '@/stores/PageConfigStore';


interface ResumeData {
    'filename': string;
    'email': string;
    'uniqueResumeId': string;
    'jobPostitionApply': string;
    'AiDetection': number;
    'plagiarism': number;
    'suitability': number;
    'stage': string;
}


interface ResumeDataFromServer {
    'data': ResumeData[];
    'count': number;
}

const getResumeData = async (currentAvailableJob: string) => {
	try {
		const formData = new FormData();
		formData.append('jobTitle', currentAvailableJob);
        formData.append('stage', 'Interview')
		const res = await fetch('http://localhost:8000/resumeRanking',
			{ 
				method: 'POST',
				body: formData
			});
		const data:ResumeDataFromServer = await res.json();
		console.log("request data done");
		console.log(currentAvailableJob, data);
		return data;
	} catch (error) {
		console.error('Error fetching data:', error);
	}
}


const ApplicantDetailPage = () => {
    const { resumeCount, currentAvailableJob, setResumeCount_Ai_detection } = usePageConfigStore();
    const [ resumeDataList, setResumeDataList ] = useState<ResumeData[]>([]);

    // const resumeRanking:any[] = await fetchResumeRanking();
    // resumeRanking.sort((a, b) => {
    //     return new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime();
    // });

    // resumeRanking.sort((a, b) => {
    //     return a.id - b.id;
    // });
	useEffect(() => {
		getResumeData(currentAvailableJob)?.then((data) => {
            if (data) {
                const sortedData = data.data.sort((a, b) => a.AiDetection - b.AiDetection);
                setResumeDataList(sortedData);
                setResumeCount_Ai_detection(data.count);
            }
        });
	}, [currentAvailableJob]);
    

    const handleProceedAiInterview = (uniqueResumeId: string) => {
        console.log("Proceeding to Ai Interviewing", uniqueResumeId);
        const formData = new FormData();
        formData.append('uniqueResumeId', uniqueResumeId);
        formData.append('stage', 'Interview');
        const res = fetch('http://localhost:8000/updateStage',
            { 
                method: 'POST',
                body: formData
            });
        console.log(res);
    }

    return (
        <div className="mt-[2rem] mx-[3rem]">
            <div className="flex flex-row items-center">
                <div className='w-[5rem] h-[5rem] rounded-full bg-white shadow-sm shadow-black flex justify-center'>
                    <img src="resume.svg" alt="resume" className='w-[3.5rem]'/>
                </div>
                <div className="py-[1rem] px-[4rem] text-2xl font-bold border-b-[0.1rem] border-gray-300">Interviewing</div>
                <div className='w-[14rem] bg-white rounded-xl text-xl justify-between flex flex-row py-[0.5rem] px-[1rem] border-b-[0.1rem] border-gray-300 shadow-md font-semibold'>
                    <div>Applicant:</div> 
                    <div className='text-red-700'>{resumeCount['Ai_detection']}</div>
                </div>
            </div>
            <div className="mt-[2rem] mx-[1rem] flex flex-col items-center w-full">
                <div className="flex justify-center w-full p-[0.5rem] mb-[1rem]">
                    <div className=" grid grid-cols-5 w-4/5">
                        <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">Name</div>
                        <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">email</div>
                        <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">AI detection</div>
                        <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">Manual proceed</div>
                        <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">Resume</div>
                    </div>
                </div>
                {resumeDataList.map((resume, index) => {
                    let bgColor = "bg-gray-200";
                    if (index < 3) {
                        bgColor = "bg-blue-200"; // Change this to the color you want for the first 3 items
                    }
                    return (
                        <div key={resume.uniqueResumeId} className={`w-4/5 ${bgColor} rounded-md shadow-md shadow-black mb-[1rem] p-[0.5rem] items-center grid grid-cols-5`}>
                            <div className="pr-2">{resume.filename}</div>
                            <div className="pr-2">{resume.email}</div>
                            <div className="pr-2">{(resume.AiDetection)}%</div>
                            {/* <div className="pr-2">{(resume.plagiarism * 100).toFixed(3)}%</div> */}
                            <div className="bg-green-400 rounded-lg px-[1rem] py-[0.5rem] text-white" onClick={()=>handleProceedAiInterview(resume.uniqueResumeId)}>Proceed to Ai Interviewing</div>
                            <div className="bg-red-700 rounded-lg px-[1rem] py-[0.5rem] text-white">View Resume</div>
                        </div>
                    );
                }
                )}
            </div>
        </div>
    );
}

export default ApplicantDetailPage;