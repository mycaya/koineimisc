import os
from collections import Counter

# Path to the 'nrtchapterjson' directory
nrtchapterjson_directory = 'chapteraudio'

# List to store filenames
filenames = []

# Iterate over each file in the 'nrtchapterjson' directory
for filename in os.listdir(nrtchapterjson_directory):
    if os.path.isfile(os.path.join(nrtchapterjson_directory, filename)):
        filenames.append(filename)

# Count occurrences of each filename
filename_counts = Counter(filenames)

# Print filenames that appear more than once
for filename, count in filename_counts.items():
    if count > 1:
        print(filename)
