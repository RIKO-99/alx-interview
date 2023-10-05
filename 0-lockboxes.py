#!/usr/bin/python3
def canUnlockAll(boxes):
    # Create a list to keep track of the boxes we can visit.
    visited = [False] * len(boxes)
    
    # We can always open the first box, so mark it as visited.
    visited[0] = True
    
    # Create a stack for DFS and initialize it with the keys from the first box.
    stack = [0]
    
    # Start DFS
    while stack:
        current_box = stack.pop()
        
        # Iterate through the keys in the current box.
        for key in boxes[current_box]:
            if not visited[key]:
                # Mark the box as visited and add it to the stack for further exploration.
                visited[key] = True
                stack.append(key)
    
    # Check if all boxes have been visited. If any box is unvisited, return False.
    return all(visited)
