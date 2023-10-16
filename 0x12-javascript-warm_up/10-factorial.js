#!/usr/bin/node

function factorialize (num) {
  let MyRes = 1;
  for (let r = 1; r <= num; r++) {
    MyRes *= r;
  }
  return (MyRes);
}
console.log(factorialize(parseInt(process.argv[2])));
