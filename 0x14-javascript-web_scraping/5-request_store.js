#!/usr/bin/node
const request = require('request');
const fs = require('fs');
request(process.argv[2], function (error, data) {
  if (error) throw error;
  fs.writeFile(process.argv[3], data.body, 'utf8', (err, data) => {
    if (err) {
      return console.log(err);
    }
  });
});
