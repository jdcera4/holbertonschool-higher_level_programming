#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      for (let cont = 0; cont < this.height; cont++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
