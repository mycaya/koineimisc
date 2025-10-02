import json

# Load the JSON file
with open('nouns.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Set to store unique 'Подробности' values
unique_details = set()

# Collect the first 50 unique 'Подробности' values
for item in data:
    details = item.get('partner', '')
    if details and details not in unique_details:
        unique_details.add(details)
    if len(unique_details) >= 50:
        break

# Print the first 50 unique 'Подробности' values
for detail in unique_details:
    print(detail)
