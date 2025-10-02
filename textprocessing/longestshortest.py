import json

# Function to read the nrt.json file and find the longest and shortest text strings
def find_longest_and_shortest_text(input_file):
    longest_text = None
    shortest_text = None
    
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            entry = json.loads(line.strip())
            text = entry['text']
            
            if longest_text is None or len(text) > len(longest_text['text']):
                longest_text = entry
            
            if shortest_text is None or len(text) < len(shortest_text['text']):
                shortest_text = entry
    
    return longest_text, shortest_text

# File path
input_file = 'nrt.json'

# Find the longest and shortest texts
longest_entry, shortest_entry = find_longest_and_shortest_text(input_file)

# Output the number of characters in the longest and shortest text strings
print(f"Number of characters in the longest text: {len(longest_entry['text'])}")
print(f"Number of characters in the shortest text: {len(shortest_entry['text'])}")
