#!/usr/bin/node
const request = require('request');
let count = 0;
if (process.argv.length > 2) {
  request(process.argv[2], (err, res, body) => {
    if (err) console.log(err);
    const json = JSON.parse(body);
    for (let i = 0; i < json.results.length; i++) {
      for (let j = 0; j < json.results[i].characters.length; j++) {
        if (json.results[i].characters[j] === 'https://swapi-api.hbtn.io/api/people/18/') count++;
      }
    }
    console.log(count);
  });
}
