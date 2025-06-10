
# COLLECTIONS
# list is ordered and can store multiple data types
x = [4, True, 3.14, "hello"]

print('first element:', x[0])  # Accessing the first element
print('last element:', x[-1])  # Accessing the last element

print('length of list:', len(x))  # Length of the list


print(x)  # Printing the entire list
x.append('test')  # Appending a new element
x.extend([3])  # Extending the list with another list
print('after appending and extending:', x)  # Printing the modified list

# Removing elements
x.remove(3.14)  # Removing the first occurrence of 3.14

x.pop()  # Removing the last element

print()

y = x.copy()  # Copying the list
print('y = copied list:', y)  # Printing the copied list
print('setting [1] to False in x')  # Commenting on the next operation
x[1] = False  # Changing the second element to False
print('x after changing second element:', x)  # Printing the modified list
print('y after changing second element in x:', y)  # Printing the modified list

# TUPLES - use round instead of square brackets
# immutable, ordered, can store multiple data types

tuple1 = (0, 0, 2, 3.14)
print('tuple1:', tuple1)  # Printing the tuple