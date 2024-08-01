#!/usr/bin/python3
"""
0-lockboxes Module
==================

This module contains the function `canUnlockAll` which determines if all
boxes in a list can be unlocked.

Example:
--------
    canUnlockAll = __import__('0-lockboxes').canUnlockAll

    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Should print: True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # Should print: True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # Should print: False
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Parameters:
    -----------
    boxes : list of lists
        A list where each element is a list containing the keys in that box.

    Returns:
    --------
    bool
        True if all boxes can be unlocked, False otherwise.

    Description:
    ------------
    - Each box is numbered sequentially from 0 to n - 1.
    - Each box may contain keys to other boxes.
    - The first box (boxes[0]) is initially unlocked.
    - A key with the same number as a box opens that box.
    - The function starts by collecting the key to the first box.
    - It then uses a loop to process each box for more keys.
    - If a key corresponds to a valid box number and hasn't been collected b
      it is added to the set of collected keys and the list of boxes to be d.
    - The function returns True if all boxes can be unlocked, otherwise False.
    """

    # Create a set to store keys we have collected
    keys = set()
    # The first box is already unlocked, so we start with the key to the  box
    keys.add(0)

    # Use a list to keep track of boxes we need to check
    to_check = [0]

    while to_check:
        # Get the next box to check
        current_box = to_check.pop()
        # Iterate through all keys in the current box
        for key in boxes[current_box]:
            # If the key is new and corresponds to a valid box, collect it
            if key not in keys and key < len(boxes):
                keys.add(key)
                # Add this box to the list of boxes to check for more keys
                to_check.append(key)

    # Check if we have keys to all boxes
    return len(keys) == len(boxes)


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Should print: True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # Should print: True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # Should print: False
