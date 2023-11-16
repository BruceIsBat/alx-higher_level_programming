#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  constructor(size) {
    super(size);
    this.size = size;
  }
  charPrint (c) {
    if (typeof c === 'undefined') {
      super.print();
    } else if (c === 'C') {
      for (let i = 0; i < this.size; i++) {
          console.log('C'.repeat(this.size));
      }
    }
  }
}
module.exports = Square;
