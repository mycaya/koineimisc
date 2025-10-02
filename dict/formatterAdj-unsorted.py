import json

# Load the JSON data from file
with open('adjectives.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Define the mapping of old field names to new field names
field_name_mapping = {
    "bare": "base_form",
    "short_m": "short_masculine",
    "short_f": "short_feminine",
    "short_n": "short_neuter",
    "short_pl": "short_plural",
    "decl_m_nom": "masculine_nominative",
    "decl_m_gen": "masculine_genitive",
    "decl_m_dat": "masculine_dative",
    "decl_m_acc": "masculine_accusative",
    "decl_m_inst": "masculine_instrumental",
    "decl_m_prep": "masculine_prepositional",
    "decl_f_nom": "feminine_nominative",
    "decl_f_gen": "feminine_genitive",
    "decl_f_dat": "feminine_dative",
    "decl_f_acc": "feminine_accusative",
    "decl_f_inst": "feminine_instrumental",
    "decl_f_prep": "feminine_prepositional",
    "decl_n_nom": "neuter_nominative",
    "decl_n_gen": "neuter_genitive",
    "decl_n_dat": "neuter_dative",
    "decl_n_acc": "neuter_accusative",
    "decl_n_inst": "neuter_instrumental",
    "decl_n_prep": "neuter_prepositional",
    "decl_pl_nom": "plural_nominative",
    "decl_pl_gen": "plural_genitive",
    "decl_pl_dat": "plural_dative",
    "decl_pl_acc": "plural_accusative",
    "decl_pl_inst": "plural_instrumental",
    "decl_pl_prep": "plural_prepositional"
}

# Process each entry in the JSON array
for entry in data:
    # Remove accented fields
    if 'accented' in entry:
        del entry['accented']
    
    # Rename fields according to the mapping
    for old_field, new_field in field_name_mapping.items():
        if old_field in entry:
            entry[new_field] = entry.pop(old_field)

# Save the modified data back to the same file
with open('adjectives.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=2)
