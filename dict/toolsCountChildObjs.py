import json

# Load the JSON data from dictEnglish dictEssentialGram.json
with open('dictEssentialGram.json', 'r', encoding='utf-8') as file:
    dict_essential_gram_data = json.load(file)

# Initialize a counter for the total number of form objects
total_forms_count = 0

# Iterate through each object and sum up the lengths of their forms arrays
for obj in dict_essential_gram_data:
    total_forms_count += len(obj['forms'])

# Print the total number of form objects
print(total_forms_count)
