class Node(object):
    """ Class object to create node instances for stack """
    _value = None
    _next = None

    def __init__(self, value):
        self._value = value

    def value(self):
        return self._value

    def next(self, next):
        self._next = next

class Stack(object):
    """ Class object to create a stack data structure """
    top = None
    size = 0

    def __init__(self):
        pass

    def push(self, node):
        """ add a node to the top of the stack """
        node._next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        """ remove a node from the top of the stack """
        if self.top is None:
            return None
        elif self.top._next == None:
            return self.top._value
        else:
            node = self.top
            self.top = node._next
            return node
        self.size -= 1
    
    def __len__(self):
        """ return the length of the stack """
        return self.size