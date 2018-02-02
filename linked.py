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

    def size(self):
        """ return the size of the list """
        pass
    
    def search(self, value):
        """ return the node containing the value if there is one, else, return none """
        pass

    def remove(self, node):
        """ remove given node if exists, else raise exception """
        pass

    def display(self, list):
        """ display a unicode string representing the list as if it were a tuple: “(12, ‘sam’, 37, ‘tango’)” """
        pass

# l = LinkedList()
# n1 = Node('A')
# #head -> n1
# l.append(n1)
# print(l.head._value)

# n2 = Node('B')
# l.append(n2)
# #head -> n1 -> n2
# print(l.head._next._value)

# n3 = Node('C')
# #push to head of list
# l.push(n3)
# print(l.head._value)
# print(l.head._next._value)

# n = l.pop()
# print("pop1:", n._value)
# print("pop2:", l.head._value)
# print("pop3:", l.head._next._value)