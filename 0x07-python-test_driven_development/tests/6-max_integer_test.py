#!/usr/bin/python3
'''unittest module'''


import unittest
from importlib import import_module


class TestMaxInteger(unittest.TestCase):
    '''Tests the maximum integer function.'''
    def test_area(self):
        max_integer = import_module('6-max_integer', '..').max_integer
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([7, 2, -3, 45, 6]), 45)
        self.assertEqual(max_integer([-7, 1, -18, -6]), 1)
        self.assertEqual(max_integer([7, 1, -18, -6]), 7)
        self.assertEqual(max_integer([-7, 1, -18, 9]), 9)
        self.assertEqual(max_integer([7, 2, 45, 6]), 45)
        self.assertEqual(max_integer([-7, -2, -45, -6]), -2)
