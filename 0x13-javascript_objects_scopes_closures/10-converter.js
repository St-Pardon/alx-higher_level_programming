#!/usr/bin/node
/**
 * Creates a number to string conversion function with a given base.
 * @param {Number} base The base of the conversion function.
 * @returns {Function} A conversion function.
 */
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
