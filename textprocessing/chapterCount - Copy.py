import json

# Load nrt.json data
with open('nrt.json', 'r', encoding='utf-8') as file:
    # Read the entire JSON array at once
    nrt_data = json.load(file)

# List to hold unique book_id and chapter pairs
unique_pairs = []
seen_pairs = set()

# Iterate through each object in the JSON data
for obj in nrt_data:
    # Create a tuple of (book_id, chapter)
    pair = (obj['book_id'], obj['chapter'])
    
    # Check if the pair is not already seen
    if pair not in seen_pairs:
        # Add the pair to the list and mark it as seen
        unique_pairs.append({'book_id': obj['book_id'], 'chapter': obj['chapter']})
        seen_pairs.add(pair)

# Write the list of unique pairs to chapter.json
with open('chapter.json', 'w', encoding='utf-8') as file:
    json.dump(unique_pairs, file, ensure_ascii=False, indent=4)
