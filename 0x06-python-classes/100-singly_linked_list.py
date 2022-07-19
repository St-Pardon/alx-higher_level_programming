#!/usr/bin/python3
'''
A module for working with singly linked lists.
'''


class Node:
    '''
    Represents a node in a singly linked list.
    '''
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    '''
    Represents a singly linked list.
    '''
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if not isinstance(value, int) or value is None:
            raise TypeError('value must be an integer')
        else:
            if self.__head is None or self.__head.data >= value:
                new_node = Node(value, self.__head)
                self.__head = new_node
            else:
                node_ptr = self.__head
                prev_ptr = None
                while node_ptr is not None and value > node_ptr.data:
                    prev_ptr = node_ptr
                    node_ptr = node_ptr.next_node
                new_node = Node(value, node_ptr)
                prev_ptr.next_node = new_node

    def __str__(self):
        node_ptr = self.__head
        res = []
        while node_ptr is not None:
            res.append(str(node_ptr.data))
            node_ptr = node_ptr.next_node
        return '' if len(res) == 0 else '\n'.join(res)
