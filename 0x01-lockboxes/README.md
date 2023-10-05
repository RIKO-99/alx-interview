<h1> PROBLEM STATEMENT </h1>

You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False

####TEST CASES

boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # False

####SOLUTION

Let's solve the lockboxes problem step by step in Python while adhering to PEP 8 style guidelines. This problem can be solved using depth-first search (DFS) to determine if all the boxes can be opened. 


<li>We initialize a list called visited to keep track of which boxes we have visited. It has the same length as the boxes list, and all elements are initially set to False.</li>

<li>We mark the first box (box 0) as visited because it's unlocked by default.</li>

<li>We use a stack (stack) for depth-first search (DFS). We start DFS from the first box by adding it to the stack.</li>

<li>Inside the DFS loop, we pop the current box from the stack and iterate through its keys.</li>

<li>For each key, if the corresponding box hasn't been visited yet, we mark it as visited and add it to the stack for further exploration.</li>

<li>We continue this process until the stack is empty, which means we have explored all reachable boxes.</li>

<li>Finally, we check if all boxes have been visited. If any box is unvisited, we return False. Otherwise, we return True.</li>
