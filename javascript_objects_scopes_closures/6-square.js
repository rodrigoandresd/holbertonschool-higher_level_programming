#!/usr/bin/node
//  class Square that defines a square and inherits from Rectangle
const Square1 = require('./5-square');
module.exports = class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
