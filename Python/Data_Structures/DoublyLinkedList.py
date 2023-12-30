# We will be covering the next element in our Data Structures Journey: Doubly Linked Lists!
# Doubly Linked Lists also are structured on nodes that contain data and TWO pointers (One forward & One backward)
# The first node in the Doubly Linked List is the head node and consequently, the last one is the tail node
# The head node's previous pointer is set to Null and the tail node's next pointer is set to Null

# Doubly Linked Lists are a sequential chain of Nodes that link the node to the next AND previous node of the list.
# Due to this, our Node class will be different to the one defined in the LinkedList class previously

class Node:

    def __init__(self, value, next_node = None, prev_node = None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    # Defining the setter methods for the pointers

    def set_next_node(self, next_node):
        self.next_node = next_node
    
    def set_prev_node(self, prev_node):
        self.prev_node = prev_node
    
    # Defining the getter methods for the value & pointers

    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
    def get_prev_node(self):
        return self.prev_node
    

# Defining the Doubly Linked List class here:

class DoublyLinkedList:
    # This constructor will allow creating a Doubly Linked List from the instantiation but also keep it empty if wanted
    def __init__(self, value = None):
        if value is None:
            self.head_node = None
            self.tail_node = None
        
        else:
            self.head_node = Node(value)
            self.tail_node = Node(value)

    # Introducing the adding to the Head function
    # This is one way I have implemented, different to how the codecademy developer does this

    # def add_to_head(self, new_value):
        # new_head = Node(new_value)
        # if self.head_node == None and self.tail_node == None:
            # self.head_node = new_head
            # self.tail_node = new_head

        # else:
            # self.head_node.set_prev_node(new_head)
            # new_head.set_next_node(self.head_node)
            # self.head_node = new_head

    # The approach taken by the course was as follows:

    def add_to_head(self, new_value):
        new_head = Node(new_value)
        current_head = self.head_node

        if current_head is not None:
            current_head.set_prev_node(new_head)
            new_head.set_next_node(current_head)
        
        self.head_node = new_head

        if self.tail_node == None:
            self.tail_node = new_head

    # Both work in the same principle, in cases of instantiation as well as in an established list

    # Defining a method for adding to the tail of the List

    def add_to_tail(self, new_value):
        new_tail = Node(new_value)
        current_tail = self.tail_node

        if current_tail is not None:
            current_tail.set_next_node(new_tail)
            new_tail.set_prev_node(current_tail)
        
        self.tail_node = new_tail

        if self.head_node == None:
            self.head_node = new_tail

    # Now we will be defining the methods to remove the head and tail in Doubly Linked List

    def remove_head(self):
        # Define a variable for the current head node to be removed
        removed_head = self.head_node

        # Check to see if the Doubly Linked List is empty
        # If it's empty (None), then there is nothing to remove
        if removed_head == None:
            return None
        
        # Now, this means that there is a head node, we will update this to the next node in the list
        self.head_node = removed_head.get_next_node()
        new_head = self.head_node

        # We will now need to verify if the next node is not None, then change the prev node to None
        if new_head != None:
            new_head.set_prev_node(None)

        # We also need to check if the removed_head was also the tail, then we will need to call the remove tail method
        if removed_head == self.tail_node:
            self.remove_tail()
        
        # Then finall return the removed_head node's value
        return "The value of the removed node was", removed_head.get_value()

    def remove_tail(self):
        removed_tail = self.tail_node

        # Check to see if the tail node is of None value, meaning the list is empty
        if removed_tail == None:
            return None
        
        # This means the tail exists, now update it to the prev node
        self.tail_node = removed_tail.get_prev_node()

        # Check to see if the prev Node is not None, if so, update the node to None
        if self.tail_node != None:
            self.tail_node.set_next_node(None)

        # Check to now see if the removed tail node wasn't also the head node
        if removed_tail == self.head_node:
            self.remove_head()
        
        # Finally, return the removed node's value
        return removed_tail.get_value()
    
    # Now that we have covered cases of how to remove the head & tail, we will focus on how to remove by values
    # We will define a remove by value method - traversing through the list and pop that value from the linked list
    def remove_by_value(self, value_to_remove):
        # First we will define the var node_to_remove to identify the node once we have found it
        node_to_remove = None
        # Current node var to track the traversal of the list
        current_node = self.head_node

        # We will now traverse the list to find the node, while loops will help us achieve that
        while current_node is not None:

            # Now we will review if the current node's value is equal to value_to_remove
            if current_node.get_value() == value_to_remove:
                node_to_remove = current_node
                break
        
            # If we are here, this means we have not found the node in the iteration, let'S traverse forwards
            current_node = current_node.get_next_node()

        # There are two possibilities now:
        # Either we have found the matching node and updated the node_to_remove var
        # Or we traversed the entirety and did not find anything here
        # Therefore we need to check if it's either of the two
        if node_to_remove is None:
            return None
        
        # Now comes the tricky part, the node_to_remove is either the head, tail or in_between node:

        if node_to_remove == self.head_node:
            self.remove_head()

        elif node_to_remove == self.tail_node:
            self.remove_tail()
        # When removing by in-between we need to update the neighboring node links
        else:
            next_node = node_to_remove.get_next_node()
            prev_node = node_to_remove.get_prev_node()

            prev_node.set_next_node(next_node)
            next_node.set_prev_node(prev_node)
        
        # FINALLY, return the 'popped' node
        return node_to_remove

    def stringify_list(self):
        string_list = ""
        current_node = self.head_node
        
        while current_node:
            
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            
            current_node = current_node.get_next_node()
        
        return string_list
    
    




subway = DoublyLinkedList()
subway.add_to_head("Times Square")
subway.add_to_head("Grand Central")
subway.add_to_head("Central Park")

subway.add_to_tail("Penn Station")
subway.add_to_tail("Wall Street")
subway.add_to_tail("Brooklyn Bridge")

print(subway.stringify_list())


print(subway.remove_head())
print(subway.remove_tail())

print(subway.stringify_list())

subway.remove_by_value("Times Square")

print(subway.stringify_list())

