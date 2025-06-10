# UNPACK operator in Python


def func(x):
    def inner_func():
        print("Inner function executed with x:", x)

    return inner_func


# calling the function with argument but not executing it
print(
    func(10)
)  # returns the inner function <function func.<locals>.inner_func at 0x000001F2FE60AF20>

print(
    func(10)()
)  # now we execute the inner function # Inner function executed with x: 10


# *args and **kwargs unpacking

# the unpack operator * is used to unpack a list or tuple into positional arguments
x = [1, 2, 3]
print(*x)  # prints: 1 2 3

# the unpack operator ** is used to unpack a dictionary into keyword arguments
y = {"a": 4, "b": 5}


# !! Note: The above line will raise a SyntaxError, as ** cannot be used directly in print.
# print(**y)
"""
    This doesn't work because when you unpack a dictionary with **, it will pass this to
    the print function print(a=4, b=5) which is not valid syntax.
"""


def func_with_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


func_with_args(1, 2, 3, a=4, b=5)

# *args and **kwargs will let you pass in a variable number of arguments to a function


def func_with_args(*args, **kwargs):
    print(args, kwargs)  # args is a tuple, kwargs is a dictionary
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


# Positional arguments: (1, 2, 3) Keyword arguments: {'a': 4, 'b': 5}
func_with_args(1, 2, 3, a=4, b=5)
func_with_args(*range(5), a=4, b=5, c=None)
