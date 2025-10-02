import json

def transform_json(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    transformed_data = []
    for entry in data:
        transformed_entry = {
            "rus": entry["base_form"],
            "grammar": "base form of",
            "normal_form": entry["base_form"],
            "eng": entry["translations_en"]
        }
        transformed_data.append(transformed_entry)

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(transformed_data, file, ensure_ascii=False, indent=4)

input_file = 'others.json'
output_file = 'wordlevelothers.json'
transform_json(input_file, output_file)
