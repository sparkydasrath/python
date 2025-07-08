# lambda functions are defined using the lambda keyword,
# followed by the function's parameters and a single expression


# Regular function
def square(x):
    return x**2


# Equivalent lambda function
# square_lambda = lambda x: x**2


"""
Lambda functions are often used as throwaway 
functions for short operations or as arguments to 
other functions like map(), filter(), and sorted().
"""

numbers = range(10)

# lambda + map
lambda_map = list(map(lambda x: x**2, numbers))
print(f"lambda_map = {lambda_map}")

# lambda + filter
filtered_even = list(filter(lambda x: x % 2 == 0, numbers))
print(f"filtered_even = {filtered_even}")


# lambda + list comprehensions
# wrong: result2 = list([lambda x: x**2 for x in numbers])
# wrong: result2 = list([(lambda x: x**2) for x in numbers])

# need to put lambda in () and use the loop variable as the arg
lambda_list_comprehension = list([(lambda x: x**2)(x) for x in numbers])
print(f"lambda_list_comprehension = {lambda_list_comprehension}")
