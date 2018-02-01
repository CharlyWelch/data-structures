import unittest
import pytest
from dll import Node, DoubleLinkedList

class DoubleTest(unittest.TestCase):

    def test_1(self):
        n1 = Node(5)
        self.assertEqual(n1.value(), 5)

    def test_2(self):
        dl = DoubleLinkedList()
        n1 = Node(5)
        n2 = Node (3)
        dl.append(n1)
        dl.append(n2)
        self.assertEqual(dl.head._next._value, 3)

    def test_3(self):
        dl = DoubleLinkedList()
        n1 = Node(5)
        n2 = Node (3)
        dl.append(n1)
        dl.append(n2)
        self.assertEqual(dl.tail._value, 3)

    def test_4(self):
        """ test that tail.next returns none """
        dl = DoubleLinkedList()
        n1 = Node(5)
        n2 = Node (3)
        dl.append(n1)
        dl.append(n2)
        self.assertEqual(dl.tail._next, None)
    
    def test_5(self):
        """ added node is now head """
        dl = DoubleLinkedList()
        n1 = Node(5)
        n2 = Node (3)
        dl.push(n1)
        dl.push(n2)
        self.assertEqual(dl.head._value, 3)

    def test_6(self):
        """ prev of prior head is now node """
        dl = DoubleLinkedList()
        n1 = Node(5)
        n2 = Node (3)
        dl.push(n1)
        dl.push(n2)
        self.assertEqual(n1._prev._value, 3)