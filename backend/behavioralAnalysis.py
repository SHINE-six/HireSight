

def main(combinedJsonData):
    emotion = combinedJsonData["sections"][0]["emotion"]
    anger = emotion.get("Angry", 0)
    disgust = emotion.get("Disgust", 0)
    fear = emotion.get("Fear", 0)
    sad = emotion.get("Sad", 0)
    emotion_prob = weights['anger'] * anger + weights['disgust'] * disgust + weights['fear'] * fear + weights['sad'] * sad
    
    eye = combinedJsonData["sections"][0]["eye"]
    blink = eye.get("blink episode", 0)
    gaze_right = eye['gaze'].get("RIGHT", 0)
    gaze_left = eye['gaze'].get("LEFT", 0)
    eye_prob = weights['blink'] * blink + weights['gaze'] * (gaze_right + gaze_left)

    result = weights['alpha'] * emotion_prob + weights['beta'] * eye_prob 
    formatted_result = "{:.2f}".format(result)
    result = {
        "Score": f"{formatted_result}%",
    }

    return result

weights = {
    'anger': 0.2,
    'disgust': 0.3,
    'fear': 0.4,
    'sad': 0.3,
    'blink': 0.4,
    'gaze': 0.4,
    'alpha': 0.3,
    'beta': 0.4,
    }
