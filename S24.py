#Q1
import heapq

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 2)],
    'C': [('D', 1)],
    'D': []
}
h = {'A': 3, 'B': 2, 'C': 1, 'D': 0}

def astar(start, goal):
    pq = [(h[start], 0, start, [start])]
    while pq:
        _, cost, node, path = heapq.heappop(pq)
        if node == goal:
            return path, cost
        for nxt, w in graph[node]:
            if nxt not in path:
                heapq.heappush(pq, (cost+w+h[nxt],
                                    cost+w, nxt, path+[nxt]))

print(astar('A', 'D'))


#Q2 OR
from sklearn.cluster import KMeans

X = [[1, 2], [2, 3], [3, 2],
     [8, 8], [9, 8], [8, 9]]

model = KMeans(n_clusters=2, random_state=0, n_init=10)
model.fit(X)

print("Cluster labels:", model.labels_)

