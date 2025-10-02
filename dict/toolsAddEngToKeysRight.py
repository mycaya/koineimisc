import json

# Load the JSON data from keysRight.json and dictWithEnglish.json files
with open('keysRight.json', 'r', encoding='utf-8') as file:
    keys_right_data = json.load(file)

with open('dictWithEnglish.json', 'r', encoding='utf-8') as file:
    dict_with_english_data = json.load(file)

# Create a dictionary for quick lookup of english strings by rus value
rus_to_english = {item['rus']: item['english'][0] for item in dict_with_english_data}

# Process each object in keysRight.json
for obj in keys_right_data:
    rus_value = obj['rus']
    
    # Check if rus value exists in dictWithEnglish.json with matching case
    if rus_value in rus_to_english:
        english_string = rus_to_english[rus_value]
        
        # Update the source and sourceliteral values for each form in forms array
        for form in obj.get('forms', []):
            form['source'] = english_string
            form['sourceliteral'] = english_string
            
        # Further process each form to update targetdict and sourcedict
        for form in obj.get('forms', []):
            dict_value = form.pop('dict', '')  # Remove the 'dict' key and get its value
            form['targetdict'] = dict_value  # Set the original dict value to targetdict
            
            # Check if dict value exists in dictWithEnglish.json with matching case
            if dict_value in rus_to_english:
                form['sourcedict'] = rus_to_english[dict_value]

# Save the modified data to dictEng.json
with open('dictEng.json', 'w', encoding='utf-8') as file:
    json.dump(keys_right_data, file, ensure_ascii=False, indent=4)
