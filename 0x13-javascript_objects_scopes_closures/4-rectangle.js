#!/usr/bin/node
class Rectangle {
    constructor (w, h) {
      if (h > 0 && w > 0) {
        this.width = w;
        this.height = h;
      }
    }
    print () {
        for (let cont = 0; cont < this.height; cont++) {
            console.log('X'.repeat(this.width));
        }
    }
    rotate () {
        const aux = this.width;
        this.width = this.height;
        this.height = aux;
    }
    
    double () {
        this.width *= 2;
        this.height *= 2;
    }
}
module.exports = Rectangle;
  