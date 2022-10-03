#!/usr/bin/node
const { argv } = require('process');
if (argv[2]) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
