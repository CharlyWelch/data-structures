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
    size = 0
    tail = None
    curr = None

    def __init__(self):
        pass

    def append(self, node): 
        """ adds value to the end of the deque"""

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail._next = node
            self.tail =node
        self.size += 1

    def appendleft(self, node): 
        """ adds a value to the front of the deque"""
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node._next = self.head
            self.head = node
        self.size += 1

    def popleft(self): 
        """ removes a value from the front of the deque and returns it (raises an exception if the deque is empty)"""

        if self.head is None:
            return "Dequeue is empty"
        else: 
            node = self.head
            self.head = self.head._next
            self.size -= 1
            return node

    def pop(self): 
        """removes a value from the end of the deque and returns it (raises an exception if the deque is empty)"""
        if self.head is None:
            return "Dequeue is empty"
        else:
            curr = self.head
            while curr:
                if curr._next is not None:
                    self.tail = curr
                    curr._next = curr
                if curr._next == None:    
                    node = curr
                    self.size -= 1
                    return node
        
                              
        
    def peek(self): 
        """returns the next value that would be returned by pop but leaves the value in the deque (returns None if the deque is empty)"""
        if self.tail is None:
            return None
        else:
            return self.tail._value



    def peekleft(self): 
        """ returns the next value that would be returned by popleft but leaves the value in the deque (returns None if the deque is empty)"""
        if self.head is None:
            return None
        else:
            return self.head._value
   
    def length(self): 
        """ returns the count of items in the queue (returns 0 if the queue is empty """
        if self.head is None:
            return 0
        else:
            return self.size