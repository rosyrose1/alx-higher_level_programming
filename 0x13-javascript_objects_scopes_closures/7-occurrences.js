#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let R = 0;

  for (let y = 0; y <= list.length; y++) {
    if (list[y] === searchElement) {
      R++;
    }
  }
  return R;
};
