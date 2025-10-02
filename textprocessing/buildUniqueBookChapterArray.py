import json

# Load data from nrt.json
with open('nrt.json', 'r', encoding='utf-8') as infile:
    data = json.load(infile)

# Extract unique sets of chapter, book_id, and book_name
unique_sets = {}
for entry in data:
    key = (entry['chapter'], entry['book_id'], entry['book_name'])
    if key not in unique_sets:
        unique_sets[key] = {
            "chapter": entry['chapter'],
            "book_id": entry['book_id'],
            "book_name": entry['book_name']
        }

# Convert the dictionary values to a list
unique_list = list(unique_sets.values())

# Write the unique list to UniqueBookChapterArray.json
with open('UniqueBookChapterArray.json', 'w', encoding='utf-8') as outfile:
    json.dump(unique_list, outfile, ensure_ascii=False, indent=4)
