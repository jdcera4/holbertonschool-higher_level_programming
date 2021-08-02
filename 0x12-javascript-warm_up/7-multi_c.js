#!/usr/bin/node
// prints x times “C is fun”
const text = 'C is fun'
if (isNaN(process.argv[2])) {
  console.log();
} else {
  for (let cont = 0; cont < parseInt(process.argv[2]); cont++) {
    console.log(text);
  }
}
