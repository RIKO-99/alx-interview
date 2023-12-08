#!/usr/bin/python3
"""The Game Module prime game challange."""

def iswinner(x, nums):
    """
    is_winner: A function that determines who wins the most rounds in the game.

    Args:
        x (int): The number of rounds.
        nums (list): A list of n for each round.

    Returns:
        str: The name of the player that won the most rounds.
             If the winner cannot be determined, return None.
    """
    def is_prime(num):
        """is_prime: Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = [num for num in range(2, n + 1) if is_prime(num)]
        nums_set = set(range(1, n + 1))
        maria_turn = True

        while nums_set and primes:
            if maria_turn:
                choice = min(primes)
            else:
                choice = max(primes)

            multiples = set(range(choice, n + 1, choice))
            nums_set -= multiples

            if not nums_set:
                if maria_turn:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            primes = [q for q in primes if q not in multiples]
            maria_turn = not maria_turn

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
