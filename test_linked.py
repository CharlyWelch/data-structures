import unittest
import pytest
from linked import Node, LinkedList

class TestList(unittest.TestCase):
    def test_1(self):
        n1 = Node(5)
        self.assertEqual(n1.value(), 5)
    
    def test_2(self):
        l = LinkedList()
        n1 = Node(5)
        l.append(n1)
        self.assertEqual(l.head._value, 5)

    def test_3(self):
        l = LinkedList()
        n1 = Node(5)
        n2 = Node(3)
        l.append(n1)
        l.append(n2)
        self.assertEqual(l.head._next._value, 3)
    
    def test_4(self):
        l = LinkedList()
        n1 = Node(5)
        n2 = Node(3)
        l.append(n1)
        l.push(n2)
        self.assertEqual(l.head._value, 3)

    def test_5(self):
        l = LinkedList()
        n1 = Node(5)
        n2 = Node(3)
        l.append(n1)
        l.append(n2)
        n = l.pop()
        self.assertEqual(n._value, 5)
    