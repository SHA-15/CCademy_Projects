# Queues are a data structure which contains an ordered set of data
# Queues provide three methods for interaction:
# 1. Enqueue: adds data to the back of the stack
# 2. Dequeue: provides and removes data from the "front" of the queue
# 3. Peek: reveals data at the front of the queue without removing it

# Queues are a FIFO, or First-In-First-Out structure

# Queues can be implemented with a Linked List as the underlying data structure
# One last constaint that can be placed on the queue is it's length
# If a limit on the amount of data that can be placed into it, it is considered a bounded queue

# Queue overflow: attempting to enqueue data in an already full queue
# Queue underflow: attempting to dequeue data in an already empty queue

# Bounded queues require limits on the number of nodes that can be contained, while other queues don't.
# For this we will need to add further properties and methods to account for this limitation

# Let's start by defining the Node class

class Node:

    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, next_node):
        self.next_node = next_node

# Now let's create the Queue class

class Queue:
    
    def __init__(self, max_size = None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    # Here, max_size defines the length of the queue should be, while size covers the actual length of the queue has reached

    # peek returns the value at the front of the queue

    def peek(self):
        # .is_empty() is referenced to ensure peek output provides the accurate output
        if self.is_empty():
            print("Nothing to see here")
        else:
            return self.head.get_value()
    
    # get_size returns the current size of the queue
    def get_size(self):
        return self.size
    
    # has_space checks whether or not it can accomodate any more nodes in the queue object
    def has_space(self):
        
        # First check if the max_size has been established, if it hasn't, then it will always have space
        if self.max_size == None:
            return True
        else:
            return self.max_size > self.size
        
    # Is_empty method is to check if the queue is empty to let people know of an empty queue, and prevent queue underflow
    def is_empty(self):
        return self.size == 0
    
    # Now we will develop the 'Enqueue' method as discussed in the beginning of the program
    # There are three scenarios when adding to a queue
    # 1. Adding to the empty queue - The addition is both the head & tail of the queue
    # 2. Atleast another node present - the new node will become the tail
    # 3. Trying to enqueue in a full queue - cases of queue overflow

    def enqueue(self, value):
        # The first if statement to check if queue overflow is occurring

        if self.has_space():
            item_to_add = Node(value)
            print("Adding", item_to_add.get_value(), "to the queue!")

            # Second if statement to check if we a completely new queue

            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            
            # else is the case where there is atleast one more node in our queue

            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            
            self.size += 1

        # Queue overflow has occurred, let's let them know

        else:
            print("Sorry, no more room!")
                
    # Just like, enqueue, now we need to be able to dequeue from the head of the queue
    # Just like with enqueue, we have three scenarios to deal with:
    # 1. Empty queue
    # 2. Queue has only one node
    # 3. We have more than one node, so manual update is required
    def dequeue(self):
        
        # First to check for queue underflows
        if self.is_empty() == False:

            # We dequeue, we need to return the value of the removed node, so we will need a separate variable for it
            item_to_remove = self.head
            print("Removing", item_to_remove.get_value(), "from the queue!")

            # Now to check if the queue has only one Node
            if self.size == 1:
                self.head = None
                self.tail = None
            
            # In the case of more than one Node
            else:
                self.head = self.head.get_next_node()
            
            # In both inner checks, decrement self.size by 1 & return the popped node's value
            self.size -= 1
            
            return item_to_remove.get_value()
        
        else:
            print("This queue is totally empty!")


q = Queue()
q.enqueue("some guy with a mustache")
q.dequeue()





       



            
