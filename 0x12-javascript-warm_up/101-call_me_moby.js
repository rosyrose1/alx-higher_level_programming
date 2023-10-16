#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let r = 0; r < x; r++) theFunction();
};
