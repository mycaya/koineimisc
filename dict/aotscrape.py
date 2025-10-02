from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import json

# Correct path to your WebDriver executable
driver_path = r'C:\chromedriver.exe'  # Replace with your actual path

# Initialize the Service object
service = Service(executable_path=driver_path)

# Initialize the WebDriver with the Service object
driver = webdriver.Chrome(service=service)

try:
    # Open the URL
    driver.get('http://aot.ru/demo/morph.html')

    # Find the input field and enter text
    search_input = driver.find_element(By.ID, 'SearchText')
    search_input.clear()
    search_input.send_keys('того')  # Replace with your input text

    # Select the language radio button if necessary
    russian_radio = driver.find_element(By.XPATH, "//input[@name='langua' and @value='Russian']")
    russian_radio.click()

    # Check the "With paradigms" checkbox if needed
    paradigms_checkbox = driver.find_element(By.ID, 'WithParadigms')
    if not paradigms_checkbox.is_selected():
        paradigms_checkbox.click()

    # Submit the form by clicking the button
    submit_button = driver.find_element(By.XPATH, "//input[@type='button' and @value='Submit Request']")
    submit_button.click()

    # Wait for the results to load (adjust time if needed)
    time.sleep(5)

    # Scrape the results
    results_div = driver.find_element(By.ID, 'morphholder')
    raw_text = results_div.text

    # Parse the text into a structured dictionary
    # This is a simple example; you may need to adjust parsing logic based on actual output
    lines = raw_text.splitlines()
    parsed_results = {"results": []}
    
    for line in lines:
        parts = line.split()
        if len(parts) > 1:
            entry = {
                "word": parts[0],
                "form": parts[1:]
            }
            parsed_results["results"].append(entry)

    # Convert the dictionary to a JSON string
    json_output = json.dumps(parsed_results, ensure_ascii=False, indent=4)

    # Save the JSON string to a file
    with open('scrapeoutput.json', 'w', encoding='utf-8') as f:
        f.write(json_output)

finally:
    # Close the browser
    driver.quit()
