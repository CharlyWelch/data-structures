import unittest
import pytest
from linked import Node, LinkedList

class TestList(unittest.TestCase):
    def test_1(self):
        """ test for node creation """
        n1 = Node(5)
        self.assertEqual(n1.value(), 5)
    
    def test_2(self):
        """ test that append adds a node """
        l = LinkedList()
        n1 = Node(5)
        l.append(n1)
        self.assertEqual(l.head._value, 5)

    def test_3(self):
        """ test that append(node) adds to end """
        l = LinkedList()
        n1 = Node(5)
        n2 = Node(3)
        l.append(n1)
        l.append(n2)
        self.assertEqual(l.head._next._value, 3)
    
    def test_4(self):
        """ test push(node) """
        l = LinkedList()
        n1 = Node(5)
        n2 = Node(3)
        l.append(n1)
        l.push(n2)
        self.assertEqual(l.head._value, 3)

    def test_5(self):
        """ test pop() """
        l = LinkedList()
        n1 = Node(5)
        n2 = Node(3)
        l.append(n1)
        l.append(n2)
        n = l.pop()
        self.assertEqual(n._value, 5)

    def test_6(self):
        """ test remove(node) for no matching node """
        l = LinkedList()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        l.append(n1)
        l.append(n2)
        l.append(n3)
        self.assertEqual(l.remove(7), "Error: Node does not exist!")

    def test_7(self):
        """ test remove(node) """
        l = LinkedList()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        l.append(n1)
        l.append(n2)
        l.append(n3)
        l.remove(2)
        self.assertEqual(n1._next._value, 3)

    def test_8(self):
        """ test len(list) """
        l = LinkedList()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        l.append(n1)
        l.append(n2)
        l.append(n3)
        self.assertEqual(len(l), 3)
    