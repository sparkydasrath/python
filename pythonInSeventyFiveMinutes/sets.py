# SETS in Python
# it is an unordered collection of unique elements

# Creating a set

empty_set = set()  # empty set
print('empty set:', empty_set)
empty_set.add(1)  # adding an element
print('after adding 1:', empty_set)


my_set = {1, 2, 3, 4, 5}  # literal set

print(type(empty_set))  # <class 'set'>
print(type(my_set))     # <class 'set'>

# Sets do not support slicing !!
# sliced = my_set[1:3]  # would raise TypeError

# check if member exists
my_set = {1, 2, 3, 4, 5}
print(3 in my_set)   # True
print(10 in my_set)  # False
