const fs = require('fs');
const path = require('path');

// Define the path to the input and output JSON files
const inputFilePath = path.join(__dirname, '2Kgs.json');
const outputFilePath = path.join(__dirname, '2Kgschapters.json');

// Function to process the JSON file
function processJsonFile(inputPath, outputPath) {
    try {
        // Read the file synchronously
        const data = fs.readFileSync(inputPath, 'utf8');

        // Split the data into lines and parse each line as JSON
        const lines = data.trim().split('\n').map(line => JSON.parse(line));

        // Use a Set to store unique combinations of book_id and chapter
        const uniqueChapters = new Set();

        // Extract unique objects
        const result = lines.reduce((acc, { book_id, chapter }) => {
            const key = `${book_id}-${chapter}`;
            if (!uniqueChapters.has(key)) {
                uniqueChapters.add(key);
                acc.push({ book_id, chapter });
            }
            return acc;
        }, []);

        // Write the result to the output file
        fs.writeFileSync(outputPath, JSON.stringify(result, null, 2), 'utf8');
        console.log(`Unique chapters written to ${outputPath}`);
    } catch (error) {
        console.error('Error processing JSON file:', error.message);
    }
}

// Call the function with the paths to the input and output files
processJsonFile(inputFilePath, outputFilePath);
