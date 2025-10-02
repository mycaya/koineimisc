import json

# Define the base URL with a placeholder for the number
base_url = 'https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20{}&version=NRT'

# Generate the list of URLs
urls = [base_url.format(i) for i in range(1, 151)]

# Write the URLs to a JSON file
with open('urls.json', 'w', encoding='utf-8') as f:
    json.dump(urls, f, ensure_ascii=False, indent=4)

print("URLs have been written to urls.json")
