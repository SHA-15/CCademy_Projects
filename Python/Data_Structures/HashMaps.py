# HashMaps are efficient key-value stores
# They are capable of assigning & retrieving data in the fastest way possible for a data structure
# The reason for this is because HashMaps use an array as the underlying data structure
# The value is stored by the array index being produced from the key using a hash function

# Defining the HashMap class

class HashMap:
    
    # The HashMap class has an array as an underlying data structure, hence we will instantiate a list with an array size to mimic the array structure behavior
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for i in range(array_size)]

    # Now we will define the methods to actuall generate the index range to store the value in the array
    def hash(self, key, collisions = 0):
        # Here we convert all the string elements into their byte equivalents using the encode function
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + collisions

    def compressor(self, hash_code):
        # We only need to take the hash_code to perform modulus against the array_size to get the array_index
        array_index = hash_code % self.array_size
        return array_index
    
    # The following setter & getter methods are defined on the Open Addressing Collision principles during our implementation of a HashMap class
    def assign(self, key, value):
        # The assign methods utilises the key to generate the array index
        # The array index is used to store the given value in the array space

        array_index = self.compressor(self.hash(key))
        
        # The current_value variable stores the existing value at the given index, this will help us to ensure 100% collision-prevention
        current_value = self.array[array_index]
        
        if current_value == None:
            self.array[array_index] = [key, value]
        
        elif current_value[0] == key:
            self.array[array_index] = [key, value]
        
        # Else statement uses the Open Addressing Collision Strategy
        else:
            
            # While is basically saying jab tak current key of array is not matching the given key in the function, do this!
            while current_value[0] != key:
                number_collisions = 1
                # Now that a collision has occurred, we need to update our hashing function, array index and eventually the location to put the value in!
                new_hash_code = self.hash(key, number_collisions)
                new_array_index = self.compressor(new_hash_code)
                updated_value = self.array[new_array_index]

                if updated_value == None:
                    updated_value = [key, value]
                    return
                
                elif updated_value[0] == key:
                    updated_value = [key, value]
                    return

                # Oh no, updating the collision did not work this time, let's try it again
                # increment the collisions
                number_collisions += 1
            
            return         
            

    def retrieve(self, key):
        # The retrieve methods looks to identify the value based on the key provided
        array_index = self.compressor(self.hash(key))
        possible_return_value = self.array[array_index]

        # The return value could be none for cases where the key and it's value do not exists
        # The return value could be the one of the key that was entered
        # The return value could belong to a different key altogether
        if possible_return_value == None:
            return None
        
        elif possible_return_value[0] == key:
            return possible_return_value[1]
        
        # The else statement will deal with Open Addressing Collision Strategy
        else:
            number_collisions = 1
            while possible_return_value[0] != key:
                new_hash_code = self.hash(key, number_collisions)
                new_array_index = self.compressor(new_hash_code)
                
                possible_return_value = self.array[new_array_index]

                if possible_return_value == None:
                    return None
                
                elif possible_return_value[0] == key:
                    return possible_return_value[1]

                number_collisions += 1
            
            return

# LET'S TEST OUR HASHMAP CLASS OUT!

hash_map = HashMap(15)

hash_map.assign("gabbro", "igneous")
hash_map.assign("sandstone", "sedimentary")
hash_map.assign("gneiss", "metamorphic")

print(hash_map.retrieve("gabbro"), hash_map.retrieve("sandstone"), hash_map.retrieve("gneiss"))