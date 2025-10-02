import json

# Load the JSON data from the file
with open('inOut.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Define the set of dict values to check for
dict_values_to_remove = {"од", "св", "нс", "но", "кач", "арх", "лок"}

# Iterate over each object and process the forms array
for item in data:
    if any(form['dict'] in dict_values_to_remove for form in item['forms']):
        item['forms'] = []

# Write the modified data back to the same file
with open('inOut.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
