import unittest
import pytest
from que_ import Node, Queue

class TestList(unittest.TestCase):
    """ check for node creation """
    def test_1(self):
        n1 = Node(5)
        self.assertEqual(n1.value(), 5)
    
    def test_2(self):
        """ check that nodes are added to the queue """
        q = Queue()
        n1 = Node(5)
        q.enqueue(n1)
        self.assertEqual(q.top._value, 5)

    def test_3(self):
        """ check that nodes are appending to the bottom of the queue, not the top """
        q = Queue()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        q.enqueue(n1)
        q.enqueue(n2)
        q.enqueue(n3)
        self.assertEqual(q.top._value, 1)

    def test_4(self):
        """ check that deque turns the second node into the top node """
        q = Queue()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        q.enqueue(n1)
        q.enqueue(n2)
        q.enqueue(n3)
        q.dequeue()
        self.assertEqual(q.top._value, 2)

    def test_5(self):
        """ Check that peek gives the value of the top node """
        q = Queue()
        n1 = Node(1)
        n2 = Node(2)
        q.enqueue(n1)
        q.enqueue(n2)
        q.peek()
        self.assertEqual(q.top._value, 1)

    def test_6(self):
        """ check that empty queue returns error upon dequeue """
        q = Queue()
        self.assertEqual(q.dequeue(), "No nodes to return")
    
    def test_7(self):
        """ Check that length returns the size of queue """
        q = Queue()
        n1 = Node(1)
        n2 = Node(2)
        q.enqueue(n1)
        q.enqueue(n2)
        self.assertEqual(q.length(), 2)

    def test_8(self):
        """ Check that length returns 0 if no nodes """
        q = Queue()
        self.assertEqual(q.length(), 0)

