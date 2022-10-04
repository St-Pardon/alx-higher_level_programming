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
    if (w > 0 || h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  /**
   * print () - prints the rectangle
   */

  print () {
    for (let i = 0; i < this.height; i++) {
      let rect = '';
      for (let j = 0; j < this.width; j++) rect += 'X';
      console.log(rect);
    }
  }

  /**
   * double() - doubles the value of the rectangle
   */
  double () {
    this.width *= 2;
    this.height *= 2;
  }

  /**
   * rotate() - rotates the value of the rectangle
   */
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }
}
module.exports = Rectangle;
