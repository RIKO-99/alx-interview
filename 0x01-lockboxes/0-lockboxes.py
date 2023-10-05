#!/usr/bin/python3
"""LockBoxes module."""


def canUnlockAll(boxes):
    """
    canUnlockAll: Determines if all the boxes can be opened by\
        the provided keys.

    The box at index 0(zero) is unlocked by default. If it contains\
        a key to the next box, we can unlock it. If it contains a key\
        to a box that has already been unlocked, we can unlock it.

    Args:
        boxes (List[List[int]]): List of lists of keys.
    """
    unlockedBoxes = [False] * len(boxes)
    unlockedBoxes[0] = True
    keys = boxes[0]

    # Check if you still have keys to unlock boxes
    while len(keys) > 0:
        # Pick a key and to open the box to that key
        key = keys.pop()
        if not isinstance(key, int) or key >= len(boxes) or key < 0:
            continue
        # Check if the box is locked and unlock it
        if not unlockedBoxes[key]:
            unlockedBoxes[key] = True
            # Add the keys in the box to the list of keys
            keys.extend(boxes[key])

    # Return True if all boxes are unlocked
    return all(unlockedBoxes)
