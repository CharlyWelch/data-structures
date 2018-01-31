import unittest
import pytest
from linked import Element, LinkedList

class TestSum(unittest.TestCase):
    def test_1(self):
        ele = Element(5)
        self.assertEqual(ele.value(), 5)
    
    def test_2(self):
        ele = Element(7)
        ele.next(Element(3))
        self.assertEqual(ele.next().value(), 3)
