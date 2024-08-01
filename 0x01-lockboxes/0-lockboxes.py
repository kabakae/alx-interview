def canUnlockAll(boxes):
    # Create a set to store keys we have
    keys = set()
    # The first box is already unlocked, so we start with the key to the first box
    keys.add(0)
    
    # Use a list to keep track of boxes we need to check
    to_check = [0]
    
    while to_check:
        current_box = to_check.pop()
        for key in boxes[current_box]:
            if key not in keys:
                keys.add(key)
                if key < len(boxes):
                    to_check.append(key)
    
    # If we have keys to all boxes, we should be able to unlock all boxes
    return len(keys) == len(boxes)
