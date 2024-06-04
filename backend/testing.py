# import plagiarism

# text = """ETL is a critical process for data integration and analytics. Some common use cases include: - Data warehousing: ETL pipelines are used to extract data from source systems such as databases, files and APIs, transform the data into a consistent format and then load it into a data warehouse. - Business intelligence: ETL is used to populate data marts and data warehouses used by BI tools. - Data migration: ETL is often used during data migrations when an organization needs to transition from one system to another. - Data integration: ETL makes possible the seamless integration of data from different sources. - Data cleansing and enrichment: ETL pipelines are also used to clean and standardize data. They also enrich data by incorporating missing information. - Batch processing: ETL jobs often run at scheduled intervals and process large amounts of data, ensuring that the data warehouse remains updated. - Data governance and compliance: ETL is a critical tool for the enforcement of data governance policies. Data can be encrypted during the transformation process to comply with data laws. - Real-time ETL: While traditional ETL is mostly done on schedule intervals (batches), real-time ETL is now used for scenarios that require instant updates, such as stock market updates. - Cloud data pipelines: ETL tools are used in cloud environments to facilitate the movement of data between cloud platforms and on-premises storage."""

# result = plagiarism.main(text)

# print(result)


# import radarChart as r

# r.main(1,2,3,4,6,5)

# print(r)

# import mbti_last as m

transcript ="""
EVA: Hello Teh Chen Ming, welcome to the interview session! I am EVA, your AI interviewer. Today, you are interviewing for the IT Business Analyst (Sustainability) position at Hilti. In this role, you will work closely with the IT Product Owner and Global Sustainability Business Teams primarily supporting SAP S/4HANA and SAP Business ByDesign. To start, could you please introduce yourself and give us a brief overview of your background?  

 

Me: Hello EVA, You can call me Chen Ming and I recently graduated from APU with a bachelor’s degree in computer science specialism in data analyst . During my studies, I worked on projects that integrated sustainable concept into our IT systems, gaining hands-on experience with SAP modules and understanding the importance of compliance and reporting. 

 

Eva: Thank you for your introduction, Chen Ming. It's great to hear about your background and experiences. Could you please share with us what you consider to be your greatest strength and your biggest weakness? 

 

Me: I believe my greatest strength is my ability to quickly adapt and learn new technologies. For example, during my internship at GreenTech Solutions, I successfully learned and implemented SAP modules within 4 months, which significantly contributed to our sustainability projects. On the other hand, my biggest weakness is time management. I sometimes find myself weak in making documentation and this cause problem to my colleague to follow up my task. So, I'm working on improving this to ease my further colleague to catch up my work and progress 

 

Eva: Thank you for sharing that, Chen Ming. Now, could you please tell us why you think you are a good fit for Hilti's company culture? 

 

Me: I believe I'm a great fit for Hilti's company culture because I'm really motivated by innovation and sustainability, which I know are important at Hilti. I love working in collaborative environments and enjoy being part of a team to create impactful solutions. Plus, I'm committed to continuous learning and personal development, and I really appreciate how Hilti supports growing lasting careers and encourages individual growth. 

 

Eva: Thank you for sharing that, Chen Ming. I'm clear on your background now, and it sounds impressive. Let's move on to some technical questions. How would you approach implementing a sustainability-focused module like the Sustainability Control Tower in these ERP systems to ensure compliance and accurate reporting? 

 

 

Me: To implement a sustainability-focused module like the Sustainability Control Tower, I would start by gathering requirements from stakeholders to understand the specific compliance and reporting needs. Next, I would configure the SAP systems to capture the necessary sustainability data, ensuring that all relevant fields and integration points are set up correctly. Finally, I would focus on accurate data integration from various sources to ensure comprehensive and reliable reporting, aligning with compliance standards. 

 

Eva: That is impression now another question for you. How would you ensure data integrity and security when implementing sustainability modules in SAP S/4HANA and SAP Business ByDesign? 

 

Me: Can you repeat it into a simpler way?  

 

Eva: Sure, How do you make sure information stays safe when adding sustainability features to SAP S/4HANA and SAP Business ByDesign? 

 

Me: Firstly, I will restrict access to sensitive sustainability data, ensuring that only authorized personnel can view or modify it. Additionally, I would implement encryption protocols and secure communication channels to protect data in transit and at rest. Regular monitoring and auditing of system activities would also be conducted to detect and prevent any unauthorized access or data breaches.  

 

Eva: I think you have covered everything I wanted to know; Do you have any questions for us? 

Me: May I know what is the expected salary for this position? 

 

Eva: The salary varies based on your background, skillset, and experience. We determine it later in the process to ensure it aligns with company standards and your expectations. We aim to offer competitive compensation packages. Is there any other questions about the position? 

 

Me: Yes, I would like to know what the next steps in the hiring process are. 

  

Eva Great question. After today's interview, we will review all candidates and make our decisions. You can expect to receive an email regarding your qualification status within the next three days.  Any other questions for us? 

 

Me: Nope I’m clear with all 

 

Eva: Thank you for your time and interest in the position. Have a great day!" 
"""

# result = m.main(transcript)

# print(result)

import LLM_report as l

result = l.main(transcript, 'INTP')

print(result)