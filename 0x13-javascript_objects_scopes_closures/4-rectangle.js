#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (!parseInt(w) || !parseInt(h) || w < 1 || h < 1) {
      return null;
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

  rotate () {
    [this.height, this.width] = [this.width, this.height];
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}
module.exports = Rectangle;
