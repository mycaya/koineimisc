import json

# Load the whisper.json file
with open('jsonWhisper.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Initialize an empty list to store all word objects
combined_words = []

# Iterate over each segment and append the words to the combined_words list
for segment in data['segments']:
    combined_words.extend(segment['words'])

# Write the combined word objects to jsonWhisperWordLevelArray.json
with open('jsonWhisperWordLevelArray.json', 'w', encoding='utf-8') as output_file:
    json.dump(combined_words, output_file, ensure_ascii=False, indent=4)

print("jsonWhisperWordLevelArray.json has been created with all word objects.")
