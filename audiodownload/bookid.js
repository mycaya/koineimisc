const fs = require('fs');

// Function to extract unique book IDs
function extractUniqueBookIds(inputFile, outputFile) {
  // Read the JSON data from the input file
  fs.readFile(inputFile, 'utf8', (err, data) => {
    if (err) {
      console.error(`Error reading ${inputFile}:`, err);
      return;
    }

    try {
      const chapters = JSON.parse(data);

      // Extract unique book IDs using a Set
      const uniqueBookIds = new Set(chapters.map(chapter => chapter.book_id));

      // Convert the Set to an array for JSON serialization
      const uniqueBookIdsArray = Array.from(uniqueBookIds);

      // Write the unique book IDs to the output file
      fs.writeFile(outputFile, JSON.stringify(uniqueBookIdsArray, null, 4), (err) => {
        if (err) {
          console.error(`Error writing to ${outputFile}:`, err);
        } else {
          console.log(`Unique book IDs have been written to ${outputFile}`);
        }
      });
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  });
}

// Define the input and output file paths
const inputFile = 'chapters.json';
const outputFile = 'booklist.json';

// Call the function to extract and save unique book IDs
extractUniqueBookIds(inputFile, outputFile);
