import json
import copy

# Load the JSON data from dictEng.json
with open('dictEssentialGram.json', 'r', encoding='utf-8') as file:
    dict_eng_data = json.load(file)

# Process each object in the list
for obj in dict_eng_data:
    # Create a new forms list to hold modified forms
    new_forms = []
    
    for form in obj['forms']:
        grammar_words = form['grammar'].split()
        
        # Check if both "imperfective" and "perfective" are present
        if "imperfective" in grammar_words and "perfective" in grammar_words:
            # Create two copies of the form
            form_imperfective = copy.deepcopy(form)
            form_perfective = copy.deepcopy(form)
            
            # Remove "imperfective" from one and "perfective" from the other
            form_imperfective['grammar'] = ' '.join(word for word in grammar_words if word != "perfective")
            form_perfective['grammar'] = ' '.join(word for word in grammar_words if word != "imperfective")
            
            # Add both modified forms to the new forms list
            new_forms.extend([form_imperfective, form_perfective])
        else:
            # If not both, just add the original form
            new_forms.append(form)
    
    # Replace the original forms with the new forms
    obj['forms'] = new_forms

# Save the modified data to dictSplitPerf.json
with open('dictSplitPerf.json', 'w', encoding='utf-8') as file:
    json.dump(dict_eng_data, file, ensure_ascii=False, indent=4)
