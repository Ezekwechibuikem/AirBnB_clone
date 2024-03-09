#!/usr/bin/python3
"""
This module provides a simple function to calculate
the factorial of a given number.
"""


def factorial(n):
    """
    Calculate the factorial of a given number.

    Args:
        n (int): The number for which to calculate the factorial.

    Returns:
        int: The factorial of the given number.

    Raises:
        ValueError: If the input is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("Factorial of 5:", factorial(5))
    print("Factorial of 10:", factorial(10))
