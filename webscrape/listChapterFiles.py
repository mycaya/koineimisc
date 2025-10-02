import os

# Specify the path to the 'scrapednrt' subfolder
subfolder_path = 'scrapednrt'

# Get all filenames in the specified subfolder
filenames = os.listdir(subfolder_path)

# Sort the filenames alphabetically
sorted_filenames = sorted(filenames)

# Write the sorted filenames to a .txt file
with open('SortedFilenames.txt', 'w') as output_file:
    for filename in sorted_filenames:
        output_file.write(filename + '\n')
