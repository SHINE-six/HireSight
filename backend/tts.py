import torch

def tts_process(output_text):
    device = torch.device('cpu')
    torch.set_num_threads(4)
    local_file = './model/v3_en.pt'


    model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
    model.to(device)


    sample_rate = 24000
    speaker='en_0'

    audio_paths = model.save_wav(text=output_text,
                                speaker=speaker,
                                sample_rate=sample_rate,
                                audio_path="uploads/audio/fromAI.wav"
                                )
    return audio_paths

def main(output_text):
    audio_paths = tts_process(output_text)
    return "Audio file created at: " + audio_paths