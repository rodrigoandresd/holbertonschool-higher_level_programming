#!/usr/bin/node
// scrip that print x times “C is fun”
const argument = process.argv.slice(2);
const myArray = 'C is fun';
if (isNaN(argument[0])) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < parseInt(argument[0]); i++) {
  console.log(myArray);
}
