# Stacks are another form of a data structure that have a LinkedList as an underlying data structure
# Stacks provide three methods for interaction.
# 1. Push - adds a node to the "top" of the stack
# 2. Pop - removes and returns the "top" node of the stack
# 3. Peek - returns data from the "top" of the stack without removing it

# This is commonly referred to as a Last In, First Out or "LIFO" structure
# The top of the stack is known as the head node and bottom, as it's tail node

# A constraint that may be placed on the stack is it's size.
# This prevents cases where a stack may "overflow" i.e. keep more nodes than prescribed
# or even stack underflow, trying to produce an output from an empty Stack

# We will start builiding our Stack journey by creating the Node class
class Node:
    
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node
    
    def get_value(self):
        return self.value

# Let's start defining our Stack class

class Stack:
    # Here we will instantiate the Stack class
    # The stack class contains the three critical parameters
    # self.top_node = identifies the top stack or "last" entered
    # self.size captures the count of nodes in the stack class
    # self.limit defines the size of the entire stack class which will help in preventing stack over- & underflow

    def __init__(self, limit = None):
        self.top_node = None
        self.size = 0
        self.limit = limit

    # Let's define helper methods to support in stack under- & overflow prevention

    # .is_empty() defines the method to check if the stack is empty
    def is_empty(self):
        return self.size == 0
    
    # .has_space() defines the method to check if the stack has any space
    def has_space(self):
        if self.limit is None:
            return True
        elif self.limit > self.size:
            return True
        else:
            return False
    
    # The above helper methods will help in creating the active methods in the Stack class

    # .push() - adding to the stack
    def push(self, value):
        
        new_node = Node(value)
        # First case is to check if it is empty
        if self.is_empty():
            self.top_node = new_node
            self.size += 1
       
        # Second to check if it has any space
        elif self.has_space():
            new_node.set_next_node(self.top_node)
            self.top_node = new_node
            self.size += 1

        # Lastly, the stack is full and hence prevent overflow!    
        else:
            print("The Stack is full!")

    # .pop() - remove & return the top node in the Stack
    def pop(self):

        node_to_remove = self.top_node

        # Check if the stack is empty, after all, you will not get any value from an empty Stack
        if not self.is_empty():
            self.top_node = node_to_remove.get_next_node()
            self.size -= 1
            return node_to_remove.get_value()

        else:
            print("Stack is empty!")

    # .peek() to only view the top node's value
    def peek(self):
        if not self.is_empty():
            return self.top_node.get_value()
        else:
            print("The Stack is empty!")


# pizza_box = Stack(3)
# print(1)
# pizza_box.push("This is Hawaiian")
# print(2)
# pizza_box.push("This is Chicken Fajita")
# print(3)
# pizza_box.push("This is Euro Supreme")
# print("This is the limit no. 4")
# pizza_box.push("This should cause an error")


# print(pizza_box.peek())
# pizza_box.pop()
# pizza_box.pop()
# pizza_box.pop()
# pizza_box.pop()

# print("Now to test the else of the peek")
# print(pizza_box.peek())




