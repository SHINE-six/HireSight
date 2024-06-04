'use client';


import { useEffect, useState, useRef } from 'react';
import { usePageConfigStore } from '@/stores/PageConfigStore';
import MoonLoader from 'react-spinners/MoonLoader';
import { useRouter } from 'next/navigation';
import { IoIosArrowBack } from "react-icons/io";

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
        formData.append('stage', 'Resume Suitability')
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


const SuitabilityRankingPage = () => {
    let [loading, setLoading] = useState(false);
    const { resumeCount, currentAvailableJob, setResumeCount_Resume_suitability } = usePageConfigStore();
    const [ resumeDataList, setResumeDataList ] = useState<ResumeData[]>([]);
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
		getResumeData(currentAvailableJob)?.then((data) => {
            if (data && data.data) {
                if (data.data.length > 1) {
                    const sortedData = data.data.sort((a, b) => a.suitability - b.suitability);
                    setResumeDataList(sortedData);
                } else if (data.data.length === 1) {
                    setResumeDataList(data.data); 
                }
                setResumeCount_Resume_suitability(data.count);
            }
        });
	}, [currentAvailableJob]);

    // const handleEndStage = () => {
    //     setLoading(true);
    //     console.log("End Stage");
    //     // top three applicants stage will change to 'Interview'
    //     const formData = new FormData();
    //     formData.append('uniqueResumeId', topThreeRef.current.join(','));
    //     formData.append('stage', 'Interview');
    //     const res = fetch('http://localhost:8000/updateStage',
    //         { 
    //             method: 'POST',
    //             body: formData
    //         });
    //     console.log(res);
    //     setLoading(false);
    //     window.location.reload();
    // }

    const handleProceedAiInterview = (uniqueResumeId: string, email: string) => {
        setLoading(true);
        console.log("Proceeding to Ai Interviewing", uniqueResumeId);
        const formData = new FormData();
        formData.append('uniqueResumeId', uniqueResumeId);
        formData.append('stage', 'Interview ai');
        const res = fetch('http://localhost:8000/updateStage',
            { 
                method: 'POST',
                body: formData
            });
        console.log(res);
        setLoading(false);
        sendEmail(email)
        window.location.reload();
    }

    const sendEmail = (email: string) => {
        const formData = new FormData();
        const subject = 'Invitation for IT Business Analyst (Sustainability) Interview at Hilti'; 
        const message = `
        Dear Teh Chen Ming,
        
        We're excited to inform you that your application for the IT Business Analyst (Sustainability) position at Hilti has impressed our team! Your qualifications and potential for contributing to our sustainability efforts are promising.
        
        As the next step, we'd like to offer you two options for your interview:
        
        AI Interview: This engaging and interactive session allows you to showcase your skills and problem-solving abilities at your own convenience. It evaluates your suitability for the role through a series of questions related to business analysis and communication.
        
        HR Interview: If you prefer a more traditional format, you can choose a live interview with a member of our HR team. This allows for a direct conversation about your experience and goals.
        
        To help you decide:

        AI Interview: This option provides flexibility and allows you to complete it at your own pace.
        
        HR Interview: This option offers a chance to directly interact with the HR team and ask questions.

        Ready to proceed?
        AI Interview: Click this link to access the platform whenever you're prepared: https://locall.host/3000/

        HR Interview: Schedule your interview at your convenience through this link: https://hr-interview.

        We look forward to learning more about you through your chosen interview format. Congratulations on reaching this stage, and best of luck!
        
        
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
        console.log('Interview Email sent successfully:', res);
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
                    <img src="resume.svg" alt="resume" className='w-[3.5rem]'/>
                </div>
                <div className="py-[1rem] px-[4rem] text-2xl font-bold border-b-[0.1rem] border-gray-300">Resume Suitability</div>
                <div className='w-[14rem] bg-white rounded-xl text-xl justify-between flex flex-row py-[0.5rem] px-[1rem] border-b-[0.1rem] border-gray-300 shadow-md font-semibold'>
                    <div>Applicant:</div> 
                    <div className='text-red-700'>{resumeCount['Resume_suitability']}</div>
                </div>
                {/* <button onClick={() => { handleEndStage(); setLoading(!loading); }} className="ml-4 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">End Stage</button> */}
                <button onClick={handleBack} className="fixed right-0 mr-[210px] ml-4 text-2xl text-black font-bold py-2 px-4 rounded"><IoIosArrowBack /></button>
            </div>
            <div className="mt-[2rem] mx-[1rem] flex flex-col items-center w-full">
                {!loading && (
                <div className="mt-[2rem] mx-[1rem] flex flex-col items-center w-full">
                    <div className="flex justify-center w-full p-[0.5rem] mb-[1rem]">
                        <div className=" grid grid-cols-5 w-4/5">
                            <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">Resume ID</div>
                            <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">Email</div>
                            <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">Resume Suitability</div>
                            <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">Manual proceed</div>
                            <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">Resume</div>
                        </div>
                    </div>
                    {resumeDataList.map((resume, index) => {
                        let bgColor = "bg-gray-200";
                        if (index < 3) {
                            topThreeRef.current.push(resume.uniqueResumeId);
                            bgColor = "bg-blue-200"; // Change this to the color you want for the first 3 items
                        }
                        return (
                            <div key={resume.uniqueResumeId} className={`w-4/5 ${bgColor} rounded-md shadow-md shadow-black mb-[1rem] p-[0.5rem] items-center grid grid-cols-5`}>
                                <div className="pr-2">{resume.uniqueResumeId}</div>
                                <div className="pr-2">{resume.email}</div>
                                <div className="pr-2">{(resume.suitability* 100).toFixed(2)}%</div> 
                                <button className="bg-green-400 rounded-lg px-[1rem] py-[0.5rem] text-white hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-400 focus:ring-opacity-50" onClick={() => { handleProceedAiInterview(resume.uniqueResumeId, resume.email);}}> Proceed to Ai Interviewing</button>
                                <button className="bg-red-700 rounded-lg px-[1rem] py-[0.5rem] text-white hover:bg-red-900 focus:outline-none focus:ring-2 focus:ring-red-700 focus:ring-opacity-50">View Resume</button>
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

export default SuitabilityRankingPage;