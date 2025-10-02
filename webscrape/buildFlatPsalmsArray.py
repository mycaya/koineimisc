import json
import os

# Directory containing the psalms files
psalms_dir = 'psalms'

# List to hold all objects from the arrays in the files
all_objects = []

# Get a sorted list of files from Ps-1.json to Ps-150.json
sorted_files = sorted(os.listdir(psalms_dir), key=lambda x: int(x.split('-')[1].split('.')[0]))

# Iterate over each file in the sorted order
for filename in sorted_files:
    filepath = os.path.join(psalms_dir, filename)
    
    # Open and read each JSON file
    with open(filepath, 'r', encoding='utf-8') as infile:
        data = json.load(infile)
        
        # Extend the all_objects list with the contents of the current file's array
        all_objects.extend(data)

# Sort the combined array by the chapter value
all_objects.sort(key=lambda obj: obj['chapter'])

# Write the sorted array to buildFlatPsalmsArray.json
with open('FlatPsalmsArray.json', 'w', encoding='utf-8') as outfile:
    json.dump(all_objects, outfile, ensure_ascii=False, indent=4)
