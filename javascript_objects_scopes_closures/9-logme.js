#!/usr/bin/node
// unction that prints the number of arguments already printed and the new argument value

let callCount = 0;

exports.logMe = function (item) {
  console.log(callCount + ": " + item);
  callCount += 1;
};
