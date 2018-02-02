import unittest
import pytest
from dll import Node, DoubleLinkedList

class DoubleTest(unittest.TestCase):

    def test_1(self):
        n1 = Node(5)
        self.assertEqual(n1.value(), 5)

    def test_2(self):
        """ test append by head """
        dl = DoubleLinkedList()
        n1 = Node(5)
        n2 = Node (3)
        dl.append(n1)
        dl.append(n2)
        self.assertEqual(dl.head._next._value, 3)

    def test_3(self):
        """ test append by tail """
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
        """ prev of prior head is now node 2 (n1 here) """
        dl = DoubleLinkedList()
        n1 = Node(5)
        n2 = Node (3)
        dl.push(n1)
        dl.push(n2)
        self.assertEqual(n1._prev._value, 3)

    def test_7(self):
        """ next of prior head is now head """
        dl = DoubleLinkedList()
        n1 = Node(5)
        n2 = Node(3)
        dl.push(n1)
        dl.push(n2)
        dl.pop()
        self.assertEqual(dl.head._value, 5)
    
    def test_8(self):
        """ prev of prior tail is now tail """
        dl = DoubleLinkedList()
        n1 = Node(5)
        n2 = Node(3)
        dl.push(n1)
        dl.push(n2)
        dl.shift()
        self.assertEqual(dl.tail._value, 3)

    

    def test_9(self):
        """ remove by value, new next of prev is now removed node's next """
        dl = DoubleLinkedList()
        n1 = Node(5)
        n2 = Node(3)
        n3 = Node(6)
        dl.append(n1)
        dl.append(n2)
        dl.append(n3)
        dl.remove(3)
        self.assertEqual(dl.head._next._value, 6)

    def test_10(self):
        """ remove by value, return an exception if doesn't exist """
        dl = DoubleLinkedList()
        n1 = Node(5)
        n2 = Node(3)
        n3 = Node(6)
        dl.append(n1)
        dl.append(n2)
        dl.append(n3)
        dl.remove(7)
        self.assertEqual(dl.remove(7), "Node does not exist!")