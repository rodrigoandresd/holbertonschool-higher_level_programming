#!/usr/bin/node
// script that prints the title of a Star Wars movie

const request = require('request');
const url = process.argv[2];
let wedgeAppearances = 0;

request.get(url, (error, response, body) => {
  if (error) console.log(error);
  else {
    for (const result of JSON.parse(body).results) {
      console.log(result)
      for (const character of result.characters) {
        if (character.includes('18')) {
          wedgeAppearances += 1;
        }
      }
    }
    console.log(wedgeAppearances);
  }
});
