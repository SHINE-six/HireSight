import mongoDB

def concat_all_transcript():
    conversationLog = mongoDB.getDataWithUniqueSessionID("conversationLog", uniqueSessionID)
    log_full = ""
    for log in conversationLog['log']:
        if log['user'] == "applicant":
            log_format = "Candidate: " + log['text'] + ". "
            log_full += log_format
        elif log['user'] == "Ai - EVA":
            log_format = "HR: " + log['text']
            log_full += log_format
    return log_full 