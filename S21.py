#Q1
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}

def dls(node, goal, depth):
    if node == goal:
        return True
    if depth == 0:
        return False
    return any(dls(n, goal, depth-1) for n in graph[node])

def ids(start, goal):
    for depth in range(10):
        if dls(start, goal, depth):
            return True
    return False

print(ids('A', 'E'))

#Q2 OR
from sklearn.naive_bayes import GaussianNB

X = [[1, 2], [2, 3], [3, 3],
     [8, 8], [9, 9], [10, 8]]
y = [0, 0, 0, 1, 1, 1]

model = GaussianNB()
model.fit(X, y)

print("Prediction:", model.predict([[2, 2]]))
