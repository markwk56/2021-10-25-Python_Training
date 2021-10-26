# Part 1

#!/usr/bin/env python3

# Take the following lists

dogs = ["fido", "spot", "lucky"]

cats = ["fluffy", "snowball", "garfield"]

# And combine them into a list called pets.
# .copy creates a new copy that uses a different memory location and does not modify the original

pets = dogs.copy()

print(pets)

pets.extend(cats)

print(pets)

# Part 2

# Using the same lists from above,
# create a dictionary called my_pets
# that has the keys of 'dogs' and 'cats'
# with the values being the appropriate
# lists.
my_pets = {}

print(dogs)
print(cats)
my_pets['dogs'] = dogs
my_pets['cats'] = cats

print(my_pets)


# Part 3

# Prove you can use the pets list to print
# "I only own spot and snowball"

# use f" to print results

# Part 4

# Prove you can use the my_pets dict to print
# "I want to adopt fido and garfield too" 


# use f" to print results

#use print(id(my_pets)) to display memory location



