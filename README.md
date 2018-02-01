# data-structures
Collection of sample code for a number of common data structures in Python.
This repository will be added to sequentially. In it you will find:

**Singly-Linked List**
- **Module**: 'linked.py'
- **Tests**: 'test_linked.py'
- **Time Complexity**: Access and searching are O(n), inserting, and deleting are O(1) (see note below)

**Doubly-Linked List**
- **Module**: 'dll.py'
- **Tests**: 'test_dll.py'
- **Time Complexity**: Access and searching are O(n), inserting, and deleting are O(1) (see note below)

**Queue**
- **Module**: 'que_.py'
- **Tests**: 'test_que\_.py'
- **Time Complexity**: 

**Stack**
- **Module**: 'stack.py'
- **Tests**: 'test_stack.py'
- **Time Complexity**: 

# Notes on Data Structures:

## Singly-linked vs. Doubly-linked lists:
A singly-linked list may be the more appropriate data stucture to implement when making use of last-in-first-out structure, and it is not necessary to traverse the entire list in order to find a specific value. If you will need to flip back and forth through the data, a doubly-linked list will be more approporiate. 

### A note on time complexity, from Vinayak Garg:

>The cost of searching in both singly-linked list and doubly-linked list is O(n).
>
>Before deletion you need to search the linked list, which is O(n). Once you have searched the node to be deleted, you can delete in O(1) for both singly-linked list and doubly-linked list. But there is an important point to be noted for singly-linked list : you need to track the previous node as well while searching for the node to be deleted. This is not required for doubly-linked list.
>
>So the cost of deletion depends on whether you are including cost of searching or not.
>(https://discuss.codechef.com/questions/16791/time-complexity-of-single-and-double-link-list)

## Collaborations:



## Resources: 

- Singly-linked list: http://stackabuse.com/python-linked-lists/
- Time complexity sheet: http://bigocheatsheet.com/

