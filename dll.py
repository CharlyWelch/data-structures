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
        if self.head is None:
            return "No value to return"
        elif self.head._next == None:
            return self.head
        else:
            node = self.head
            self.head = self.head._next
            self.size -= 1
            return node

    def shift(self):
        """ remove and return tail value - reassign tail to prev"""
        if self.tail is None:
            return "No value to return"
        elif self.tail._prev == None:
            return self.tail
        else:
            node = self.tail
            self.tail = self.tail._prev
            self.size -= 1
            return node

    def remove(self, value):
        """ search by value, remove that node - reassign bookending head and next """
        prev = None
        curr = self.head
        while curr is not None:
            if curr._value == value:
                if prev is not None:
                    prev._next = curr._next
                    if curr._next is not None:
                        curr._next._prev = prev
                if self.head == curr:
                    self.head = curr._next
                if self.tail == curr:
                    self.tail = curr._prev
                break
            else:
                prev = curr
                curr = curr._next
    