import json
import cv2
import numpy as np
import tensorflow as tf
import os
import datetime


model_path = 'model/version4.h5'

if not os.path.exists(model_path):
    print(f"Error: Model file '{model_path}' does not exist")
    exit()

new_model = tf.keras.models.load_model(model_path)


def prediction(video_path: str, new_model: tf.keras.Model):
    # Define the path to the Haar cascade file
    path = "haarcascade_frontalface_default.xml"

    # Initialize the video capture
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Failed to open video file")
        exit()

    original_fps = cap.get(cv2.CAP_PROP_FPS)
    # frame_skip = int(round(original_fps / 10))

    # fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # out = cv2.VideoWriter('uploads/video/output.avi', fourcc, original_fps, (int(cap.get(3)), int(cap.get(4))))


    # Initialize variables to count emotions
    status_dict = {0: "Angry", 1: "Disgust", 2: "Fear", 3: "Happy", 4: "Sad", 5: "Surprise", 6: "Neutral"}
    emotion_counts = {status_dict[i]: 0 for i in range(7)}


    # Load the face cascade classifier
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + path)

    start_time = datetime.datetime.now()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to retrieve frame from webcam")
            break
        
        if cap.get(cv2.CAP_PROP_POS_FRAMES) % 8 == 0:
            # Convert the frame to grayscale
            gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Detect faces in the grayscale frame
            faces = faceCascade.detectMultiScale(gray_scale, scaleFactor=1.1, minNeighbors=4)
            
            # Process each detected face
            for x, y, w, h in faces:
                roi_gray = gray_scale[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                facess = faceCascade.detectMultiScale(roi_gray)
                if len(facess) == 0:
                    print("Face not detected")
                else:
                    for (ex, ey, ew, eh) in facess:
                        face_roi = roi_color[ey: ey+eh, ex: ex+ew]
                    
                        # Preprocess the face image for prediction
                        final_image = cv2.resize(face_roi, (48, 48))
                        final_image = cv2.cvtColor(final_image, cv2.COLOR_BGR2GRAY)
                        
                        final_image = np.expand_dims(final_image, axis=-1)
                        final_image = np.expand_dims(final_image, axis=0)
                        
                        # Make predictions using the model
                        Predictions = new_model.predict(final_image)
                        status = status_dict[np.argmax(Predictions)]
                        emotion_counts[status] += 1

    cap.release()

    print("Time taken: ", datetime.datetime.now() - start_time)
    return emotion_counts


def main():
    prepare_to_json = prediction('uploads/video/webcam-video.mp4', new_model)

    with open('uploads/video/emotion_detected.json', 'w') as file:
        json.dump(prepare_to_json, file)
        file.close()
    print("Emotion saved successfully")
