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
    
    def priority(self, priority):
        self._priority = priority

class PriorityQ(object):
    """ to build a priority queue: ordered by an optional priority attribute """

    def insert(self, value, priority = 0):
        """ inserts a value into the queue. Takes an optional argument for node’s priority, set by default to lowest priority. """
        pass

    def pop(self):
        """ removes and returns the value of the highest priority node """
        pass

    def peek(self):
        """ return the value of but do not remove the highest priority node """
        pass
