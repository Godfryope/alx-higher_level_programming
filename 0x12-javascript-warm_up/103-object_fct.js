#!/usr/bin/node

(function () {
  let count = 0;

  function counter() {
    console.log(count);
  }

  function incr() {
    count++;
  }

  window.counter = counter;
  window.incr = incr;
})();

counter(); // Outputs 0
incr();
counter(); // Outputs 1
incr();
counter(); // Outputs 2

