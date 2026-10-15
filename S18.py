#Q1
import heapq

graph = {'A': [('B', 1), ('C', 3)],
         'B': [('D', 2)], 'C': [('D', 1)],
         'D': []}
h = {'A': 3, 'B': 2, 'C': 1, 'D': 0}

def astar(start, goal):
    pq = [(h[start], 0, start, [start])]
    while pq:
        _, cost, node, path = heapq.heappop(pq)
        if node == goal:
            return path, cost
        for nxt, w in graph[node]:
            heapq.heappush(pq, (cost + w + h[nxt],
                                cost + w, nxt, path + [nxt]))

path, cost = astar('A', 'D')
print("Path:", path)
print("Cost:", cost)

#Q2
import numpy as np
from sklearn.neural_network import MLPRegressor

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

model = MLPRegressor(hidden_layer_sizes=(),
                     max_iter=5000,
                     random_state=1)
model.fit(X, y)

print("Prediction:", model.predict([[6]]))
