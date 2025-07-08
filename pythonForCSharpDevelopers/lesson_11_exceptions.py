# python uses try, except, finally
# C# uses try, catch, finally

# In Python, you can use a try-except block to handle exceptions.
# The try block contains the code that might raise an exception,
# and the except block specifies how to handle the exception
#   if it occurs.
try:
    result = 1 / 0
except ZeroDivisionError as e:
    print(e)

# You can handle different types of exceptions using
# multiple except blocks.

try:
    # Some code that might raise an exception
    result = 1 / 0
except ZeroDivisionError as e:
    print(e)
# Handle ZeroDivisionError
except ValueError as e:
    print(e)
# Handle ValueError
except Exception as e:
    print(e)
# Handle any other exception (catch-all)

"""
Handling Exceptions with else and finally:

- The else block is executed if no exceptions occur in the try block. 
    It is useful for code that should run only when no exceptions are raised.
- The finally block is executed regardless of whether an 
    exception occurred or not. It is used for cleanup operations that need 
    to be performed, such as closing files or releasing resources.
"""

try:
    # Some code that might raise an exception
    result = 1 / 0
except ZeroDivisionError as e:
    print(e)
else:
    print("success")
finally:
    print("finally")


# Raising exceptions
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b
