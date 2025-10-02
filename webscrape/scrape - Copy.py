import requests
from bs4 import BeautifulSoup
import json

# List of URLs to scrape
urls = [
    'https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20149&version=NRT',
    'https://www.biblegateway.com/passage/?search=%D0%9F%D1%81%D0%B0%D0%BB%D1%82%D0%B8%D1%80%D1%8C%20150&version=NRT',
    # Add more URLs as needed
]

# Function to scrape text from a webpage
def scrape_text_from_url(url):
    verses = []
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        poetry_div = soup.find('div', class_='passage-text')
        if poetry_div:
            spans = poetry_div.find_all('span', class_='text')
            for span in spans:
                text = span.text.strip()
                if text:
                    parts = text.split(' ', 1)
                    if len(parts) == 2 and parts[0].isdigit():
                        verse_number = int(parts[0])
                        verse_text = parts[1]
                        verses.append({"verse": verse_number, "text": verse_text})
    except Exception as e:
        print(f"Error scraping {url}: {e}")
    
    return verses

all_verses = []
for url in urls:
    all_verses.extend(scrape_text_from_url(url))

# Output to JSON file
with open('verses.json', 'w', encoding='utf-8') as f:
    json.dump(all_verses, f, ensure_ascii=False, indent=4)
