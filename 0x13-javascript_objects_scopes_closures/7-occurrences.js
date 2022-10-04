#!/usr/bin/node
/**
 * nbOccurences - function that returns the number of occurrences in a list.
 * @param {Array} arr the list of items
 * @param {*} n the item to check for
 */
const nbOccurences = (arr, n) => {
  return arr.filter(item => item === n).length;
};
module.exports = { nbOccurences };
