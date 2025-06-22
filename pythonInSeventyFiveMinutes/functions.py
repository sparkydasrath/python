# FUNCTIONS


def function1():
    print("Function 1 executed")


function1()


def function2(x, y):
    print("Function 2 executed with parameters:", x * y)


function2(5, 10)


def function3(x, y, z=None):
    if z is not None:
        return x + y + z
    return x + y


result = function3(5, 10)
print("Function 3 executed with result:", result)


# return tuple
def function4(x, y):
    return x * y, x + y


result1, result2 = function4(5, 10)
print("Function 4 executed with results:", result1, result2)


# show return type in function signature
def function5(x: int, y: int) -> tuple[int, int]:
    return x * y, x + y


def show_date() -> None:
    print("Date")
