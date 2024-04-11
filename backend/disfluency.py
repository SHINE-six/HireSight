import json
import re

def detect_disfluencies(text):
    repetitionPattern = re.compile(r'\b(\w+)\s+\1\b', re.IGNORECASE)
    hesitationPattern = re.compile(r'\b(?:uh|um|er|hmm?|ahem?|just|actually|literally)\b|\b(?:like|you know|so|well|basically|actually|i mean|sort of|kind of|anyway|you see|in my opinion|to be honest|I guess|i don\'t know|let me think|I\'m not sure|I suppose|it\'s like|to tell you the truth|honestly speaking|it seems like|as far as I know|from my perspective)\b|\b(?:well, you see|well, I don\'t know|you know what i mean|to be fair|to be clear|now, let me see|well, honestly|uh, let me think|well, in my opinion|um, I suppose|honestly, I don\'t know|to be perfectly honest|you know what i\'m saying|you get what i mean|you know, right?|let\'s see|it\'s kinda like|you see, like|actually, I don\'t know|you know what|you see, I mean|to tell the truth|well, let me think|um, to be clear|uh, to be fair|uh, like|ah, I see|like, I guess|um, you know|to be perfectly fair|uh, sort of|like, you see|uh, to be precise|um, to be precise|you know, in my opinion|like, to be honest|um, to be honest|you know, kind of|like, kind of|um, kind of|uh, kind of|you know, sort of|like, sort of|um, sort of|uh, sort of|you know, well|like, well|um, well|uh, well|you know, basically|like, basically|um, basically|uh, basically|you know, actually|like, actually|um, actually|uh, actually)\b', re.IGNORECASE)

    repetitionCount = 0
    hesitationCount = 0
    disfluenciesText = []

    # Detect repetitions
    repetitions = repetitionPattern.findall(text)
    repetitionCount = len(repetitions)
    if repetitions:
        disfluenciesText.extend(repetitions)

    # Detect hesitations
    hesitations = hesitationPattern.findall(text)
    hesitationCount = len(hesitations)
    if hesitations:
        disfluenciesText.extend(hesitations)


    totalCount = repetitionCount + hesitationCount

    toReturnJson = {
        "totalCount": totalCount,
        "repetitionCount": repetitionCount,
        "hesitationCount": hesitationCount,
        "disfluenciesText": disfluenciesText
    }

    return toReturnJson


def main(combinedJson):
    disfluenciesJson = detect_disfluencies(combinedJson['transcript'])
    combinedJson['disfluencies'] = disfluenciesJson

    return combinedJson
