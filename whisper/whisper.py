import os
import subprocess

# Define the source and output directories
source_dir = './source2Kgs'
output_dir = './output'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Iterate through all files in the source directory
for filename in os.listdir(source_dir):
    # Check if the file is an MP3 file
    if filename.endswith('.mp3'):
        input_file_path = os.path.join(source_dir, filename)
        
        # Construct the command to run
        command = [
            'whisper_timestamped', 
            input_file_path, 
            '--model', 'tiny', 
            '--language', 'ru', 
            '--output_dir', output_dir, 
            '--output_format', 'json'
        ]
        
        # Execute the command
        try:
            subprocess.run(command, check=True)
            print(f"Processed file: {filename}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to process file {filename}: {e}")
