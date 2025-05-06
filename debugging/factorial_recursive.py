#!/usr/bin/python3
import sys

def factorial(n):
    """ 
    Computes the factorial of a given number using recursion.
    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.
    Returns:
    int: The factorial of the given number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
# Read the command-line argument, compute factorial, and print the result
f = factorial(int(sys.argv[1]))
print(f)