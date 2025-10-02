import json

# Load the JSON data from formValues.json
with open('formValues.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Sort the data based on the length of the grammar strings in descending order
sorted_data = sorted(data, key=lambda x: len(x['grammar']), reverse=True)

# Get the 13 longest grammar strings
longest_grammars = sorted_data[:13]

# Print the 13 longest grammar strings
for item in longest_grammars:
    print(item['grammar'])
