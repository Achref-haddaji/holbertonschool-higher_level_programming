#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  process.argv.sort(function (a, b) {
    return a - b;
  });
  console.log(process.argv.reverse()[1]);
}
