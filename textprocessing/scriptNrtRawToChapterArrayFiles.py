import json
import os

# Ensure the nrtchapters directory exists
os.makedirs('nrtchapters', exist_ok=True)

# Load nrt.json data
with open('2Kgs.json', 'r', encoding='utf-8') as file:
    # Read the entire JSON array at once
    nrt_data = json.load(file)

# Dictionary to hold grouped objects by book_id and chapter
grouped_data = {}

# Group objects by book_id and chapter
for obj in nrt_data:
    key = f"{obj['book_id']}-{obj['chapter']}"
    
    if key not in grouped_data:
        grouped_data[key] = []
    
    grouped_data[key].append(obj)

# Save each group as a separate JSON file
for key, objects in grouped_data.items():
    filename = f"nrtchapters/{key}.json"
    with open(filename, 'w', encoding='utf-8') as outfile:
        json.dump(objects, outfile, ensure_ascii=False, indent=4)
