import unittest
import pytest
from stack import Node, Stack

class TestList(unittest.TestCase):

    def test_1(self):
        """ check node creation """
        n1 = Node(5)
        self.assertEqual(n1.value(), 5)
    
    def test_2(self):
        """ check that nodes are added to stack """
        s = Stack()
        n1 = Node(5)
        s.push(n1)
        self.assertEqual(s.top._value, 5)

    def test_3(self):
        """ check that nodes are added to top of stack """
        s = Stack()
        n1 = Node(5)
        n2 = Node(4)
        s.push(n1)
        s.push(n2)
        self.assertEqual(s.top._value, 4)

    def test_4(self):
        """ check that nodes are removed from top of stack """
        s = Stack()
        n1 = Node(5)
        n2 = Node(4)
        s.push(n1)
        s.push(n2)
        s.pop()
        self.assertEqual(s.top._value, 5)

    def test_5(self):
        """ check that returns None if no nodes to pop """ 
        s = Stack()
        s.pop()
        self.assertEqual(s.top, None)

    def test_6(self):
        """ check that returns value if only one node to pop """
        s = Stack()
        n1 = Node(5)
        s.push(n1)
        self.assertEqual(s.pop(), 5)

    def test_7(self):
        """ check that len returns length of stack """ 
        s = Stack()
        n1 = Node(5)
        n2 = Node(4)
        s.push(n1)
        s.push(n2)
        self.assertEqual(len(s), 2)

    def test_8(self):
        """ check that len returns 0 if no nodes """ 
        s = Stack()
        self.assertEqual(len(s), 0)



    

    

