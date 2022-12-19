#!/usr/bin/node
// scrip that prints the addition of 2 integers

const argument = process.argv.slice(2);

function add (a, b) {
  return a + b;
}
const x = parseInt(argument[0]);
const y = parseInt(argument[1]);

console.log(add(x, y));
