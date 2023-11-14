#!/usr/bin/node
const { argv } = require('process');
let max = argv[0];
if (argv.length <= 3) {
  console.log('0');
} else {
  for (let i = 0; i < argv.length; i++) {
    if (argv[i] > max) {
      max = argv[i];
    }
  }
  console.log(max);
}
