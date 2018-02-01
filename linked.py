class Element(object):
    _value = None
    _next = None

    def __init__(self, value):
        self._value = value

    def value(self):
        return self._value

    def next(self, next):
        self._next = next

class LinkedList(object):
    head = None
    tail = None
    size = 0 

    def __init__(self):
        pass

    def append(self, node):
        """ add a node to the end of the list """
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            curr = self.head
            while curr:
                if curr._next is None:
                    curr._next = node
        self.size += 1

    def add_to_front(self, node):
        """add an item to the front of the list"""
        if self.head is None:
            self.head = node
        else:
            node._next = self.head
            self.head = node
        
        self.size += 1

    def pop(self):
        if self.head is None:
            return None
        else: 
            node = self.head
            self.head = self.head_next
            self.size -= 1
            return node