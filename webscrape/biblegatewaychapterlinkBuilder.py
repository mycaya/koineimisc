import json

def clean_urls(input_file, output_file):
    # Open and read the input JSON file
    with open(input_file, 'r', encoding='utf-8') as infile:
        data = json.load(infile)
    
    # Define the base URL
    base_url = "https://www.biblegateway.com"
    
    # Process each line to remove content after 'NRT' and add the base URL
    cleaned_data = []
    for entry in data:
        # Find the index of 'NRT' and slice the string up to that point
        index = entry.find('NRT')
        if index != -1:
            cleaned_entry = entry[:index + 3]  # Include 'NRT' in the result
            # Remove any leading characters like '=' and append the base URL
            if cleaned_entry.startswith('="'):
                cleaned_entry = cleaned_entry[2:]
            full_url = base_url + cleaned_entry.replace("&amp;", "&")
            cleaned_data.append(full_url)
    
    # Write the cleaned data to the output JSON file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(cleaned_data, outfile, indent=4)

# Specify the input and output file paths
input_file = 'biblegatewaychapterhtml.json'
output_file = 'biblegatewaychapterlinks.json'

# Run the function to clean URLs
clean_urls(input_file, output_file)
