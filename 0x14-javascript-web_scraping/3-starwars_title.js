#!/usr/bin/node
const request = require('request');
if (process.argv.length > 2) {
  request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (err, res, body) => {
    if (err) console.log(err);
    const json = JSON.parse(body);
    console.log(json.title);
  });
}
