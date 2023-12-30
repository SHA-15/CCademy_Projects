# X--------------------------------------------------- NODES --------------------------------------------------------------X

# Defining a class Node with data and node_link attribute:

class Node:

    def __init__(self, value, node_link = None):
        self.value = value
        self.node_link = node_link

    # Adding getter methods to access the node_link and the data value

    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.node_link
    
    # We have defined that the data stored in the Node is immutable upon instatiation, not the link node.
    # Hence we need to be able to provide a setter method to update the link node attribute accordingly

    def set_next_node(self, link_node):
        self.node_link = link_node
    
# We are going to instantiate three objects of this class to understand linkage of Nodes

hamza = Node('Has a dream of becoming a computer scientist')
hasnain = Node('Has a dream of becoming an engineering manager')
danish = Node('Has a dream of becoming married')

# Here we have used the setter methods to establish linkages from one Node to another Node
hamza.set_next_node(hasnain)
hasnain.set_next_node(danish)

# Let's use the getter methods to access data of all three:
# Use Hamza to get danish's data and use present each three's data

hamzas_data = hamza.get_value()
hasnain_data = hamza.get_next_node().get_value()
danish_data = hasnain.get_next_node().get_value()
danish_again = hamza.get_next_node().get_next_node().get_value()

# print('This is Hamza and he', hamzas_data)
# print('This is Hasnain and he', hasnain_data)
# print('This is danish and he', danish_data)
# print('Hi, Danish again, Did I mention that', danish_again)


# X-------------------------------------------------------- LINKED LIST ------------------------------------------------------X
# Linked Lists are comprised of series of Nodes sequentially linked to other Nodes.
# Each node points to anohter node in the list, until the last Node is reached
# Consequently, the first node in the list is known as the 'Head Node', and the last node is known as the 'Tail Node'

# The four main operations performed on Linked Lists include:
# 1. adding nodes
# 2. removing nodes
# 3. finding a node
# 4. traversing (or travelling through the linked list)

class LinkedList:

    def __init__(self, value = None):
        if value is not None:
            self.head_node = Node(value)
        else:
            self.head_node = None
    
    # Define a get head node value

    def get_head_node(self):
        return self.head_node
    
    # Now we will define setter methods to include new data nodes in the LinkedList and produce linked list's datapoints as strings

    def insert_starting_node(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    

    def stringify_list(self):
        stringify = ''
        # creating a current node variable to use variable reassingment as we traverse through this list
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                stringify += '\n Yeap there it is. ' + str(current_node.get_value())
            # By setting the current node to the next, we are able to ensure we go through the list 
            # and not create an infinite Loop
            current_node = current_node.get_next_node()
        return stringify
    
# Let's test it out

# ll = LinkedList(5)
# ll.insert_starting_node(70)
# ll.insert_starting_node(5675)
# ll.insert_starting_node(90)
# print(ll.stringify_list())

    # Now we define a method to remove a node from somewhere in the list
    def remove_node(self, value_to_remove):
        current_node = self.head_node
        if self.head_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while not current_node is None:
                if current_node.get_next_node().get_value() == value_to_remove:
                    current_node.set_next_node(current_node.get_next_node().get_next_node())
                    current_node = None
                else:
                    current_node = current_node.get_next_node()

    # After defining a method to remove a single node from a Linked List
    # We will be reviewing how to swap elements a in a Linked list
    # While swapping in a singly linked listf, the following steps are to be considered.
    # 1. Record the nodes that match the values input into the function
    # 2. Record the previous nodes that link to the nodes which match the values
    # 3. Update the links of the previous nodes to the nodes that are swapped
    # 4. Update the matched nodes next pointers to each other

    # Here is an example of how to do that:

    def swap_nodes(self, val1, val2):
        print(f'Swapping {val1} with {val2}.')
        node1 = self.head_node
        node2 = self.head_node
        node1_prev = None
        node2_prev = None

        if val1 == val2:
            print("both values are the same!, no need to perform swap.")

        while not node1 is None:
            if node1.get_value() == val1:
                break
            node1_prev = node1
            node1 = node1.get_next_node()
        
        while not node2 is None:
            if node2.get_value() == val2:
                break
            node2_prev = node2
            node2 = node2.get_next_node()
        
        # Checking if after going through the while Loop if,
        # one of the values was not found in the Linked List

        if (node1 is None or node2 is None):
            print("Swap not possible - one or more elements is not in the list")
            return
        
        # We have been identified with the node which matches the value
        # Now we will update the previous node's pointers to the swapped nodes

        if node1_prev is None:
            self.head_node = node2
        else:
            node1_prev.set_next_node(node2)
        
        if node2_prev is None:
            self.head_node = node1
        else:
            node2_prev.set_next_node(node1)
        
        # Now we will update the swapped node's next pointers
        # Temp is added to record node1's original next node otherwise,
        # The node of either will be updated in the code line before it
        # goes to the next line to execute
        temp = node1.get_next_node()
        # Set node1's next node as the node2's next node
        node1.set_next_node(node2.get_next_node())
    
        # Set node2's next node as the node1's next node
        node2.set_next_node(temp)

# Introducing a test mechanism

# ll = LinkedList()
# for i in range(10):
    # ll.insert_starting_node(i)


# print(ll.stringify_list())
# ll.swap_nodes(7,3)

# print(ll.stringify_list())


    
