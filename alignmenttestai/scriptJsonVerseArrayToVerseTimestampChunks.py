import json
from difflib import SequenceMatcher

# Load whisper.json
with open('whisper.json', 'r', encoding='utf-8') as whisper_file:
    whisper_data = json.load(whisper_file)

# Load acts1.json
with open('acts1.json', 'r', encoding='utf-8') as acts1_file:
    acts1_data = json.load(acts1_file)

# Function to find the best matching segment for a given text
def find_best_match(text, segments):
    best_match = None
    highest_ratio = 0
    
    for segment in segments:
        # Calculate similarity ratio between the act's text and the segment's text
        ratio = SequenceMatcher(None, text, segment['text']).ratio()
        
        if ratio > highest_ratio:
            best_match = segment
            highest_ratio = ratio
    
    return best_match

# Add timestamps to acts1 based on whisper data
for act in acts1_data:
    match = find_best_match(act['text'], whisper_data['segments'])
    if match:
        act['timestamp'] = match['start']
    else:
        act['timestamp'] = None  # If no match found, set timestamp to None

# Save the output to output.json
with open('output.json', 'w', encoding='utf-8') as output_file:
    json.dump(acts1_data, output_file, ensure_ascii=False, indent=4)

print("Timestamps added and saved to output.json")
