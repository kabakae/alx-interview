def minOperations(n):
    if n <= 1:
        return 0  # If n is 1 or less, it's either not possible or trivial

    def get_factors(x):
        factors = []
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                factors.append(i)
                if i != x // i:
                    factors.append(x // i)
        factors.append(x)
        return sorted(factors)
    
    operations = float('inf')

    # For each factor of n, calculate the number of operations
    for factor in get_factors(n):
        # number of operations needed for this factor is:
        # (factor - 1) pastes + 1 copy all operation
        # Plus the operations to reach 'factor'
        # i.e., we need factor operations to build 'factor' H's
        ops = (n // factor) + (factor - 1)
        operations = min(operations, ops)
    
    return operations
