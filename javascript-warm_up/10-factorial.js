#!/usr/bin/node
// scrip that computes and prints a factorial

const argument = process.argv.slice(2);
const firstArgument = parseInt(argument[0]);
function factorial (num) {
	if (num <= 1) return 1;
	return num * factorial(num - 1);
} if (isNaN(firstArgument)) {
	console.log(factorial(1));
} else {
	console.log(factorial(firstArgument));
}
