# HireSight
<p align="center">
  <img src="https://github.com/SHINE-six/HireSight/assets/91732305/fa354b16-5b01-492b-bd81-2e2e0914997e" alt="image" width="40%" />
</p>

HireSight is an artificial intelligence recruiting solution designed to improve the efficiency and accuracy of talent acquisition. The platform offers a comprehensive approach to the recruitment process, leveraging advanced technologies to streamline candidate selection.

## Matching Resumes:
HireSight begins by matching resumes against job requirements, using sophisticated algorithms to identify suitable candidates based on factors such as skills, experience, and educational background.

## Natural Language Processing (NLP) Analysis:
The platform utilizes natural language processing technology to delve deeper into the content of resumes. By analyzing the applicant's skills, experience, and qualifications, HireSight provides a detailed assessment of each candidate's suitability for the role.

## AI Content and Plagiarism Detection:
HireSight incorporates AI-generated content detection and plagiarism detection tools to further verify the accuracy and authenticity of candidate resumes. This ensures that only qualified and candidates with actual skillset can proceed to the next stage of the recruitment process.

## Interview Process:
The interview process consists of two rounds:

1. **AI Interview:** Candidates undergo an initial interview conducted by artificial intelligence. During this stage, the system analyzes the candidate's responses, utilizing techniques such as emotion recognition, body language analysis, and eye movement tracking to detect potential discrepancies or dishonesty.
<p align="center">
  <img src="https://github.com/SHINE-six/HireSight/assets/91732305/206f692f-946e-4d3f-b304-2caf33db5ffa" alt="AI Interview" width="30%" />
  <br/>
  <b>Figure: EVA - AI interview model</b>
</p>


2. **Technical Interview:** Successful candidates from the AI interview proceed to the final round, where they are interviewed by technical personnel to assess their proficiency in relevant skills and knowledge.

3. **Soft Skill Evaluation** Determine the candidates' softskill during interview shorten the time to evaluate talents actual skill and characteristic.

## Evaluation and Feedback:
Following the completion of the interview process, HireSight generates a comprehensive report based on all interview information. This report evaluates whether the candidate's abilities align with the job requirements and provides constructive feedback for candidates to improve their performance in future interviews.The report have several parts like overall performance, soft skill, technical skill, MBTI, overall performance and alternative job suggestions.
# System Architecture
<p align="center">
  <img src="https://github.com/SHINE-six/HireSight/assets/91732305/03800935-4da0-4021-a364-e00ba10256b5" alt="System Architecture" width="80%" />
</p>

# AI Recruitment System Models
The following models were trained as part of the AI Recruitment System:

1. **Resume Matching Similarity Algorithm Model**
   We will use a parse model to take down all the text from the resume and perform detection to ensure the authoritative of the resume owner.
2. **Resume Ranker Model**
   Resume Ranker will provide suitability calculation algorithm to provide suitability rank based on candidates' resume toward the job description.
3. **MBTI Personality Prediction Model**
   In our report we will have a section for the MBTI which we check from the performance of the interviewee as well as the work they sent to us. The MBTI test is a trend and it is an accurate personality model. It can let the candidate and company know the user behaviour for a better talents allocation.
4. **Facial Emotion Recognition Model**
   The is one of the main model in the AI interviewer where we will detect the facial emotion from the candidate to evaluate the performances of the user
5. **Eye Tracking Model**
   The eyes tracking model consist of left right eyeball movement tracking as well as blinking detection which is significant to know whether the user not focusing on the   
   interview window.
6. **Plagiarism Detection Model**
<p align="">
  <img src="https://github.com/SHINE-six/HireSight/assets/91732305/bdf3a1c8-2fb2-4379-b3de-eb072f735c69" alt="image" width="60%" />
</p>
<p align="">
  <img src="https://github.com/SHINE-six/HireSight/assets/91732305/2a89da7e-3563-4e60-a24b-5dd7116ef091" alt="image" width="60%" />
</p>
   The plagirism model will detect the similiar text that found from the website.
   
6. **AI text Detection Model**
<p align="">
  <img src="https://github.com/SHINE-six/HireSight/assets/91732305/c1a0f9c2-2a37-4e8b-95d7-4076c16f2ccc" alt="image" width="60%" />
</p>
<p align="">
  <img src="https://github.com/SHINE-six/HireSight/assets/91732305/09d02a52-481d-4946-b465-25fd43890292" alt="image" width="60%" />
</p>
For the extra information please look at this model that we run in on kaggle
https://www.kaggle.com/code/chenming777/ai-gen-preprocess/notebook
https://www.kaggle.com/code/chenming777/ai-gen-feature
https://www.kaggle.com/code/chenming777/ai-gen-train/notebook

7. **Interview Performance Assessment Model**
    This model will summarize all the model information and compile into two different version of reports like interviewee report and HR report
8. **Identifying Speech Disfluency Models**
    This model will detect the fluency of the model and help HR to evaluate the performance during the interview.
9. **LLM Conversation Model**
<p align="">
  <img src="https://github.com/SHINE-six/HireSight/assets/91732305/be798721-7072-42c2-bfda-05473d0d36ee" alt="image" width="60%" />
</p>
    We called gemini API for the LLM generation this will handle all the conversation during the EVA interviewer process
    
10. **AI Avatar**
    This is the AI avatar with the model and lip sync and text-to-speech and speech-to-text model with audio to make it more real and interactable.

# Impact and Future of AI in Recruitment

## Impact:

1. **Efficiency Improvement:** The integration of AI and NLP technology in recruitment processes significantly boosts efficiency by automating resume parsing, matching, and conducting AI interviews. This leads to quicker identification of suitable candidates, shortening the recruitment cycle, and reducing human resource costs.

2. **Standardization and Fairness:** By introducing standardized tools like AI interviews, subjective biases in traditional interviews are minimized. All candidates are evaluated against the same criteria, ensuring a fair and consistent hiring process.

3. **Enhanced Candidate Experience:** Automated tools, such as AI interviews and candidate experience surveys, improve the overall hiring experience. Candidates can complete interviews comfortably, and their feedback is promptly collected, making the process more humane and transparent.

4. **Authenticity and Adaptability Assurance:** AI content detection tools and plagiarism detectors ensure the authenticity of candidate information, enhancing the integrity and transparency of the recruitment process.

5. **Comprehensive Candidate Evaluation:** Employing various evaluation tools provides a more comprehensive understanding of candidates' abilities, qualities, and adaptability. This facilitates better candidate-job matching, reduces turnover, and enhances job satisfaction and performance levels.

6. **Personalized Feedback:** Automatically generated candidate and interviewer performance reports offer personalized feedback, increasing transparency and candidate satisfaction.

## Future:

1. **Human Interviews with AI Copilot and Analysis:**  AI assistants will become integral in conducting interviews, providing real-time analysis and feedback to assess candidates' skills and adaptability accurately.

2. **Customized Services:** AI systems will offer tailored services based on individual needs and backgrounds, ensuring fair treatment and enhancing workplace inclusivity.

3. **Onboard Chatbots:** Chatbots will assist new employees in familiarizing themselves with company policies and culture, accelerating their integration into the organization.

4. **Lockdown Browsers:** To maintain assessment accuracy and fairness, closed browsers will be employed for online testing and assessments, preventing candidates from accessing external resources during evaluations.

Overall, the integration of AI and automation technologies in recruitment processes not only streamlines operations but also fosters fairness, transparency, and inclusivity in the workplace, promising a more efficient and equitable future of recruitment.
