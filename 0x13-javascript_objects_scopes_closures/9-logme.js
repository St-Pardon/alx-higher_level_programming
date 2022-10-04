#!/usr/bin/node
let count = 0;

/**
 * function that prints the number of arguments already printed and the new argument value.
 * @param {*} item: item to be prited
 */
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
