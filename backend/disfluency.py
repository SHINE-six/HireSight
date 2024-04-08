import json
import re

def detect_disfluencies(text):
    repetition_pattern = re.compile(r'\b(\w+)\s+\1\b', re.IGNORECASE)
    hesitation_pattern = re.compile(r'\b(?:uh|um|er|hmm?|ahem?|just|actually|literally)\b|\b(?:like|you know|so|well|basically|actually|i mean|sort of|kind of|anyway|you see|in my opinion|to be honest|I guess|i don\'t know|let me think|I\'m not sure|I suppose|it\'s like|to tell you the truth|honestly speaking|it seems like|as far as I know|from my perspective)\b|\b(?:well, you see|well, I don\'t know|you know what i mean|to be fair|to be clear|now, let me see|well, honestly|uh, let me think|well, in my opinion|um, I suppose|honestly, I don\'t know|to be perfectly honest|you know what i\'m saying|you get what i mean|you know, right?|let\'s see|it\'s kinda like|you see, like|actually, I don\'t know|you know what|you see, I mean|to tell the truth|well, let me think|um, to be clear|uh, to be fair|uh, like|ah, I see|like, I guess|um, you know|to be perfectly fair|uh, sort of|like, you see|uh, to be precise|um, to be precise|you know, in my opinion|like, to be honest|um, to be honest|you know, kind of|like, kind of|um, kind of|uh, kind of|you know, sort of|like, sort of|um, sort of|uh, sort of|you know, well|like, well|um, well|uh, well|you know, basically|like, basically|um, basically|uh, basically|you know, actually|like, actually|um, actually|uh, actually)\b', re.IGNORECASE)

    repetition_count = 0
    hesitation_count = 0
    disfluencies_text = []

    # Detect repetitions
    repetitions = repetition_pattern.findall(text)
    repetition_count = len(repetitions)
    if repetitions:
        disfluencies_text.extend(repetitions)

    # Detect hesitations
    hesitations = hesitation_pattern.findall(text)
    hesitation_count = len(hesitations)
    if hesitations:
        disfluencies_text.extend(hesitations)


    total_count = repetition_count + hesitation_count

    to_return_json = {
        "total_count": total_count,
        "repetition_count": repetition_count,
        "hesitation_count": hesitation_count,
        "disfluencies_text": disfluencies_text
    }

    return to_return_json


def main(combined_json):
    disfluencies_json = detect_disfluencies(combined_json['transcript'])
    combined_json['disfluencies'] = disfluencies_json

    return combined_json
