#!/usr/bin/node
const MyVar = process.argv[2];
let R = '';
if (isNaN(MyVar) === true) {
  console.log('Missing size');
} else {
  for (let m = 0; m < MyVar; m++) {
    R += 'X';
  }
  for (let m = 0; m < MyVar; m++) {
    console.log(R);
  }
}
