#!/usr/bin/node
const List = [];
exports.logMe = function (item) {
  List.push(item);
  console.log(List.indexOf(item), ': ', item);
};
