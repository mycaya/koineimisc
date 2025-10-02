import os
from mutagen.mp3 import MP3

def get_total_runtime(directory):
    total_runtime = 0.0

    for filename in os.listdir(directory):
        if filename.endswith('.mp3'):
            file_path = os.path.join(directory, filename)
            try:
                audio = MP3(file_path)
                total_runtime += audio.info.length
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    return total_runtime

# Specify the path to your chapteraudio subfolder
chapteraudio_folder = 'chapteraudio'

total_runtime = get_total_runtime(chapteraudio_folder)
print(f"Total combined runtime: {total_runtime} seconds")
