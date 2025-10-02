import json

# Load the JSON file
with open('dictWithEnglish.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Sort the data by count in descending order, then alphabetically by 'rus'
sorted_data = sorted(data, key=lambda x: (-x['count'], x['rus']))

# Save the sorted data back to grammarFormsSort.json
with open('dictWithEnglish.json', 'w', encoding='utf-8') as outfile:
    json.dump(sorted_data, outfile, ensure_ascii=False, indent=4)
