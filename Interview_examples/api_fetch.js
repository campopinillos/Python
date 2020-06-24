#!/usr/bin/node
const fetch = require('node-fetch');

for (let index = 0; index < 6; index++) {
  fetch('https://jsonplaceholder.typicode.com/posts/' + index)
    .then(response => response.json())
    .then(json => console.log(json));
}
