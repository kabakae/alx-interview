#!/usr/bin/python3
"""
Prime Game: Determines the winner between Maria and Ben
in a game where they take turns choosing prime numbers
and removing them and their multiples.
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game between Maria and Ben
    :param x: number of rounds
    :param nums: list of integers where each integer represents the set of numbers {1, 2, ..., n}
    :return: the player that won the most rounds or None if it's a tie
    """

    # Step 1: Precompute primes up to the maximum number in nums using Sieve of Eratosthenes
    def sieve(n):
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False  # 0 and 1 are not primes
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        return [i for i in range(n + 1) if sieve[i]]

    max_n = max(nums)
    primes = sieve(max_n)

    # Step 2: Count the number of moves (prime removals) needed for each n
    def count_prime_moves(n):
        multiples_removed = [False] * (n + 1)
        prime_moves = 0

        for prime in primes:
            if prime > n:
                break
            if not multiples_removed[prime]:
                # Prime can be chosen, remove it and its multiples
                prime_moves += 1
                for multiple in range(prime, n + 1, prime):
                    multiples_removed[multiple] = True
        return prime_moves

    # Step 3: Determine who wins each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        moves = count_prime_moves(n)
        if moves % 2 == 0:
            ben_wins += 1  # Ben wins if the number of moves is even
        else:
            maria_wins += 1  # Maria wins if the number of moves is odd

    # Step 4: Return the winner based on most wins
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
