import json

# Load the JSON data from file
with open('nouns.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# List of fields to process
fields_to_process = [
    "base_form",
    "singular_nominative",
    "singular_genitive",
    "singular_dative",
    "singular_accusative",
    "singular_instrumental",
    "singular_prepositional",
    "plural_nominative",
    "plural_genitive",
    "plural_dative",
    "plural_accusative",
    "plural_instrumental",
    "plural_prepositional"
]

# Prepare a list to hold the new objects
new_objects = []

# Process each entry in the JSON array
for entry in data:
    for field in fields_to_process:
        if field in entry and entry[field]:  # Check if the field has a non-empty value
            new_object = {
                'rus': entry[field],
                'grammar': f"{field.replace('_', ' ')} of {entry['gender']}",
                'normal_form': entry['base_form']
            }
            new_objects.append(new_object)

# Save the new objects to a new file
with open('wordlevelnouns.json', 'w', encoding='utf-8') as file:
    json.dump(new_objects, file, ensure_ascii=False, indent=2)
