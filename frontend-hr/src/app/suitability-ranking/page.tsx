'use client';

async function fetchResumeRanking() {
    const res = await fetch('http://localhost:8000/resume-ranking', { cache: "no-store" });
    const data = await res.json();
    console.log("request data done");
    return data;
}

const ApplicantDetailPage = async () => {
    const resumeRanking:any[] = await fetchResumeRanking();
    resumeRanking.sort((a, b) => {
        return new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime();
    });

    resumeRanking.sort((a, b) => {
        return a.id - b.id;
    });

    const displayedResumes = resumeRanking.slice(0, 33);
    


    return (
        <div className="mt-[2rem] mx-[3rem]">
            <div className="flex flex-row items-center">
                <div className='w-[5rem] h-[5rem] rounded-full bg-white shadow-sm shadow-black flex justify-center'>
                    <img src="resume.svg" alt="resume" className='w-[3.5rem]'/>
                </div>
                <div className="py-[1rem] px-[4rem] text-2xl font-bold border-b-[0.1rem] border-gray-300">Resume Suitabality</div>
                <div className='w-[14rem] bg-white rounded-xl text-xl justify-between flex flex-row py-[0.5rem] px-[1rem] border-b-[0.1rem] border-gray-300 shadow-md font-semibold'>
                    <div>Applicant:</div> 
                    <div className='text-red-700'>33</div>
                </div>
            </div>
            <div className="mt-[2rem] mx-[1rem] flex flex-col items-center w-full">
                <div className="w-fit flex flex-row pl-[4rem] pr-[16rem] gap-[5rem]">
                    <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">Rank</div>
                    <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">id</div>
                    <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">Suitability Score</div>
                    <div className="px-[1rem] py-[0.5rem] border-gray-500 border-b-[0.1rem] w-fit rounded-lg shadow-lg shadow-gray-500">Date</div>
                </div>
                {displayedResumes.map((resume) => {
                    const formattedTimestamp = new Date(resume.timestamp).toISOString().split('T')[0];
                    return (
                        <div key={resume.id} className="w-3/5 bg-gray-200 rounded-md shadow-md shadow-black mb-[1rem] flex flex-row justify-around p-[0.5rem] items-center">
                            <div>{resume.rank}</div>
                            <div>{resume.id}</div>
                            <div>{(resume.similarity * 100).toFixed(3)}%</div>
                            <div>{formattedTimestamp}</div>
                            <div className="bg-green-400 rounded-lg px-[1rem] py-[0.5rem] text-white">Proceed to interview</div>
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