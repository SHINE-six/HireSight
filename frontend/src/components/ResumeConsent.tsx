import React, { useState } from 'react';

const ConsentPopUp = () => {
    const [showConsent, setShowConsent] = useState(true);
    
    if (!showConsent) return null;

    return (
        <div className='fixed top-0 left-0 w-full h-full bg-black bg-opacity-50 flex justify-center items-center z-40'>
            <div className='bg-white p-[2rem] rounded-lg shadow-lg w-4/5 h-4/5 overflow-auto'>
                <div className='text-2xl font-bold text-red-700 mb-4'>Consent</div>
                <div className='mt-[1rem] text-lg'>
                    <p className='mb-4'>Thank you for your interest in the Business Analyst position at Hilti. We use HireSight, an advanced AI-powered recruitment platform, to ensure a fair and efficient hiring process. Please review the following details about how AI will be used in the initial stage of your evaluation:</p>
                    
                    <h2 className='font-bold mb-2'>Purpose of AI in Resume Screening:</h2>
                    <ul className='list-disc list-inside mb-4'>
                        <li>Automated Resume-Job Matching: AI matches your resume with job descriptions to identify the best fit.</li>
                        <li>Information Verification: AI verifies the authenticity of your resume.</li>
                    </ul>

                    <h2 className='font-bold mb-2'>Data Collection and Usage:</h2>
                    <ul className='list-disc list-inside mb-4'>
                        <li>Resume Data (including Personal Information): Information provided in your resume.</li>
                    </ul>

                    <h2 className='font-bold mb-2'>Privacy and Security:</h2>
                    <p className='mb-4'>We are committed to protecting your privacy and ensuring the security of your personal data. All data collected will be used solely for recruitment purposes and stored securely in compliance with relevant data protection regulations, such as GDPR.</p>

                    <h2 className='font-bold mb-2'>Consent:</h2>
                    <p className='mb-4'>By proceeding with your application, you consent to the use of AI in the resume screening process as described above. If you have any concerns or wish to discuss this further, please contact us at hr@hilti.com.</p>

                    <p className='mb-4'>Note: Once you pass the screening process, the interview section will be conducted by AI.</p>

                    <p className='mb-4'>By clicking 'I agree', you agree to the collection and processing of your personal data for the purpose of this application. You also agree on the interaction with an Artificial Intelligent digital model name 'Eva' for the purpose of this application.</p>
                </div>
                <div className='mt-[1rem] flex justify-between'>
                    <button className='bg-red-700 text-white p-[0.5rem] rounded-md' onClick={() => setShowConsent(false)}>I Agree</button>
                    <button className='bg-gray-200 p-[0.5rem] rounded-md'>I Disagree</button>
                </div>
            </div>
        </div>
    )
}
export default ConsentPopUp;