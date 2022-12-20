#!/usr/bin/node
// script that reads and prints the content of a file.

const fs = require('fs');
const file = process.argv[2];
const theString = process.argv[3];

fs.writeFile(file, theString, 'utf-8', (error) => {
  if (error) console.log(error);
});
