class Node(object):
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
    size = 0 

    def __init__(self):
        pass

    def append(self, node):
        """ add a node to the end of the list """
        if self.head is None:
            self.head = node
        else:
            curr = self.head
            while curr:
                if curr._next is None:
                    curr._next = node
                    return
        self.size += 1

    def push(self, node):
        """add an item to the front of the list"""
        if self.head is None:
            self.head = node
        else:
            node._next = self.head
            self.head = node
        
        self.size += 1

    def pop(self):
        """ remove and return the head of the list """
        if self.head is None:
            return None
        else: 
            node = self.head
            self.head = self.head._next
            self.size -= 1
            return node

    
    ### This is sending my terminal into a neverending loop when testing. Tried many things, so far unable to fix -- continues to loop after passing 5 tests (five dots show up), even if this and the corresponding tests are commented out. Linter in test_linked says "Instance of 'LinkedList' has no 'remove' member" when I hover over the l. 
    def remove(self, value):
        """ search by value, remove that node - reassign next. If not present, return exception """
        prev = None
        curr = self.head
        while curr is not None:
            
            if curr._value == value:
                node = curr._value
                if self.head == curr:
                    self.head = curr._next
                else:
                    prev._next = curr._next
                    curr._next.prev = prev
                self.size -= 1
                return node 

            else:
                curr._next.prev = curr
                curr = curr._next

        if curr is None:
            return "Error: Node does not exist!"


    def __len__(self):
        """ return the length of the list """
        return self.size