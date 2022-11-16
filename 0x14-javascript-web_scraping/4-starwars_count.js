#!/usr/bin/node
const request = require('request');
if (process.argv.length > 2) {
  request(process.argv[2], (err, res, body) => {
    if (err) console.log(err);
    const json = JSON.parse(body);
    const count = json.results.filter(
      x => x.characters.find(y => y.match(/\/people\/18\/?$/))
    );
    console.log(count.length);
  });
}
