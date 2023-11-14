#!/usr/bin/node
const { argv } = require('process');

function factorial (num) {
  if (num <= 1 || !Number.isInteger(num)) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
const input = parseInt(argv[2]);
console.log(factorial(input));
