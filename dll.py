class Node(object):
    _value = None
    _next = None
    _prev = None

    def __init__(self, value):
        self._value = value

    def value(self):
        return self._value

    def next(self, next):
        self._next = next

    def prev(self, prev):
        self.prev = prev

class DoubleLinkedList(object):
    head = None
    tail = None
    curr = None
    size = 0

    def __init__(self):
        pass

    def append(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail._next = node
            self.tail = node

        self.size += 1
    
    def push(self, node):
        """ add to front - reassign head value to current node """
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head._prev = node
            node._next = self.head
            self.head = node

        self.size += 1

    def pop(self):
        """ remove and return head value - reassign head to current head.next"""
        pass

    def shift(self):
        """ remove and return tail value - reassign tail to prev"""
        pass

    def remove(self):
        """ search by value, remove that node - reassign bookending head and next """
        pass
    