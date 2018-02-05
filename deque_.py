class Node(object):
    _value = None
    _next = None

    def __init__(self, value):
        self._value = value

    def value(self):
        return self._value

    def next(self, next):
        self._next = next

class Dequeue(object):
    head = None
    tail = None
    size = 0

    def __init__(self):
        pass

    def append(self, node): 
    """ adds value to the end of the deque"""

        if self.head is None:
            self.head = node
        else:
            curr = self.head
            while curr:
                if curr._next is None:
                    curr._next = node
                    return
        self.size += 1

    def appendleft(self, val): 
    """ adds a value to the front of the deque"""
        self.size += 1

    def pop(self): 
    """removes a value from the end of the deque and returns it (raises an exception if the deque is empty)"""
        self.size -= 1

    def popleft(self): 
    """ removes a value from the front of the deque and returns it (raises an exception if the deque is empty)"""
        self.size -= 1

    def peek(self): 
    """returns the next value that would be returned by pop but leaves the value in the deque (returns None if the deque is empty)"""

    def peekleft(self): 
    """ returns the next value that would be returned by popleft but leaves the value in the deque (returns None if the deque is empty)"""

    def size(self): 
    """ returns the count of items in the queue (returns 0 if the queue is empty """