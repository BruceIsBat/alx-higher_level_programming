#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const s of list) {
    if (s === searchElement) {
      count++;
    }
  }
  return count;
};
