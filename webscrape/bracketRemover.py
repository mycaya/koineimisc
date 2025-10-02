import os
import json
import re

# Path to the 'psalms' directory
psalms_directory = 'psalms'

def remove_square_brackets(text):
    # Remove square brackets and text within them using regex
    return re.sub(r'\[.*?\]', '', text)

# Iterate over each file in the 'psalms' directory
for filename in os.listdir(psalms_directory):
    if filename.endswith('.json'):
        file_path = os.path.join(psalms_directory, filename)
        
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Update the text field for each entry in the JSON data
        for entry in data:
            entry['text'] = remove_square_brackets(entry['text'])
        
        # Write the updated data back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
