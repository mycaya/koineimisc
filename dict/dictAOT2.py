from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import UnexpectedAlertPresentException
import time
import json

# Correct path to your WebDriver executable
driver_path = r'C:\chromedriver.exe'  # Replace with your actual path

# Initialize the Service object
service = Service(executable_path=driver_path)

# Initialize the WebDriver with the Service object
driver = webdriver.Chrome(service=service)

# Mapping for Russian abbreviations to English meanings
abbreviation_mapping = {
    "мр": "masculine gender",
    "жр": "feminine gender",
    "ср": "neuter gender",
    "од": "animate",
    "но": "inanimate",
    "ед": "singular",
    "мн": "plural",
    "им": "nominative case",
    "рд": "genitive case",
    "дт": "dative case",
    "вн": "accusative case",
    "тв": "instrumental case",
    "пр": "prepositional case",
    "зв": "vocative case",
    "2": "secondary genitive or prepositional case",
    "св": "perfective aspect",
    "нс": "imperfective aspect",
    "пе": "transitive",
    "нп": "intransitive",
    "дст": "active voice",
    "стр": "passive voice",
    "нст": "present tense",
    "прш": "past tense",
    "буд": "future tense",
    "пвл": "imperative mood",
    "1л": "first person",
    "2л": "second person",
    "3л": "third person",
    "0": "invariable",
    "кр": "short form",
    "сравн": "comparative form",
    "имя": "first name",
    "фам": "last name",
    "отч": "patronymic",
    "лок": "locativity",
    "орг": "organization",
    "кач": "qualitative adjective",
    "вопр": "interrogative",
    "относ": "relative",
    "дфст": "singularia tantum",
    "опч": "frequent typo",
    "жарг": "jargon",
    "арх": "archaism",
    "проф": "professionalism",
    "аббр": "abbreviation",
    "безл": "impersonal verb"
}

# Mapping for grammatical parts
part_mapping = {
    "С": "noun",
    "П": "adjective",
    "МС": "nominal pronoun",
    "Г": "verb",
    "ПРИЧАСТИЕ": "participle",
    "ДЕЕПРИЧАСТИЕ": "gerund",
    "ИНФИНИТИВ": "infinitive",
    "МС-ПРЕДК": "predicative pronoun",
    "МС-П": "pronoun-adjective",
    "ЧИСЛ": "cardinal numeral",
    "ЧИСЛ-П": "ordinal numeral",
    "Н": "adverb",
    "ПРЕДК": "predicative",
    "ПРЕДЛ": "preposition",
    "СОЮЗ": "conjunction",
    "МЕЖД": "interjection",
    "ЧАСТ": "particle",
    "ВВОДН": "introductory word",
    "КР_ПРИЛ": "short adjective",
    "КР_ПРИЧАСТИЕ": "short participle"
}

def process_entry(entry):
    rus_word = entry['rus']
    
    try:
        # Open the URL
        driver.get('http://aot.ru/demo/morph.html')

        # Find the input field and enter text
        search_input = driver.find_element(By.ID, 'SearchText')
        search_input.clear()
        search_input.send_keys(rus_word)

        # Select the language radio button if necessary
        russian_radio = driver.find_element(By.XPATH, "//input[@name='langua' and @value='Russian']")
        russian_radio.click()

        # Check the "With paradigms" checkbox if needed
        paradigms_checkbox = driver.find_element(By.ID, 'WithParadigms')
        if not paradigms_checkbox.is_selected():
            paradigms_checkbox.click()

        # Submit the form by clicking the button
        submit_button = driver.find_element(By.XPATH, "//input[@type='button' and @value='Submit Request']")
        submit_button.click()

        # Wait for the results to load (adjust time if needed)
        time.sleep(0.5)

        # Scrape the results
        results_div = driver.find_element(By.ID, 'morphholder')
        raw_text = results_div.text

        # Parse the text into a structured dictionary
        lines = raw_text.splitlines()
        forms_list = []
        
        for line in lines:
            if line.startswith(('+', '-')):
                parts = line.split()
                lemma = None
                form_parts = []
                part_parts = []

                # Look for the lemma anywhere in the line
                for part in parts:
                    # Check if the part is all caps and not in mappings
                    if part.isalpha() and part.isupper() and part not in abbreviation_mapping and part not in part_mapping:
                        lemma = part.lower()
                        break

                for part in parts[1:]:
                    # Check if the part contains commas and split it into sub-parts
                    sub_parts = part.split(',') if ',' in part else [part]
                    
                    for sub_part in sub_parts:
                        if sub_part in abbreviation_mapping:
                            form_parts.append(abbreviation_mapping[sub_part])
                        elif sub_part in part_mapping:
                            part_parts.append(part_mapping[sub_part])

                if lemma:
                    form_str = ' '.join(form_parts)
                    part_str = ' '.join(part_parts)
                    forms_list.append({
                        "text": rus_word,
                        "form": form_str,
                        "part": part_str,
                        "dict": lemma
                    })

        return forms_list
    
    except UnexpectedAlertPresentException as e:
        print("An unexpected alert was present:", e.alert_text)
        alert = driver.switch_to.alert
        alert.accept()  # Accept the alert
        return []  # Return an empty list if an alert interrupts processing


# Load the inOut.json file
with open('inOut2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Process each entry in the inOut.json
for entry in data:
    if not entry['forms']:  # Only process entries with empty forms
        forms = process_entry(entry)
        if forms:
            entry['forms'] = forms
            # Save back to inOut.json after updating
            with open('inOut2.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

# Close the browser
driver.quit()
