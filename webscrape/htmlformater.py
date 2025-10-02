import json

def extract_href_lines(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split content by 'href' and keep the delimiter in each part
    parts = content.split('href')
    
    # Reattach 'href' to each part except the first one
    href_lines = ['href'.join(parts[i:i+2]) for i in range(1, len(parts))]
    
    # Write each href-containing line to a JSON file as a list of strings
    with open(output_file, 'w', encoding='utf-8') as out_f:
        json.dump(href_lines, out_f, ensure_ascii=False, indent=4)

# Specify the input and output file paths
input_file = 'links.txt'
output_file = 'biblegatewaychapterhtml.json'

# Extract href lines and save to JSON
extract_href_lines(input_file, output_file)
