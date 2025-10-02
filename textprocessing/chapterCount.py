import json

# Load nrt.json data
with open('nrt.json', 'r', encoding='utf-8') as file:
    nrt_data = json.load(file)

# List to hold unique book_id and chapter pairs
unique_pairs = []
seen_pairs = set()

# Dictionary to track the highest consecutive chapter number for each book_id
highest_consecutive_chapters = {}

# Iterate through each object in the JSON data
for obj in nrt_data:
    # Create a tuple of (book_id, chapter)
    pair = (obj['book_id'], obj['chapter'])
    
    # Check if the pair is not already seen
    if pair not in seen_pairs:
        # Add the pair to the list and mark it as seen
        unique_pairs.append({'book_id': obj['book_id'], 'chapter': obj['chapter']})
        seen_pairs.add(pair)
        
        # Update the highest consecutive chapter number for the book_id
        book_id = obj['book_id']
        chapter = obj['chapter']
        if book_id not in highest_consecutive_chapters:
            highest_consecutive_chapters[book_id] = set()
        highest_consecutive_chapters[book_id].add(chapter)

# Compute the highest consecutive chapter number for each book_id
highest_consecutive_list = [
    {'book_id': book_id, 'highest_consecutive_chapter': max(chapters)}
    for book_id, chapters in highest_consecutive_chapters.items()
]

# Write the list of unique pairs to chapter.json
with open('chapter.json', 'w', encoding='utf-8') as file:
    json.dump(unique_pairs, file, ensure_ascii=False, indent=4)

# Write the list of highest consecutive chapters to highest_consecutive.json
with open('highest_consecutive.json', 'w', encoding='utf-8') as file:
    json.dump(highest_consecutive_list, file, ensure_ascii=False, indent=4)
