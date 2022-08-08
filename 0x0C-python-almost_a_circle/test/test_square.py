#!/usr/bin/python3
"""A unit test module for the polygon models.
"""
from io import StringIO
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests the Square class and its methods.
    """

    def test_init(self):
        """Tests the initialization of the Square class.
        """
        self.assertIsInstance(Square(5), Base)
        self.assertIsInstance(Square(5), Rectangle)
        self.assertTrue(issubclass(Square, Base))
        self.assertTrue(issubclass(Square, Rectangle))
        polygon = Square(5)
        id_init = polygon.id
        self.assertEqual(Square(5, 0, 0, 1).width, 5)
        self.assertEqual(Square(5, 0, 0, 1).height, 5)
        self.assertEqual(Square(5, 0, 0, 1).size, 5)
        self.assertEqual(Square(5, 0, 0, 1).x, 0)
        self.assertEqual(Square(5, 0, 0, 1).y, 0)
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Square('10')
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Square(None)
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Square(True)
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Square(10, '20')
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Square(10, None)
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Square(10, False)
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Square(10, 20, '25')
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Square(10, 20, None)
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Square(10, 20, False)
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon = Square(0)
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon = Square(-6)
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon = Square(6, -3)
        self.assertEqual(str(asrt_ctxt.exception), 'x must be >= 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon = Square(6, 3, -7)
        self.assertEqual(str(asrt_ctxt.exception), 'y must be >= 0')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Square(10, 13, 3, 7, 12)

    def test_str(self):
        """Tests the __str__ method for the Square.
        """
        self.assertEqual(
            str(Square(4, 0, 0, 1)),
            '[Square] (1) 0/0 - 4'
        )
        self.assertEqual(
            str(Square(4, 7, 12, 2)),
            '[Square] (2) 7/12 - 4'
        )
        self.assertEqual(
            str(Square(4, 4, 4, 3)),
            '[Square] (3) 4/4 - 4'
        )
        self.assertEqual(
            str(Square(4, 4, 4, 3.4)),
            '[Square] (3.4) 4/4 - 4'
        )
        self.assertEqual(
            str(Square(4, 2, 5, (4, 4))),
            '[Square] ((4, 4)) 2/5 - 4'
        )
