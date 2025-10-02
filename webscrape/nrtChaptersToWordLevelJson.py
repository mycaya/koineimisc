import os
import json

# Define the input and output directories
input_directory = 'biblegatewaynrt'
output_directory = 'wordlevelscrapejson'

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Iterate over each .json file in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith('.json'):
        input_file_path = os.path.join(input_directory, filename)
        
        # Load the JSON file
        with open(input_file_path, 'r', encoding='utf-8') as acts1_file:
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

        # Define the output file path
        output_file_path = os.path.join(output_directory, filename)

        # Save the word objects to a new JSON file
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            json.dump(word_objects, output_file, ensure_ascii=False, indent=4)

        print(f"Word objects saved to {output_file_path}")
