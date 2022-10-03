#!/usr/bin/node
const { argv } = require('process');
if (argv[2]) {
  argv.filter((arg, i) => i > 1).forEach(val => console.log(val));
} else {
  console.log('No argument');
}
