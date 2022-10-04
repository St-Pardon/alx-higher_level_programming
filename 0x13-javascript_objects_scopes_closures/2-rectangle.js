#!/usr/bin/node
/**
 * Class Rectangle - that defines a rectangle
 */
class Rectangle {
  /**
   * Class Contructor Function - Creates a new Rectangle with the given dimensions
   * @param {Number} w The value of the width.
   * @param {Number} h The value of the height.
   */
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
