import json

# Function to find and log the word containing the 25th character
def log_25th_character_word(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
            for entry in data:
                text = entry["text"]
                if len(text) >= 25:
                    # Find the word containing the 25th character
                    words = text.split()
                    char_count = 0
                    for word in words:
                        char_count += len(word) + 1  # Adding 1 for the space
                        if char_count >= 25:
                            print(word)
                            break
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON from the file.")

# Specify the path to your JSON file
file_path = 'acts1.json'
log_25th_character_word(file_path)
