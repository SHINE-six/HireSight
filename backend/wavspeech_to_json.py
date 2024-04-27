import subprocess

def convert_wav_to_json(input_file, output_file):
    command = [
        './Rhubarb-Lip-Sync/Rhubarb-Lip-Sync/rhubarb', 
        '-f', 
        'json', 
        input_file, 
        '-o', 
        output_file
    ]
    
    try:
        subprocess.run(command, check=True)
        return f"Conversion complete: '{input_file}' to '{output_file}'"
    except subprocess.CalledProcessError:
        return "Error during conversion."

def main():
    status = convert_wav_to_json('uploads/audio/fromAI.wav', 'uploads/audio/fromAI.json')
    return "Status: " + status