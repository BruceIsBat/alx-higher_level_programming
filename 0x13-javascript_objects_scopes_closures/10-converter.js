#!/usr/bin/node
exports.converter = function (base) {
  return function convertNumber (number) {
    if (number < base) {
      return number.toString(base);
    } else {
      return convertNumber(Math.floor(number / base)) + (number % base).toString(base);
    }
  };
};
