import json

def load_json(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)

def normalize_word(word):
    return word.replace('ё', 'е').lower()

def find_unmatched_words(dict_file, *wordlevel_files):
    dict_data = load_json(dict_file)
    wordlevel_data = []

    for file in wordlevel_files:
        wordlevel_data.extend(load_json(file))

    wordlevel_rus_set = {normalize_word(entry["rus"]) for entry in wordlevel_data}

    unmatched_words = []
    for entry in dict_data:
        rus_word = normalize_word(entry["rus"])
        if rus_word not in wordlevel_rus_set:
            unmatched_words.append({"rus": entry["rus"], "count": entry["count"]})

    return unmatched_words

def save_unmatched_words(unmatched_words, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(unmatched_words, file, ensure_ascii=False, indent=4)

dict_file = 'dict.json'
wordlevel_files = [
    'wordleveladjectives.json',
    'wordlevelverbs.json',
    'wordlevelnouns.json',
    'wordlevelothers.json'
]
output_file = 'unmatchedEe.json'

unmatched_words = find_unmatched_words(dict_file, *wordlevel_files)
save_unmatched_words(unmatched_words, output_file)
