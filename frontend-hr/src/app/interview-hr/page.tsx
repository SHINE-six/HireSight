'use client';


import { useEffect, useState, useRef } from 'react';
import { usePageConfigStore } from '@/stores/PageConfigStore';
import MoonLoader from 'react-spinners/MoonLoader';
import { useRouter } from 'next/navigation';
import { IoIosArrowBack } from "react-icons/io";

interface ReportData{
    "email": string,
    "uniqueResumeId": string,
}


interface ReportDataFromServer {
    'data': ReportData[];
    'count': number;
}

const getReportData = async (currentAvailableJob: string) => {
	try {
		const formData = new FormData();
		formData.append('jobTitle', currentAvailableJob);
        formData.append('stage', 'Interview hr')
		const res = await fetch('http://localhost:8000/resumeRanking',
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
                // if (data.data.length > 1) {
                //     const sortedData = (data.data).sort((a, b) => a.overallSuitability - b.overallSuitability);
                //     setReportDataList(sortedData);
                // } else if (data.data.length === 1) {
                    setReportDataList(data.data); 
                // }
                setResumeCount_Interview_Ai(data.count);
            }
        });
	}, [currentAvailableJob]);
    

    const handleProceedHr = (uniqueResumeId: string, email: string, status: string) => {
        setLoading(true);
        console.log("Proceeding to HR Interviewing", uniqueResumeId);
        const formData = new FormData();
        formData.append('uniqueResumeId', uniqueResumeId);
        formData.append('stage', status);
        const res = fetch('http://localhost:8000/updateStage',
            { 
                method: 'POST',
                body: formData
            });
        setLoading(false);
        window.location.reload();
        sendEmail(email, status);
    }

    const sendEmail = (email: string, status: string) => {
        const formData = new FormData();
        const subject = 'Opportunity at Hilti'; 
        const offermessage = `Dear Teh Chen Ming,

        Offer
        
        Yi Kai
        HR Team
        Hilti`;

        const rejectmessage = `Dear Teh Chen Ming,
        Rejected
        
        Yi Kai
        HR Team
        Hilti`;
        formData.append('email_receiver', email);
        formData.append('subject', subject);

        if (status === "offered") {
            formData.append('message', offermessage);
        } else {
            formData.append('message', rejectmessage);
        }

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
                    <img src="hr_interview.svg" alt="resume" className='w-[3.5rem]'/>
                </div>
                <div className="py-[1rem] px-[4rem] text-2xl font-bold border-b-[0.1rem] border-gray-300">Hr Interviewing</div>
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
                        <div className=" grid grid-cols-3 w-4/5">
                            <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">Interviewee ID</div>
                            <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">Email</div>
                            <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">Final Decision</div>
                        </div>
                    </div>
                    {ReportDataList.map((resume, index) => {
                        let bgColor = "bg-gray-200";
                        if (index < 3) {
                            topThreeRef.current.push(resume.uniqueResumeId);
                            bgColor = "bg-blue-200"; // Change this to the color you want for the first 3 items
                        }
                        return (
                            <div key={resume.uniqueResumeId} className={`w-4/5 ${bgColor} rounded-md shadow-md shadow-black mb-[1rem] p-[0.5rem] items-center grid grid-cols-4`}>
                                <div className="pr-2">{resume.uniqueResumeId}</div>
                                <div className="pr-2">{resume.email}</div>
                                <button className="bg-green-400 rounded-lg px-[1rem] py-[0.5rem] text-white hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-400 focus:ring-opacity-50" onClick={() => { handleProceedHr(resume.uniqueResumeId, resume.email, "offered"); setLoading(!loading); }}> Offered</button>
                                <button className="bg-red-700 rounded-lg px-[1rem] py-[0.5rem] text-white hover:bg-red-900 focus:outline-none focus:ring-2 focus:ring-red-700 focus:ring-opacity-50" onClick={() => { handleProceedHr(resume.uniqueResumeId, resume.email, "rejected"); setLoading(!loading); }}>Rejected</button>
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