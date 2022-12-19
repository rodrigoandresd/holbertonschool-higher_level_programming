#!/usr/bin/node
// scrip that print a square
const argument = process.argv.slice(2);
const sizeOfSquare = parseInt(argument[0]);
const character = 'X'
if (isNaN(argument[0])) {
  console.log('Missing size');
}
for (let i = 0; i < sizeOfSquare; i++) {
  console.log(character.repeat(sizeOfSquare));
}

