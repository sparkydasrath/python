# python does not have a concept of constants like some other languages,
# but you can use uppercase variable names to indicate that a variable should be treated as a constant.

from typing import Final

# Constants in Python are typically defined using uppercase variable names.
PI: Final[float] = 3.14159  # constant for the value of pi
print(PI)  # Output: 3.14159


# You can also reassign a variable, but it's not recommended for constants.
PI = "test"
print(PI)  # Output: test
