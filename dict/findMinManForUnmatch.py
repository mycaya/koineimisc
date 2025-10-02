import json

def load_json(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)

def find_matches_in_minman(unmatched_file, minman_file):
    unmatched_data = load_json(unmatched_file)
    minman_data = load_json(minman_file)

    minman_rus_dict = {entry["rus"].lower(): entry for entry in minman_data}

    matched_minman_objects = []
    for entry in unmatched_data:
        rus_word = entry["rus"].lower()
        if rus_word in minman_rus_dict:
            matched_minman_objects.append(minman_rus_dict[rus_word])

    return matched_minman_objects

def save_matched_objects(matched_objects, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(matched_objects, file, ensure_ascii=False, indent=4)

unmatched_file = 'unmatchedEe.json'
minman_file = 'minMan.json'
output_file = 'unmatchWithMinManEe.json'

matched_objects = find_matches_in_minman(unmatched_file, minman_file)

# Print the number of top-level objects
print(f'Number of top-level objects: {len(matched_objects)}')

save_matched_objects(matched_objects, output_file)
