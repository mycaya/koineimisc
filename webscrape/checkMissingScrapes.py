import json
import os

# Load book data from UniqueBookChapterArray.json
with open('UniqueBookChapterArray.json', 'r', encoding='utf-8') as f:
    book_data = json.load(f)

# Directory to check for files
directory = 'scrapednrt'

# List to store missing filenames
missing_files = []

# Ensure the directory exists
if not os.path.exists(directory):
    print(f"Directory '{directory}' does not exist.")
else:
    # Iterate over each entry in the JSON data
    for entry in book_data:
        book_id = entry['book_id']
        chapter_number = entry['chapter']
        expected_filename = f"{book_id}-{chapter_number}.json"
        file_path = os.path.join(directory, expected_filename)
        
        # Check if the file exists
        if not os.path.isfile(file_path):
            missing_files.append(expected_filename)

# Print all missing files
if missing_files:
    print("Missing files:")
    for filename in missing_files:
        print(filename)
else:
    print("All files are present.")
