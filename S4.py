#Q1
from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}

def bfs(start):
    visited = set()
    q = deque([start])

    while q:
        node = q.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            q.extend(graph[node])

bfs('A')

#Q2
def student(x):
    return x in ["Amit", "Rahul"]
students = ["Amit", "Rahul", "Priya"]
print("Exists:", any(student(x) for x in students))
print("For All:", all(student(x) for x in students))
