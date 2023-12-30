# Importing the LinkedList class from the file LinkedList.py

import LinkedList

# Runner method added for parallel tracking

def nth_last_element(linkedlist, n):
    counter = 1
    tail_pointer = linkedlist.head_node
    nth_last_pointer = None
    
    while tail_pointer:
        tail_pointer = tail_pointer.get_next_node()
        counter += 1
        if counter >= n + 1:
           
            if nth_last_pointer == None:
                nth_last_pointer = linkedlist.head_node
            
            else:
                nth_last_pointer = nth_last_pointer.get_next_node()
    return nth_last_pointer

def generate_test_linked_list():
    linked_list = LinkedList.LinkedList()
    for i in range(50, 0, -1):
        linked_list.insert_starting_node(i)
    return linked_list

# test_list = generate_test_linked_list()
# print(test_list.stringify_list())
# nth_last = nth_last_element(test_list, 4)
# print(nth_last.value)

# List Traversal at different speeds

# Finding the middle element of a list

def find_middle(linked_list):
    fast_pointer = linked_list.head_node
    slow_pointer = linked_list.head_node
    while fast_pointer:
        fast_pointer = fast_pointer.get_next_node()
        if fast_pointer is not None:
            fast_pointer = fast_pointer.get_next_node()
            slow_pointer = slow_pointer.get_next_node()
    return slow_pointer

def generate_test_linked_list(length):
  linked_list = LinkedList.LinkedList()
  for i in range(length, 0, -1):
    linked_list.insert_starting_node(i)
  return linked_list

test_list = generate_test_linked_list(7)
print(test_list.stringify_list())
middle_node = find_middle(test_list)
print(middle_node.value)


