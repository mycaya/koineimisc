from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Correct path to your WebDriver executable
driver_path = r'C:\chromedriver.exe'  # Replace with your actual path
#driver_path = 'C:\\chromedriver.exe'


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
    print(results_div.text)

finally:
    # Close the browser
    driver.quit()
