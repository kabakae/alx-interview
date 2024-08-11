#!/usr/bin/python3

def minOperations(n):
    """
    Calculate the minimum number of operations needed to reach exactly n 'H' characters
    using only the Copy All and Paste operations.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations needed to achieve exactly n 'H' characters.
             Returns 0 if it is impossible to achieve exactly n characters.
    """
    if n <= 1:
        return 0  # If n is 1 or less, it's either not possible or trivial

    def get_factors(x):
        """
        Get all factors of a given number x.

        Args:
            x (int): The number to factorize.

        Returns:
            list: A sorted list of factors of x.
        """
        factors = []
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                factors.append(i)
                if i != x // i:
                    factors.append(x // i)
        factors.append(x)
        return sorted(factors)
    
    operations = float('inf')

    for factor in get_factors(n):
        ops = (n // factor) + (factor - 1)
        operations = min(operations, ops)
    
    return operations
