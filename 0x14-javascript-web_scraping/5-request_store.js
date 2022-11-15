#!/usr/bin/node
const request = require('request');
const { writeFile } = require('fs');
if (process.argv.length > 2) {
  request(process.argv[2], (err, res, body) => {
    if (err) console.log(err);
    writeFile(process.argv[3], body, 'utf8', (err) => {
      if (err) console.log(err);
    });
  });
}
