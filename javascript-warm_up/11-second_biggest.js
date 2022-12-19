#!/usr/bin/node
// scrip that searches the second biggest integer in the list of arguments.

const argument = process.argv.slice(2);
const newArray = [];
if (argument.length === 0 || argument.length === 1) {
  console.log('0');
} else {
  const theBiggest = Math.max.apply(null, argument);
  for (let i = 0; i < argument.length; i++) {
    if (parseInt(argument[i]) !== theBiggest) {
      newArray.push(argument[i]);
    }
  }
  console.log(Math.max.apply(null, newArray));
}
