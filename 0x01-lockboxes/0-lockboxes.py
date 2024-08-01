#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Parameters:
    boxes (list of lists): A list where each element is a list containing the

    Returns:
    bool: True if all boxes can be unlocked, False otherwise.

    Description:
    - Each box is numbered sequentially from 0 to n - 1.
    - Each box may contain keys to other boxes.
    - The first box (boxes[0]) is initially unlocked.
    - A key with the same number as a box opens that box.
    - The function starts by collecting the key to the first box.
    - It then uses a loop to process each box for more keys.
    - ore, it is ade set of collected keys and the list of boxes to be checked.
    - The functionrue if all boxes can be unlocked, otherwise it returns False.
    """

    # Create a set to store keys we have collected
    keys = set()
    # The first box is already unlocked, so we start with th to the first box
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
