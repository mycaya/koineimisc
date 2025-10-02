import json

# Load acts1.json
with open('jsonRawNrtChapter.json', 'r', encoding='utf-8') as acts1_file:
    acts1_data = json.load(acts1_file)

# Create a list to hold the word objects
word_objects = []

# Iterate over each entry in the acts1.json data
for act in acts1_data:
    # Split the text into words
    words = act['text'].split()
    
    # Create an object for each word and add it to the word_objects list
    for word in words:
        word_object = {
            "text": word,
            "chapter": act["chapter"],
            "verse": act["verse"],
            "translation_id": act["translation_id"],
            "book_id": act["book_id"],
            "book_name": act["book_name"]
        }
        word_objects.append(word_object)

# Save the word objects to a new JSON file
with open('jsonNrtWordLevelArray.json', 'w', encoding='utf-8') as output_file:
    json.dump(word_objects, output_file, ensure_ascii=False, indent=4)

print("Word objects saved to jsonNrtWordLevelArray.json")

