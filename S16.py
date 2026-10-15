#Q1
Aim: To implement Depth Limited Search (DLS) in Python.

Program:

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}

def dls(node, goal, limit):
    if node == goal:
        return True
    if limit <= 0:
        return False

    for child in graph[node]:
        if dls(child, goal, limit - 1):
            return True
    return False

print(dls('A', 'E', 2))

#Q2
rules = {'B': ['A'], 'C': ['B']}
facts = ['A']

def backward(goal):
    if goal in facts:
        return True
    if goal in rules:
        return all(backward(x) for x in rules[goal])
    return False

print("C is", backward('C'))


Conclusion: DLS searches a graph up to a specified depth li
