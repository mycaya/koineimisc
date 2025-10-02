const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');

// Define the source and output directories
const sourceDir = path.join(__dirname, 'source2Kgs');
const outputDir = path.join(__dirname, 'output');

// Ensure the output directory exists
if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir, { recursive: true });
}

// Get all files in the source directory
fs.readdir(sourceDir, (err, files) => {
  if (err) {
    console.error('Error reading source directory:', err);
    return;
  }

  // Filter for audio files (assuming .mp3 format)
  const audioFiles = files.filter(file => path.extname(file).toLowerCase() === '.mp3');

  // Process each audio file
  audioFiles.forEach(file => {
    const inputFilePath = path.join(sourceDir, file);
    const command = `whisper_timestamped "${inputFilePath}" --model tiny --language ru --output_dir "${outputDir}" --output_format "json"`;

    // Execute the command
    exec(command, (error, stdout, stderr) => {
      if (error) {
        console.error(`Error processing file ${file}:`, error);
        return;
      }
      if (stderr) {
        console.error(`stderr for file ${file}:`, stderr);
      }
      console.log(`Processed file ${file} successfully.`);
    });
  });
});
