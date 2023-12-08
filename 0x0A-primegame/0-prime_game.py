#!/usr/bin/python3
"""The Game Module."""


def isWinner(x, nums):
    """
    isWinner: Determine the winner for each round of the game.

    Args:
        x (int): The number of rounds.
        nums (list): A list of n for each round.

    Returns:
        str: The name of the player that won the most rounds.
             If the winner cannot be determined, return None.
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Check if the total number of rounds is even or odd
        if n % 2 == 0:
            # If even, Maria wins
            maria_wins += 1
        else:
            # If odd, Ben wins
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
