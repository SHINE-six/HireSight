'use client';

async function fetchResumeRanking() {
    const res = await fetch('https://chp1g6v4-8000.asse.devtunnels.ms/resume-ranking', { cache: "no-store" });
    const data = await res.json();
    console.log("request data done");
    return data;
}

const ApplicantDetailPage = async () => {
    const resumeRanking:any[] = await fetchResumeRanking();
    


    return (
        <div className="mt-[2rem] mx-[3rem]">
            <div className="flex flex-row items-center">
                <div className='w-[5rem] h-[5rem] rounded-full bg-white shadow-sm shadow-black flex justify-center'>
                    <img src="resume.svg" alt="resume" className='w-[3.5rem]'/>
                </div>
                <div className="py-[1rem] px-[4rem] text-2xl font-bold border-b-[0.1rem] border-gray-300">Resume AI Detection</div>
                <div className='w-[14rem] bg-white rounded-xl text-xl justify-between flex flex-row py-[0.5rem] px-[1rem] border-b-[0.1rem] border-gray-300 shadow-md font-semibold'>
                    <div>Applicant:</div> 
                    <div className='text-red-700'>98</div>
                </div>
            </div>
            <div className="mt-[2rem] mx-[1rem] flex flex-col items-center w-full">
                <div className="w-fit flex flex-row pl-[4rem] pr-[16rem] gap-[5rem]">
                    <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">Rank</div>
                    <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">id</div>
                    <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">Ai Likelihood Score</div>
                </div>
                {resumeRanking.map((resume) => {
                    return (
                        <div key={resume.id} className="w-3/5 bg-gray-200 rounded-md shadow-md shadow-black mb-[1rem] flex flex-row justify-around p-[0.5rem] items-center">
                            <div>{resume.rank}</div>
                            <div>{resume.id}</div>
                            <div>{resume.similarity.toFixed(3)}%</div>
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