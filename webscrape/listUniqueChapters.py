import json

# Load the JSON data from the file
with open('UniqueBookChapterArray.json', 'r') as file:
    data = json.load(file)

# Extract and combine book_id and chapter values
combined_list = [f"{item['book_id']}-{item['chapter']}" for item in data]

# Sort the list alphabetically
sorted_list = sorted(combined_list)

# Write the sorted list to a new file
with open('SortedBookChapters.txt', 'w') as output_file:
    for entry in sorted_list:
        output_file.write(entry + '\n')
