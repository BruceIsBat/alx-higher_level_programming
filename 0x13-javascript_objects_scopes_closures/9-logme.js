#!/usr/bin/node
var List = [];
exports.logMe = function (item) {
  List.push(item);
  console.log(List.indexOf(item), ':', item);
};
