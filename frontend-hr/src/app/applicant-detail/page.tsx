'use client';

import { useEffect, useState, useRef } from 'react';
import { usePageConfigStore } from '@/stores/PageConfigStore';
import MoonLoader from 'react-spinners/MoonLoader';
import { useRouter } from 'next/navigation';
import { IoIosArrowBack } from "react-icons/io";
import IntervieweeReport from "../interviewee-report/page"

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
        formData.append('stage', 'Ai detection')
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
    let [loading, setLoading] = useState(false);
    let [loading, setLoading] = useState(false);
    const { resumeCount, currentAvailableJob, setResumeCount_Ai_detection } = usePageConfigStore();
    const [ resumeDataList, setResumeDataList ] = useState<ResumeData[]>([]);
    const [showReport, setShowReport] = useState(false)
    const topThreeRef = useRef<string[]>([]);
    const router = useRouter();
    const router = useRouter();

    // const resumeRanking:any[] = await fetchResumeRanking();
    // resumeRanking.sort((a, b) => {
    //     return new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime();
    // });

    // resumeRanking.sort((a, b) => {
    //     return a.id - b.id;
    // });
	useEffect(() => {
        topThreeRef.current = [];
		getResumeData(currentAvailableJob)?.then((data) => {
            if (data && data.data) {
                if (data.data.length > 1) {
                    const sortedData = data.data.sort((a, b) => a.AiDetection - b.AiDetection);
                    setResumeDataList(sortedData);
                } else if (data.data.length === 1) {
                    setResumeDataList(data.data); 
                }
            if (data && data.data) {
                if (data.data.length > 1) {
                    const sortedData = data.data.sort((a, b) => a.AiDetection - b.AiDetection);
                    setResumeDataList(sortedData);
                } else if (data.data.length === 1) {
                    setResumeDataList(data.data); 
                }
                setResumeCount_Ai_detection(data.count);
            }
        });
	}, [currentAvailableJob]);

    const handleEndStage = () => {
        setLoading(true);
        setLoading(true);
        console.log("End Stage");
        // top three applicants stage will change to 'Resume_suitability'
        const formData = new FormData();
        formData.append('uniqueResumeId', topThreeRef.current.join(','));
        formData.append('stage', 'Resume Suitability');
        const res = fetch('http://localhost:8000/updateStage',
            { 
                method: 'POST',
                body: formData
            });
        window.location.reload();
        console.log(res);
        setLoading(false);
    }

    const handleProceedResumeSuitability = (uniqueResumeId: string) => {
        setLoading(true);
        console.log("Proceeding to Resume Suitability", uniqueResumeId);
        const formData = new FormData();
        formData.append('uniqueResumeId', uniqueResumeId);
        formData.append('stage', 'Resume Suitability');
        const res = fetch('http://localhost:8000/updateStage',
            { 
                method: 'POST',
                body: formData
            });
        window.location.reload();
        window.location.reload();
        console.log(res);
        setLoading(false);
    }

    const handleProceedResumeSuitability = (uniqueResumeId: string) => {
        setLoading(true);
        console.log("Proceeding to Resume Suitability", uniqueResumeId);
        const formData = new FormData();
        formData.append('uniqueResumeId', uniqueResumeId);
        formData.append('stage', 'Resume Suitability');
        const res = fetch('http://localhost:8000/updateStage',
            { 
                method: 'POST',
                body: formData
            });
        window.location.reload();
        console.log(res);
        setLoading(false);
        setLoading(false);
    }
    
    const handleBack = () => {
        // if (window.history.length > 1) {
            router.back();
        // } else {
        //     router.push('/');
        // }
    }

    const handleReportClick = () => {
        // router.push('/interviewee-report');
        window.open('/interviewee-report', '_blank')
    }

    return (
        <div className="mt-[2rem] mx-[3rem] sweet-loading">
            <div className="flex flex-row items-center">
                <div className='w-[5rem] h-[5rem] rounded-full bg-white shadow-sm shadow-black flex justify-center'>
                    <img src="resume.svg" alt="resume" className='w-[3.5rem]'/>
                </div>
                <div className="py-[1rem] px-[4rem] text-2xl font-bold border-b-[0.1rem] border-gray-300">Resume AI Detection</div>
                <div className='w-[14rem] bg-white rounded-xl text-xl justify-between flex flex-row py-[0.5rem] px-[1rem] border-b-[0.1rem] border-gray-300 shadow-md font-semibold'>
                    <div>Applicant:</div> 
                    <div className='text-red-700'>{resumeCount['Ai_detection']}</div>
                </div>
                <button onClick={() => { handleEndStage(); setLoading(!loading); }} className="ml-4 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">End Stage</button>
                <button onClick={handleBack} className="fixed right-0 mr-[210px] ml-4 text-2xl text-black font-bold py-2 px-4 rounded"><IoIosArrowBack /></button>
                <button onClick={() => { handleEndStage(); setLoading(!loading); }} className="ml-4 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">End Stage</button>
                <button onClick={handleBack} className="fixed right-0 mr-[210px] ml-4 text-2xl text-black font-bold py-2 px-4 rounded"><IoIosArrowBack /></button>
            </div>
            <div className="mt-[2rem] mx-[1rem] flex flex-col items-center w-full">
                <div className="flex justify-center w-full p-[0.5rem] mb-[1rem]">
                    <div className="grid grid-cols-6 w-5/6"> 
                    <div className="grid grid-cols-6 w-5/6"> 
                        <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">Name</div>
                        <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">email</div>
                        <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">AI detection</div>
                        <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">Plagiarism</div> 
                        <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">Plagiarism</div> 
                        <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">Manual proceed</div>
                        <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">Resume</div>
                    </div>
                </div>
                {resumeDataList.map((resume, index) => {
                    let bgColor = "bg-gray-200";
                    if (index < 3) {
                        topThreeRef.current.push(resume.uniqueResumeId);
                        bgColor = "bg-blue-200"; 
                        bgColor = "bg-blue-200"; 
                    }
                    return (
                        <div key={resume.uniqueResumeId} className={`w-5/6 ${bgColor} rounded-md shadow-md shadow-black mb-[1rem] p-[0.5rem] items-center grid grid-cols-6`}>
                        <div key={resume.uniqueResumeId} className={`w-5/6 ${bgColor} rounded-md shadow-md shadow-black mb-[1rem] p-[0.5rem] items-center grid grid-cols-6`}>
                            <div className="pr-2">{resume.filename}</div>
                            <div className="pr-2">{resume.email}</div>
                            <div className="pr-2">{(resume.AiDetection)}%</div>
                            <div className="pr-2">{(resume.plagiarism)}</div>
                            <button className="bg-green-400 rounded-lg px-[1rem] py-[0.5rem] text-white hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-400 focus:ring-opacity-50" onClick={() => { handleProceedResumeSuitability(resume.uniqueResumeId); setLoading(!loading); }}> Proceed to Resume Suitability</button>
                            <button className="bg-red-700 rounded-lg px-[1rem] py-[0.5rem] text-white hover:bg-red-900 focus:outline-none focus:ring-2 focus:ring-red-700 focus:ring-opacity-50">View Resume</button>
                        </div>
                    );
                })}
                })}
            </div>
            <MoonLoader
                color="#B91C1C"  
                loading={loading}  
                size={150}  
                aria-label="Loading Spinner"  
                data-testid="loader"  
            />
            <MoonLoader
                color="#B91C1C"  
                loading={loading}  
                size={150}  
                aria-label="Loading Spinner"  
                data-testid="loader"  
            />
        </div>
    );
}

export default ApplicantDetailPage;