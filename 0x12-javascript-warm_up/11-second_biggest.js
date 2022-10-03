#!/usr/bin/node
const { argv } = require('process');
if (argv.length <= 3) {
  console.log(0);
} else {
  console.log(argv
    .filter((val, i) => i > 1)
    .sort((a, b) => a - b).slice(-2, -1)[0]
  );
}
