#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) console.log(error);
  else {
    fs.writeFile(filePath, body, 'utf-8', (error) => {
      if (error) console.log(error);
    });
  }
});
