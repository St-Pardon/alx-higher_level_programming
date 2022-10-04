#!/usr/bin/node
const Rectangle = require('./4-rectangle');
/**
 * class Square - that defines a square and inherits from Rectangle of 4-rectangle.js
 */
class Square extends Rectangle {
  /**
   * constructor() - Creates a new Square with the given dimensions
   * @param {Number} size The value of the size.
   */
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
