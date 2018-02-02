class Node(object):
    """ A class for creating node instances for the queue """
    _value = None
    _next = None

    def __init__(self, value):
        self._value = value

    def value(self):
        return self._value

    def next(self, next):
        self._next = next

class Queue(object):
    """ A class object that will function as a queue """
    top = None
    size = 0

    def __init__(self):
        pass

    def enqueue(self, node):
        """ add a node to the end of the queue """
        if self.top is None:
            self.top = node

        else:
            curr = self.top
            while curr._next is not None:
                curr = curr._next
            curr._next = node

        self.size += 1


    def dequeue(self):
        """  remove and return the top of the queue """
        if self.top is None:
            return "No nodes to return"
        node = self.top
        self.top = node._next
        return node

        self.size -= 1

    def peek(self):
        """ look athe value of the next node without removing it """
        if self.top == None:
            return None
        else: 
            return self.top._value

    def length(self):
        """ return the size of the queue """
        if self.top == None:
            return 0
        return self.size