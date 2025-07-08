# 1. Basic List Slicing

# Use list slicing to extract a portion of a list using the
# following syntax:

# new_list = original_list[start_index:end_index]
# ex:

# FUCKING RANGE DOES NOT WORK ANYMORE - fuck this
# original_list = range(10)
original_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"original_list = {original_list1}")
new_list1 = original_list1[3:7]  # index 4 exclusive
print(f"new_list1 = {new_list1}")  # [4, 5, 6, 7]

# 2. List slicing with step
# new_list = original_list[start_index:end_index:step]
with_step = original_list1[0:10:2]
print(f"with_step = {with_step}")  # [1, 3, 5, 7, 9]

# 3. Negative indexing
# use negative indices to slice the list from the end.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Slice the last three elements
slice5 = numbers[-3:]  # Output: [8, 9, 10]

# Slice all elements except the last two
slice6 = numbers[:-2]  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# 4. Modifying List Slices
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Replace elements in the slice
numbers[1:4] = [20, 30, 40]
print(numbers)  # Output: [1, 20, 30, 40, 5, 6, 7, 8, 9, 10]
