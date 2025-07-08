def sum_of_two(a: int, b: int) -> int:
    """
    Calculates the sum of two integers.
    Args:
        a (int): The first integer.
        b (int): The second integer.
    Returns:
        int: The sum of a and b.
    """
    return a + b


def function_with_default(a: int, b: int = 10) -> int:
    """
    Calculates the sum of two integers with a default value for b.
    Args:
        a (int): The first integer.
        b (int, optional): The second integer, defaults to 10.
    Returns:
        int: The sum of a and b.
    """
    return a + b
