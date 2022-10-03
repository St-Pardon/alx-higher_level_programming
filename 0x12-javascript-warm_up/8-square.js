#!/usr/bin/node
const { argv } = require('process');
if (!argv[2] || isNaN(parseInt(argv[2]))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(argv[2]); i++) {
    let row = '';
    for (let j = 0; j < parseInt(argv[2]); j++) row += 'X';
    console.log(row);
  }
}
