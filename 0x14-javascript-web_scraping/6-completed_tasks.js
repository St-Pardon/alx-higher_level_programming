#!/usr/bin/node
const request = require('request');
const tasks = {};
if (process.argv.length > 2) {
  request(process.argv[2], (err, res, body) => {
    if (err) console.log(err);
    const json = JSON.parse(body);
    json.forEach(item => {
      if (item.completed) {
        if (!tasks[item.userId]) {
          tasks[item.userId] = 0;
        }
        tasks[item.userId]++;
      }
    });
    console.log(tasks);
  });
}
