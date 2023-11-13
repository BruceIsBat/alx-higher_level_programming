#!/usr/bin/node
const { argv } = require('process');

function factorial(num) {
  if (num === 0 || num === 1) {
    return 1; // Base case: factorial of 0 or 1 is 1
  } else {
    return num * factorial(num - 1); // Recursive call for factorial
  }
}

const input = parseInt(argv[2], 10);
const result = isNaN(input) ? 'Invalid input' : factorial(input);
console.log(`The factorial of ${input} is: ${result}`);

