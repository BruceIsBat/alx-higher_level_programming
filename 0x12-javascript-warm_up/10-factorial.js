#!/usr/bin/node
const { argv } = require('process');

function factorial (num) {
  if (num === 0 || num === 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
let input = parseInt(argv[2]);
console.log(factorial(input));
