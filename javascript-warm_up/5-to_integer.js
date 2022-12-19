#!/usr/bin/node
/* script that prints My number: if the first argument can be
converted to an integer */
const argument = process.argv.slice(2);
if (isNaN(argument[0]) || argument.length === 0) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(argument[0]));
}
