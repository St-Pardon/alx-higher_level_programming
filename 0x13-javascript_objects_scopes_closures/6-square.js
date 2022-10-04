#!/usr/bin/node
const FirstSquare = require('./5-square');
/**
 * class Square - that defines a square and inherits from Rectangle of 4-rectangle.js
 */
class Square extends FirstSquare {
  /**
   * charPrint() - Prints Square with the specified character
   * @param {String} c The specified character.
   */
  charPrint (c) {
    c = c === undefined ? 'X' : c;
    for (let i = 0; i < this.width; i++) {
      let square = '';
      for (let j = 0; j < this.height; j++) square += c;
      console.log(square);
    }
  }
}
module.exports = Square;
