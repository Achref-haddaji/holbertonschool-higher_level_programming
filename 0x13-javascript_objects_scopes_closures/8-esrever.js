#!/usr/bin/node
exports.esrever = function (list) {
  const reversedarray = [];
  for (let index = list.length - 1; index >= 0; index--) {
    reversedarray.push(list[index]);
  }
  return reversedarray;
};
