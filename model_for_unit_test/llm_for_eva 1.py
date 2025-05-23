import google.generativeai as genai
import re
 
# Configure the SDK with your API key by recovering the API key from a config file
genai.configure(api_key= 'AIzaSyBf4CTKNe4hTUTNRNxjDbs9sMNOnEwwgFk') # Please do not share 

#Setting the Gen AI model to be used (one of- gemini-1.0-pro, gemini-1.0-pro-001,gemini-1.0-pro-latest,gemini-1.0-pro-vision-latest,gemini-pro,gemini-pro-vision)
model = genai.GenerativeModel('gemini-pro')


def is_question_no_symbols(text):
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
    sentence_lower = text.lower()

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

def request_repeat(text):
    # Common phrases that indicate a desire to repeat the question
    repeat_phrases = [
        'repeat that', 'say that again', 'once more', 'another time',
        'could you repeat', 'please repeat', 'sorry', 'didnt get that',
        'didnt catch that', 'one more time', 'come again', 'what was that'
    ]
    
    # Lowercase the sentence for comparison
    sentence_lower = text.lower()

    # Check if the sentence contains any repeat phrases
    if any(phrase in sentence_lower for phrase in repeat_phrases):
        return True

    # More complex pattern to capture variations of repeating phrases
    complex_patterns = [
        r"\b(can you|could you|would you)\b.*\b(repeat|say)\b",
        r"\b(i|we|he|she|they)\b.*\b(didn't|did not|don't|do not)\b.*\b(hear|understand|get|catch)\b"
    ]

    for pattern in complex_patterns:
        if re.search(pattern, sentence_lower):
            return True
    return False


def request_end(text):
    # Phrases that suggest satisfaction and no further questions in a job interview context
    satisfaction_phrases = [
        "no further questions", "no more questions", "all my questions have been answered",
        "I have no other questions", "that covers everything", "I'm all set with questions",
        "I am satisfied with the information", "I feel well informed", "no, that's everything",
        "you've covered everything", "I think that's all", "I think we're done",
        "I don't have any questions", "I do not have any questions"
    ]
    
    # Lowercase the sentence for comparison
    sentence_lower = text.lower()

    # Check if the sentence contains any of the satisfaction phrases
    if any(phrase in sentence_lower for phrase in satisfaction_phrases):
        return True

    # Pattern to catch variations of satisfaction and completeness
    patterns = [
        r"\b(that's all|that is all)\b", r"\b(nothing else)\b",
        r"\b(thank you,? I'm good|thank you,? I am good)\b", r"\b(thank you,? that will be all)\b"
    ]

    for pattern in patterns:
        if re.search(pattern, sentence_lower):
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
    prompt = f"""Answer this question:{text} with some related content and ask if there is any question. Please only generate the answer for the question do not add extra things just one line summary"""
    response = model.generate_content(prompt)

    #formatting the output to make it look cleaner
    generated_answers=response.text.replace("**", "")
    generated_answers=generated_answers.strip()
    return generated_answers


    
def generate_repeat(text):
    prompt = f"""Repeat this question:{text} in a simpler way. Please only generate the answer for the question do not add extra things"""
    response = model.generate_content(prompt)

    #formatting the output to make it look cleaner
    generated_answers=response.text.replace("**", "")
    generated_answers=generated_answers.strip()
    return generated_answers


def generate_end_message():
    prompt = f"""Just generate a message to end the interview. Please do not add extra things just one line."""
    response = model.generate_content(prompt)

    #formatting the output to make it look cleaner
    generated_answers=response.text.replace("**", "")
    generated_answers=generated_answers.strip()
    return generated_answers



def main(text):
    if request_end(text):
         return generate_end_message()
    if request_repeat(text):
         return generate_repeat(text)
    if is_question_no_symbols(text):
         return generate_interview_answer(text) # This is a question
    else:
         return generate_interview_questions(text) # This is not a question


