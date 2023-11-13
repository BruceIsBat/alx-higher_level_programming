#!/usr/bin/node
const { argv } = require('process');
const num = parseInt(argv[2]);
if (num) {
  for (let i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
} else if (num < 0) {
} else {
  console.log('Missing size');
}
