# raise exceptions

# raise Exception("This is a custom exception message.")


# HANDLING EXCEPTIONS IN PYTHON

try:
    # Simulating an error
    result = 10 / 0
except Exception as e:
    print("Error occurred:", e)

try:
    # Simulating an error
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error occurred:", e)

try:
    # Simulating an error
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error occurred:", e)
finally:
    print("This block always executes, regardless of an error.")
