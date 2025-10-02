import json

# Load the JSON file
with open('nouns.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Remove the character "'" from all values
for item in data:
    for key, value in item.items():
        if isinstance(value, str):
            item[key] = value.replace("'", "")

# Save the modified data back to the same file
with open('nouns.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=2)
