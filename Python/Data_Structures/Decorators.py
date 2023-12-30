# Functions are objects
# functions within functions
# Returning functions from functions

def get_math_function(operation):
    def add(n1, n2):
        return n1 + n2
    def subtract(n1, n2):
        return n1 - n2


    if operation == '+':
        return add
    elif operation == '-':
        return subtract

add_function = get_math_function('+')
# print(add_function) 
# print(add_function(4, 6))

sub_function = get_math_function('-')
# print(sub_function)
# print(sub_function(6,4))

# Decorating a function

def title_decorator(print_name_function):
    def wrapper():
        print('Professor:')
        print_name_function()
    return wrapper

def print_my_name():
    print('Hamza')

# print_my_name()
@title_decorator
def print_hamzas_name():
    print('Hamza Saleem')


decorated_function = title_decorator(print_my_name)
decorated_function_2 = title_decorator(print_hamzas_name)

# decorated_function()
# decorated_function_2()

# print_hamzas_name()

# Decorators w/ parameters
def decorator_function(my_function):
    def wrapper(*args):
        print('Salutations, ')
        print(my_function(*args))
    return wrapper

# Wrapper function is essential within the decorator function


@decorator_function
def print_salutations(name, age):
    return '{name}, you are {age}'.format(name = name, age = age)

print_salutations('Hamza', 26)
