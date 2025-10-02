import json
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Function to translate Russian words to English using Google Translate
def translate_to_english(russian_word):
    try:
        # Translate the word and return the English translation
        translated = translator.translate(russian_word, src='ru', dest='en')
        return translated.text
    except Exception as e:
        print(f"Error translating '{russian_word}': {e}")
        return ""

# Load the JSON data from keysRight.json file
with open('keysRight.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Update each form in every top-level object
for item in data:
    for form in item.get('forms', []):
        # Translate target and dict values
        english_translation_target = translate_to_english(form["target"])
        english_translation_dict = translate_to_english(form["dict"])
        
        # Update source and sourceliteral with the translation of target
        form["source"] = english_translation_target
        form["sourceliteral"] = english_translation_target
        
        # Update sourcedict with the translation of dict
        form["sourcedict"] = english_translation_dict

# Save the modified data to dictEnglish.json file
with open('dictEnglish.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
