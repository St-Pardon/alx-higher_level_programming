#!/usr/bin/node
const { argv } = require('process');
function add (a, b) {
  return a + b;
}
console.log(add(parseInt(argv[2]), parseInt(argv[3])));
