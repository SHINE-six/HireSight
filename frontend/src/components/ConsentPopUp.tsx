import React from 'react';

const ConsentPopUp = ({handleConsent}: {handleConsent: () => void}) => {

    return (
        <div className='fixed top-0 left-0 w-full h-full bg-black bg-opacity-50 flex justify-center items-center z-40'>
            <div className='bg-white p-[2rem] rounded-lg shadow-lg w-4/5 overflow-auto h-4/5'>
                <div className='text-2xl font-bold text-red-700 mb-4'>Consent</div>
                <div className='mt-[1rem] text-lg'>
                    <h2 className='font-bold mb-2'>Informed Consent for AI Use in Interview</h2>
                    <p className='mb-4'>Congratulations on passing the initial screening process! The next step in our recruitment process involves an AI-conducted interview. Please review the following details about how AI will be used in this stage of your evaluation:</p>

                    <h2 className='font-bold mb-2'>Purpose of AI in Interview:</h2>
                    <ul className='list-disc list-inside mb-4'>
                        <li>AI-Conducted Interviews: Initial interviews are conducted by an AI interviewer to ensure consistency and reduce biases.</li>
                        <li>Performance Analysis: AI evaluates your responses, facial expressions, and soft skills during interviews.</li>
                        <li>Information Verification: AI verifies the authenticity of your interview responses.</li>
                    </ul>

                    <h2 className='font-bold mb-2'>Data Collection and Usage:</h2>
                    <ul className='list-disc list-inside mb-4'>
                        <li>Interview Responses: Your answers and performance during AI-conducted interviews.</li>
                        <li>Behavioral Data: Includes facial expressions, speech patterns, and other behavioral indicators.</li>
                        <li>Audio and Video: Your audio and video will be captured for behavioral analysis and performance evaluation. The video will be used for emotional and eye tracking, while the audio will be converted to text for MBTI prediction, skills assessment, and content authenticity checks.</li>
                    </ul>

                    <h2 className='font-bold mb-2'>Privacy and Security:</h2>
                    <p className='mb-4'>We are committed to protecting your privacy and ensuring the security of your personal data. All data collected will be used solely for recruitment purposes and stored securely in compliance with relevant data protection regulations, such as GDPR.</p>

                    <h2 className='font-bold mb-2'>Transparency and Accountability:</h2>
                    <p className='mb-4'>You will have access to a summary of your performance analysis, including insights into your strengths and areas for improvement. Should you have any questions or require clarification regarding the AI's assessment, our HR team is available to provide further information.</p>

                    <h2 className='font-bold mb-2'>Candidate Rights and Human Oversight:</h2>
                    <p className='mb-4'>While AI plays a significant role in our recruitment process, final hiring decisions will involve human oversight to ensure fairness and accuracy. You have the right to request a human review of any AI-generated decision and to appeal if you believe there has been an error or bias.</p>

                    <h2 className='font-bold mb-2'>Consent:</h2>
                    <p className='mb-4'>By proceeding with your AI interview, you consent to the use of AI in the interview process as described above. If you have any concerns or wish to discuss this further, please contact us at hr@hilti.com.</p>
                    <p className='mb-4'>By clicking 'I agree', you agree to the collection and processing of your personal data for the purpose of this application. You also agree on the interaction with an Artificial Intelligent digital model name 'Eva' for the purpose of this application.</p>
                </div>
                <div className='mt-[1rem] flex justify-between'>
                    <button className='bg-red-700 text-white p-[0.5rem] rounded-md' onClick={() => handleConsent()}>I Agree</button>
                    <button className='bg-gray-200 p-[0.5rem] rounded-md'>I Disagree</button>
                </div>
            </div>
        </div>
    )
}
export default ConsentPopUp;