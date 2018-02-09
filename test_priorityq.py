import pytest
import unittest

from priorityq import Node, PriorityQ

class PriorityTest(unittest.TestCase):
    def test_1(self):
        """ test that insert puts the node in the queue """
        p = PriorityQ()
        n1 = Node(1)
        p.insert(n1)
        self.assertEqual(p.head._value, 1)

    def test_2(self):
        """ test that insert puts the node in the queue in the correct position with no priority assignment """
        p = PriorityQ()
        n1 = Node(1)
        n2 = Node(2)
        p.insert(n1)
        p.insert(n2)
        self.assertEqual(p.head._value, 1)

    def test_3(self):
        """ test that insert puts the node in the queue in the correct position if given a priority value """
        p = PriorityQ()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        p.insert(n1, 1)
        p.insert(n2, 2)
        p.insert(n3, 3)
        self.assertEqual(p.head._priority, 3)

    def test_4(self):
        """ test that pop() removes the highest priority node """
        pass

    def test_5(self):
        """ test that pop() returns the value of the highest priority node """

    def test_6(self):
        """ test that peek() returns the value of the highest ptriority node """

    def test_7(self):
        """ test that pop() returns None if empty """
        pass

    def test_8(self):
        """ test that peek() returns None if empty """
        pass
