import cv2
import dlib
import numpy as np
import time
import matplotlib.pyplot as plt


# Initialize dlib's face detector and facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  # Update the path as needed

def eye_aspect_ratio(eye):
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    C = np.linalg.norm(eye[0] - eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Update the calculate_gaze_ratio function to also return the eye center
def calculate_gaze_ratio_and_center(eye_points, facial_landmarks, frame, gray):
    eye_region = np.array([(facial_landmarks.part(point).x, facial_landmarks.part(point).y) for point in eye_points], np.int32)
    # Calculate the eye center
    eye_center = eye_region.mean(axis=0).astype(int)
    
    mask = np.zeros((frame.shape[0], frame.shape[1]), np.uint8)
    cv2.polylines(mask, [eye_region], True, 255, 2)
    cv2.fillPoly(mask, [eye_region], 255)
    eye = cv2.bitwise_and(gray, gray, mask=mask)
    
    min_x = np.min(eye_region[:, 0])
    max_x = np.max(eye_region[:, 0])
    min_y = np.min(eye_region[:, 1])
    max_y = np.max(eye_region[:, 1])
    
    gray_eye = eye[min_y:max_y, min_x:max_x]
    _, threshold_eye = cv2.threshold(gray_eye, 70, 255, cv2.THRESH_BINARY)
    
    height, width = threshold_eye.shape
    left_side_threshold = threshold_eye[0:height, 0:int(width/2)]
    right_side_threshold = threshold_eye[0:height, int(width/2):width]
    
    left_side_white = cv2.countNonZero(left_side_threshold)
    right_side_white = cv2.countNonZero(right_side_threshold)

    gaze_ratio = 1
    if left_side_white == 0:
        gaze_ratio = 1
    elif right_side_white == 0:
        gaze_ratio = 5
    else:
        gaze_ratio = left_side_white / right_side_white
    
    return gaze_ratio, eye_center

cap = cv2.VideoCapture(0)

blink_timestamps = []
start_time = time.time()
gaze_counts = {"RIGHT": 0, "CENTER": 0, "LEFT": 0}

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    
    for face in faces:
        landmarks = predictor(gray, face)
        
        # Blink Detection
        left_eye = np.array([(landmarks.part(n).x, landmarks.part(n).y) for n in range(42, 48)])
        right_eye = np.array([(landmarks.part(n).x, landmarks.part(n).y) for n in range(36, 42)])
        left_EAR = eye_aspect_ratio(left_eye)
        right_EAR = eye_aspect_ratio(right_eye)
        ear = (left_EAR + right_EAR) / 2.0
        
        if ear < 0.21:  # Threshold for blink detection
            blink_timestamps.append(time.time() - start_time)
            cv2.putText(frame, "BLINK", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        
        # Updated Gaze Detection with pupil marker
        gaze_ratio_left_eye, left_eye_center = calculate_gaze_ratio_and_center([36, 37, 38, 39, 40, 41], landmarks, frame, gray)
        gaze_ratio_right_eye, right_eye_center = calculate_gaze_ratio_and_center([42, 43, 44, 45, 46, 47], landmarks, frame, gray)
        
        gaze_ratio = (gaze_ratio_right_eye + gaze_ratio_left_eye) / 2
        
        if gaze_ratio <= 0.80:
            text = "RIGHT"
        elif 0.80 < gaze_ratio < 1.85:
            text = "CENTER"
        else:
            text = "LEFT"
        
        gaze_counts[text] += 1
        cv2.putText(frame, text, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
        
        # Draw a cross marker on each eye center green
        cv2.drawMarker(frame, tuple(left_eye_center), (0, 255, 0), cv2.MARKER_CROSS, markerSize=6, thickness=1)
        cv2.drawMarker(frame, tuple(right_eye_center), (0, 255, 0), cv2.MARKER_CROSS, markerSize=6, thickness=1)
        # Drawing a filled circle at the pupil's center green
        # cv2.circle(frame, tuple(left_eye_center), 3, (0, 255, 0), cv2.FILLED)  # Green filled circle for left eye
        # cv2.circle(frame, tuple(right_eye_center), 3, (0, 255, 0), cv2.FILLED)  # Green filled circle for right eye

    
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()

# Analyze blinks for high-frequency episodes
def analyze_blinks(blink_timestamps, duration=5, threshold=3):
    high_freq_blinks = 0
    start_index = 0

    while start_index < len(blink_timestamps):
        end_index = start_index
        while end_index < len(blink_timestamps) and blink_timestamps[end_index] - blink_timestamps[start_index] <= duration:
            end_index += 1

        if (end_index - start_index) >= threshold:
            high_freq_blinks += 1
            start_index = end_index  # Skip to the next set of blinks
        else:
            start_index += 1

    return high_freq_blinks

# After exiting the main loop, we analyze the blinks
high_freq_blink_count = analyze_blinks(blink_timestamps)
print(f"High-frequency blink episodes: {high_freq_blink_count}")




# Assuming gaze_counts contains your gaze direction frequencies
directions = list(gaze_counts.keys())
frequencies = list(gaze_counts.values())

# Summarize gaze direction counts
print("Gaze direction summary:")
for direction, count in gaze_counts.items():
    print(f"{direction}: {count}")

plt.figure(figsize=(10, 6))
plt.bar(directions, frequencies, color=['red', 'green', 'blue'])
plt.title('Gaze Direction Frequencies')
plt.xlabel('Gaze Direction')
plt.ylabel('Frequency')
plt.xticks(directions)  # Ensure the x-axis has labels for each gaze direction
plt.show()