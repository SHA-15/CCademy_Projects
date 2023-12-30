# Towers of Hanoi is an ancient mathematical puzzle that starts off with three stacks and many disks
# The objective of the game is to move the disks from the left stack to the right stack

# The game follows three rules.
# 1. Only one disk can be moved at a time.
# 2. Take an upper disk and move it to a lower disk or an empty stack.
# 3. No disk to be placed on a smaller disk.

# We will use the Stack Class to develop this project

# Node Class
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

# Stack Class

class Stack:

    def __init__(self, name, limit = 1000):
        self.name = name
        self.size = 0
        self.limit = limit
        self.top_item = None

    def has_space(self):
        return self.limit > self.size
    
    def is_empty(self):
        return self.size == 0
    
    def peek(self):
        return self.top_item.get_value()
    
    def get_name(self):
        return self.name
    
    def get_size(self):
        return self.size
    
    def push(self, value):
        if self.has_space():
            new_item = Node(value)
            
            new_item.set_next_node(self.top_item)
            self.top_item = new_item
            
            self.size += 1
        else:
            print("No more space in stack!")
    
    def pop(self):
        if not self.is_empty():
            removed_item = self.top_item
            
            self.top_item = removed_item.get_next_node()
            self.size -= 1
            
            return removed_item.get_value()
        else:
            print("The stack is empty!")

    def print_items(self):
        
        pointer = self.top_item
        print_list = []
        
        while pointer:
            
            print_list.append(pointer.get_value())
            pointer = pointer.get_next_node()
        
        print_list.reverse()
        
        print("{0} Stack: {1}".format(self.get_name(), print_list))


# Let's start creating the game!
# Start off by creating the 3 Stacks on which the disks will sit upon

# This print statement, initiates the start of the game
print("\nLet's play Towers of Hanoi!!")


#Create the Stacks
# Three Stack instances are created and placed in an array to mimic the structure of the Towers
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)



#Set up the Game

# Request User input from the player on the number of disks to play with
num_disks = int(input("\nHow many disks do you want to play with?\n"))

# Minimum disks allowed is 3, ensured using the while loop
while num_disks < 3:
  num_disks = int(input("\nEnter a number greater than or equal to 3\n"))

# Once we have gotten the disks from the player, we need to create them and stack them on the left stack
# The size of each disk matters so we use integers to differentiate as size difference 
for i in range(num_disks, 0, -1):
  left_stack.push(i)

# Optimal moves is an output to declare the least moves possible to win the game
num_optimal_moves = (2**num_disks) - 1
print("\nThe fastest you can solve this game is in {0} moves".format(num_optimal_moves))

# Once we have setup the disks on the left stack and curated the optimal moves, we need to develop the process of getting input
#Get User Input

# Get input is a method of requesting moves from the player to move each disk from a stack onto another stack
def get_input():
  
  # Choices is a list of short names for each stack in stacks
  choices = [stack.get_name()[0] for stack in stacks]

  # The while True loop here runs indefinitely to allow our user to keep input moves in the game
  while True:

    # This for loop requests for the user input
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {0} for {1}".format(letter, name))
    user_input = input('')

    # The conditional checks if the input added in the game is correct, it returns the stack equivalent of the choice selected
    # Once the correct choice is selected it returns the stack equivalent and exits the function
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]


#Play the Game
# This variable will keep track of the number of moves a user makes
num_user_moves = 0

# Checks while the right stack is not filled with all the disks, meaning the end of the game
while right_stack.get_size() != num_disks:
  print("\n\n\n...Current Stacks...")
  
  # printing the stacks with the disks currently in them
  for stack in stacks:
    stack.print_items()
  
  # Another while True loop to run the game for the user
  while True:
    print("\nWhich stack do you want to move from?\n")
    # from_stack records the stack from which you want to move
    from_stack= get_input()
    print("\nWhich stack do you want to move to?\n")
    # records the stack to which is disk to be moved
    to_stack = get_input()

    # Let's implement the rules of the game to prevent the player from breaking the rules
    if from_stack.get_size == 0:
      print("\n\nInvalid Move. Try Again")
    # from_stack.peek() value is smaller than to_stack.peek() value  
    elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print("\n\nInvalid Move. Try Again")



print("\n\nYou completed the game in {0} moves, and the optimal number of moves in {1}.".format(num_user_moves, num_optimal_moves))

