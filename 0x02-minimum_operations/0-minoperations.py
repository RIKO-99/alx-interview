#!/usr/bin/python3
"""0-minoperations module module."""


def minOperations(n: int) -> int:
    """
    minOperations: calculates the fewest number of operations for \
        copy and paste to result in exactly n H characters in the file.

    @n: the number of H characters in the file.

    Return: an integer. Number of operations.
    """
    if (n <= 0):
        return 0

    countMinOps = 0
    i = 2
    while (i <= n):
        while (n % i == 0):
            countMinOps += i
            n = n // i
        i += 1
    return countMinOps
