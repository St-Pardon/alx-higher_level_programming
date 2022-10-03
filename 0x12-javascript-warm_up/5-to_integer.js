#!/usr/bin/node
const { argv } = require('process');
console.log(isNaN(parseInt(argv[2])) ? 'Not a number' : `My number: ${parseInt(argv[2])}`);
