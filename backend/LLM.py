import google.generativeai as genai
import re
import os
 
# Configure the SDK with your API key by recovering the API key from a config file
GENAI_API_KEY = os.getenv('GENAI_API_KEY')
genai.configure(api_key= GENAI_API_KEY)

#Setting the Gen AI model to be used (one of- gemini-1.0-pro, gemini-1.0-pro-001,gemini-1.0-pro-latest,gemini-1.0-pro-vision-latest,gemini-pro,gemini-pro-vision)
model = genai.GenerativeModel('gemini-pro')


def is_question_no_symbols(sentence):
    # Extended list of interrogative words and common question phrases
    interrogatives = [
        'who', 'what', 'when', 'where', 'why', 'how',
        'is', 'can', 'do', 'does', 'are', 'was', 'were',
        'will', 'shall', 'could', 'would', 'should', 'have',
        'has', 'had', 'may', 'might', 'am']

    # Patterns that often indicate a question
    question_patterns = [
        r'\b(can you|do you|did you|have you|will you|are you|were you|was you|should you|could you|would you)\b',
        r'\b(how many|how much|how long|how far|how old|how often)\b',
        r'^(does|did|is|are|was|were|can|could|will|would|should|shall|might|do)\b']

    # Lowercase the sentence for comparison
    sentence_lower = sentence.lower()

    # Check if the sentence starts with an interrogative word
    if any(sentence_lower.startswith(word) for word in interrogatives):
        return True

    # Check for question patterns
    for pattern in question_patterns:
        if re.search(pattern, sentence_lower):
            return True

    # Check for inversion in sentence structure typical for questions, e.g., "Are you going"
    if re.search(r'^\b(are|were|was|is|do|does|did|have|has|had|can|could|will|would|shall|should|might|must)\b\s+\w+', sentence_lower):
        return True

    # Check for a structure indicating a question without using interrogative words, e.g., "Your name"
    if re.search(r'\b(your|you|he|she|they|we|it)\b\s+\w+', sentence_lower):
        return True

    return False


#function to generate the interview questions by connecting to the Gen AI model
def generate_interview_questions(text):
    prompt = f"""Generate just only one scrum master position related interview questions, 
    the one question should be related to the previous reply and just only write the question.
    Previous answer:{text} """

    response = model.generate_content(prompt)

    #formatting the output to make it look cleaner
    generated_questions=response.text.replace("**", "")
    generated_questions=generated_questions.strip()
    return generated_questions


def generate_interview_answer(text):
    prompt = f"""Answer this question:{text} and ask if there is any question. Please only generate the answer for the question do not add extra things"""
    response = model.generate_content(prompt)

    #formatting the output to make it look cleaner
    generated_answers=response.text.replace("**", "")
    generated_answers=generated_answers.strip()
    return generated_answers


def main(text):
    if is_question_no_symbols(text):
        reply = generate_interview_answer(text) # This is a question
    else:
        reply = generate_interview_questions(text) # This is not a question
    return reply