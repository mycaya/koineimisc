const fs = require('fs');
const path = require('path');
const axios = require('axios');
const cheerio = require('cheerio');
const https = require('https');

// Create chapteraudio directory if it doesn't exist
const audioDir = path.join(__dirname, 'chapteraudio');
if (!fs.existsSync(audioDir)) {
  fs.mkdirSync(audioDir);
}

// Function to download a file
async function downloadFile(url, outputPath) {
  const writer = fs.createWriteStream(outputPath);

  return axios({
    method: 'get',
    url,
    responseType: 'stream'
  }).then(response => {
    response.data.pipe(writer);
    return new Promise((resolve, reject) => {
      writer.on('finish', resolve);
      writer.on('error', reject);
    });
  });
}

// Main function to process chapters and download audio
async function processChapters(inputFile) {
  try {
    const data = fs.readFileSync(inputFile, 'utf8');
    const chapters = JSON.parse(data);

    for (const chapter of chapters) {
      const { book_id, chapter: chap } = chapter;
      const url = `https://www.biblegateway.com/audio/biblica/nrt/${book_id}.${chap}`;

      console.log(`Fetching URL: ${url}`);

      // Fetch the webpage content
      const response = await axios.get(url);
      const $ = cheerio.load(response.data);

      // Find the mp3 source in the page
      const mp3Src = $('audio source').attr('src');
      if (mp3Src) {
        const outputFilePath = path.join(audioDir, `${book_id}-${chap}.mp3`);
        console.log(`Downloading MP3 from: ${mp3Src}`);
        await downloadFile(mp3Src, outputFilePath);
        console.log(`Downloaded and saved to: ${outputFilePath}`);
      } else {
        console.log(`MP3 source not found for ${book_id}.${chap}`);
      }
    }
  } catch (err) {
    console.error('Error processing chapters:', err);
  }
}

// Define the input file path
const inputFile = 'chapterspart.json';

// Execute the main function
processChapters(inputFile);
