#!/usr/bin/node
// script that computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  const content = JSON.parse(body);
  const taskCompletedByUser = {};
  if (error) console.log(error);
  else {
    content.forEach(task => {
      if (task.completed === true) {
        const user = task.userId;
        if (user in taskCompletedByUser) {
          taskCompletedByUser[user]++;
        } else {
          taskCompletedByUser[user] = 1;
        }
      }
    });
    console.log(taskCompletedByUser);
  }
});
