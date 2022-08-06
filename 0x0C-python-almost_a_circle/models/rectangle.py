#!/usr/bin/python3
'''Rectangle from Base'''
from models.base import Base


class Rectangle(Base):
    """Rectangle that inherits from Base"""
    __width = width
    __height = height
    __x = x
    __y = y

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = Rectangle.width
        self.height = Rectangle.height
        self.x = Rectangle.x
        self.y = Rectangle.y
        
