#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (!parseInt(w) || !parseInt(h) || w < 1 || h < 1) {
      null;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
