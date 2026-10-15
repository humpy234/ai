#Q1
from collections import deque

def bfs():
    q = deque([(0, 0)])
    visited = set()

    while q:
        x, y = q.popleft()

        if (x, y) in visited:
            continue
        visited.add((x, y))
        print(x, y)

        if x == 2 or y == 2:
            print("Goal Reached!")
            return

        q.extend([(4, y), (x, 3), (0, y), (x, 0),
                  (max(0, x-(3-y)), min(3, x+y)),
                  (min(4, x+y), max(0, y-(4-x)))])

bfs()


#Q2 OR
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [], 'E': [], 'F': [], 'G': []
}

def display(node):
    print(node, "->", tree[node])
    for child in tree[node]:
        display(child)

display('A')

