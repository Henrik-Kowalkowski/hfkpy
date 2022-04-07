def add(*args):
    """A function to add elements together and return a sum.

    Returns:
        numeric: The sum of the numbers passed to the function.

    >>> add(1, 2, 3)
    """
    total = 0
    for arg in args:
        total += arg

    return total


def multiply(a, b):
    """A function that multiplies two elements together and returns the result.

    Args:
        a (numeric): A number to multiply.
        b (numeric): A number to multiply.

    Returns:
        numeric: The result of the multiplication.

    >>> multiply(4, 3)
    """
    return a * b

