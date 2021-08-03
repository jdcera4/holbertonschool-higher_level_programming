#!/usr/bin/node
const SquareBase = require('./5-square');

class Square extends SquareBase {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let cont = 0; cont < this.height; cont++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
