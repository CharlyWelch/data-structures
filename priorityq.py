class Node(object):
    """ to create node instances for insertion into the priority queue """
    _value = None
    _next = None
    _priority = None

    def __init__(self, value):
        self._value = value

    def value(self):
        return self._value

    def next(self, next):
        self._next = next

    def priority(self):
        return self._priority
    
class PriorityQ(object):
    """ to build a priority queue: ordered by an optional priority attribute """
    head = None
    tail = None 

    def insert(self, node, priority = 0):
        """ insert a node into the queue by priority (0 lowest), sets default priority to 0."""
        node._priority = priority

        if self.head is None:
            self.head = node
            self.tail = node

        elif priority == 0:
            self.tail._next = node
            self.tail = node
        
        else:
            curr = self.head
            prev = None
            if curr._next is not None:
                if node._priority <= curr._priority:
                    prev = curr
                    curr = curr._next
                else:
                    if prev is not None:
                        prev._next = node
                    curr._next = node._next
            else:
                if node._priority <= curr._priority:
                    self.tail._next = node
                    self.tail = node
                else: 
                    curr.prev = node
                    node._next = self.head
                    self.head = node



    def pop(self):
        """ removes and returns the value of the highest priority node """
        pass

    def peek(self):
        """ return the value of but do not remove the highest priority node """
        pass
