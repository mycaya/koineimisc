import json

def process_adjectives(file_path):
    fields_to_check = [
        "base_form", "comparative", "superlative", "short_masculine",
        "short_feminine", "short_neuter", "short_plural",
        "masculine_nominative", "masculine_genitive", "masculine_dative",
        "masculine_accusative", "masculine_instrumental", "masculine_prepositional",
        "feminine_nominative", "feminine_genitive", "feminine_dative",
        "feminine_accusative", "feminine_instrumental", "feminine_prepositional",
        "neuter_nominative", "neuter_genitive", "neuter_dative",
        "neuter_accusative", "neuter_instrumental", "neuter_prepositional",
        "plural_nominative", "plural_genitive", "plural_dative",
        "plural_accusative", "plural_instrumental", "plural_prepositional"
    ]

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    processed_data = []

    for entry in data:
        normal_form = entry.get("base_form", "")
        
        for key in fields_to_check:
            value = entry.get(key, "")
            if value:  # Check if the field has a non-empty value
                new_object = {
                    "rus": value,
                    "grammar": f"{key.replace('_', ' ')} of",
                    "normal_form": normal_form
                }
                processed_data.append(new_object)

    return processed_data

file_path = 'adjectives.json'
result = process_adjectives(file_path)

with open('wordleveladjectives.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, ensure_ascii=False, indent=2)
