#!/usr/bin/node
// script that prints a message depending of the number of arguments passed
console.log(
  process.argv.length === 2 ? "No argument" : process.argv.length === 3 ?
  "Argument found" : "Arguments found");
