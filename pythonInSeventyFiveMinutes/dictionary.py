# DICTIONARY in Python
# it is an unordered collection of key-value pairs

# Creating a dictionary

empty_dict = {}  # empty dictionary
print('empty dictionary:', empty_dict)

empty_dict['a'] = 1  # adding a key-value pair
print('after adding key "a":', empty_dict)

my_dict = {'a': 1, 'b': 2, 'c': 3}  # literal dictionary
print('a' in my_dict)  # True
print(my_dict['a'])  # 1

# delete a key-value pair
del my_dict['b']
print('after deleting key "b":', my_dict)