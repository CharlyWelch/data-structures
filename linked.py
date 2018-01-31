# Write the required Python class(es) to implement a linked list. The list class should be named LinkedList. Your list implementation should support the following methods:

# push(val) will insert the value ‘val’ at the head of the list
# pop() will pop the first value off the head of the list and return it. Raises an exception with an appropriate message if there are no values to return.
# size() will return the length of the list
# search(val) will return the node containing ‘val’ in the list, if present, else None
# remove(node) will remove the given node from the list, wherever it might be (node must be an item in the list). If the node is not in the list, it should raise an exception with an appropriate message.
# display() will return a unicode string representing the list as if it were a Python tuple literal: “(12, ‘sam’, 37, ‘tango’)”
# In addition to these methods above, your implementation also needs to be able to interact with these built-in Python functions:

# len(the_list) returns the size of the list
# print(the_list) returns what the display() method returns
# The constructor for your LinkedList class should allow optionally passing an iterable of values. This is the only optional parameter it should take. If an iterable is provided, the result will be a linked list instance containing the values in the iterable. The head of the list should be the last item in the iterable: