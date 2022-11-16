#!/usr/bin/node
const request = require('request');
if (process.argv.length > 2) {
  request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (err, res, body) => {
    if (err) console.log(err);
    // for (let i = 0; i < JSON.parse(body).characters.length; i++) {
    const names = JSON.parse(body).characters.map(item => new Promise((resolve, reject) => {
      request(item, (err, res, body) => {
        if (err) console.log(err);
        resolve(JSON.parse(body).name);
      });
    }));
    Promise.all(names)
      .then(item => console.log(item.join('\n')))
      .catch(err => console.log(err));
  });
}
