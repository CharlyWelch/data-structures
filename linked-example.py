#     """ will be posted """ 
    
# class Element(object):
#     _value = None
#     _next = None

#     def __init__ (self, value, next = None):
#         self.value = value
#         self.next = next

#     @property
#     def next(self):
#         return self.next
    
#     @next.setter
#     def next(self, next):




#     def append(self.value)

""" In-class example:"""

class Node(object):
    _value = 0
    _next = None

    def __init__(self, value):
        self._value = value
    
    def next(self, node):
        self._next = node

n1 = Node(17)
n2 = Node(3)
n1._next = n2 # manually make n2 the 'next' for n1

print (n1._value)
print(n1._next._value) 

n3 = Node(44)
n2.next(n3) # don't need private _ for 
print("n2 next: ", n2._next._value) 

class LinkedList(object):
    head = None
    size = 0

    def append(self, node):
        # Empty condition
        if self.head is None:
            self.head = node
        #Non-empty list
        else:
            curr = self.head
            #Find the end of the list (tail)....
            while curr:
                if curr._next is None:
                    curr._next = node
                    return
        self.size += 1
                
    def push(self, node):
        # Empty condition
        if self.head is None:
            self.head = node
        #Non-empty list
        else:
            # set new node's next to current head of the list
            node._next = self.head
            # reset head to new node
            self.head = node
        self.size += 1

    def pop(self):
        # Empty condition
        if self.head is None:
            return None
        #Non-empty list
        else:
            node = self.head
            self.head = self.head._next
            self.size -= 1
            return node


##### Test Cases #######

l = LinkedList()
n1 = Node('A')
#head -> n1
l.append(n1)
print(l.head._value)

n2 = Node('B')
l.append(n2)
#head -> n1 -> n2
print(l.head._next._value)

n3 = Node('C')
#push to head of list
l.push(n3)
print(l.head._value)
print(l.head._next._value)

n = l.pop()
print("pop1:", n._value)
print("pop2:", l.head._value)
print("pop3:", l.head._next._value)






