import requests
from bs4 import BeautifulSoup
import json
import os
import re

# Load URLs from BibleGatewayChapterLinks.json
with open('BibleGatewayChapterLinks.json', 'r', encoding='utf-8') as f:
    urls = json.load(f)

# Load book data from UniqueBookChapterArray.json
with open('UniqueBookChapterArray.json', 'r', encoding='utf-8') as f:
    book_data = json.load(f)

def parse_verses(verses, chapter_number, book_id, book_name):
    chapter_data = []
    current_verse = 1
    text_buffer = ""
    
    # Check for text before the first number and add it as verse 0
    if verses:
        first_verse = re.sub(r'\[.*?\]', '', verses[0])  # Remove text within square brackets
        pre_number_text_match = re.match(r'^\D+', first_verse)
        if pre_number_text_match:
            pre_number_text = pre_number_text_match.group().strip()
            chapter_data.append({
                "chapter": chapter_number,
                "verse": 0,
                "text": pre_number_text,
                "translation_id": "NRT",
                "book_id": book_id,
                "book_name": book_name
            })
            verses[0] = first_verse[len(pre_number_text):].strip()

    for verse in verses:
        verse = re.sub(r'\[.*?\]', '', verse)  # Remove text within square brackets
        numbers = list(map(int, re.findall(r'\d+', verse)))
        if numbers:
            if text_buffer.strip():
                chapter_data.append({
                    "chapter": chapter_number,
                    "verse": current_verse,
                    "text": text_buffer.strip(),
                    "translation_id": "NRT",
                    "book_id": book_id,
                    "book_name": book_name
                })
                current_verse += 1
            text_buffer = verse.split(str(numbers[0]), 1)[-1].strip()
        else:
            text_buffer += " " + verse

    # Add the remaining text buffer if not empty
    if text_buffer.strip():
        chapter_data.append({
            "chapter": chapter_number,
            "verse": current_verse,
            "text": text_buffer.strip(),
            "translation_id": "NRT",
            "book_id": book_id,
            "book_name": book_name
        })

    return chapter_data

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
                    verses.append(text)
    except Exception as e:
        print(f"Error scraping {url}: {e}")
    
    return verses

# Create 'scrapednrt' directory if it doesn't exist
os.makedirs('biblegatewaynrt', exist_ok=True)

for index, url in enumerate(urls):
    if index < len(book_data):
        book_info = book_data[index]
        book_id = book_info['book_id']
        book_name = book_info['book_name']
        chapter_number = book_info['chapter']

        verses = scrape_text_from_url(url)
        chapter_data = parse_verses(verses, chapter_number, book_id, book_name)
        
        if chapter_data:
            with open(f'biblegatewaynrt/{book_id}-{chapter_number}.json', 'w', encoding='utf-8') as f:
                json.dump(chapter_data, f, ensure_ascii=False, indent=4)
