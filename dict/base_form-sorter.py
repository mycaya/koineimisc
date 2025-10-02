import json

def reorder_json_fields(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for i, entry in enumerate(data):
        base_form_value = entry['base_form']
        # Remove base_form and reinsert it at the beginning
        del entry['base_form']
        data[i] = {'base_form': base_form_value, **entry}

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

file_path = 'adjectives.json'
reorder_json_fields(file_path)
