#!/usr/bin/node
const { writeFile } = require('fs');
if (process.argv.length > 2) {
  writeFile(process.argv[2], process.argv[3], 'utf8', (err) => {
    if (err) {
      console.log(err);
    }
  });
}
