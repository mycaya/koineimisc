import json

# Load the JSON data from dictEssentialGram.json
with open('dictEssentialGram.json', 'r', encoding='utf-8') as file:
    essential_gram_data = json.load(file)

# Load the JSON data from dictEnglish.json
with open('dictEnglish.json', 'r', encoding='utf-8') as file:
    english_data = json.load(file)

# Ensure both files have the same number of objects
if len(essential_gram_data) != len(english_data):
    print("The files do not have the same number of objects.")
else:
    # Iterate through each object and compare the forms array
    for i, (essential_obj, english_obj) in enumerate(zip(essential_gram_data, english_data)):
        if len(essential_obj['forms']) != len(english_obj['forms']):
            print(f"Object {i} does not have the same number of forms.")
        else:
            for j, (essential_form, english_form) in enumerate(zip(essential_obj['forms'], english_obj['forms'])):
                if essential_form['targetdict'] != english_form['targetdict']:
                    print(f"Difference found at {english_form['targetdict']}:")
                    print(f"  Essential targetdict: {essential_form['targetdict']}")
                    print(f"  English targetdict: {english_form['targetdict']}")
                if essential_form['sourcedict'] != english_form['sourcedict']:
                    print(f"Source difference found at {english_form['targetdict']}:")
                    print(f"  Essential sourcedict: {essential_form['sourcedict']}")
                    print(f"  English sourcedict: {english_form['sourcedict']}")
