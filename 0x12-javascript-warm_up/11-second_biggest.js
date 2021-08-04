#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = process.argv.sort(function (a, b) { return (a - b); });
  console.log(list.reverse()[1]);
}
