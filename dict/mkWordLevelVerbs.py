import json

# Load data from verbs.json
with open('verbs.json', 'r', encoding='utf-8') as f:
    verbs_data = json.load(f)

# Define the source fields to check
source_fields = [
    "infinitive",
    "singular_imperative",
    "plural_imperative",
    "past_masculine",
    "past_feminine",
    "past_neuter",
    "past_plural",
    "1st_person_singular_present",
    "2nd_person_singular_present",
    "3rd_person_singular_present",
    "1st_person_plural_present",
    "2nd_person_plural_present",
    "3rd_person_plural_present",
    "present_participle",
    "past_participle",
    "present_active_participle",
    "past_active_participle",
    "present_passive_participle",
    "past_passive_participle"
]

# Create a list to store new objects
new_objects = []

# Iterate over each object in verbs.json
for verb_item in verbs_data:
    infinitive_value = verb_item.get("infinitive", "")
    aspect_value = verb_item.get("aspect", "")
    
    # Check each source field for non-empty values
    for field in source_fields:
        field_value = verb_item.get(field, "")
        if field_value:  # If the field has a non-empty value
            # Create a new object with the specified structure
            new_object = {
                "rus": field_value,
                "grammar": f"{field.replace('_', ' ')} of {aspect_value}",
                "normal_form": infinitive_value
            }
            new_objects.append(new_object)

# Save the new objects to a file (optional)
with open('wordlevelverbs.json', 'w', encoding='utf-8') as f:
    json.dump(new_objects, f, ensure_ascii=False, indent=4)
