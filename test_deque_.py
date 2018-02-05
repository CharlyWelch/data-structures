import unittest
import pytest

from deque_ import Node, Dequeue

class DequeueTest(unittest.TestCase):

    def test_1(self):
        """ check node creation """
        n1 = Node(3)
        