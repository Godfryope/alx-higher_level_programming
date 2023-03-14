#!/usr/bin/node

function executeNTimes(x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

