'use client';


import { useEffect, useState, useRef } from 'react';
import { usePageConfigStore } from '@/stores/PageConfigStore';
import MoonLoader from 'react-spinners/MoonLoader';
import { useRouter } from 'next/navigation';
import { IoIosArrowBack } from "react-icons/io";

interface ReportData{
    "InterveweeName": string,
    "InterveweeID": string,
    "overallSuitability": number,
}


interface ReportDataFromServer {
    'data': ReportData[];
    'count': number;
}

interface ResumeData {
    'email': string;
    'uniqueResumeId': string;
    'jobPostitionApply': string;
    'stage': string;
}


interface ResumeDataFromServer {
    'data': ResumeData[];
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

const getResumeData = async (currentAvailableJob: string) => {
	try {
		const formData = new FormData();
		formData.append('jobTitle', currentAvailableJob);
        formData.append('stage', 'Interview ai')
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

const InterviewResultPage = () => {
    let [loading, setLoading] = useState(false);
    const { resumeCount, currentAvailableJob, setResumeCount_Interview_Ai } = usePageConfigStore();
    const [ ReportDataList, setReportDataList ] = useState<ReportData[]>([]);
    const [ ResumeDataList, setResumeDataList ] = useState<ResumeData[]>([]);
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
                console.log("asdsad", data.data) 
                if (data.data.length > 1) {
                    const sortedData = (data.data).sort((a, b) => a.overallSuitability - b.overallSuitability);
                    setReportDataList(sortedData);
                } else if (data.data.length === 1) {
                    setReportDataList(data.data); 
                }
                setResumeCount_Interview_Ai(data.count);

                const uniqueReportIds = data.data.map(item => item.InterveweeID);
                getResumeData(currentAvailableJob)?.then((resumeData) => {
                    if (resumeData && resumeData.data) {
                        const filteredResumeData = resumeData.data.filter(item => !uniqueReportIds.includes(item.uniqueResumeId));
                        setResumeDataList(filteredResumeData);
                        console.log(filteredResumeData);
                    }
                });
            }
        });
    }, [currentAvailableJob]);
    

    const handleProceedHrInterview = async (uniqueResumeId: string, email: string, stage: string) => {
        setLoading(true);
        console.log("Proceeding to HR Interviewing", uniqueResumeId);
        const formData = new FormData();
        formData.append('uniqueResumeId', uniqueResumeId);
        formData.append('stage', stage);
        const res = fetch('http://localhost:8000/updateStage',
            { 
                method: 'POST',
                body: formData
            });
        const data = await res;
        console.log(res);
        setLoading(false);
        sendEmail(email, stage);
        window.location.reload();
    }

    const sendEmail = (email: string, stage: string) => {
        const formData = new FormData();
        const offersubject = 'Congratulations! Invitation to HR Interview at Hilti'; 
        const rejectmessage = `
        Dear Teh Chen Ming,

        We sincerely appreciate the time and effort you've dedicated to the application process for the IT Business Analyst (Sustainability) position at Hilti. We recognize the competitive nature of the selection process and are grateful for your interest in joining our team.

        After thorough consideration, we regret to inform you that your application was not selected to proceed to the next stage. Please understand that we had to make difficult decisions among a pool of highly qualified candidates.

        While this outcome may be disappointing, we encourage you to continue pursuing opportunities that align with your skills and career aspirations. Your determination and perseverance will undoubtedly lead you to the right fit.

        Additionally, we value your feedback on our recruitment process. If you would like specific feedback on your application, please do not hesitate to reach out to us.

        We wish you all the best in your future endeavors and hope our paths may cross again in the future. Thank you for considering Hilti as a potential employer.

        Warm regards,

        Yi Kai
        HR Team
        Hilti`; 

        const rejectsubject = 'Application Update: IT Business Analyst (Sustainability) Position at Hilti'; 
        const offermessage = `
        Dear Teh Chen Ming,

        I trust this email finds you in good spirits.

        I am delighted to inform you that your application for the Business Analyst position at Hilti has successfully cleared the resume screening phase. Congratulations on reaching this milestone!

        Your qualifications and experience have left a positive impression on our team, and we believe you possess the potential to make significant contributions to our organization. As the next step in our recruitment process, we would like to extend an invitation for you to participate in an HR interview session.

        During the HR interview session, our aim is to gain a deeper understanding of your background, experiences, and motivations. We will explore how your skills and competencies align with the requirements of the role and assess your fit within our team culture.

        Please reply to this email with your availability for the HR interview, and we will coordinate a suitable date and time.

        Once again, congratulations on progressing to this stage of our selection process. We eagerly anticipate the opportunity to learn more about you during the HR interview session and wish you the very best of luck!

        Warm regards,

        Yi Kai
        HR Team
        Hilti`;
        formData.append('email_receiver', email);

        if (stage === "offered") {
            formData.append('message', offermessage);
            formData.append('subject', offersubject);
        } else {
            formData.append('message', rejectmessage);
            formData.append('subject', rejectsubject);
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
                    <div className="flex w-full justify-center">
                        <div className="flex w-full justify-between">
                            <div className="mt-[2rem] mx-[1rem] flex flex-col items-center w-1/3">
                                <div className="flex justify-center w-full p-[0.5rem] mb-[1rem]">
                                    <div className="grid grid-cols-2 w-full">
                                        <div className="px-[1rem] py-[0.5rem] justify-self-center border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">Interviewee ID</div>
                                        <div className="px-[1rem] py-[0.5rem] justify-self-center border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">Email</div>
                                    </div>
                                </div>
                                {ResumeDataList.map((resume, index) => {
                                    return (
                                        <div key={resume.uniqueResumeId} className={`bg-gray-200 w-full rounded-md shadow-md shadow-black mb-[1rem] py-[1.4rem] items-center grid grid-cols-2`}>
                                            <div className="justify-self-center">{resume.uniqueResumeId}</div>
                                            <div className="justify-self-center">{resume.email}</div>
                                        </div>
                                    );
                                })}
                            </div>

                            <div className="mt-[2rem] mx-[1rem] flex flex-col items-center w-2/3 ">
                                <div className="flex justify-center w-5/6 p-[0.5rem] mb-[1rem]">
                                    <div className=" grid grid-cols-6 w-full justify-items-center">
                                        <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">Interviewee ID</div>
                                        <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">Email</div>
                                        <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">Overall Suitability</div>
                                        <div className="px-[1rem] py-[0.5rem] col-span-2 border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">Manual proceed</div>
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
                                        <div className='mx-[2rem]'>
                                            <div key={resume.InterveweeID} className={`w-full ${bgColor} rounded-md shadow-md text- smdhadow-black mb-[1rem] p-[1rem] justify-items-center items-center grid grid-cols-6`}>
                                                <div className="pr-2">{resume.InterveweeID}</div>
                                                <div className="pr-2">{resume.InterveweeName}</div>
                                                <div className="pr-2">{(resume.overallSuitability)}%</div>
                                                <div className="grid grid-cols-2 gap-[1rem] items-center col-span-2">
                                                    <button className="bg-green-400 rounded-lg px-[1rem] py-[0.5rem] h-full text-white hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-400" onClick={() => { handleProceedHrInterview(resume.InterveweeID, resume.InterveweeName,"Interview hr"); setLoading(!loading); }}> Proceed to Hr Interview</button>
                                                    <button className="bg-red-700 rounded-lg px-[1rem] py-[0.5rem] h-full text-white hover:bg-red-900 focus:outline-none focus:ring-2 focus:ring-red-700" onClick={() => { handleProceedHrInterview(resume.InterveweeID, resume.InterveweeName,"rejected"); setLoading(!loading); }}> Rejected</button>
                                                </div>
                                                <button className="bg-blue-700 rounded-lg px-[1rem] py-[0.5rem] h-full text-white hover:bg-blue-900 focus:outline-none focus:ring-2">View Report</button>
                                            </div>
                                        </div>
                                    );
                                })}
                            </div>
                        </div>
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