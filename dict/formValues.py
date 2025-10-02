import json
from collections import defaultdict

# Load the JSON data from inOut.json
with open('dictPerfect.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Dictionary to hold the count of each unique form value
form_counts = defaultdict(int)

# Iterate over each object and its forms array
for obj in data:
    for form_obj in obj.get('forms', []):
        form_value = form_obj.get('grammar', '')
        form_counts[form_value] += 1

# Convert the dictionary to a list of dictionaries, sorted by count
sorted_form_counts = sorted(
    [{'grammar': grammar, 'count': count} for grammar, count in form_counts.items()],
    key=lambda x: x['count'],
    reverse=True
)

# Write the result to formValues.json
with open('formValues.json', 'w', encoding='utf-8') as outfile:
    json.dump(sorted_form_counts, outfile, ensure_ascii=False, indent=4)
