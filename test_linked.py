import unittest
import pytest
from linked import Element, LinkedList

class TestList(unittest.TestCase):
    def test_1(self):
        ele = Element(5)
        self.assertEqual(ele.value(), 5)
    
    def test_2(self):
        ele = Element(7)
        ele.next(Element(3))
        self.assertEqual(ele.next().value(), 3)

    def test_3(self):
        ele = Element(7)
        LinkedList().append(ele)
        LinkedList().append(3)
        self.assertEqual(LinkedList.tail, 3)
        #This is returning None != 3... tail is not being reassigned. 
