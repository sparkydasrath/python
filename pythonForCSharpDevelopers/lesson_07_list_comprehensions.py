# new_list = [expression for item in iterable]

numbers = range(0, 5)
squared = []

# normal
for num in numbers:
    squared.append(num**2)

# with list comprehension
list1 = [num**2 for num in numbers]
print(f"squared normal {squared}")
print(f"squared list comprehension {list1}")

# filtering even numbers
# even_numbers_wrong = [(num % 2 == 0) for num in range(20)]
even_numbers_2 = [num for num in range(20) if num % 2 == 0]
print(f"even numbers: {even_numbers_2}")


even1 = []
odd1 = []
even_numbers_3 = [
    even1.append(num) if num % 2 == 0 else odd1.append(num) for num in range(20)
]

print(even1)
print(odd1)

print("---------------")

print(f"even1 before slice = {even1}")
print(f"even1 len = {len(even1)}")
print("slicing even1 as even1[1:4]")
even2 = even1[1:4]
print(f"even1 len after slice = {len(even1)}")
print(f"even1 after slice = {even1}")
print(f"even2 = {even2}")
print("changing index 1 in even1")
even1[0] = 100
print(f"even2 after changing even1 index 0 {even2}")
