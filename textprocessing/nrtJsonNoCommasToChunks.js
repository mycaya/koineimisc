const fs = require('fs');
const path = require('path');

// Load the JSON file line by line
const filePath = path.join(__dirname, 'nrt.json');
const fileContent = fs.readFileSync(filePath, 'utf8');
const lines = fileContent.split('\n').filter(line => line.trim() !== '');

// Parse each line as a JSON object
const data = lines.map(line => JSON.parse(line));

// Function to split text by punctuation, hyphen, and length
function splitText(text) {
  const punctuationRegex = /([.,:;])/;
  const hyphenRegex = /\s-\s/;
  const maxLength = 27;
  const midLength = 54;

  // Remove special characters « and »
  text = text.replace(/[«»]/g, '');

  // Split by punctuation and hyphen, keeping punctuation
  let parts = text.split(hyphenRegex).join(' ').split(punctuationRegex).filter(Boolean);

  // Reconstruct parts with punctuation
  let reconstructedParts = [];
  for (let i = 0; i < parts.length; i++) {
    if (punctuationRegex.test(parts[i])) {
      reconstructedParts[reconstructedParts.length - 1] += parts[i];
    } else {
      reconstructedParts.push(parts[i].trim());
    }
  }

  // Further split parts based on length
  let result = [];
  reconstructedParts.forEach(part => {
    if (part.length > midLength) {
      // Split into multiple parts if over 54 characters
      while (part.length > maxLength) {
        let splitIndex = part.lastIndexOf(' ', maxLength);
        if (splitIndex === -1) splitIndex = maxLength;

        // Check for space followed by 'и'
        const andIndex = part.lastIndexOf(' и', maxLength);
        if (andIndex !== -1 && andIndex < splitIndex) {
          splitIndex = andIndex;
        }

        result.push(part.slice(0, splitIndex).trim());
        part = part.slice(splitIndex).trim();
      }
    } else if (part.length > maxLength) {
      // Split into two parts if between 27 and 54 characters
      let splitIndex = part.lastIndexOf(' ', Math.floor(part.length / 2));
      if (splitIndex === -1) splitIndex = Math.floor(part.length / 2);

      result.push(part.slice(0, splitIndex).trim());
      part = part.slice(splitIndex).trim();
    }
    if (part) result.push(part);
  });

  // Replace multiple spaces with a single space
  return result.map(str => str.replace(/\s+/g, ' '));
}

// Process each object in the array
const processedData = data.map(item => {
  const splitTexts = splitText(item.text);
  return splitTexts.map((text, index) => ({
    chapter: item.chapter,
    verse: item.verse,
    book_name: item.book_name,
    book_id: item.book_id,
    part: 1 + index,
    text: text
  }));
}).flat();

// Save the processed data back to a JSON file
const outputFilePath = path.join(__dirname, 'chunkednrt.json');
fs.writeFileSync(outputFilePath, JSON.stringify(processedData, null, 2), 'utf8');

console.log('Processing complete. Output saved to chunkednrt.json');
