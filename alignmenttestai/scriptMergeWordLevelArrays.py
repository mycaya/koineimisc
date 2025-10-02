import json
import string
import difflib

def is_close_match(text1, text2, threshold=0.7):
    # Create a SequenceMatcher object
    matcher = difflib.SequenceMatcher(None, text1, text2)
    
    # Get the similarity ratio
    return matcher.ratio() >= threshold

def normalize_text(text):
    # Remove punctuation and normalize text
    return text.lower().translate(str.maketrans('', '', string.punctuation))

# Load nrtwordobjects.json
with open('jsonNrtWordLevelArray.json', 'r', encoding='utf-8') as nrt_file:
    nrt_word_objects = json.load(nrt_file)

# Load wordonlyarray.json
with open('jsonWhisperWordLevelArray.json', 'r', encoding='utf-8') as wordonly_file:
    word_only_array = json.load(wordonly_file)

# Initialize the starting index for searching in nrtwordobjects.json
start_index = 0

# Iterate over each object in wordonlyarray.json
for wordonly_obj in word_only_array:
    # Get the current text from wordonlyarray.json and normalize it
    wordonly_text = normalize_text(wordonly_obj['text'])
    
    # Skip objects that are only punctuation or dashes
    if not wordonly_text:
        continue
    
    # Limit the search to the next 12 objects after the last match
    search_limit = min(start_index + 12, len(nrt_word_objects))
    
    # Search for a match starting from start_index
    for i in range(start_index, search_limit):
        nrt_obj = nrt_word_objects[i]
        
        # Normalize the text in nrtwordobjects.json
        nrt_text = normalize_text(nrt_obj['text'])
        
        if nrt_text == wordonly_text or is_close_match(nrt_text, wordonly_text):
            # Retrieve start and end values
            start, end = wordonly_obj['start'], wordonly_obj['end']
            
            # Add start and end values to the nrtwordobjects.json object
            nrt_obj['start'] = start
            nrt_obj['end'] = end
            
            # Update start_index for the next iteration
            start_index = i + 1
            break

# Filter out objects that consist only of punctuation or dashes
nrt_word_objects = [obj for obj in nrt_word_objects if normalize_text(obj['text'])]

# Save the updated nrtwordobjects.json data
with open('jsonNrtWordsWithTimestamps.json', 'w', encoding='utf-8') as output_file:
    json.dump(nrt_word_objects, output_file, ensure_ascii=False, indent=4)
