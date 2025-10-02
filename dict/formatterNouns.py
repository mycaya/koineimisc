import json

# Load the JSON data from file
with open('nouns.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Process each entry in the JSON array
for entry in data:
    # Remove unwanted fields
    for field in ["accented", "partner", "animate", "indeclinable", "sg_only", "pl_only"]:
        entry.pop(field, None)
    
    # Rename fields
    entry['base_form'] = entry.pop('bare', None)  # Use pop with default value
    entry['translations_en'] = entry.pop('translations_en', '')

    # Update gender values
    gender_map = {'m': 'masculine', 'f': 'feminine', 'n': 'neuter'}
    entry['gender'] = gender_map.get(entry.get('gender', ''), entry.get('gender', ''))
    
    # Rename case fields
    rename_map = {
        "sg_nom": "singular_nominative",
        "sg_gen": "singular_genitive",
        "sg_dat": "singular_dative",
        "sg_acc": "singular_accusative",
        "sg_inst": "singular_instrumental",
        "sg_prep": "singular_prepositional",
        "pl_nom": "plural_nominative",
        "pl_gen": "plural_genitive",
        "pl_dat": "plural_dative",
        "pl_acc": "plural_accusative",
        "pl_inst": "plural_instrumental",
        "pl_prep": "plural_prepositional"
    }
    
    for old_key, new_key in rename_map.items():
        if old_key in entry:
            entry[new_key] = entry.pop(old_key)

    # Reorder keys
    entry = {k: entry[k] for k in ['base_form', 'translations_en', 'gender'] if k in entry} | {k: v for k, v in entry.items() if k not in ['base_form', 'translations_en', 'gender']}

# Save the modified data back to the same file
with open('nouns.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=2)
