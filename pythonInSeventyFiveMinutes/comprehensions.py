"""
Python comprehensions provide a concise way to create sequences (like lists, sets, or dicts) 
from existing iterables. They are often more readable and efficient than using loops.
"""

"""Simple Example: List Comprehension 
Create a list of squares from 0 to 4:"""
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

"""Intermediate Example: List Comprehension with Condition
Create a list of even numbers from 0 to 9:"""
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

"""Advanced Example: Nested List Comprehension
Create a 2D grid (list of lists) with values 0-4 for both rows and columns:"""

grid = [[(i, j) for j in range(5)] for i in range(5)]
print(grid)  # [[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
