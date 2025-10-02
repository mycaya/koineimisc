import json

# Load the JSON data from inOut.json
with open('dictPerfect.json', 'r', encoding='utf-8') as file:#was inOut
    data = json.load(file)

# Array to hold parent objects with specified form value
selected_objects = []

# Iterate over each object and its forms array
for obj in data:
    for form_obj in obj.get('forms', []):
        if form_obj.get('grammar') == "first present future imperative passive inanimate transitive masculine singular":
            selected_objects.append(obj)
            break  # Stop checking other forms of this object once a match is found
    if len(selected_objects) >= 20:
        break  # Stop if we have collected 20 parent objects

# Write the result to formValueGrabber.json
with open('formValueGrabber.json', 'w', encoding='utf-8') as outfile:
    json.dump(selected_objects, outfile, ensure_ascii=False, indent=4)
