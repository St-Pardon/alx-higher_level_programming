#!/usr/bin/node
const request = require('request');
if (process.argv.length > 2) {
  request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (err, res, body) => {
    if (err) console.log(err);
    for (let i = 0; i < JSON.parse(body).characters.length; i++) {
      request(JSON.parse(body).characters[i], (err, res, body) => {
        if (err) console.log(err);
        console.log(JSON.parse(body).name);
      });
    }
  });
}
