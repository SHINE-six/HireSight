"""Synthesizes speech from the input string of text."""
from google.cloud import texttospeech

# print(client)
# input_text = texttospeech.SynthesisInput(text="Hi Chenming 7 7 7 welcome to Hilti AI interview session I'm your AI interviewer EVA, and today I will be interviewing you on business analyst specialize on sustainability. Before we start, please introduce yourself") 

# Note: the voice can also be specified by name.
# Names of voices can be retrieved with client.list_voices().
client = texttospeech.TextToSpeechClient()
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    name="en-US-Studio-O",
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.LINEAR16,
    speaking_rate=1.15
)


def tts_process(input_text):

    input_text = texttospeech.SynthesisInput(text=input_text)
    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )

    # The response's audio_content is binary.
    with open("uploads/audio/fromAI.wav", "wb") as out:
        out.write(response.audio_content)
    
    return "uploads/audio/fromAI.wav"


def main(output_text):
    audio_paths = tts_process(output_text)
    return "Audio file created at: " + audio_paths



main("Hi Chenming 7 7 7 welcome to Hilti AI interview session I'm your AI interviewer EVA, and today I will be interviewing you on business analyst specialize on sustainability. Before we start, please introduce yourself")