'use client';


import { useEffect, useState, useRef } from 'react';
import { usePageConfigStore } from '@/stores/PageConfigStore';
import MoonLoader from 'react-spinners/MoonLoader';
import { useRouter } from 'next/navigation';
import { IoIosArrowBack } from "react-icons/io";

interface ReportData{
    "uniqueSessionID": string,
    "InterveweeName": string,
    "InterveweeID": string,
    "overallSuitability": number,
}


interface ReportDataFromServer {
    'data': ReportData[];
    'count': number;
}

const getReportData = async (currentAvailableJob: string) => {
	try {
		const formData = new FormData();
		formData.append('jobTitle', currentAvailableJob);
        formData.append('stage', 'Interview ai')
		const res = await fetch('http://localhost:8000/interviewRanking',
			{ 
				method: 'POST',
				body: formData
			});
		const data:ReportDataFromServer = await res.json();
		console.log("request data done");
		console.log(currentAvailableJob, data);
		return data;
	} catch (error) {
		console.error('Error fetching data:', error);
	}
}


const InterviewResultPage = () => {
    let [loading, setLoading] = useState(false);
    const { resumeCount, currentAvailableJob, setResumeCount_Interview_Ai } = usePageConfigStore();
    const [ ReportDataList, setReportDataList ] = useState<ReportData[]>([]);
    const topThreeRef = useRef<string[]>([]);
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
		getReportData(currentAvailableJob)?.then((data) => {
            if (data && data.data) {
                if (data.data.length > 1) {
                    const sortedData = (data.data).sort((a, b) => a.overallSuitability - b.overallSuitability);
                    setReportDataList(sortedData);
                } else if (data.data.length === 1) {
                    setReportDataList(data.data); 
                }
                setResumeCount_Interview_Ai(data.count);
            }
        });
	}, [currentAvailableJob]);
    

    const handleProceedHrInterview = async (uniqueResumeId: string) => {
        setLoading(true);
        console.log("Proceeding to HR Interviewing", uniqueResumeId);
        const formData = new FormData();
        formData.append('uniqueResumeId', uniqueResumeId);
        formData.append('stage', 'Interview hr');
        const res = fetch('http://localhost:8000/updateStage',
            { 
                method: 'POST',
                body: formData
            });
        const data = await res;
        console.log('Email sent successfully:', res);
        setLoading(false);
        // window.location.reload();
    }

    const sendEmail = (email: string) => {
        const formData = new FormData();
        const subject = 'Opportunity at Hilti'; 
        const message = `Dear Teh Chen Ming,

        I trust this email finds you in good spirits.
        
        I am delighted to inform you that your application for the Business Analyst position at Hilti has successfully cleared the resume screening phase. Congratulations on reaching this milestone!
        
        Your qualifications and experience have left a positive impression on our team, and we believe you possess the potential to make significant contributions to our organization. As the next step in our recruitment process, we would like to extend an invitation for you to participate in an HR interview session.
        
        The HR interview session aims to evaluate your skills, competencies, and suitability for the role in an engaging and interactive manner. It will provide you with the opportunity to demonstrate your expertise in business analysis, problem-solving capabilities, and communication skills.
        
        We encourage you to prepare thoroughly for the interview by revisiting your knowledge of business analysis principles, methodologies, and drawing upon relevant experiences. Should you have any inquiries or require additional information ahead of the interview, please don't hesitate to reach out to us.
        
        Your HR interview session can be started any time you want. Please follow this link to our HR interviewer platform when you are fully prepared, http://localhost:3000/ai-interview
        
        Once again, congratulations on progressing to this stage of our selection process. We eagerly anticipate the opportunity to learn more about you during the HR interview session and wish you the very best of luck!
        
        Your feedback is absolutely valuable for us. Please take a moment to share your thoughts through our feedback link, https://HireSight/Feedback
        
        Warm regards,
        
        Yi Kai
        HR Team
        Hilti`;
        formData.append('email_receiver', email);
        formData.append('subject', subject);
        formData.append('message', message);
        const res = fetch('http://localhost:8000/send_email', 
            {
                method: 'POST',
                body: formData
            });
        console.log('Email sent successfully:', res);
    }    

    const handleBack = () => {
        // if (window.history.length > 1) {
            router.back();
        // } else {
        //     router.push('/');
        // }
    }

    return (
        <div className="mt-[2rem] mx-[3rem] sweet-loading">
            <div className="flex flex-row items-center">
                <div className='w-[5rem] h-[5rem] rounded-full bg-white shadow-sm shadow-black flex justify-center'>
                    <img src="interview.svg" alt="resume" className='w-[3.5rem]'/>
                </div>
                <div className="py-[1rem] px-[4rem] text-2xl font-bold border-b-[0.1rem] border-gray-300">Ai Interviewing</div>
                <div className='w-[14rem] bg-white rounded-xl text-xl justify-between flex flex-row py-[0.5rem] px-[1rem] border-b-[0.1rem] border-gray-300 shadow-md font-semibold'>
                    <div>Applicant:</div> 
                    <div className='text-red-700'>{resumeCount['Interview_ai']}</div>
                </div>
                <button onClick={handleBack} className="fixed right-0 mr-[210px] ml-4 text-2xl text-black font-bold py-2 px-4 rounded"><IoIosArrowBack /></button>
            </div>
            <div className="mt-[2rem] mx-[1rem] flex flex-col items-center w-full">
                {!loading && (
                <div className="mt-[2rem] mx-[1rem] flex flex-col items-center w-full">
                <div className="flex justify-center w-full p-[0.5rem] mb-[1rem]">
                        <div className=" grid grid-cols-5 w-4/5">
                            <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">Interviewee ID</div>
                            <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">Email</div>
                            <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">Overall Suitability</div>
                            <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">Manual proceed</div>
                            <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">View Report</div>
                        </div>
                    </div>
                    {ReportDataList.map((resume, index) => {
                        let bgColor = "bg-gray-200";
                        if (index < 3) {
                            topThreeRef.current.push(resume.InterveweeID);
                            bgColor = "bg-blue-200"; // Change this to the color you want for the first 3 items
                        }
                        return (
                            <div key={resume.uniqueSessionID} className={`w-4/5 ${bgColor} rounded-md shadow-md shadow-black mb-[1rem] p-[0.5rem] items-center grid grid-cols-5`}>
                                <div className="pr-2">{resume.InterveweeID}</div>
                                <div className="pr-2">{resume.InterveweeName}</div>
                                <div className="pr-2">{(resume.overallSuitability)}%</div>
                                <button className="bg-green-400 rounded-lg px-[1rem] py-[0.5rem] text-white hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-400 focus:ring-opacity-50" onClick={() => { handleProceedHrInterview(resume.InterveweeID); sendEmail(resume.InterveweeName); setLoading(!loading); }}> Proceed to Hr Interviewing</button>
                                <button className="bg-red-700 rounded-lg px-[1rem] py-[0.5rem] text-white hover:bg-red-900 focus:outline-none focus:ring-2 focus:ring-red-700 focus:ring-opacity-50">View Report</button>
                            </div>
                        );
                        })}
                    </div>
                    )}
            </div>
            <div className='flex justify-center items-center text-center'>
            <MoonLoader
                color="#B91C1C"  
                loading={loading}  
                size={150}  
                aria-label="Loading Spinner"  
                data-testid="loader"  
            />
            </div>
        </div>
    );
}

export default InterviewResultPage;