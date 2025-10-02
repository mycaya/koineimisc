import subprocess
import os
import shutil

def run_whisper(input_file, model='tiny', language='ru', output_dir='.'):
    # Construct the command
    command = [
        'whisper_timestamped',
        input_file,
        '--model', model,
        '--language', language,
        '--output_dir', output_dir
    ]

    # Run the command
    subprocess.run(command, check=True)

def process_files(source_folder='source', output_folder='output'):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Process each file in the source folder
    for filename in os.listdir(source_folder):
        if filename.endswith('.mp3'):
            # Get the base filename without extension
            base_filename = os.path.splitext(filename)[0]

            # Define full paths
            input_path = os.path.join(source_folder, filename)
            output_path = os.path.join(output_folder, f"{base_filename}.json")

            # Run whisper on the current file
            run_whisper(input_path)

            # Rename the generated .words.json to <filename>.json and move it to the output folder
            original_json = f"{input_path}.words.json"
            if os.path.exists(original_json):
                shutil.move(original_json, output_path)

            # Clean up the source folder except required files
            for file in os.listdir(source_folder):
                if file not in {'whisper.py', filename, f"{base_filename}.json"}:
                    file_path = os.path.join(source_folder, file)
                    try:
                        os.remove(file_path)
                    except FileNotFoundError:
                        pass

if __name__ == "__main__":
    process_files()
