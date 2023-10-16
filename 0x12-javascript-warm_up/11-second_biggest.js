#!/usr/bin/node
function secondBiggest (arr) {
  let maxi = 0; let output = 0;

  for (const value of arr) {
    const n = Number(value);

    if (n > maxi) {
      [output, maxi] = [maxi, n];
    } else if (n < maxi && n > output) {
      output = n;
    }
  }

  return output;
}

console.log(secondBiggest(process.argv));
