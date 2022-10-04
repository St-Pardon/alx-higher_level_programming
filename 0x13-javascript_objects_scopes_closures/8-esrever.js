#!/usr/bin/node
/**
 * returns the reverse list
 * @param {Array} list - the list to be reversed
 */
exports.esrever = function (list) {
  const reversedList = [];
  list.forEach(item => reversedList.unshift(item));
  return reversedList;
};
