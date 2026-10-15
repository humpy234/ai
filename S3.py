#Q!
from collections import deque

def bfs(graph, start):
    visited = set()
    q = deque([start])

    while q:
        node = q.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            q.extend(graph[node])

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}

bfs(graph, 'A')


#Q2 OR
A = True
B = False

print("AND:", A and B)
print("OR:", A or B)
print("NOT A:", not A)
