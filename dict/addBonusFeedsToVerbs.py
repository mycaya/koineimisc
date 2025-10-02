import json

# Load data from storkstverbparticiples.json
with open('storkstverbparticiples.json', 'r', encoding='utf-8') as f:
    stork_data = json.load(f)

# Load data from verbs.json
with open('verbs.json', 'r', encoding='utf-8') as f:
    verbs_data = json.load(f)

# Iterate over each object in storkstverbparticiples.json
for stork_item in stork_data:
    infinitive = stork_item.get("Инфинитив", "")
    
    # Search for the Инфинитив value in each object's rus value in verbs.json
    for verb_item in verbs_data:
        if infinitive in verb_item.get("rus", ""):
            # Map and add the values to the verbs.json object
            verb_item["present_participle"] = stork_item.get("Деепричастие Наст. время", "")
            verb_item["past_participle"] = stork_item.get("Деепричастие Прош. время", "")
            verb_item["present_active_participle"] = stork_item.get("Действит. причастие Наст. время", "")
            verb_item["past_active_participle"] = stork_item.get("Действит. причастие Прош. время", "")
            verb_item["present_passive_participle"] = stork_item.get("Страдат. причастие Наст. время", "")
            verb_item["past_passive_participle"] = stork_item.get("Страдат. причастие Прош. время", "")

# Save the updated verbs.json
with open('verbs.json', 'w', encoding='utf-8') as f:
    json.dump(verbs_data, f, ensure_ascii=False, indent=4)
