#!/usr/bin/node
// script that prints the first argument passed to it
const argument = process.argv.slice(2);

if (argument[0]) {
    console.log(argument[0]);
} else {
    console.log('No argument')
}
