import os

# Define the directory containing the files
directory = 'output'

# Iterate over all files in the specified directory
for filename in os.listdir(directory):
    # Check if the file ends with '.mp3.words.json'
    if filename.endswith('.mp3.words.json'):
        # Construct the full path to the file
        old_file_path = os.path.join(directory, filename)
        # Split the filename and keep only the part before the first period
        base_name = filename.split('.')[0]
        # Create a new filename by adding '.json' to the base name
        new_filename = f"{base_name}.json"
        # Construct the full path for the new filename
        new_file_path = os.path.join(directory, new_filename)
        # Rename the file
        os.rename(old_file_path, new_file_path)

print("Files have been renamed successfully.")
