import unittest
import pytest
from stack import Node, Stack

class TestList(unittest.TestCase):
    def test_1(self):
        n1 = Node(5)
        self.assertEqual(n1.value(), 5)
    
    def test_2(self):
        s = Stack()
        n1 = Node(5)
        s.push(n1)
        self.assertEqual(s.top._value, 5)

    def test_3(self):
        s = Stack()
        n1 = Node(5)
        n2 = Node(4)
        s.push(n1)
        s.push(n2)
        self.assertEqual(s.top._value, 4)

    def test_4(self):
        s = Stack()
        n1 = Node(5)
        n2 = Node(4)
        s.push(n1)
        s.push(n2)
        s.pop()
        self.assertEqual(s.top._value, 5)

    def test_5(self):
        s = Stack()
        s.pop
        self.assertEqual(s.top, None)

    

    

