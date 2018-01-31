
class Element(object):

    def __init__(self, value):
        self._value = value
        self._next = None

    def value(self):
        return self._value

    def next(self, next = None):
        if next == None:
            return self._next
        else:
            self._next = next

# class LinkedList(object):

#     def __init__(self):
#         self.head = None
#         self.tail = None
#         return

#     def add_list_item(self, item):
#         """add an item to the end of the list"""

#         if not isinstance(item, Element):
#             item = Element(item)

#         if self.head is None:
#             self.head = item
#         else:
#             self.tail.next = item

#         self.tail = item

#         return

#     def list_length(self):
#         """ return number of items in list """
#         count = 0
#         current_node = self.head

#         while current_node is not None:
#             count += 1
#             current_node = current_node.next

#         return count