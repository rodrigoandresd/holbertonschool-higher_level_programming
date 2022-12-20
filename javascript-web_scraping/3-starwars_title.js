#!/usr/bin/node
// script that prints the title of a Star Wars movie

const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request.get(url, (error, response, body) => {
  if (error) console.log(error);
  else console.log(JSON.parse(body).title);
});
