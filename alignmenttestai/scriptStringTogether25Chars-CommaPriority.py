import json
import string

def combine_words(timestamps_file, output_file, char_limit=25):
    with open(timestamps_file, 'r', encoding='utf-8') as timestamps_f:
        timestamps_data = json.load(timestamps_f)
    
    combined_entries = []
    highest_end_value = 0.0
    current_text = ""
    current_start = None
    current_end = None
    current_objects = []
    
    i = 0
    while i < len(timestamps_data):
        entry = timestamps_data[i]
        word = entry.get("text", "")
        start = entry.get("start")
        end = entry.get("end")

        # Check if adding this word exceeds the character limit or follows punctuation
        if (len(current_text) + len(word) + (1 if current_text else 0) <= char_limit and
            not (current_text and current_text[-1] in string.punctuation)):
            
            if not current_text and start is not None:
                current_start = start
            current_text = f"{current_text} {word}".strip()
            current_end = end if end is not None else current_end
            current_objects.append(entry)
        else:
            if current_text:
                combined_entries.append({
                    "text": current_text,
                    "start": current_start if current_start is not None else (
                        highest_end_value + 1),
                    "end": current_end,
                    "combined_objects": current_objects
                })
                highest_end_value = max(highest_end_value, current_end or 0)
            current_text = word
            current_start = start if start is not None else (
                highest_end_value + 1)
            current_end = end
            current_objects = [entry]
        
        i += 1

    if current_text:
        combined_entries.append({
            "text": current_text,
            "start": current_start if current_start is not None else (
                highest_end_value + 1),
            "end": current_end,
            "combined_objects": current_objects
        })
        highest_end_value = max(highest_end_value, current_end or 0)

    with open(output_file, 'w', encoding='utf-8') as output_f:
        json.dump(combined_entries, output_f, ensure_ascii=False, indent=4)

# Specify the paths to your JSON files
timestamps_file = 'jsonNrtWordsWithTimestamps.json'
output_file = 'json25StrungTogetherNrtWordChars.json'

combine_words(timestamps_file, output_file)
