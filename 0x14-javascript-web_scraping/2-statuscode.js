#!/usr/bin/node
const request = require('request');
if (process.argv.length > 2){
    request(process.argv[2], (err, res, body) => {
	console.log(`code: ${res.statusCode}`);
    })
}
