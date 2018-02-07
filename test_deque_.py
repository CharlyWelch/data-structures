import unittest
import pytest

from deque_ import Node, Dequeue

class DequeueTest(unittest.TestCase):

    def test_1(self):
        """ check node creation """
        n1 = Node(1)
        self.assertEqual(n1._value, 1)

    def test_2(self):
        """ test append adds to end (right) """ 
        d = Dequeue()
        n1 = Node(1)
        n2 = Node(2)
        d.append(n1)
        d.append(n2)
        self.assertEqual(d.head._value, 1)

    def test_3(self):
        """ test appendleft adds to front (left) """
        d = Dequeue()
        n1 = Node(1)
        n2 = Node(2)
        d.append(n1)
        d.appendleft(n2)
        self.assertEqual(d.head._value, 2)

    def test_4(self):
        """ test popleft() removes node from front (left) """
        d = Dequeue()
        n1 = Node(1)
        n2 = Node(2)
        d.append(n1)
        d.append(n2)
        d.popleft()
        self.assertEqual(d.head._value, 2)

    def test_5(self):
        """ test popleft() returns node removed from front (left) """
        d = Dequeue()
        n1 = Node(1)
        n2 = Node(2)
        d.append(n1)
        d.append(n2)
        self.assertEqual(d.popleft()._value, 1)
    
    def test_6(self):
        """ test popleft() returns exception if list is empty """
        d = Dequeue()
        self.assertEqual(d.popleft(), "Dequeue is empty")

    def test_7(self):
        """ test popleft() returns node removed from front (left) """
        d = Dequeue()
        n1 = Node(1)
        n2 = Node(2)
        d.append(n1)
        d.append(n2)
        self.assertEqual(d.popleft()._value, 1)

    def test_8(self):
        """ test appendleft maintains tail assignment """
        d = Dequeue()
        n1 = Node(1)
        n2 = Node(2)
        d.append(n2)
        d.appendleft(n1)
        self.assertEqual(d.tail._value, 2)
    
    def test_9(self):
        """ test length() returns length of list """
        d = Dequeue()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        d.append(n1)
        d.append(n2)
        d.append(n3)
        self.assertEqual(d.length(), 3)

    def test_10(self):
        """ test peek() for return value """
        d = Dequeue()
        n1 = Node(1)
        n2 = Node(2)
        d.append(n1)
        d.append(n2)
        self.assertEqual(d.peek(), 2)
        
    def test_11(self):
        """ test peek() for empty dequeue """
        d = Dequeue()
        self.assertEqual(d.peek(), None)

    def test_12(self):
        """ test peekleft() for return value """
        d = Dequeue()
        n1 = Node(1)
        n2 = Node(2)
        d.append(n1)
        d.append(n2)
        self.assertEqual(d.peekleft(), 1)
        
    def test_13(self):
        """ test peekleft() for empty dequeue """
        d = Dequeue()
        self.assertEqual(d.peekleft(), None)



# class MoreTest(unittest.TestCase):
#      def test_9(self):
#         """ """
#         d = Dequeue()
#         n1 = Node(1)
#         n2 = Node(2)
#         n3 = Node(3)
#         d.append(n1)
#         d.append(n2)
#         d.append(n3)
#         self.assertEqual(d.tail._value, 3)