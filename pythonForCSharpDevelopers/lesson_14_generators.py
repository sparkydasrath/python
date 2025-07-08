# A powerful feature for lazy evaluation of sequences
# Generators allow you to create iterators efficiently,
#   especially for large datasets, without generating all
#   the elements upfront.


# 1. Creating a generator - using yield keyword
def countdown(n: int) -> any:
    while n > 0:
        yield n
        n -= 1


# 2. Using a generator

# Create the generator
counter = countdown(5)

for number in counter:
    print(number)

# 3. Can use the next() function to get the next value
#   in the generator
counter = countdown(5)

print(next(counter))  # Output: 5
print(next(counter))  # Output: 4
print(next(counter))  # Output: 3

# 4. Generator expressions
"""
Generator expressions are similar to list comprehensions 
but produce generator objects instead of lists. 
They are defined using parentheses () instead of square brackets [].
"""
# Generator expression for even numbers
even_numbers = (x for x in range(10) if x % 2 == 0)

# Using the generator expression with a loop
for number in even_numbers:
    print(f"generator expression number = {number}")  # Output: 0, 2, 4, 6, 8
