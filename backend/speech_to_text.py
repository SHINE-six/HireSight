import json
import speech_recognition as sr
import subprocess

def convert_webm_to_wav(input_file, output_file):
    command = [
        "C:/ffmpeg/bin/ffmpeg.exe",      # "C:/ffmpeg/bin/ffmpeg.exe" for Windows, "/usr/bin/ffmpegthis current is for docker
        '-y',  # Always overwrite output file
        '-i', input_file,  # Input file
        '-vn',  # No video
        '-acodec', 'pcm_s16le',  # WAV codec
        '-ar', '44100',  # Audio sample rate
        '-ac', '2',  # Number of audio channels
        output_file  # Output file
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"Conversion complete: '{input_file}' to '{output_file}'")
    except subprocess.CalledProcessError:
        print("Error during conversion.")


def convert_wav_to_text(input_file):
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()

    with sr.AudioFile(input_file) as source:
        r.adjust_for_ambient_noise(source)
        audio_text = r.listen(source)
        json_data = {
            "text": "null"
        }
        
        try:
            # using google speech recognition
            text = r.recognize_google(audio_text)
            json_data = {
                "text": text
            }
        
        except:
                print('Sorry.. run again...')
        
        return json_data

def main():
    convert_webm_to_wav("uploads/audio/mic-audio.webm", 'uploads/audio/mic-audio.wav')
    prepare_to_json = convert_wav_to_text('uploads/audio/mic-audio.wav')
    with open('uploads/audio/transcript_detected.json', 'w') as json_file:
        json.dump(prepare_to_json, json_file, indent=2)
        json_file.close()
    print("Transcript saved successfully")

def main_for_live():
    convert_webm_to_wav("uploads/audio/mic-audio_live.webm", 'uploads/audio/mic-audio_live.wav')
    prepare_to_json = convert_wav_to_text('uploads/audio/mic-audio_live.wav')
    return prepare_to_json
    