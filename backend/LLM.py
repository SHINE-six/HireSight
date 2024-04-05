# import json


# # with open('LLM_sample.json', 'r') as response_file:
# #     response = json.load(response_file)
# #     response_file.close()
# #     print(response)

# # response_file = open('LLM_sample.json', 'r')
# # response = json.load(response_file)
# response = {
#     "Response": [
#         {
#             "Type": "Introduction",
#             "Questions":[
#                 "Hello and welcome to WPH Digital! Thank you for joining us today for the interview for the position of Scrum Master. I'm the AI interviewer, and I'll be guiding you through this session. Before we begin, I'd like to introduce WPH Digital and explain a bit about what to expect. We're a multidisciplinary IT consulting company specializing in digital transformation, technology implementation, AI, data analytics, cybersecurity, and cloud computing. We work closely with clients to drive growth opportunities and cost optimization through innovative solutions. Now, let's proceed with the interview process. I'll be asking you a series of questions to understand your suitability for the role of a Scrum Master."
#             ]
#         },
#         {
#             "Type": "General HR Analyst Interview Questions",
#             "Questions": [
#                 "To kick things off, can you tell me a bit about yourself and what motivated you to apply for the position of Scrum Master at WPH Digital?",
#                 "What do you consider to be your greatest strengths and weaknesses, and how do you think they will influence your performance as a Scrum Master within our dynamic and multidisciplinary environment?",
#                 "How do you handle conflicts within a team, and can you provide an example of a situation where you successfully resolved a conflict in a previous role, particularly within the context of a technology-driven environment?",
#                 "How do you stay organized and prioritize tasks in a fast-paced environment like that of a Scrum team, especially considering the diverse range of services and expertise offered by WPH Digital?",
#                 "Let's begin with getting to know you better. Could you tell us more about yourself and your background?",
#                 "From your perspective, what do you believe are the most necessary skills and characteristics for someone in the role of a Scrum Master?",
#                 "Maintaining a healthy work-life balance is crucial. How do you ensure you practice good work-life balance, especially in a demanding role like that of a Scrum Master?",
#                 "What specifically attracted you to apply for a position with our organization, WPH Digital?",
#                 "Reflecting on your experiences, what would you consider to be your biggest workplace strengths?",
#                 "Would you prefer working as part of a large team, a small group, or independently? And could you explain why?",
#                 "Could you share your career goals with us? How do you envision an organization like ours supporting your long-term plans?",
#                 "What motivated you to build a career in WPH, and how do you believe your background aligns with the role of a Scrum Master in our multidisciplinary company?",
#                 "Organization is key in any role. How do you maintain your organization at work to ensure tasks and projects are completed on time?"
#             ]
#         }
#     ]
# }
# Type_counter = 0
# counter = 0

# def main():
#     global Type_counter
#     global counter
#     try:
#         if Type_counter < len(response["Response"]):
#             Type_counter += 1
#             if counter < len(response["Response"][Type_counter-1]['Questions']):
#                 counter += 1
#                 return {"type": response["Response"][Type_counter-1]['Type'], "response": response["Response"][Type_counter-1]['Questions'][counter - 1]}
#             counter = 0
#             return response["Response"][Type_counter - 1]['Type']
#         else:
#             return "No more questions"
#     except:
#         return "Error"

